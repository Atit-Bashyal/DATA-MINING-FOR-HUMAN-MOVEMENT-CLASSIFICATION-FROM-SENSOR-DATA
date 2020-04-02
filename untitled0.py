#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:05:38 2019

@author: atit
"""

import pandas as pd
import xlsxwriter

df= pd.read_excel("training_data.xlsx")
data_matrix = df.as_matrix()
activity = data_matrix[0:6401,133]

activity_label=["activity_label"]
for item in activity:
    if item == "curve-left-step":
        activity_label.append(1)
    elif item == "stand-to-sit":
        activity_label.append(2)
    elif item == "curve-right-spin-Rfirst":
        activity_label.append(3)
    elif item == "jump-one-leg":
        activity_label.append(4)
    elif item == "lateral-shuffle-right":
        activity_label.append(5)
    elif item == "curve-right-spin-Lfirst":
        activity_label.append(6)   
    elif item == "v-cut-right-Lfirst":
        activity_label.append(7)
    elif item == "stair-down":
        activity_label.append(8)
    elif item == "v-cut-left-Rfirst":
        activity_label.append(9)
    elif item == "v-cut-right-Rfirst":
        activity_label.append(10)
    elif item == "jump-two-leg":
        activity_label.append(11)
    elif item == "sit":
        activity_label.append(12)
    elif item == "stair-up":
        activity_label.append(13)
    elif item == "curve-right-step":
        activity_label.append(14)
    elif item == "sit-to-stand":
        activity_label.append(15)
    elif item == "run":
        activity_label.append(16)
    elif item == "v-cut-left-Lfirst":
        activity_label.append(17)
    elif item == "stand":
        activity_label.append(18)
    elif item == "curve-left-spin-Lfirst":
        activity_label.append(19)
    elif item == "walk":
        activity_label.append(20)
    elif item == "curve-left-spin-Rfirst":
        activity_label.append(21)
    elif item == "lateral-shuffle-left":
        activity_label.append(22)
    elif item == "lay":
        activity_label.append(23)
    
       
workbook = xlsxwriter.Workbook('label.xlsx') 
worksheet = workbook.add_worksheet() 


row=0
column = 0
for item in activity_label:
    worksheet.write(row,column,item)
    row +=1
workbook.close()




















