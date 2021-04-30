"""
Why we need a custom model for this preprocessing?
Sklearn have a implementation that could possible break the application in case you pass a k greater than the number of
current features in the available features. This is possible, because we don't know at the moment that we running kbest
how many features we still have left in the pipeline.

Also, added in the wrapper a parameter to change the score function just passing a parameter.
"""

from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression


class CustomSelectKBest(SelectKBest):

    def set_params(self, **params):
        if 'score_func' in params.keys():
            if params['score_func'] == 'f_regression':
                params['score_func'] = f_regression
            elif params['score_func'] == 'mutual_info_regression':
                params['score_func'] = mutual_info_regression
        else:
            params['score_func'] = f_regression
        super().set_params(**params)
        return self

    def _check_params(self, X, y):
        pass

    def fit(self, X, y):
        if X.shape[1] < self.k:
            super().fit(X, y)
        return self

    def transform(self, X):
        if X.shape[1] < self.k:
            X = super().transform(X)
        return X