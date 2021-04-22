#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


from tkinter import *

#Creating object 'tk' of Tk()
tk = Tk()

#Providing Geometry to the form
tk.geometry("920x650")

#Providing title to the form
tk.title('Machine Learning Process')

#Form for preprocessing method and uses place() method.
label_0 =Label(tk,text="Preprocessing Method", width=20,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)


###################
#Standard Scaler
###################
chkVT = IntVar()
Checkbutton(tk, text="Standard Scaler", width=20,font=('bold',11), variable=chkVT).place(x=95,y=130)

#Parameter Label.
label_1 =Label(tk,text="with_std", width=20,font=("bold",10))
label_1.place(x=100,y=160)
    
#list of Parameter.
lstSSParam=[ 'True' ,'False']

#the variable 'c' mentioned here holds String Value, by default ""
lstWithStd=StringVar()
droplist=OptionMenu(tk,lstWithStd, *lstSSParam)
droplist.config(width=8)
lstWithStd.set('True')
droplist.place(x=240,y=160)



###################
#Normalizer
###################
chkNorm = IntVar()
Checkbutton(tk, text="Normalizer         ", width=20,font=('bold',11), variable=chkNorm).place(x=95,y=190)

#Parameter Label.
label_2 =Label(tk,text="norm", width=20,font=("bold",10))
label_2.place(x=100,y=220)
    
#list of parameter.
lstNormParam=[ 'l1' ,'l2', 'max']


lstNorm=StringVar()
droplist=OptionMenu(tk,lstNorm, *lstNormParam)
droplist.config(width=8)
lstNorm.set('l1')
droplist.place(x=240,y=220)


###################
#Simple Imputer
###################
chkSI = IntVar()
Checkbutton(tk, text="Simple Imputer   ", width=20,font=('bold',11), variable=chkSI).place(x=95,y=250)

#Parameter label.
label_3 =Label(tk,text="strategy", width=20,font=("bold",10))
label_3.place(x=100,y=280)
    
#List of Parameter.
lstSIParam=[ 'mean' ,'median', 'most_frequent', 'constant']


lstSI=StringVar()
droplist=OptionMenu(tk,lstSI, *lstSIParam)
droplist.config(width=8)
lstSI.set('mean')
droplist.place(x=240,y=280)


###################
#MinMaxScaler
###################
chkMMS = IntVar()
Checkbutton(tk, text="MinMaxScaler     ", width=20,font=('bold',11), variable=chkMMS).place(x=95,y=310)

#Parameter label.
label_4 =Label(tk,text="range", width=20,font=("bold",10))
label_4.place(x=100,y=340)
    
#Parameter Input.
rangeMMS=Entry(tk)
rangeMMS.place(x=240,y=340)


###################
#Binarization
###################
chkBin = IntVar()
Checkbutton(tk, text="Binarization         ", width=20,font=('bold',11), variable=chkBin).place(x=95,y=370)
#Parameter label.
label_5 =Label(tk,text="threshold", width=20,font=("bold",10))
label_5.place(x=110,y=400)
    
#Parameter Input.
thresholdBin=Entry(tk)
thresholdBin.place(x=240,y=400)


###################
#Variance Threshold
###################
chkVT = IntVar()
Checkbutton(tk, text="Variance Threshold", width=20,font=('bold',11), variable=chkVT).place(x=100,y=430)
#Parameter label.
label_6 =Label(tk,text="threshold", width=20,font=("bold",10))
label_6.place(x=110,y=460)
    
#Parameter Input.
thresholdVT=Entry(tk)
thresholdVT.place(x=240,y=460)


###################
#Select KBest
###################
chkKBest = IntVar()
Checkbutton(tk, text="SelectKBest        ", width=20,font=('bold',11), variable=chkKBest).place(x=95,y=490)
#Parameter label.
label_7 =Label(tk,text="k_feat  ", width=20,font=("bold",10))
label_7.place(x=110,y=520)
    
#Parameter Input.
k_feat=Entry(tk)
k_feat.place(x=240,y=520)






############################################
#####       Machine Learning Model     #####
############################################

#this creates 'Label' widget for Registration Form and uses place() method.
label_8 =Label(tk,text="Machine Learning Model", width=20,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_8.place(x=500,y=60)

###################
#KNN
###################
chkKNN = IntVar()
Checkbutton(tk, text="KNN                  ", width=20,font=('bold',11), variable=chkKNN).place(x=490,y=130)

#Parameter Label.
label_9 =Label(tk,text="k_value", width=20,font=("bold",10))
label_9.place(x=500,y=160)
    
#Parameter Input.
k_value=Entry(tk)
k_value.place(x=650,y=160)


###################
#RandomForest
###################
chkRForest = IntVar()
Checkbutton(tk, text="RandomForest  ", width=20,font=('bold',11), variable=chkRForest).place(x=490,y=190)

#Parameter Label.
label_10 =Label(tk,text="n_estimator", width=20,font=("bold",10))
label_10.place(x=510,y=220)
    
#Parameter Input.
n_estimatorRF=Entry(tk)
n_estimatorRF.place(x=650,y=220)

#Parameter Label.
label_11 =Label(tk,text="max_depth", width=20,font=("bold",10))
label_11.place(x=510,y=250)
    
#Parameter Input.
max_depth=Entry(tk)
max_depth.place(x=650,y=250)


###################
#AdaBoostRegressor
###################
chkAdaBoost = IntVar()
Checkbutton(tk, text="AdaBoostRegressor", width=20,font=('bold',11), variable=chkAdaBoost).place(x=502,y=280)

#Parameter Label.
label_12 =Label(tk,text="n_estimator", width=20,font=("bold",10))
label_12.place(x=510,y=310)

#Parameter Input.
n_estimatorABR=Entry(tk)
n_estimatorABR.place(x=650,y=310)


###################
#this creates button for submitting the details provides by the user


Button(tk, text='Submit' , width=20, font =('bold',12), height = 1, bg="black",fg='white').place(x=360,y=570)

#this will run the mainloop.
tk.mainloop()


# In[ ]:





# In[ ]:




