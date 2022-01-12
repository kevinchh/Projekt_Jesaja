from collections import deque

labels = ['O', 'Lead', 'Position', 'Claim', 'Counterclaim', 'Rebuttal', 'Evidence', 'Concluding Statement']

def map_label(dat):
    res = deque([])
    for i in dat[0]:
        if i == 'O':
            res.append(i)
        else:
            res.append(i[2:])

    return res



def provide_post_return(pred, inp):

    res = {}
    out_dict_form = {}

    pred = map_label(pred)

    slow, fast = 0, 1
    while fast < len(pred):
        if pred[fast] != pred[slow]:
            out_dict_form[slow] = (fast - 1, pred[slow])
            slow = fast

        fast += 1

    out_dict_form[slow] = (fast - 1, pred[slow])


    res["input"] = inp
    res["out_dict"] = out_dict_form
    #res["out_list"]
    return res
