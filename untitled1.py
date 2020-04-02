#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:21:13 2019

@author: atit
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:46:04 2019

@author: atit
"""
import numpy as np
import pandas as pd
import xlsxwriter 

from scipy import stats as s

def coor(a,b):
    coore = s.pearsonr(a,b)
    return coore[0]
    
emg1 =[]
emg2 =[]
emg3 =[]
emg4 =[]
airborne =[]
accupperx =[]
accuppery=[]
accupperz =[]
goniometerx =[]
acclowerx =[]
acclowery =[]
acclowerz =[]
goniometery =[]
gyroupperx =[]
gyrouppery  =[]
gyroupperz =[]
gyrolowerx  =[]
gyrolowery  =[]
gyrolowerz =[]


data_train = pd.read_csv("challenge.csv") 
train_matrix = data_train.as_matrix()
file_path = train_matrix[0:1739,1]
reading_val = pd.read_csv(file_path[1],header=None)
value_matrix = reading_val.as_matrix()
r,c = value_matrix.shape
    
emg1.append(value_matrix[0:r,0])
emg2.append(value_matrix[0:r,1])
emg3.append(value_matrix[0:r,2])
emg4.append(value_matrix[0:r,3])
airborne.append(value_matrix[0:r,4])
accupperx.append(value_matrix[0:r,5])
accuppery.append(value_matrix[0:r,6])
accupperz.append(value_matrix[0:r,7])
goniometerx.append(value_matrix[0:r,8])
acclowerx.append(value_matrix[0:r,9])
acclowery.append(value_matrix[0:r,10])
acclowerz.append(value_matrix[0:r,11])
goniometery.append(value_matrix[0:r,12])
gyroupperx.append(value_matrix[0:r,13])
gyrouppery.append(value_matrix[0:r,14])
gyroupperz.append(value_matrix[0:r,15])
gyrolowerx.append(value_matrix[0:r,16])
gyrolowery.append(value_matrix[0:r,17])
gyrolowerz.append(value_matrix[0:r,18])
    
for item in emg1 :
    print(item)
     
    



workbook = xlsxwriter.Workbook('coor_.xlsx') 
worksheet = workbook.add_worksheet() 
 
head = ['emg1','emg2','emg3','emg4','airborne','accupperx','accuppery' ,'accupperz' ,'goniometerx','acclowerx' ,'acclowery' ,'acclowerz' ,'goniometery' ,'gyroupperx','gyrouppery' ,'gyroupperz','gyrolowerx','gyrolowery','gyrolowerz']  


row=0
column = 0
for item in head:
    worksheet.write(row,column,item)
    column +=1




row = 1
column = 0
for i in emg1 : 
    for item in i:
         worksheet.write(row, column, item) 
         row += 1 


row = 1
column = 1
for i in emg2 :
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 2
for i in emg3 : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 3
for i in emg4 : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 

row = 1
column = 4
for i in airborne : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 5
for i in accupperx : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 

row = 1
column = 6
for i in accuppery : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 7
for i in accupperz : 
    for item in i:
       worksheet.write(row, column, item) 
       row += 1 


row = 1
column = 8
for i in goniometerx : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 9
for i in acclowerx :
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 

row = 1
column = 10
for i in acclowery : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 

row = 1
column = 11
for i in acclowerz : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 12
for i in goniometery : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 13
for i in gyroupperx : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 14
for i in gyrouppery : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 15
for i in gyroupperz : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 


row = 1
column = 16
for i in gyrolowerx : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 
    
row = 1
column = 17
for i in gyrolowery :
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 
    
row = 1
column = 18
for i in gyrolowerz : 
    for item in i:
        worksheet.write(row, column, item) 
        row += 1 

workbook.close()

    


  

      



    
    


























    
    
    
