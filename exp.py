#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 00:16:27 2019

@author: atit
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from pandas.plotting import andrews_curves
from pandas.plotting import scatter_matrix
import seaborn as sns

df= pd.read_excel("training_iq_coor.xlsx")
df['activity'] = df['activity'].astype('category')
df['Subject'] = df['Subject'].astype('category')








plt.figure()
df.hist(column='emg1_mean', by='activity',bins = 500,figsize=(10,10),layout=(5,5),xrot=360)
plt.savefig('mean.png')


plt.figure()
df.hist(column='emg2_stdev', by='activity',bins=500,figsize=(10,10),layout=(5,5),xrot=360)
plt.savefig('stdev.png')

plt.figure()
df.hist(column='emg3_mini', by='activity',bins=500,figsize=(10,10),layout=(5,5),xrot=360)
plt.savefig('mini.png')

plt.figure()
df.hist(column='emg4_maxi', by='activity',bins=500,figsize=(10,10),layout=(5,5),xrot=360)
plt.savefig('maxi.png')

plt.figure()
df.hist(column='gux_ent', by='activity',bins=500,figsize=(10,10),layout=(5,5),xrot=360)
plt.savefig('ent.png')

plt.figure()
df.hist(column='guy_arcoff', by='activity',bins=500,figsize=(10,10),layout=(5,5),xrot=360)
plt.savefig('arcoff.png')

plt.figure()
df.hist(column='alxz_coor', by='activity',bins=500,figsize=(10,10),layout=(5,5),xrot=360)
plt.savefig('coor.png')

plt.figure()
df.hist(column='guy_mad', by='activity',bins=500,figsize=(10,10),layout=(5,5),xrot=360)
plt.savefig('mad.png')


g = sns.catplot(y="activity",kind="count", orient="h",palette="pastel", data=df)

h = sns.catplot(x='alxz_coor',y="activity",kind="box", orient="h",palette="pastel",sharex=True,data=df)
#h.set(xlim=(np.format_float_scientific(0.1, precision=12),np.format_float_scientific(0.2, precision=12)))



df1= pd.read_excel("coor_.xlsx")
df1_sub = df1.iloc[:,[5,6,7,8,9,10,11,12,13,14,15,16,17,18]]







# Compute the correlation matrix
corr = df1_sub.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})




