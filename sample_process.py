from Controller import Controller
from datetime import datetime
import json
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score

file_path = 'Boston.csv'
dataset = pd.read_csv(file_path, index_col=False)
features = dataset.drop(labels=['medv'], axis=1)
# features.replace({'?':0}, inplace=True)
target = dataset['medv']

test_size = 0.2

# features, target = load_boston(return_X_y=True)

score_func = r2_score
with open('constructor.json', 'r') as fp:
    constructor_json = json.load(fp)

c = Controller(features=features,
               target=target,
                test_size = test_size,
               score_func=score_func,
               pipeline_constructor_json=constructor_json,
               pipelines_to_test=10)

results_df = pd.DataFrame(c.results)
results_df.to_csv(f"{str(datetime.today()).replace(' ', '_').replace(':', '_').replace('-', '_').replace('.', '_')}_result.csv")



