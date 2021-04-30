#!/usr/bin/env python
# coding: utf-8


import json
filename = "../ML_Process_GUI/ml_process.json"
init_mlp_dict = {"pre-estimators":{},"estimators":{}}



# creating Initial value
init_mlp_dict = {"pre-estimators":{},"estimators":{}}

with open(filename, 'w') as json_file:
  json.dump(init_mlp_dict, json_file, indent=2)


with open (filename) as access_json:
  read_content = json.load(access_json)
print (read_content)



import PySimpleGUI as sg


def preestimator():
    sg.theme('SystemDefaultForReal')
    layout = [
    [sg.Frame(layout=[
        [sg.Checkbox('Standard Scaler', size=(14,1)),
         sg.Frame(layout=[[sg.Checkbox('True', default=True),
                           sg.Checkbox('False')]]
                  ,title='with_std',title_color='red', relief=sg.RELIEF_SUNKEN)],
        [sg.Checkbox('Normalizer', size=(14,1)),
         sg.Frame(layout=[[sg.Checkbox('l1', size=(3,1)),
                           sg.Checkbox('l2', default=True),
                           sg.Checkbox('max')]]
                  ,title='norm',title_color='red', relief=sg.RELIEF_SUNKEN)],
        
        [sg.Checkbox('SimpleImputer', size=(14,1)), 
         sg.Frame(layout=[[sg.Checkbox('mean'),  
                           sg.Checkbox('median', default=True),
                           sg.Checkbox('most_frequent'),
                           sg.Checkbox('constant')]]
                  ,title='strategy',title_color='red', relief=sg.RELIEF_SUNKEN)],
    
        [sg.Checkbox('MinMaxScaler', size=(14,1)),
         sg.Frame(layout=[[
             sg.Text('min'),
             sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=1),
             sg.Text('max'),sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=100)]]
                  ,title='MinMax Value',title_color='red', relief=sg.RELIEF_SUNKEN)],
        
        [sg.Checkbox('Binarization', size=(14,1)), 
         sg.Frame(layout=[[
             sg.Text('min'),
             sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=1),
             sg.Text('max'),sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=100)]]
                  ,title='threshold',title_color='red', relief=sg.RELIEF_SUNKEN)],
        
        [sg.Checkbox('VarianceThreshold', size=(14,1)),
         sg.Frame(layout=[[
             sg.Text('min'),
             sg.Slider(range=(0, 10), orientation='h', size=(14, 20), default_value=0),
             sg.Text('max'),sg.Slider(range=(0, 10), orientation='h', size=(14, 20), default_value=10)]]
                  ,title='threshold',title_color='red', relief=sg.RELIEF_SUNKEN)],
        
        [sg.Checkbox('SelectKBest', size=(14,1)),
         sg.Frame(layout=[[
             sg.Text('min'),
             sg.Slider(range=(1, 8), orientation='h', size=(14, 20), default_value=1),
             sg.Text('max'),sg.Slider(range=(1, 8), orientation='h', size=(14, 20), default_value=8)]]
                  ,title='k feat',title_color='red', relief=sg.RELIEF_SUNKEN)]
    ],title='Pre-Estimators',title_color='Blue', relief=sg.RELIEF_SUNKEN, tooltip='Use these to choose pre-estimators'),
    ],
    [sg.Button('Estimator'), sg.Button('Exit')]]
    return sg.Window('Machine Learning Process', layout, default_element_size=(40, 1), grab_anywhere=False, finalize=True)

    
    
    
def estimator():
    layout = [[sg.Frame(layout=[
        [sg.Checkbox('RandomForestRegressor', size=(19,1))], 
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
                          
                  ,title='RandomForestRegressor Parameters',title_color='red', relief=sg.RELIEF_SUNKEN)],
         
        [sg.Checkbox('Lasso', size=(14,1))],
         [sg.Frame(layout=[[sg.Text('Alpha :         '),
                           sg.Text('min'),
                           sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=1),
                           sg.Text('max'),sg.Slider(range=(1, 100), orientation='h', size=(14, 20), default_value=100)],
                           
                          [sg.Text('fit intercept : '),
                           sg.Checkbox('True', default=True),  
                           sg.Checkbox('False')],
                           
                         [sg.Text('normalize :   '),
                           sg.Checkbox('True', default=True),  
                           sg.Checkbox('False')]]
                  ,title='Parameter',title_color='red', relief=sg.RELIEF_SUNKEN)],
             ],title='Estimators',title_color='Blue', relief=sg.RELIEF_SUNKEN, tooltip='Use these to choose estimators')
        ],
        [sg.Button('Submit'), sg.Button('Exit')]]
    return sg.Window('Machine Learning Process', layout, default_element_size=(40, 1), grab_anywhere=False, finalize = True)

def parsePreestimators():
    pre_model = ['StandardScaler', 'Normalizer', 'SimpleImputer', 'MinMaxScale', 'Binarization', 'VarianceThreshold', 'SelectKBest']
            
    if values[0] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        standardScaler(i,pre_model)

    if values[3] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        normalizer(i, pre_model)
    
    if values[7] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        simpleImputer(i, pre_model)
   
    if values[12] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        minMaxScaler(i, pre_model)
    if values[15] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        binarization(i, pre_model)
    if values[18] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        varianceThreshold(i, pre_model)
    if values[21] == True:
        if not bool(read_content['pre-estimators']):
            i=0
        else:
            i+=1
        selectKBest(i, pre_model)


def standardScaler(index, pre_model):
    newlist = []
            
    if values[1] == True:
        newlist.append("True")
    if values[2] == True:
        newlist.append("False")
                
    preestimator_value = {index:{
            "model":pre_model[0], 
            "parameters":{"0":
                          {"name":"with_std",
                           "values":{"type":"list", 
                                     "list": newlist
                                    }
                          }
                         }
        }}
        
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)


def normalizer(index, pre_model):
    strl=[]
    norm = ['l1','l2','max']
    ran = 0
    for val in range(4,7): 
        if window.FindElement(val).get()==True:
            strl.append(norm[ran])
        ran+=1
            
    preestimator_value = {index:{
            "model":pre_model[1], 
            "parameters":{"0":
                          {"name":"with_std",
                           "values":{"type":"list", 
                                     "list": [strl]
                                    }
                          }
                         }
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)
        

def simpleImputer(index, pre_model):
    strl=[]
    strategy = ['mean','median','most_frequent', 'constant']
    ran = 0
    for val in range(8,12): 
        if window.FindElement(val).get()==True:
            strl.append(strategy[ran])
        ran+=1
            
    preestimator_value = {index:{
            "model":pre_model[2], 
            "parameters":{"0":
                          {"name":"with_std",
                           "values":{"type":"list", 
                                     "list": [strl]
                                    }
                          }
                         }
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)


def minMaxScaler(index, pre_model):
            
    preestimator_value = {index:{
            "model":pre_model[3], 
            "parameters":{"0":
                          {"name":"feature_range",
                           "values":{"type":"int", 
                                     "min": int(values[13]), 
                                     "max": int(values[14])
                                    }
                          }
                         }
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)

def binarization(index, pre_model):
            
    preestimator_value = {index:{
            "model":pre_model[4], 
            "parameters":{"0":
                          {"name":"threshold",
                           "values":{"type":"float", 
                                     "min": float(values[16]), 
                                     "max": float(values[17])
                                    }
                          }
                         }
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)

def varianceThreshold(index, pre_model):
            
    preestimator_value = {index:{
            "model":pre_model[5], 
            "parameters":{"0":
                          {"name":"threshold",
                           "values":{"type":"float", 
                                     "min": float(values[13]), 
                                     "max": float(values[14])
                                    }
                          }
                         }
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)

def selectKBest(index, pre_model):
            
    preestimator_value = {index:{
            "model":pre_model[6], 
            "parameters":{"0":
                          {"name":"k",
                           "values":{"type":"int", 
                                     "min": int(values[22]), 
                                     "max": int(values[23])
                                    }
                          }
                         }
        }}  
    read_content['pre-estimators'].update(preestimator_value)
        
    with open(filename, "w") as f:
        json.dump(read_content, f, indent=1)


def parseEstimators():
    ml_model = ['RandomForestRegressor', 'Lasso']
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
                                     "list": [strl]
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
                                     "list": [strlmf]
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
                           "values":{"type":"list", 
                                     "list": [strl]
                                    }
                          },
                          "2":
                          {"name":lasso_param[2],
                           "values":{"type":"list", 
                                     "list": [strl2]
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





