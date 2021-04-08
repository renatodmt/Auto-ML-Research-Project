"""
The controller will be responsible to get inputs from the user and run the experiment. 
Information such as what are the preprocessing algorithms, models, how many ML process
to run or the time to take into the experiment. After the experiment runs, the controller will
responsible to save and communicate the results.

Glossary:
Experiment -> Test different ML process to find the best for a given dataset and problem.
ML Process -> Combination of Preprocessing Algorithms and Model to get to a prediction.
"""
import random
from MLProcess import MLProcess


class Controller:
    def __init__(self, features, target, score_func, pre_estimators, estimators, pipelines_to_test):
        self.features = features  # The features of your dataset
        self.target = target  # y part of your dataset
        self.score_func = score_func  # Function that you pass y and y_hat and return a score (example MAPE)
        self.pre_estimators = pre_estimators  # List of pre_estimators objects that you want to test
        self.estimators = estimators  # List of estimators that you want to test
        self.pipelines_to_test = pipelines_to_test  # Number of pipelines that will be tested

    def run_experiment(self):
        """
        Create pipelines at random score it and save the best pipeline in the object
        """
        # TODO: Split train and test
        X_train = self.features
        y_train = self.target
        X_test = self.features
        y_test = self.target
        max_score = -float('inf')

        for i in range(self.pipelines_to_test):
            n_pre_estimators = random.randint(1, len(self.pre_estimators))
            pre_estimators = random.sample(self.pre_estimators, n_pre_estimators)
            estimator = random.choice(self.estimators)
            print(estimator)
            print(pre_estimators)
            pipeline = MLProcess(estimator,
                                 pre_estimators,
                                 self.score_func)
            pipeline.fit(X=X_train, y=y_train)
            score = pipeline.score(X=X_test, y=y_test)
            print(score)
            if score > max_score:
                self.pipeline = pipeline

    def show_results(self):
        pass