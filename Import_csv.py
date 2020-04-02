#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:46:04 2019

@author: atit
"""
import numpy as np
import pandas as pd
from scipy.special import entr
from pandas import Series
from statsmodels.tsa.ar_model import AR
import xlsxwriter 


def mean(value):
    return np.mean(value)

def stdev(value):
    return np.std(value)

def mini(value):
    return np.min(value)

def maxi(value):
    return np.max(value)

def ent(value):
    return entr(value).sum()

def arcoff(value):
    ser = pd.Series(value)
    train, test = ser[1:int(len(ser)*0.6)], ser[int(len(ser)*0.6):]
    model = AR(train)
    model_fit = model.fit()
    predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
    return np.average(predictions)

def m_a_d(value):
    
    series = pd.Series(value) 
    return series.mad() 
    
def
emg1_mean = []
emg1_stdev = []
emg1_mini = []
emg1_maxi = []
emg1_ent = []
emg1_arcoff = []
emg1_mad = []

emg2_mean = []
emg2_stdev = []
emg2_mini = []
emg2_maxi = []
emg2_ent = []
emg2_arcoff = []
emg2_mad = []

emg3_mean = []
emg3_stdev = []
emg3_mini = []
emg3_maxi = []
emg3_ent = []
emg3_arcoff = []
emg3_mad = []

emg4_mean = []
emg4_stdev = []
emg4_mini = []
emg4_maxi = []
emg4_ent = []
emg4_arcoff = []
emg4_mad = []

ab_mean = []
ab_stdev = []
ab_mini = []
ab_maxi = []
ab_ent = []
ab_arcoff = []
ab_mad = []

aux_mean = []
aux_stdev = []
aux_mini = []
aux_maxi = []
aux_ent = []
aux_arcoff = []
aux_mad = []

auy_mean = []
auy_stdev = []
auy_mini = []
auy_maxi = []
auy_ent = []
auy_arcoff = []
auy_mad = []

auz_mean = []
auz_stdev = []
auz_mini = []
auz_maxi = []
auz_ent = []
auz_arcoff = []
auz_mad = []

gox_mean = []
gox_stdev = []
gox_mini = []
gox_maxi = []
gox_ent = []
gox_arcoff = []
gox_mad = []

alx_mean = []
alx_stdev = []
alx_mini = []
alx_maxi = []
alx_ent = []
alx_arcoff = []
alx_mad = []

aly_mean = []
aly_stdev = []
aly_mini = []
aly_maxi = []
aly_ent = []
aly_arcoff = []
aly_mad = []

alz_mean = []
alz_stdev = []
alz_mini = []
alz_maxi = []
alz_ent = []
alz_arcoff = []
alz_mad = []

goy_mean = []
goy_stdev = []
goy_mini = []
goy_maxi = []
goy_ent = []
goy_arcoff = []
goy_mad = []

gux_mean = []
gux_stdev = []
gux_mini = []
gux_maxi = []
gux_ent = []
gux_arcoff = []
gux_mad = []

guy_mean = []
guy_stdev = []
guy_mini = []
guy_maxi = []
guy_ent = []
guy_arcoff = []
guy_mad = []

guz_mean = []
guz_stdev = []
guz_mini = []
guz_maxi = []
guz_ent = []
guz_arcoff = []
guz_mad = []

glx_mean = []
glx_stdev = []
glx_mini = []
glx_maxi = []
glx_ent = []
glx_arcoff = []
glx_mad = []

gly_mean = []
gly_stdev = []
gly_mini = []
gly_maxi = []
gly_ent = []
gly_arcoff = []
gly_mad = []

glz_mean = []
glz_stdev = []
glz_mini = []
glz_maxi = []
glz_ent = []
glz_arcoff = []
glz_mad = []



    



data_train = pd.read_csv("challenge.csv") 
train_matrix = data_train.as_matrix()
file_path = np.array(train_matrix[0:400,1])
x = file_path.shape[0]
for i in range(x):
    reading_val = pd.read_csv(file_path[i],header=None)
    value_matrix = reading_val.as_matrix()
    r,c = value_matrix.shape
    
    emg1 = np.array(value_matrix[0:r,0])
    emg1_mean.append(mean(emg1))
    emg1_stdev.append(stdev(emg1))
    emg1_mini.append(mini(emg1))
    emg1_maxi.append(maxi(emg1))
    emg1_ent.append(ent(emg1))
    emg1_arcoff.append(arcoff(emg1))
    emg1_mad.append(m_a_d(emg1))
    

    emg2 = np.array(value_matrix[0:r,1])
    emg2_mean.append(mean(emg2))
    emg2_stdev.append(stdev(emg2))
    emg2_mini.append(mini(emg2))
    emg2_maxi.append(maxi(emg2))
    emg2_ent.append(ent(emg2))
    emg2_arcoff.append(arcoff(emg2))
    emg2_mad.append(m_a_d(emg2))
    
    emg3 = np.array(value_matrix[0:r,2])
    emg3_mean.append(mean(emg3))
    emg3_stdev.append(stdev(emg3))
    emg3_mini.append(mini(emg3))
    emg3_maxi.append(maxi(emg3))
    emg3_ent.append(ent(emg3))
    emg3_arcoff.append(arcoff(emg3))
    emg3_mad.append(m_a_d(emg3))
    
    emg4 = np.array(value_matrix[0:r,3])
    emg4_mean.append(mean(emg4))
    emg4_stdev.append(stdev(emg4))
    emg4_mini.append(mini(emg4))
    emg4_maxi.append(maxi(emg4))
    emg4_ent.append(ent(emg4))
    emg4_arcoff.append(arcoff(emg4))
    emg4_mad.append(m_a_d(emg4))
    
    airborne = np.array(value_matrix[0:r,4])
    ab_mean.append(mean(airborne))
    ab_stdev.append(stdev(airborne))
    ab_mini.append(mini(airborne))
    ab_maxi.append(maxi(airborne))
    ab_ent.append(ent(airborne))
    ab_arcoff.append(arcoff(airborne))
    ab_mad.append(m_a_d(airborne))
    
    
    accupperx = np.array(value_matrix[0:r,5])
    aux_mean.append(mean(accupperx))
    aux_stdev.append(stdev(accupperx))
    aux_mini.append(mini(accupperx))
    aux_maxi.append(maxi(accupperx))
    aux_ent.append(ent(accupperx))
    aux_arcoff.append(arcoff(accupperx))
    aux_mad.append(m_a_d(accupperx))
    
    
    
    accuppery = np.array(value_matrix[0:r,6])
    auy_mean.append(mean(accuppery))
    auy_stdev.append(stdev(accuppery))
    auy_mini.append(mini(accuppery))
    auy_maxi.append(maxi(accuppery))
    auy_ent.append(ent(accuppery))
    auy_arcoff.append(arcoff(accuppery))
    auy_mad.append(m_a_d(accuppery))
    
    accupperz = np.array(value_matrix[0:r,7])
    auz_mean.append(mean(accupperz))
    auz_stdev.append(stdev(accupperz))
    auz_mini.append(mini(accupperz))
    auz_maxi.append(maxi(accupperz))
    auz_ent.append(ent(accupperz))
    auz_arcoff.append(arcoff(accupperz))
    auz_mad.append(m_a_d(accupperz))
    
    goniometerx = np.array(value_matrix[0:r,8])
    gox_mean.append(mean(goniometerx))
    gox_stdev.append(stdev(goniometerx))
    gox_mini.append( mini(goniometerx))
    gox_maxi.append(maxi(goniometerx))
    gox_ent.append(ent(goniometerx))
    gox_arcoff.append(arcoff(goniometerx))
    gox_mad.append(m_a_d(goniometerx))
    
    
    acclowerx= np.array(value_matrix[0:r,9])
    alx_mean.append(mean(acclowerx))
    alx_stdev.append(stdev(acclowerx))
    alx_mini.append(mini(acclowerx))
    alx_maxi.append(maxi(acclowerx))
    alx_ent.append(ent(acclowerx))
    alx_arcoff.append(arcoff(acclowerx))
    alx_mad.append(m_a_d(acclowerx))
    
    acclowery = np.array(value_matrix[0:r,10])
    aly_mean.append(mean(acclowery))
    aly_stdev.append(stdev(acclowery))
    aly_mini.append(mini(acclowery))
    aly_maxi.append(maxi(acclowery))
    aly_ent.append(ent(acclowery))
    aly_arcoff.append(arcoff(acclowery))
    aly_mad.append(m_a_d(acclowery))
    
    acclowerz= np.array(value_matrix[0:r,11])
    alz_mean.append(mean(acclowerz))
    alz_stdev.append(stdev(acclowerz))
    alz_mini.append(mini(acclowerz))
    alz_maxi.append(maxi(acclowerz))
    alz_ent.append(ent(acclowerz))
    alz_arcoff.append(arcoff(acclowerz))
    alz_mad.append(m_a_d(acclowerz))
    
    goniometery= np.array(value_matrix[0:r,12])
    goy_mean.append(mean(goniometery))
    goy_stdev.append(stdev(goniometery))
    goy_mini.append( mini(goniometery))
    goy_maxi.append(maxi(goniometery))
    goy_ent.append(ent(goniometery))
    goy_arcoff.append(arcoff(goniometery))
    goy_mad.append(m_a_d(goniometery))
    
    gyroupperx= np.array(value_matrix[0:r,13])
    gux_mean.append(mean(gyroupperx))
    gux_stdev.append(stdev(gyroupperx))
    gux_mini.append(mini(gyroupperx))
    gux_maxi.append(maxi(gyroupperx))
    gux_ent.append(ent(gyroupperx))
    gux_arcoff.append(arcoff(gyroupperx))
    gux_mad.append(m_a_d(gyroupperx))
    
    gyrouppery = np.array(value_matrix[0:r,14])
    guy_mean.append(mean(gyrouppery))
    guy_stdev.append(stdev(gyrouppery))
    guy_mini.append(mini(gyrouppery))
    guy_maxi.append(maxi(gyrouppery))
    guy_ent.append(ent(gyrouppery))
    guy_arcoff.append(arcoff(gyrouppery))
    guy_mad.append(m_a_d(gyrouppery))
    
    gyroupperz = np.array(value_matrix[0:r,15])
    guz_mean.append(mean(gyroupperz))
    guz_stdev.append(stdev(gyroupperz))
    guz_mini.append(mini(gyroupperz))
    guz_maxi.append(maxi(gyroupperz))
    guz_ent.append(ent(gyroupperz))
    guz_arcoff.append(arcoff(gyroupperz))
    guz_mad.append(m_a_d(gyroupperz))
    
    gyrolowerx = np.array(value_matrix[0:r,16])
    glx_mean.append(mean(gyrolowerx))
    glx_stdev.append(stdev(gyrolowerx))
    glx_mini.append(mini(gyrolowerx))
    glx_maxi.append(maxi(gyrolowerx))
    glx_ent.append(ent(gyrolowerx))
    glx_arcoff.append(arcoff(gyrolowerx))
    glx_mad.append(m_a_d(gyrolowerx))
        
    gyrolowery = np.array(value_matrix[0:r,17])
    gly_mean.append(mean(gyrolowery))
    gly_stdev.append(stdev(gyrolowery))
    gly_mini.append(mini(gyrolowery))
    gly_maxi.append(maxi(gyrolowery))
    gly_ent.append(ent(gyrolowery))
    gly_arcoff.append(arcoff(gyrolowery))
    gly_mad.append(m_a_d(gyrolowery))
        
    gyrolowerz = np.array(value_matrix[0:r,18])
    glz_mean.append(mean(gyrolowerz))
    glz_stdev.append(stdev(gyrolowerz))
    glz_mini.append(mini(gyrolowerz))
    glz_maxi.append(maxi(gyrolowerz))
    glz_ent.append(ent(gyrolowerz))
    glz_arcoff.append(arcoff(gyrolowerz))
    glz_mad.append(m_a_d(gyrolowerz))
     

  
workbook = xlsxwriter.Workbook('test.xlsx') 
worksheet = workbook.add_worksheet() 
 
head = ['emg1_mean','emg1_stdev','emg1_mini','emg1_maxi','emg1_ent' ,'emg1_arcoff','emg1_mad','emg2_mean','emg2_stdev','emg2_mini','emg2_maxi','emg2_ent','emg2_arcoff','emg2_mad','emg3_mean' ,'emg3_stdev' ,'emg3_mini' ,'emg3_maxi' ,'emg3_ent' ,'emg3_arcoff','emg3_mad' ,'emg4_mean','emg4_stdev','emg4_mini','emg4_maxi','emg4_ent','emg4_arcoff','emg4_mad','ab_mean','ab_stdev','ab_mini','ab_maxi','ab_ent' ,'ab_arcoff','ab_mad','aux_mean ','aux_stdev','aux_mini' ,'aux_maxi' ,'aux_ent' ,'aux_arcoff' ,'aux_mad','auy_mean','auy_stdev' ,'auy_mini','auy_maxi','auy_ent','auy_arcoff','auy_mad','auz_mean' ,'auz_stdev','auz_mini' ,'auz_maxi','auz_ent','auz_arcoff','auz_mad','gox_mean','gox_stdev','gox_mini','gox_maxi','gox_ent','gox_arcoff','gox_mad','alx_mean','alx_stdev','alx_mini' ,'alx_maxi' ,'alx_ent' ,'alx_arcoff','alx_mad','aly_mean','aly_stdev','aly_mini','aly_maxi','aly_ent','aly_arcoff','aly_mad','alz_mean' ,'alz_stdev' ,'alz_mini' ,'alz_maxi' ,'alz_ent' ,'alz_arcoff' ,'alz_mad','goy_mean' ,'goy_stdev' ,'goy_mini' ,'goy_maxi' ,'goy_ent' ,'goy_arcoff' ,'goy_mad' ,'gux_mean' ,'gux_stdev' ,'gux_mini' ,'gux_maxi','gux_ent','gux_arcoff' ,'gux_mad','guy_mean' ,'guy_stdev' ,'guy_mini' ,'guy_maxi' ,'guy_ent' ,'guy_arcoff','guy_mad','guz_mean' ,'guz_stdev' ,'guz_mini','guz_maxi','guz_ent' ,'guz_arcoff','guz_mad' ,'glx_mean' ,'glx_stdev','glx_mini' ,'glx_maxi' ,'glx_ent' ,'glx_arcoff','glx_mad','gly_mean','gly_stdev','gly_mini','gly_maxi','gly_ent','gly_arcoff','gly_mad','glz_mean','glz_stdev' ,'glz_mini' ,'glz_maxi' ,'glz_ent' ,'glz_arcoff','glz_mad','activity'] 


row=0
column = 0
for item in head:
    worksheet.write(row,column,item)
    column +=1




row = 1
column = 0
for item in emg1_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 1
for item in emg1_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 2
for item in emg1_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 3
for item in emg1_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 4
for item in emg1_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 5
for item in emg1_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 6
for item in emg1_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 7
for item in emg2_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 8
for item in emg2_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 9
for item in emg2_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 10
for item in emg2_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 11
for item in emg2_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 12
for item in emg2_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 13
for item in emg2_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 14
for item in emg3_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 15
for item in emg3_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 16
for item in emg3_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 17
for item in emg3_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 18
for item in emg3_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 19
for item in emg3_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 20
for item in emg3_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 21
for item in emg4_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 22
for item in emg4_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 23
for item in emg4_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 24
for item in emg4_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 25
for item in emg4_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 26
for item in emg4_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 27
for item in emg4_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 28
for item in ab_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 29
for item in ab_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 30
for item in ab_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 31
for item in ab_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 32
for item in ab_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 33
for item in ab_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 34
for item in ab_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 35
for item in aux_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 36
for item in aux_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 37
for item in aux_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 38
for item in aux_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 39
for item in aux_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 40
for item in aux_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 41
for item in aux_mad : 
    worksheet.write(row, column, item) 
    row += 1 



row = 1
column = 42
for item in auy_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 43
for item in auy_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 44
for item in auy_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 45
for item in auy_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 46
for item in auy_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 47
for item in auy_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 48
for item in auy_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 49
for item in auz_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 50
for item in auz_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 51
for item in auz_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 52
for item in auz_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 53
for item in auz_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 54
for item in auz_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 55
for item in auz_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 56
for item in gox_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 57
for item in gox_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 58
for item in gox_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 59
for item in gox_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 60
for item in gox_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 61
for item in gox_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 62
for item in gox_mad : 
    worksheet.write(row, column, item) 
    row += 1 




row = 1
column = 63
for item in alx_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 64
for item in alx_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 65
for item in alx_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 66
for item in alx_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 67
for item in alx_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 68
for item in alx_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 69
for item in alx_mad : 
    worksheet.write(row, column, item) 
    row += 1 






row = 1
column = 70
for item in aly_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 71
for item in aly_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 72
for item in aly_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 73
for item in aly_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 74
for item in aly_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 75
for item in aly_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 76
for item in aly_mad : 
    worksheet.write(row, column, item) 
    row += 1 




row = 1
column = 77
for item in alz_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 78
for item in alz_stdev : 
    worksheet.write(row, column, item) 
    row += 1   



row = 1
column = 79
for item in alz_mini : 
    worksheet.write(row, column, item) 
    row += 1


row = 1
column = 80
for item in alz_maxi : 
    worksheet.write(row, column, item) 
    row += 1


row = 1
column = 81
for item in alz_ent : 
    worksheet.write(row, column, item) 
    row += 1



row = 1
column = 82
for item in alz_arcoff : 
    worksheet.write(row, column, item) 
    row += 1


row = 1
column = 83
for item in alz_mad : 
    worksheet.write(row, column, item) 
    row += 1    





row = 1
column = 84
for item in goy_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 85
for item in goy_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 86
for item in goy_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 87
for item in goy_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 88
for item in goy_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 89
for item in goy_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 90
for item in goy_mad : 
    worksheet.write(row, column, item) 
    row += 1 




row = 1
column = 91
for item in gux_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 92
for item in gux_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 93
for item in gux_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 94
for item in gux_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 95
for item in gux_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 96
for item in gux_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 97
for item in gux_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 98
for item in guy_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 99
for item in guy_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 100
for item in guy_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 101
for item in guy_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 102
for item in guy_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 103
for item in guy_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 104
for item in guy_mad : 
    worksheet.write(row, column, item) 
    row += 1 




row = 1
column = 105
for item in guz_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 106
for item in guz_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 107
for item in guz_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 108
for item in guz_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 109
for item in guz_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 110
for item in guz_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 111
for item in guz_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 112
for item in glx_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 113
for item in glx_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 114
for item in glx_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 115
for item in glx_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 116
for item in glx_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 117
for item in glx_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 118
for item in glx_mad : 
    worksheet.write(row, column, item) 
    row += 1 






row = 1
column = 119
for item in gly_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 120
for item in gly_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 121
for item in gly_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 122
for item in gly_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 123
for item in gly_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 124
for item in gly_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 125
for item in gly_mad : 
    worksheet.write(row, column, item) 
    row += 1 





row = 1
column = 126
for item in glz_mean : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 127
for item in glz_stdev : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 128
for item in glz_mini : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 129
for item in glz_maxi : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 130
for item in glz_ent : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 131
for item in glz_arcoff : 
    worksheet.write(row, column, item) 
    row += 1 


row = 1
column = 132
for item in glz_mad : 
    worksheet.write(row, column, item) 
    row += 1   

workbook.close()
    
    


  

      



    
    
























