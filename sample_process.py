from Controller import Controller

import json

from sklearn.datasets import load_boston
from sklearn.metrics import r2_score


features, target = load_boston(return_X_y=True)
score_func = r2_score
with open('constructor.json', 'r') as fp:
    constructor_json = json.load(fp)

c = Controller(features=features,
               target=target,
               score_func=score_func,
               pipeline_constructor_json=constructor_json,
               pipelines_to_test=50)

