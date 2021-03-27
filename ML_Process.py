'''
This class will be responsible to receive the preprocessing algorithms and estimator from the controller,
create a dynamic pipeline, train, predict and score the pipeline, communicate back to the controller the results.
The ML Process saves the trained preprocessing algorithms and estimator to be used to restimate the model in the test period.

features_train =>
'''

class ML_Process:
  def __init__(self,
              features_train,
              features_test,
              label_train,
              label_test,
              estimator,
              pre_estimators,
              score):
    self.features_train = features_train
    self.features_test =  features_test
    self.label_train = label_train
    self.label_test = label_test
    self.estimator = estimator
    self.pre_estimators = pre_estimators
    self.score = score
  
  def train(self):
    x = self.feature_train
    y = self.label_train
    for pre in self.pre_estimators:
      pre.train(x=x, y=y)
      x, y = pre.transform(x=x, y=y)
    
    self.estimator.train(x=x, y=y)
                                   
  def score(self, train_or_test='test'):
    if train_or_test == 'test':
      x = self.features_test
      y = self.label_test
    else:
      x = self.feature_train
      y = self.label_train
      
    for pre in self.pre_estimators:
      x, y = pre.transform(x=x, y=y)
     
    y_hat = self.estimator(x=x, y=y)
    return self.score(y_hat=y_hat, y=y)
    
