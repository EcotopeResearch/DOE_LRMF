# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:03:59 2019

@author: scott

EnergyUsePlots:
    Histogram plots for individual buildings
    
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

commonBsmt_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\commonBsmt\\AllCombinedResults.csv'
commonSlab_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\commonSlab\\AllCombinedResults.csv'
gardenBsmt_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\gardenBsmt\\AllCombinedResults.csv'
gardenSlab_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\gardenSlab\\AllCombinedResults.csv'

commonBsmt = pd.read_csv(commonBsmt_path)
commonSlab = pd.read_csv(commonSlab_path)
gardenBsmt = pd.read_csv(gardenBsmt_path)
gardenSlab = pd.read_csv(gardenSlab_path)


commonBsmt_eui = []
for i in range(0,len(commonBsmt)):
    commonBsmt_eui.append(commonBsmt.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
    
commonSlab_eui = []
for i in range(0,len(commonSlab)):
    commonSlab_eui.append(commonSlab.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)

gardenBsmt_eui = []
for i in range(0,len(gardenBsmt)):
    gardenBsmt_eui.append(gardenBsmt.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
    
gardenSlab_eui = []
for i in range(0,len(gardenSlab)):
    gardenSlab_eui.append(gardenSlab.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
    
    
# plots
ax = sns.distplot(commonBsmt_eui, hist=True, kde=True, norm_hist=False)
plt.show()
ax = sns.distplot(commonSlab_eui, hist=True, kde=False, norm_hist=False, bins=8)
plt.show()
ax = sns.distplot(gardenBsmt_eui, hist=True, kde=False, norm_hist=False, bins=8)
plt.show()
ax = sns.distplot(gardenSlab_eui, hist=True, kde=False, norm_hist=False)
plt.show()