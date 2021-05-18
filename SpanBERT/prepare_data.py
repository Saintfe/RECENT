import json
import os

in_path = './dataset/tacred'
out_path = './dataset/tacred/entity_type_restriction'


file_name = in_path + '/test.json'
with open(file_name, 'r') as f:
    data = json.load(f)

gold_relations = []
docid2id = []
for index, d in enumerate(data):
    r = d['relation']
    gold_relations.append(r+'\n')
    docid2id.append('%d\t%s\n' % (index, d['id']))

out_file = in_path + '/test_gold_relations.txt'
out_f = open(out_file, 'w')
out_f.writelines(gold_relations)
out_f.close()

out_file = in_path + '/docid2id.txt'
out_f = open(out_file, 'w')
out_f.writelines(docid2id)
out_f.close()

for data_type in ['train', 'dev', 'test']:

    print('prepare %s set ...' % data_type)

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    so = [
            ('PERSON', 'TITLE'),
            ('PERSON', 'RELIGION'),
            ('PERSON', 'NUMBER'),
            ('ORGANIZATION', 'URL'),
            ('ORGANIZATION', 'CITY'),
            ('ORGANIZATION', 'NUMBER'),
            ('ORGANIZATION', 'RELIGION'),
            ('PERSON', 'DURATION'),
            ('PERSON', 'CAUSE_OF_DEATH'),
            ('PERSON', 'MISC'),
            ('PERSON', 'CRIMINAL_CHARGE'),
            ('ORGANIZATION', 'IDEOLOGY'),
            ('ORGANIZATION', 'MISC')
        ]

    file_name = '%s/%s.json' % (in_path, data_type)
    with open(file_name, 'r') as f:
        data = json.load(f)

    so2samples = {}
    so2reltion = {}
    for i, d in enumerate(data):
        if data_type == 'test':
            d['order_id'] = i
        r = d['relation']
        s = d['subj_type']
        o = d['obj_type']
        t = (s,o)
        if t not in so2reltion:
            so2reltion[t] = set((r,))
        else:
            so2reltion[t].add(r)
        if r == 'no_relation':
            continue
        if t not in so2samples:
            so2samples[t] = [d]
        else:
            so2samples[t].append(d)
    num_samples = 0

    out_file = out_path + '/semantic_relations.txt' 
    out_f = open(out_file, 'w')
    for t, samples in so2samples.items():


        if len(so2reltion[t]) == 2: 
            r = so2reltion[t]
            r.remove('no_relation')
            r = r.pop()
            if data_type == 'test':
                for s in samples:
                    out_f.write('%d %s\n' % (s['order_id'], r))
            continue

        (s,o) = t 
        num_samples += len(samples)
        # print("number of samples %s_%s:" % (  s, o), len(samples))
        print("%s_%s" % (s,o))
        file_name = "%s/%s_%s_%s.json" % (out_path, s, o, data_type)
        with open(file_name, 'w') as f:
             json.dump(samples, f)
        if data_type == 'train':
            file_name = "%s/%s_%s_relation.txt" % (out_path, s, o)
            with open(file_name, 'w') as f:
                 rel = list(so2reltion[t])
                 rel.sort()
                 rel = [r + '\n' for r in rel]
                 f.writelines(rel[1:])

    print('prepare %s set ends' % data_type)
print('prepare data ends')

