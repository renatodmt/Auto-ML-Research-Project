# -*- coding: utf-8 -*-
"""UI_JSON.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xll4B1qU3G-JCiClQkqgrnqmeCPnYGam
"""

import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn import preprocessing as pre
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
import json 
from collections import defaultdict
from collections import ChainMap
mlp_filename = "/content/ml_process.json"

# creating Initial value
#init value for preprocessing JSON
#init_ppm_dict = [{"p_name":"Null", 
#                         "p_parameter":[{"sample":"Null"}]}]
init_mlp_dict = {"Preprocessing":[],"MLA":[]}
with open(mlp_filename, 'w') as json_file:
  json.dump(init_mlp_dict, json_file, indent=2)

#accessing dict files from JSON
#for Preprocessing Method JSON
newdata={}
with open (mlp_filename) as access_json:
  read_content = json.load(access_json)
  #temp1 = read_content['Preprocessing']
  #temp2 = read_content['MLA']

#for MLA JSON
with open (mlp_filename) as access_mla_json:
  read_mla_content = json.load(access_mla_json)

print (read_content)

#method to parse MLA to JSON
#method for KNN
def knn():
  mla_info = {"name":mla_name,
                "parameter": {"k_value":value}}
  read_content['MLA'].append(mla_info)

  with open(mlp_filename, "w") as f:
      json.dump(read_content, f, indent=2)

#method for RandomForest
def randomForest():

  mla_info = {"name":mla_name,
                "parameter": {"estimator": estimator, 
                                   "max_depth": max_depth}}
  read_content['MLA'].append(mla_info)

  with open(mlp_filename, "w") as f:
      json.dump(read_content, f, indent=2)

#method for AdaBoostRegressor
def adaBoostRegressor():

  mla_info = {"name":mla_name,
                "parameter": {"n_estimator": abr_n_estimator, 
                                   "loss": abr_loss}}
  read_content['MLA'].append(mla_info)

  with open(mlp_filename, "w") as f:
      json.dump(read_content, f, indent=2)

#Parse Preprocessing Method to JSON
def parseDict(s_name, s_parameter_name, s_param):
  preprocessing_info = {"name":s_name, 
                          "parameter":{s_parameter_name: s_param}}
  read_content['Preprocessing'].append(preprocessing_info)
  
  with open(mlp_filename , "w") as f:
      json.dump(read_content, f, indent=2)

#@title Preprocessing Option
pp_StandardScaler = True #@param {type:"boolean"}
si_with_std = "True" #@param ["True", "False"]
pp_Normalizer = True #@param {type:"boolean"}
si_norm = "l1" #@param ["l1", "l2", "max"]
pp_SimpleImputer = True #@param {type:"boolean"}
si_strategy = "most_frequent" #@param ["mean", "median", "most_frequent", "constant"]
pp_MinMaxScaler = True #@param {type:"boolean"}
mms_range = "20" #@param {type:"string"}
pp_Binarization = True #@param {type:"boolean"}
bin_threshold = "1" #@param {type:"string"}
pp_sample = True #@param {type:"boolean"}
sample = "1" #@param {type:"string"}
#@title Feature Selection
pp_VarianceThreshold = True #@param {type:"boolean"}
vt_threshold = "50" #@param {type:"string"}
pp_SelectKBest = True #@param {type:"boolean"}
skb_k_feat = "20" #@param {type:"string"}

if pp_StandardScaler == True:
  name = "StandardScaler"
  param_name = "with_std"
  param_value = si_with_std
  parseDict(name, param_name, param_value)

if pp_Normalizer == True:
  name = "Normalizer"
  param_name = "norm"
  param_value = si_norm
  parseDict(name, param_name, param_value)

if pp_SimpleImputer == True:
  name = "SimpleImputer"
  param_name = "strategy"
  param_value = si_strategy
  parseDict(name, param_name, param_value)

if pp_MinMaxScaler == True:
  name = "MinMaxScaler"
  param_name = "range"
  param_value = mms_range
  parseDict(name, param_name, param_value)

if pp_Binarization == True:
  name = "Binarization"
  param_name = "threshold"
  param_value = bin_threshold
  parseDict(name, param_name, param_value)

if pp_VarianceThreshold == True:
  name = "VarianceThreshold"
  param_name = "threshold"
  param_value = vt_threshold
  parseDict(name, param_name, param_value)

if pp_SelectKBest == True:
  name = "SelectKBest"
  param_name = "k_feat"
  param_value = skb_k_feat
  parseDict(name, param_name, param_value)

#@title Machine Learning Algorithm Option
mla_KNN = True #@param {type:"boolean"}
knn_k_value = "" #@param {type:"string"}
mla_RandomForest = True #@param {type:"boolean"}
rf_n_estimators = "2" #@param {type:"string"}
rf_max_depth = "2" #@param {type:"string"}
mla_AdaBoostRegressor = True #@param {type:"boolean"}
abr_n_estimators = "2" #@param {type:"string"}
abr_loss = "linear" #@param ["linear", "square", "exponential"]

if mla_KNN == True:
  mla_name = "KNN"
  value = knn_k_value
  knn()

if mla_RandomForest == True:
  mla_name = "RandomForest"
  estimator = rf_n_estimators
  max_depth = rf_max_depth
  randomForest()

if mla_AdaBoostRegressor == True:
  mla_name = "AdaBoostRegressor"
  abr_n_estimator = abr_n_estimators
  abr_loss = abr_loss
  adaBoostRegressor()
