"""
Run evaluation with saved models.
"""

import yaml
import  scorer
import os

f = open(r'recent.eval.yml')
y = yaml.load(f)
print (y)

docid2id = {}
data = open(y['docid2id_file'], 'r')
for d in data:
    _id, docid = d.split('\t')
    docid = docid.strip()
    docid2id[docid] = int(_id)

binary_path = '%s%s' % (y['binary_path'],  '/predictions.txt')
binary_predictions = {}
data = open(binary_path, 'r')
for d in data:
    docid, r = d.split('\t')
    r = r.strip()
    if r != 'no_relation':
        r = ''
    _id = docid2id[docid]
    _id = int(_id)
    binary_predictions[_id] = r


semantic_preditions = {}
data = open(y['semantic_file'], 'r')
for d in data:
    d = d.strip()
    _id, r = d.split(' ')
    _id = int(_id)
    semantic_preditions[_id] = r

# use predicted relation overwrite the original relation
for type_id in range(int(y['min_rel_id']), int(y['max_rel_id']) + 1):

    path = 'saved_models/depot-recent-%d/' % (type_id)
    p_file = path + 'predictions.txt'
    preds = open(p_file, 'r').readlines()
    for p in preds:
        p = p.strip()
        docid, r = p.split('\t')
        _id = docid2id[docid]
        semantic_preditions[_id] = r

# Re-assign from the predicted relation 
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

if not os.path.exists('saved_models/depot-all-recent/'):
    os.mkdir('saved_models/depot-all-recent/')

out_file = 'saved_models/depot-all-recent/predictions.txt'
out_f = open(out_file, 'w')
for i, p in enumerate(predictions):
    out_f.write('%d %s\n' % (i, p))

p, r, f1 = scorer.score(gold, predictions, verbose=True)
print("{} set evaluate result: {:.2f}\t{:.2f}\t{:.2f}".format('test',p,r,f1))


print("Evaluation ended.")

