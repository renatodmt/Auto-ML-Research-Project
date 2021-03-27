import sklearn.feature_selection as sk_feat

class VarianceThreshold:
  def __init__(self,
               params):
    self.variance_threshold = sk_feat.VarianceThreshold()
    self.variance_threshold.set_params(**params)
  
  def train(x, y):
    self.variance_threshold.fit(x)
  
  def transform(x, y):
    return self.variance_threshold.transform(x), y
