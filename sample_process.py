from sklearn.feature_selection import VarianceThreshold, SelectKBest
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.metrics import r2_score
from Controller import Controller

'''
#to be inserted for reading user input json
#import json
#mlp_filename = "/content/ml_process.json"
#with open (mlp_filename) as access_json:
  #read_content = json.load(access_json)

#num_of_ppm = len(read_content['Preprocessing'])

#for preprocess_method in read_content['Preprocessing']:
  #print(preprocess_method['name'])
  #print(preprocess_method['parameter'])
#for ml_method in read_content['MLA']:
  #print(ml_method['name'])
  #print(ml_method['parameter'])
'''


features, target = load_boston(return_X_y=True)
vt = VarianceThreshold()
kbest = SelectKBest()
random_forest = RandomForestRegressor()
adaboost = AdaBoostRegressor()
score_func = r2_score

c = Controller(features=features,
               target=target,
               score_func=score_func,
               pre_estimators=[vt, kbest],
               estimators=[random_forest,adaboost],
               pipelines_to_test=5)
c.run_experiment()
