#!/usr/bin/env python
# coding: utf-8

import json
import PySimpleGUI as sg

filename = "constructor.json"
init_mlp_dict = {"pre-estimators":{},"estimators":{}}


# creating Initial value
init_mlp_dict = {"pre-estimators":{},"estimators":{}}

with open(filename, 'w') as json_file:
  json.dump(init_mlp_dict, json_file, indent=2)


with open (filename) as access_json:
  read_content = json.load(access_json)


def preestimator():
    sg.theme('Dark Blue 3')
    layout = [
    [sg.Frame(layout=[
        [sg.Checkbox('Standard Scaler', size=(14,1))],
        
        [sg.Checkbox('MinMaxScaler', size=(14,1))],
        
        [sg.Checkbox('SimpleImputer', size=(14,1)), 
         sg.Frame(layout=[[sg.Checkbox('mean'),  
                           sg.Checkbox('median', default=True),
                           sg.Checkbox('most_frequent'),
                           sg.Checkbox('constant')]]
                  ,title='strategy', relief=sg.RELIEF_SUNKEN)],
    
        
        [sg.Checkbox('VarianceThreshold', size=(14,1)),
         sg.Frame(layout=[[
             sg.Text('min'),
             sg.Slider(range=(0, 20), orientation='h', size=(14, 16), default_value=0),
             sg.Text('max'),sg.Slider(range=(0, 20), orientation='h', size=(14, 16), default_value=10)]]
                  ,title='threshold', relief=sg.RELIEF_SUNKEN)],
        
        [sg.Checkbox('SelectKBest', size=(14,1)),
         sg.Frame(layout=[[
             sg.Text('K value:   '),
             sg.Text('min'),
             sg.Slider(range=(1, 20), orientation='h', size=(10, 16), default_value=1),
             sg.Text('max'),sg.Slider(range=(1, 20), orientation='h', size=(10, 16), default_value=10)],
             [sg.Text('Function:'),sg.Checkbox('f_regression'), sg.Checkbox('mutual_info_regression')]
         ]
                  ,title='Parameters', relief=sg.RELIEF_SUNKEN)],
        
        [sg.Checkbox('RFE', size=(14,1)),
         sg.Frame(layout=[
             [sg.Text('step:                        '),
              sg.Text('min: '),
              sg.InputText('0', size=(7, 16)), 
              sg.Text('max: '),
              sg.InputText('10', size=(7, 16))],
             [sg.Text('n_features_to_select:'),
              sg.Text('min: '),
              sg.InputText('0', size=(7, 16)), 
              sg.Text('max: '),
              sg.InputText('10', size=(7, 16))]
             
             
         ]
                  ,title='Parameters', relief=sg.RELIEF_SUNKEN)],
        
    ],title='Pre-Estimators', relief=sg.RELIEF_SUNKEN, tooltip='Use these to choose pre-estimators'),
    ],
    [sg.Button('Estimator'), sg.Button('Exit')]]
    
    return sg.Window('Machine Learning Process', layout, default_element_size=(40, 1), grab_anywhere=False, finalize=True)


colEstimator = [[sg.Checkbox('RandomForestRegressor', size=(19,1))], 
         [sg.Frame(layout=[[sg.Text('n_estimators:       '),
                           sg.Text('min'),
                           sg.Slider(range=(1, 1000), orientation='h', size=(14, 20), default_value=1),
                           sg.Text('max'),sg.Slider(range=(1, 1000), orientation='h', size=(14, 20), default_value=1000)
                          ],
                          
                          [sg.Text('criterion:              '),
                           sg.Checkbox('mse'),  
                           sg.Checkbox('mae', default=True)
                          ],
                          
                          [sg.Text('max_depth:          '),
                           sg.Text('min'),
                           sg.Slider(range=(2, 13), orientation='h', size=(14, 20), default_value=2),
                           sg.Text('max'),sg.Slider(range=(2, 13), orientation='h', size=(14, 20), default_value=13)
                          ],
                          
                          [sg.Text('min_samples_leaf:'),
                           sg.Text('min'),
                           sg.Slider(range=(1, 250), orientation='h', size=(14, 20), default_value=1),
                           sg.Text('max'),sg.Slider(range=(1, 250), orientation='h', size=(14, 20), default_value=250)
                          ],
                          
                          [sg.Text('max_features:       '),
                           sg.Checkbox('auto', default=True),  
                           sg.Checkbox('sqrt'),
                           sg.Checkbox('log2')
                          ]
                         ]
                          
                  ,title='Parameters')],
         
        [sg.Checkbox('Lasso', size=(14,1))],
         [sg.Frame(layout=[[sg.Text('Alpha :               '),
                           sg.Text('min'),
                           sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=1),
                           sg.Text('max'),sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=100)],
                           
                          [sg.Text('Fit_intercept :    '),
                           sg.Checkbox('True', default=True),  
                           sg.Checkbox('False'),
                            
                           sg.Text('   Normalize  : ', ),
                           sg.Checkbox('True', default=True),  
                           sg.Checkbox('False')],
                          ]
                  ,title='Parameters')],
        
        [sg.Checkbox('LinearRegression', size=(14,1), key = 'LinearRegression')],
         [sg.Frame(layout=[[sg.Text('Fit_intercept :    '),
                            sg.Checkbox('True', default=True, key='lr_fit_true'),  
                            sg.Checkbox('False', key='lr_fit_false'),
                            
                            sg.Text('   Normalize  : ', ),
                            sg.Checkbox('True', default=True, key='lr_norm_true'),  
                            sg.Checkbox('False', key='lr_norm_false')],
                           
                          ]
                  ,title='Parameters')],
       
        [sg.Checkbox('AdaBoostRegressor', size=(14,1), key='AdaBoostRegressor')],
         [sg.Frame(layout=[[sg.Text('n_estimators :     '),
                           sg.Text('min'),
                           sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=1, key='abr_n_esti_min'),
                           sg.Text('max'),
                           sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=50, key='abr_n_esti_max')],
                           
                           [sg.Text('Learning Rate:     '),
                           sg.Text('min: '),
                           sg.InputText('0', size=(16, 16), key='abr_lr_min'), 
                           sg.Text('max: '),
                           sg.InputText('1', size=(16, 16), key='abr_lr_max')]
                          ]
                  ,title='Parameters')],
       
        [sg.Checkbox('KNeighborsRegressor', size=(19,1), key = 'KNeighborsRegressor')], 
         [sg.Frame(layout=[[sg.Text('n_neighbors:       '),
                           sg.Text('min'),
                           sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=1, key='knr_n_neighbors_min'),
                           sg.Text('max'),
                           sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=5, key='knr_n_neighbors_max')
                          ],
                          
                          [sg.Text('weights:              '),
                           sg.Checkbox('uniform', key='knr_w_uniform'),  
                           sg.Checkbox('distance', key='knr_w_distance')
                          ],
                                                   
                          [sg.Text('algorithm:         '),
                           sg.Checkbox('auto', default=True, key = 'knr_algo_auto'),  
                           sg.Checkbox('ball_tree', key='knr_algo_ball_tree'),
                           sg.Checkbox('kd_tree', key='knr_algo_kd_tree'),
                           sg.Checkbox('brute', key='knr_algo_brute')
                          ]
                         ]
                          
                  ,title='Parameters')]]

def estimator():
    layout = [[sg.Column(colEstimator, size=(510, 500), scrollable=True)],
        [sg.Button('Submit'), sg.Button('Exit')]]

    return sg.Window('Estimators', layout, grab_anywhere=False, finalize=True)


def parsePreestimators():
    pre_model = ['StandardScaler', 'MinMaxScale', 'SimpleImputer', 'VarianceThreshold', 'SelectKBest', 'RFE']
            
    if values[0] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        standardScaler(i,pre_model)
    
    if values[1] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        minMaxScaler(i,pre_model)
    
    if values[2] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        simpleImputer(i, pre_model)
   
    if values[7] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        varianceThreshold(i, pre_model)
        
    if values[10] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        selectKBest(i, pre_model)
    
    if values[15] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        rfe(i, pre_model)




def standardScaler(index, pre_model):
                
    preestimator_value = {index:{
            "model":pre_model[0]
        }}
        
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)


def simpleImputer(index, pre_model):
    si_List=[]
    strategy = ['mean','median','most_frequent', 'constant']
    i = 0
    for val in range(3,7): 
        if window.FindElement(val).get()==True:
            si_List.append(strategy[i])
        i+=1
            
    preestimator_value = {index:{
            "model":pre_model[1], 
            "parameters":{"0":
                          {"name":"strategy",
                           "values":{"type":"list", 
                                     "list": si_List
                                    }
                          }
                         }
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)


def minMaxScaler(index, pre_model):
            
    preestimator_value = {index:{
            "model":pre_model[2]
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)


def varianceThreshold(index, pre_model):
            
    preestimator_value = {index:{
            "model":pre_model[3], 
            "parameters":{"0":
                          {"name":"threshold",
                           "values":{"type":"float", 
                                     "min": float(values[8]), 
                                     "max": float(values[9])
                                    }
                          }
                         }
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)

def selectKBest(index, pre_model):
    skb_List=[]
    function = ['f_regression', 'mutual_info_regression']
    i = 0
    for val in range(13,15): 
        if window.FindElement(val).get()==True:
            skb_List.append(function[i])
        i+=1
        
    preestimator_value = {index:{
            "model":pre_model[4], 
            "parameters":{"0":
                          {"name":"k",
                           "values":{"type":"int", 
                                     "min": int(values[11]), 
                                     "max": int(values[12])
                                    }
                          },
                          "1":
                          {"name": "function",
                           "values":{"type":"list", 
                                     "list": skb_List
                                    }
                              
                          }
                          }
                         }
        }  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)
        
        
def rfe(index, pre_model):
            
    preestimator_value = {index:{
            "model":pre_model[5], 
            "parameters":{"0":
                          {"name":"threshold",
                           "values":{"type":"float", 
                                     "min": float(values[16]), 
                                     "max": float(values[17])
                                    }
                          },
                          "1":
                          {"name":"threshold",
                           "values":{"type":"float", 
                                     "min": float(values[18]), 
                                     "max": float(values[19])
                                    }
                          }
                         }
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)




def parseEstimators():
    ml_model = ['RandomForestRegressor', 'Lasso', 'LinearRegression', 'AdaBoostRegressor', 'KNeighborsRegressor']
    rfr_parameters = ['n_estimators', 'criterion', 'max_depth', 'min_sample_leaf', 'max_features']
    max_features = ['auto', 'sqrt', 'log2']        
    lasso_param = ['alpha', 'fit_intercept', 'normalize']
    if values[0] == True:
        if not bool(read_content['estimators']):
            j=0
        else:
            j+=1
        randomForestReg(j,ml_model, rfr_parameters)
    
    if values[12] == True:
        if not bool(read_content['estimators']):
            j=0
        else:
            j+=1
        lasso(j,ml_model, lasso_param)
    
    if values['LinearRegression'] == True:
        if not bool(read_content['estimators']):
            j=0
        else:
            j+=1
        linearRegression(j,ml_model)
    
    if values['AdaBoostRegressor'] == True:
        if not bool(read_content['estimators']):
            j=0
        else:
            j+=1
        adaBoostRegressor(j,ml_model)
        
    if values['KNeighborsRegressor'] == True:
        if not bool(read_content['estimators']):
            j=0
        else:
            j+=1
        kNeighborsRegressor(j,ml_model)




def randomForestReg(index, ml_model,rfr_param):
    strl=[]
    criterion = ['mse', 'mae']
    ran = 0
    for val in range(3,5): 
        if window.FindElement(val).get()==True:
            strl.append(criterion[ran])
        ran+=1
    
    mf_ran = 0
    strlmf = []
    max_feat = ['auto', 'sqrt', 'log2']
    for val in range(9,12): 
        if window.FindElement(val).get()==True:
            strlmf.append(max_feat[mf_ran])
        mf_ran+=1
    estimator_value = {index:{
            "model":ml_model[index], 
            "parameters":{"0":
                          {"name":rfr_param[0],
                           "values":{"type":"int", 
                                     "min": int(values[1]), 
                                     "max": int(values[2])
                                    }
                          },
                          "1":
                          {"name":rfr_param[1],
                           "values":{"type":"list", 
                                     "list": strl
                                    }
                          },
                          "2":
                          {"name":rfr_param[2],
                           "values":{"type":"int", 
                                     "min": int(values[5]), 
                                     "max": int(values[6])
                                    }
                          },
                          "3":
                          {"name":rfr_param[3],
                           "values":{"type":"int", 
                                     "min": int(values[7]), 
                                     "max": int(values[8])
                                    }
                          },
                          "4":
                          {"name":rfr_param[4],
                           "values":{"type":"list", 
                                     "list": strlmf
                                    }
                          }
                         }
        }}  
    read_content['estimators'].update(estimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)
    
    
def lasso(index, ml_model, lasso_param): 
    bool_val = ['True', 'False']
    strl=[]
    strl2=[]
    ran = 0
    ran2 = 0
    for val in range(15,17): 
        if window.FindElement(val).get()==True:
            strl.append(bool_val[ran])
        ran+=1
     
    for val in range(15,17): 
        if window.FindElement(val).get()==True:
            strl2.append(bool_val[ran2])
        ran2+=1
        
    estimator_value = {index:{
            "model":ml_model[1], 
            "parameters":{"0":
                          {"name":lasso_param[0],
                           "values":{"type":"int", 
                                     "min": int(values[13]), 
                                     "max": int(values[14])
                                    }
                          },
                          "1":
                          {"name":lasso_param[1],
                           "values":{"type":"boolean", 
                                     "list": strl
                                    }
                          },
                          "2":
                          {"name":lasso_param[2],
                           "values":{"type":"boolean", 
                                     "list": strl2
                                    }
                          }
                          }
        }}  
    read_content['estimators'].update(estimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)
                

def linearRegression(index, ml_model): 
    bool_value=['True', 'False']
    lr_fit=[]
    lr_norm=[]

    if values['lr_fit_true']==True:
        lr_fit.append(bool_value[0])
    if values['lr_fit_false']==True:
        lr_fit.append(bool_value[1])
    
    if values['lr_norm_true']==True:
        lr_norm.append(bool_value[0])
    if values['lr_norm_false']==True:
        lr_norm.append(bool_value[1])
        
        
    estimator_value = {index:{
            "model":ml_model[2], 
            "parameters":{"0":
                          {"name":'fit_intercept',
                           "values":{"type":"boolean",
                                     "list":lr_fit
                                    }
                          },
                          "1":
                          {"name":'normalize',
                           "values":{"type":"boolean", 
                                     "list": lr_norm
                                    }
                          }
                          }
        }}  
    read_content['estimators'].update(estimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)
        

def adaBoostRegressor(index, ml_model): 
        
    estimator_value = {index:{
            "model":ml_model[3], 
            "parameters":{"0":
                          {"name":'n_estimators',
                           "values":{"type":"int", 
                                     "min": int(values['abr_n_esti_min']), 
                                     "max": int(values['abr_n_esti_max'])
                                    }
                          },
                          "1":
                          {"name":'learning_rate',
                           "values":{"type":"int", 
                                     "min": float(values['abr_lr_min']), 
                                     "max": float(values['abr_lr_max'])
                                    }
                          }
                          }
        }}  
    read_content['estimators'].update(estimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)
                

def kNeighborsRegressor(index, ml_model): 
    knr_weights=[]
    knr_algorithm=[]

    if values['knr_w_uniform']==True:
        knr_weights.append('uniform')
    if values['knr_w_distance']==True:
        knr_weights.append('distance')
    
    if values['knr_algo_auto']==True:
        knr_algorithm.append('auto')
    if values['knr_algo_ball_tree']==True:
        knr_algorithm.append('ball_tree')
    if values['knr_algo_kd_tree']==True:
        knr_algorithm.append('kd_tree')
    if values['knr_algo_brute']==True:
        knr_algorithm.append('brute')
        
        
    estimator_value = {index:{
            "model":ml_model[4], 
            "parameters":{"0":
                          {"name":'n_neighbors',
                           "values":{"type":"int", 
                                     "min": int(values['knr_n_neighbors_min']), 
                                     "max": int(values['knr_n_neighbors_max'])
                                    }
                          },
                          "1":
                          {"name":'weights',
                           "values":{"type":"list",
                                     "list":knr_weights
                                    }
                          },
                          "2":
                          {"name":'algorithm',
                           "values":{"type":"list", 
                                     "list": knr_algorithm
                                    }
                          }
                          }
        }}  
    read_content['estimators'].update(estimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)
        


window1  = preestimator()
window2 = None        # start off with 1 window open
while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    
    if event in (sg.WIN_CLOSED, 'Exit'):
        window.close()
        if window == window1:
            break
        elif window == window2:
            window2 = None

    if event == 'Estimator':
        parsePreestimators()
        window2 = estimator()

    elif event == 'Submit':
        parseEstimators()
        window1.close()
        window2.close()


