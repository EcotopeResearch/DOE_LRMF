# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:37:52 2019

@author: scott
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

param_path = "C:\\Users\\scott\\github\\DOE_LRMF\\DCI_to_EnergyPlus\\MeasureAnalysis\\"


# bring in results as dataframe
results = pd.read_csv('AllCombinedResults.csv')
# bring in DCI for histograms
dci = pd.read_csv('_stat_modeldata.csv')

data = []

for i in range(0,len(dci)):
    if dci.loc[i,'KeyCodeName']=='GenWallAGU' and dci.loc[i,'State']=='Washington' and dci.loc[i,'ClimateZone']=='CZ 4':
        data.append(dci.loc[i,'KeyCodeValue'])
        
ax = sns.distplot(data, hist=True, kde=True, norm_hist=True)
plt.show()

print(dci['KeyCodeName'][4])
