#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:08:26 2019

@author: atit
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:05:38 2019

@author: atit
"""

import pandas as pd
import xlsxwriter

df= pd.read_excel("training_iq_coor.xlsx")

activity = df['activity_label']



activity_label=["Label"]
for item in activity:
    if item == 1:
        activity_label.append("curve-left-step")
    elif item == 2:
        activity_label.append( "stand-to-sit")
    elif item == 3:
        activity_label.append("curve-right-spin-Rfirst")
    elif item == 4:
        activity_label.append( "jump-one-leg")
    elif item == 5 :
        activity_label.append("lateral-shuffle-right")
    elif item == 6 :
        activity_label.append( "curve-right-spin-Lfirst")   
    elif item == 7 :
        activity_label.append("v-cut-right-Lfirst")
    elif item == 8 :
        activity_label.append( "stair-down")
    elif item == 9 :
        activity_label.append("v-cut-left-Rfirst")
    elif item == 10 :
        activity_label.append("v-cut-right-Rfirst")
    elif item == 11 :
        activity_label.append("jump-two-leg")
    elif item == 12 :
        activity_label.append("sit")
    elif item == 13 :
        activity_label.append("stair-up")
    elif item == 14 :
        activity_label.append("curve-right-step")
    elif item == 15 :
        activity_label.append("sit-to-stand")
    elif item == 16 :
        activity_label.append("run")
    elif item == 17 :
        activity_label.append("v-cut-left-Lfirst")
    elif item == 18 :
        activity_label.append("stand")
    elif item == 19 :
        activity_label.append("curve-left-spin-Lfirst")
    elif item == 20:
        activity_label.append("walk")
    elif item == 21:
        activity_label.append("curve-left-spin-Rfirst")
    elif item == 22 :
        activity_label.append("lateral-shuffle-left")
    elif item == 23:
        activity_label.append("lay")
    
       
workbook = xlsxwriter.Workbook('label_lll.xlsx') 
worksheet = workbook.add_worksheet() 


row=0
column = 0
for item in activity_label:
    worksheet.write(row,column,item)
    row +=1
workbook.close()




















