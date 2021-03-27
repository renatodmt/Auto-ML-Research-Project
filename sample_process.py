from sklearn.feature_selection import VarianceThreshold, SelectKBest
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.metrics import r2_score
from Controller import Controller


features, target = load_boston(return_X_y=True)
vt = VarianceThreshold()
kbest = SelectKBest()
random_forest = RandomForestRegressor()
adaboost = AdaBoostRegressor()
score_func = r2_score

Controller(features=features, target=target, score_func=score_func, pre_estimators=[vt, kbest], estimators=[random_forest,adaboost])
Controller.run_experiment()

