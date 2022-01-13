import os
from transformers import *

import numpy as np, os
import pandas as pd, gc

from transformers import AutoTokenizer, AutoModelForTokenClassification
from torch.utils.data import Dataset, DataLoader
import torch
import ast
import sys

### own imports
from data_struct import dataset
from formats import provide_post_return

# CREATE MODEL
config_model = AutoConfig.from_pretrained("predefined/config.json")
model = AutoModelForTokenClassification.from_pretrained("predefined/pytorch_model.bin",
                                                        config=config_model)
#model.to(config['device'])
#optimizer = torch.optim.Adam(params=model.parameters(), lr=config['learning_rates'][0])
model.load_state_dict(torch.load("predefined/bigbird_v26.pt",
                                 map_location=torch.device('cpu')))

# CREATE DICTIONARIES THAT WE CAN USE DURING TRAIN AND INFER
output_labels = ['O', 'B-Lead', 'I-Lead', 'B-Position', 'I-Position', 'B-Claim', 'I-Claim', 'B-Counterclaim', 'I-Counterclaim',
          'B-Rebuttal', 'I-Rebuttal', 'B-Evidence', 'I-Evidence', 'B-Concluding Statement', 'I-Concluding Statement']

labels_to_ids = {v:k for k,v in enumerate(output_labels)}
ids_to_labels = {k:v for k,v in enumerate(output_labels)}

test_params = {'batch_size': 1, #4
                'shuffle': False,
                #'num_workers': 2,
                'pin_memory':False # True
                }

tokenizer = AutoTokenizer.from_pretrained("predefined")


def inference(batch):

    #The input_ids are simply the numeric representations of the tokens.Attention_mask is useful when we add padding to the input tokens. The attention mask tells us which input_ids correspond to padding
    # MOVE BATCH TO GPU AND INFER
    ids = batch["input_ids"]#.to(config['device'])
    mask = batch["attention_mask"]#.to(config['device'])
    outputs = model(ids, attention_mask=mask, return_dict=False)
    all_preds = torch.argmax(outputs[0], axis=-1).cpu().numpy()

    # INTERATE THROUGH EACH TEXT AND GET PRED
    predictions = []
    for k,text_preds in enumerate(all_preds):
        token_preds = [ids_to_labels[i] for i in text_preds]

        prediction = []
        word_ids = batch['wids'][k].numpy()
        previous_word_idx = -1
        for idx,word_idx in enumerate(word_ids):
            if word_idx == -1:
                pass
            elif word_idx != previous_word_idx:
                prediction.append(token_preds[idx])
                previous_word_idx = word_idx
        predictions.append(prediction)

    return predictions

def get_predictions(df, loader):

    # put model in training mode
    model.eval()

    # GET WORD LABEL PREDICTIONS
    y_pred2 = []
    for batch in loader:
        labels = inference(batch)
        y_pred2.extend(labels)

    final_preds2 = []
    for i in range(len(df)):

        idx = df.id.values[i]
        #pred = [x.replace('B-','').replace('I-','') for x in y_pred2[i]]
        pred = y_pred2[i] # Leave "B" and "I"
        preds = []
        j = 0
        while j < len(pred):
            cls = pred[j]
            if cls == 'O': j += 1
            else: cls = cls.replace('B','I') # spans start with B
            end = j + 1
            while end < len(pred) and pred[end] == cls:
                end += 1

            if cls != 'O' and cls != '' and end - j > 7:
                final_preds2.append((idx, cls.replace('I-',''),
                                     ' '.join(map(str, list(range(j, end))))))

            j = end

    oof = pd.DataFrame(final_preds2)
    oof.columns = ['id','class','predictionstring']

    return oof




def predict(text):
    #print(text["1"])
    test_names, test_texts = [], []
    #print("insert root to txt file:")
    #inFile = input()
    if text is None:
        text = ["Furthermore, asking for multiple opinions can benifit during competitions for a position slot, as cadidates needs to make decisions on what they need to say or do. For example, it can be helpful in situations like elections, both for the U.S. or simply in school. If a student is running for a position in office to represent his/her school, he/she can ask a widespread and diverse audience. First, asking other students is their best bet to obtaining information. Other students can inform him/her about what they want, like better water fountains, recess, or healthier food. Then, the student running can make changes to the way they run for the election, and on his/her speech, take a different approach. In addition, if the student running asks an adult, they will get to know a more realistic way the school can be improved. Since a student, even as a student officer, isn't able to make a significant change to a school, they can inform the school board about ways to make the school better. If someone is running for the president of the United States, a similar approach can be taken. First, they can ask the people, on social media or in speeches, about positive ways to reform our country. After the candidate receives the opinion of general audiences, they can campaign differently to match the view of those voting. All in all, asking for the opinion of multiple different people can set the candidate apart from others."]
    #test_names.append(inFile.replace('.txt', ''))
    #test_texts.append(open(inFile, 'r').read())
    test = pd.DataFrame({'id': 1, 'text': text})
    test_texts_set = dataset(test, tokenizer, 1024, True)
    test_texts_loader = DataLoader(test_texts_set, **test_params)
    for i in test_texts_loader:
        prediction = inference(i)
    res =  provide_post_return(prediction, text)

    return res
