"""
Run evaluation with saved models.
"""

import yaml
from utils import  scorer
from utils.vocab import Vocab
import os
from data.loader import DataLoader

f = open(r'recent.eval.yml')
y = yaml.load(f)
print (y)

binary_path = '%s%d%s' % (y['binary_path'], y['binary_id'], '/predictions.txt')
binary_predictions = {}
data = open(binary_path, 'r')
_id = 0
for d in data:
    _id, r = d.split(' ')
    r = r.strip()
    _id = int(_id)
    binary_predictions[_id] = r


semantic_preditions = {}
data = open(y['semantic_file'], 'r')
for d in data:
    d = d.strip()
    _id, r = d.split(' ')
    _id = int(_id)
    semantic_preditions[_id] = r
print(11, len(semantic_preditions))

# use predicted relation overwrite the original relation
for type_id, exp_id in y.items():
    if not isinstance(type_id, int) :continue
for type_id in range(int(y['min_rel_id']), int(y['max_rel_id']) + 1):
    
    path = 'saved_models/%d-%d/' % (type_id, y['multiple_id'])
    p_file = path + 'predictions.txt'
    preds = open(p_file, 'r').readlines()
    for p in preds:
        p = p.strip()
        _id, r = p.split(' ')
        _id = int(_id)
        semantic_preditions[_id] = r

# Re-assign the semantic relation
for k, v in binary_predictions.items():
    if v != '':continue 
    if k in semantic_preditions:
        binary_predictions[k] = semantic_preditions[k]
    else:
        binary_predictions[k] = 'no_relation'


predictions = []
for i in range(0, len(binary_predictions)):
    assert binary_predictions[i] != ''
    predictions.append(binary_predictions[i])

gold = []
data = open(y['gold_file'], 'r')
for d in data:
    d = d.strip()
    gold.append(d)

if not os.path.exists('saved_models/X-%d-%d/' % (y['binary_id'],y['multiple_id'])):
    os.mkdir('saved_models/X-%d-%d/' % (y['binary_id'],y['multiple_id']))

out_file = 'saved_models/X-%d-%d/predictions.txt' % (y['binary_id'],y['multiple_id'])
out_f = open(out_file, 'w')
for i, p in enumerate(predictions):
    out_f.write('%d %s\n' % (i, p))

p, r, f1 = scorer.score(gold, predictions, verbose=True)
print("{} set evaluate result: {:.2f}\t{:.2f}\t{:.2f}".format('test',p,r,f1))


print("Evaluation ended.")

