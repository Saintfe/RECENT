import numpy as np
from sklearn.metrics import precision_score, f1_score, recall_score

def micro(y_true, y_pred):
    return precision_micro(y_true, y_pred), recall_micro(y_true, y_pred), f1_micro(y_true, y_pred)

def macro(y_true, y_pred):
    return precision_macro(y_true, y_pred), recall_macro(y_true, y_pred), f1_macro(y_true, y_pred)

def micro_exclude_zero(y_true, y_pred):
    return f1_micro_exclude_zero(y_true, y_pred)

def macro_exclude_zero(y_true, y_pred):
    return f1_macro_exclude_zero(y_true, y_pred)

def precision_micro(y_true, y_pred):
    return precision_score(y_true, y_pred, average='micro')

def recall_micro(y_true, y_pred):
    return recall_score(y_true, y_pred, average='micro')

def f1_micro(y_true, y_pred):
    return f1_score(y_true, y_pred, average='micro')

def precision_macro(y_true, y_pred):
    return precision_score(y_true, y_pred, average='macro')

def recall_macro(y_true, y_pred):
    return recall_score(y_true, y_pred, average='macro')

def f1_macro(y_true, y_pred):
    return f1_score(y_true, y_pred, average='macro')

def precision_micro_exclude_zero(y_true, y_pred):
    '''y_true and y_pred need to be list'''
    labels = list(set(y_true))
    labels.remove(0)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    mask = (y_true > 0 )
    correct =  (y_true[mask] == y_pred[mask]).sum()
    guessed = (y_pred > 0).sum()
    precision = correct / guessed
    return precision
    

def recall_micro_exclude_zero(y_true, y_pred):
    '''y_true and y_pred need to be np.array'''
    labels = list(set(y_true))
    labels.remove(0)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    mask = (y_true > 0 )
    correct =  (y_true[mask] == y_pred[mask]).sum()
    gold = mask.sum()
    recall = correct / gold
    return recall

def f1_micro_exclude_zero(y_true, y_pred):
    '''y_true and y_pred need to be np.array'''
    labels = list(set(y_true))
    labels.remove(0)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    mask = (y_true > 0 )
    correct =  (y_true[mask] == y_pred[mask]).sum()
    guessed = (y_pred > 0).sum()
    gold = mask.sum()
    precision = correct / guessed
    recall = correct / gold
    f1 = 2 * precision * recall / (precision + recall)
    return precision, recall, f1

def precision_macro_exclude_zero(y_true, y_pred):
    '''y_true and y_pred need to be list'''
    labels = list(set(y_true))
    labels.remove(0)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    precisions = []
    for i in labels:
        mask = (y_true == i)
        correct =  (y_true[mask] == y_pred[mask]).sum()
        guessed = (y_pred == i).sum()
        prec = correct / guessed
        precisions.append(prec)

    precisions_np = np.asarray(precisions)

    return precisions_np.mean()

def recall_macro_exclude_zero(y_true, y_pred):
    '''y_true and y_pred need to be list'''
    labels = list(set(y_true))
    labels.remove(0)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    recalls = []
    for i in labels:
        mask = (y_true == i)
        correct =  (y_true[mask] == y_pred[mask]).sum()
        gold = (y_true == i).sum()
        rec = correct / gold
        recalls.append(rec)

    recalls_np = np.asarray(recalls)
    return recalls_np.mean()

def f1_macro_exclude_zero(y_true, y_pred):
    '''y_true and y_pred need to be list'''
    labels = list(set(y_true))
    labels.remove(0)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    precisions = []
    recalls = []
    f1s = []
    for i in labels:
        mask = (y_true == i)
        correct =  (y_true[mask] == y_pred[mask]).sum()
        guessed = (y_pred == i).sum()
        gold = (y_true == i).sum()
        if guessed == 0:
            prec = 1
        else:
            prec = correct / guessed
        if gold == 0:
            rec = 0
        else:
            rec = correct / gold
        if (prec + rec) == 0:
            f1 = 0
        else:
            f1 = 2 * prec * rec / (prec + rec)
        precisions.append(prec)
        recalls.append(rec)
        f1s.append(f1)
    
    precisions_np = np.asarray(precisions)
    recalls_np = np.asarray(recalls)
    f1_np = np.asarray(f1s)
    return precisions_np.mean(), recalls_np.mean(), f1_np.mean()

def p_r_f1_binary(y_true, y_pred):
    p =  precision_score(y_true, y_pred)
    r =  recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return p, r, f1