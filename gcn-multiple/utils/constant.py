"""
Define constants.
"""
EMB_INIT_RANGE = 1.0

# vocab
PAD_TOKEN = '<PAD>'
PAD_ID = 0
UNK_TOKEN = '<UNK>'
UNK_ID = 1

VOCAB_PREFIX = [PAD_TOKEN, UNK_TOKEN]

# hard-coded mappings from fields to ids
SUBJ_NER_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'ORGANIZATION': 2, 'PERSON': 3}

OBJ_NER_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'PERSON': 2, 'ORGANIZATION': 3, 'DATE': 4, 'NUMBER': 5, 'TITLE': 6, 'COUNTRY': 7, 'LOCATION': 8, 'CITY': 9, 'MISC': 10, 'STATE_OR_PROVINCE': 11, 'DURATION': 12, 'NATIONALITY': 13, 'CAUSE_OF_DEATH': 14, 'CRIMINAL_CHARGE': 15, 'RELIGION': 16, 'URL': 17, 'IDEOLOGY': 18}

NER_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'O': 2, 'PERSON': 3, 'ORGANIZATION': 4, 'LOCATION': 5, 'DATE': 6, 'NUMBER': 7, 'MISC': 8, 'DURATION': 9, 'MONEY': 10, 'PERCENT': 11, 'ORDINAL': 12, 'TIME': 13, 'SET': 14}

POS_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'NNP': 2, 'NN': 3, 'IN': 4, 'DT': 5, ',': 6, 'JJ': 7, 'NNS': 8, 'VBD': 9, 'CD': 10, 'CC': 11, '.': 12, 'RB': 13, 'VBN': 14, 'PRP': 15, 'TO': 16, 'VB': 17, 'VBG': 18, 'VBZ': 19, 'PRP$': 20, ':': 21, 'POS': 22, '\'\'': 23, '``': 24, '-RRB-': 25, '-LRB-': 26, 'VBP': 27, 'MD': 28, 'NNPS': 29, 'WP': 30, 'WDT': 31, 'WRB': 32, 'RP': 33, 'JJR': 34, 'JJS': 35, '$': 36, 'FW': 37, 'RBR': 38, 'SYM': 39, 'EX': 40, 'RBS': 41, 'WP$': 42, 'PDT': 43, 'LS': 44, 'UH': 45, '#': 46}

DEPREL_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'punct': 2, 'compound': 3, 'case': 4, 'nmod': 5, 'det': 6, 'nsubj': 7, 'amod': 8, 'conj': 9, 'dobj': 10, 'ROOT': 11, 'cc': 12, 'nmod:poss': 13, 'mark': 14, 'advmod': 15, 'appos': 16, 'nummod': 17, 'dep': 18, 'ccomp': 19, 'aux': 20, 'advcl': 21, 'acl:relcl': 22, 'xcomp': 23, 'cop': 24, 'acl': 25, 'auxpass': 26, 'nsubjpass': 27, 'nmod:tmod': 28, 'neg': 29, 'compound:prt': 30, 'mwe': 31, 'parataxis': 32, 'root': 33, 'nmod:npmod': 34, 'expl': 35, 'csubj': 36, 'cc:preconj': 37, 'iobj': 38, 'det:predet': 39, 'discourse': 40, 'csubjpass': 41}

NEGATIVE_LABEL = 'no_relation'

ID_TO_TYPE_PAIR = {
    0: 'ORGANIZATION_PERSON',
    1: 'ORGANIZATION_COUNTRY',
    2: 'PERSON_PERSON',
    3: 'PERSON_COUNTRY',
    4: 'ORGANIZATION_ORGANIZATION',
    5: 'PERSON_CITY',
    6: 'PERSON_NATIONALITY',
    7: 'PERSON_ORGANIZATION',
    8: 'ORGANIZATION_LOCATION',
    9: 'PERSON_LOCATION',
    10: 'PERSON_STATE_OR_PROVINCE',
    11: 'PERSON_DATE',
    12: 'ORGANIZATION_DATE',
}

LABEL_TO_ID = {
    0: #ORGANIZATION_PERSON
    {
        'org:founded_by': 0,
        'org:shareholders': 1,
        'org:top_members/employees': 2,
    },
    1: #ORGANIZATION_COUNTRY
    {
        'org:country_of_headquarters': 0,
        'org:member_of': 1,
        'org:members': 2,
        'org:parents': 3,
        'org:subsidiaries': 4,
    },
    2: #PERSON_PERSON
    {
        'per:alternate_names': 0,
        'per:children': 1,
        'per:other_family': 2,
        'per:parents': 3,
        'per:siblings': 4,
        'per:spouse': 5,
    },
    3: #PERSON_COUNTRY
    {
        'per:countries_of_residence': 0,
        'per:country_of_birth': 1,
        'per:country_of_death': 2,
        'per:origin': 3,
    },
    4: #ORGANIZATION_ORGANIZATION
    {
        'org:alternate_names': 0,
        'org:member_of': 1,
        'org:members': 2,
        'org:parents': 3,
        'org:shareholders': 4,
        'org:subsidiaries': 5,
    },
    5: #PERSON_CITY
    {
        'per:cities_of_residence': 0,
        'per:city_of_birth': 1,
        'per:city_of_death': 2,
    },
    6: #PERSON_NATIONALITY
    {
        'per:countries_of_residence': 0,
        'per:country_of_birth': 1,
        'per:country_of_death': 2,
        'per:origin': 3,
    },
    7: #PERSON_ORGANIZATION
    {
        'per:employee_of': 0,
        'per:schools_attended': 1,
    },
    8: #ORGANIZATION_LOCATION
    {
        'org:city_of_headquarters': 0,
        'org:country_of_headquarters': 1,
        'org:member_of': 2,
        'org:parents': 3,
        'org:stateorprovince_of_headquarters': 4,
        'org:subsidiaries': 5,
    },
    9: #PERSON_LOCATION
    {
        'per:cities_of_residence': 0,
        'per:city_of_birth': 1,
        'per:city_of_death': 2,
        'per:countries_of_residence': 3,
        'per:country_of_birth': 4,
        'per:country_of_death': 5,
        'per:employee_of': 6,
        'per:origin': 7,
        'per:stateorprovince_of_death': 8,
        'per:stateorprovinces_of_residence': 9,
    },
    10: #PERSON_STATE_OR_PROVINCE
    {
        'per:stateorprovince_of_birth': 0,
        'per:stateorprovince_of_death': 1,
        'per:stateorprovinces_of_residence': 2,
    },
    11: #PERSON_DATE
    {
        'per:date_of_birth': 0,
        'per:date_of_death': 1,
    },
    12: #ORGANIZATION_DATE
    {
        'org:dissolved': 0,
        'org:founded': 1,
    },
}



INFINITY_NUMBER = 1e12
