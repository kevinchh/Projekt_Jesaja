<template>
  <div>
    <v-container>
      <v-row :style = "{'padding-top': '100px'}">
        <v-col cols="12" md="5" class = "text-center">
          <div :style="{'background': '#eee', 'padding-bottom':'20px'}">
            <h2 :style = "{'padding-top': '10px'}">What does the model do?</h2>
            <br />
            <p class =".subtitle-1 text--secondary font-italic">
              Helping students increase their writing proficiency.
            </p>
          </div>
        </v-col>
        <v-col cols="12" md="7" :style = "{
          'text-align': 'left',
          'padding-left': '50px',
          'padding-right': '50px',
          'overflow': 'auto'}">
          <span class=".body-1" >
            Writing is an important prerequisite for success. But according to the American National Assessment of Educational Progress,
            less than a third of US high school students are proficient writers. Low-income students fare even worse than that,
            as less than 15 percent demonstrate writing proficiency. Therefore, the goal of our model is to
            help students improve their writing via automated feedback tools. More specifically, we want to provide feedback by
            identifying writing structures, such as thesis statements and support for claims in student essays.
            We took data provided by a Kaggle competition and used it to train a model which is able to
            automatically segment texts and classify argumentative,
            as well as rhetorical elements in essays written by 6th-12th grade students. All in all, the model we implemented is able to differentiate between Leads (L),
            Positions (Pos), Claims (C), Counterclaims (CC), Rebuttals (R), Evidences (Ev) and Concluding Statements (ConSt).
          </span>
          <v-img
            alt="textfeedback"
            contain
            src="../../assets/feedback_eval/txtfeedback.png"
            transition="scale-transition"
          />
          <br />
          <span class=".body-1">
            Our model can be used to make it easier for students to receive feedback on their writing and increase opportunities to improve writing outcomes.
            It may be directly integrated and used by virtual writing tutors or automated writing systems, while teachers could make use of them to reduce grading time.
          </span>
        </v-col>
      </v-row>
      <v-row :style = "{'padding-top': '200px'}">
        <v-col class = "text-center hidden-lg-and-up">
          <div :style="{'background': '#eee', 'padding-bottom':'20px'}">
            <h2 :style = "{'padding-top': '10px'}">How does the model work?</h2>
            <br />
            <p class =".subtitle-1 text--secondary font-italic">
              Levering scientifc advances in the field of NLP through usage of the Big Bird architecture.
            </p>
          </div>
        </v-col>
        <v-col cols="12" md="7" :style = "{
          'text-align': 'left',
          'padding-left': '50px',
          'padding-right': '50px',
          'overflow': 'auto'}">
          <span class=".body-1">
              The model we used for solving this task is a state-of-the-art DL architecture called Big Bird provided by HuggingFace.
              More specifically, we leverage their implementation of the
            </span>
               <a href="https://arxiv.org/abs/2007.14062">Big Bird architecture</a>,
          <span> which is a transformer-based model. Transformers receive a set of tokens each represented
                by a vector as input and
                send them through a number of layers in order to get an higher order represenation of the input.
                Usually, one needs as many nodes in a layer as tokens in the sequence.
                After each layer, the representation should be better than the representation from the
                previous layer.
                Transformer models have proven to be some of the most successfull when it comes to
                the application of DL to NLP. However, they come with a core limitation:
                they have a quadratic dependency on the sequence length due to the full attention
                mechanism.
          </span>
          <span class ="font-weight-bold">
            But what is the full-attention mechanism?
          </span>
          <span>
            As mentioned before, transformers work based on different layers, each taking the input from the
            layer before and creating a new and better representation. This is done by incorporating
            information from all other tokens from the previous layer. This means that the representation of each
            token in layer n is calculated based on all tokens form layer n-1. In short: we need attention
            routed from every token in the layer before to every token in the following layer.
            Thus, transformers have n-squared computation and memory requirements. This makes it hard to
            scale large inputs into qualitative models with feasible training time. The big bird architecture
            is able to solve this problem by theoretically scaling the computational requirements down
            to O(n),
          </span>
          <br />
          <span>
            In order to do this, the architecture uses 3 different types of attention: random attention,
            window attention, and global attention. Window and global attention are already known concepts from
            the long former archtecure, making the big bird architecture basically a long former with an
            additional random attention component.
          </span>
          <br />
          <span>
            Random attention is used to connect random nodes from
            one layer to the next layer. Each query only selects a fixed number (r) of random tokens, not
            dependent on the sequence length. The random attention component makes use of knowledge of
            the random walk theory, which tells us that we do not need a fully connected component (e.g. a model
            with full-attention) to make all nodes reachable from all other nodes. Thus, the same routing as in
            full-attention models is possible if enough layers are used (in combination with window attention).
            As the number of connections r is constant for each output node,
            random attention requires O(r * n) = O(n) run-time.
          </span>
          <br />
          <span>
            Window attention is based on the position of the specific tokens. Each token at the i-th
            position is attending to itself and to its direct neighbors. Window attention can be seen
            as a kind of convolution: each next layer takes input form a window of the previous layer.
            Thus, the last layers will be dependant on all input tokens. In order to make up for the lack
            of full-attention, we can compensate by adding a higher number of layers. Window attention also
            has a constant complexity of O(n).
          </span>
          <br />
          <span>
            Global attention is necessary to process tokens which are so important that they have to be
            connected to everything else. E.g. a classifier token which has to be prepent to some piece of text
            in order to represent the classification output. Every other node in the network sends information to
            nodes representing such tokens and receives information from it.
          </span>
          <br />
          <span>
            It is also important to keep in mind that all three attention mechanisms are able to
            route information from one node to every other. Therefore, it is possible to "simulate" the behavior
            of full attention without having to deal with the high computation costs. It is said that in worst case,
            n layers are necessary to simulate full attention, resulting in a quadratic worst-case run-time.
          </span>
        </v-col>
        <v-col cols="5" class = "text-center hidden-md-and-down">
          <div :style="{'background': '#eee', 'padding-bottom':'20px'}">
            <h2 :style = "{'padding-top': '10px'}">How does the model work?</h2>
            <br />
            <p class =".subtitle-1 text--secondary font-italic">
              Levering scientifc advances in the field of NLP through usage of the Big Bird architecture.
            </p>
          </div>
        </v-col>
      </v-row>
      <v-row :style = "{'padding-top': '200px'}">
        <v-col cols="12" md="5" class = "text-center">
          <div :style="{'background': '#eee', 'padding-bottom':'20px'}">
            <h2 :style = "{'padding-top': '10px'}">How is the data processed?</h2>
            <br />
            <p class =".subtitle-1 text--secondary font-italic">
              Our data processing pipeline explained.
            </p>
          </div>
        </v-col>
        <v-col cols="12" md="7" :style = "{
          'text-align': 'left',
          'padding-left': '50px',
          'padding-right': '50px',
          'overflow': 'auto'}">
          <span>
            So how is the big bird data architecture used? We basically used student writing data
            provided by </span><a href = "https://www.kaggle.com/c/feedback-prize-2021/data"> a Kaggle challange </a> <span>as input for our model. The training data was already pre-labelled
            and already contained the underlying classes of each token. Furthermore, we applied IOB-NER labelling to each token to enhance our feature space.

          </span>
        </v-col>
      </v-row>
      <v-row :style = "{'padding-top': '200px'}">
        <v-col cols="12" class = "text-center hidden-lg-and-up">
          <div :style="{'background': '#eee', 'padding-bottom':'20px'}">
            <h2 :style = "{'padding-top': '10px'}">How does the model perform?</h2>
            <br />
            <p class =".subtitle-1 text--secondary font-italic">
              Providing a performance level for our model.
            </p>
          </div>
        </v-col>
        <v-col cols="12" md="7" :style = "{
          'text-align': 'left',
          'padding-left': '50px',
          'padding-right': '50px',
          'overflow': 'auto'}">
          <span class=".body-1">
            Our model was able to archieve a validation F1 score of 0.615 based on the test dataset.
          </span>
          </v-col>
          <v-col cols="5"  class = "text-center hidden-md-and-down">
            <div :style="{'background': '#eee', 'padding-bottom':'20px'}">
              <h2 :style = "{'padding-top': '10px'}">How does the model perform?</h2>
              <br />
              <p class =".subtitle-1 text--secondary font-italic">
                Providing a performance level for our model.
              </p>
            </div>
          </v-col>
        </v-row>
    </v-container>
  </div>
</template>





<script>

  export default {
    name: 'WritingFeedbackExp',
    components : {
    }
}
</script>
