######To install this package with conda run one of the following:###
## conda install -c conda-forge pysimplegui
## conda install -c conda-forge/label/cf202003 pysimplegui

import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')


layout = [
    

###################################
##Frame Layout for Pre-Estimators##
###################################
    [sg.Frame(layout=[
        [sg.Checkbox('Standard Scaler', size=(12,1))],
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
     
     
###############################
##Frame Layout for Estimators##
###############################
     sg.Frame(layout=[
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
        
        
    
        
    ],title='Estimators',title_color='Blue', relief=sg.RELIEF_SUNKEN, tooltip='Use these to choose pre-estimators')
    ],
    
    
    
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

window = sg.Window('Machine Learning Process', layout, default_element_size=(40, 1), grab_anywhere=False)
event, values = window.read()
window.close()

sg.Popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values)
