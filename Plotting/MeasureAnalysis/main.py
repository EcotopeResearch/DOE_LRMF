# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:52:16 2019

@author: scott

Plot results from measure analysis run. 

1072 runs for Measure Analysis to create EUI maps for 
different building components

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from df_restructure import df_restructure

df = pd.DataFrame()
df = df_restructure()

            
# plot dataframes
row = ['Baseline', 'Basement Wall U-Value', 'Ceiling U-Value', 'Exterior Wall U-Value', 'Slab U-Value', 'Window U-Value', 'Window SHGC']
col = ['IL4A','WA4C','OR4C','IL5A','WA5B','OR5B','MN6A','MN7A']


ax = sns.lineplot(data=df[col[3]][row[3]], legend=False)
ax.set(xlabel='U Value', ylabel='EUI')
plt.axvline(0.05, 0, 5, linestyle=':', color='red')
plt.axhline(0, 0, 5, linestyle=':', color='red')
ax.set_title('Basement Wall U-Value')
plt.savefig("bsmtU.png")
plt.show()


# =============================================================================
# ax = sns.lineplot(data=IL4A_ceilingU, legend=False)
# ax.set(xlabel='U Value', ylabel='EUI')
# plt.axvline(0.026, 0, 5, linestyle=':', color='red')
# plt.axhline(0, 0, 5, linestyle=':', color='red')
# ax.set_title('Ceiling U-Value')
# plt.savefig("ceilU.png")
# plt.show()
# 
# 
# ## HISTOGRAM INSERT
# data = []
# 
# for i in range(0,len(dci)):
#     if dci.loc[i,'KeyCodeName']=='GenWallAGU' and dci.loc[i,'State']=='Washington' and dci.loc[i,'ClimateZone']=='CZ 4':
#         data.append(dci.loc[i,'KeyCodeValue'])
# 
# 
# # set up figure object for subplots
# fig, ax = plt.subplots()
# 
# # create histogram plot
# 
# 
# sns.lineplot(data=IL4A_extWallU, legend=False)
# ax2 = ax.twinx()
# ax.set(xlabel='U Value', ylabel='EUI Delta')
# 
# #create line plot
# sns.distplot(data, hist=True, kde=False, norm_hist=False)
# ax2.set(ylabel='Building Quantity')
# 
# plt.axvline(0.057, 0, 5, linestyle=':', color='red')
# 
# 
# 
# 
# ax.set_title('Exteroir Wall U-Value')
# plt.savefig("ExtWallU.png")
# 
# 
# 
# plt.show()
# 
# 
# ax = sns.lineplot( data=IL4A_slabU, legend=False)
# ax.set(xlabel='U Value', ylabel='EUI')
# plt.axvline(0.54, 0, 5, linestyle=':', color='red')
# plt.axhline(0, 0, 5, linestyle=':', color='red')
# ax.set_title('Slab F-Value')
# plt.savefig("slabF.png")
# plt.show()
# 
# ax = sns.lineplot(data=IL4A_windowU, legend=False)
# ax.set(xlabel='U Value', ylabel='EUI')
# ax.set_title('Window U-Value')
# plt.axvline(0.4, 0, 5, linestyle=':', color='red')
# plt.axhline(0, 0, 5, linestyle=':', color='red')
# plt.savefig("windU.png")
# plt.show()
# 
# 
# ax = sns.lineplot(data=IL4A_windowSHGC, legend=False)
# ax.set(xlabel='SHGC', ylabel='EUI')
# plt.axvline(0.4, 0, 5, linestyle=':', color='red')
# plt.axhline(0, 0, 5, linestyle=':', color='red')
# ax.set_title('Window SHGC')
# plt.savefig("shgc.png")
# plt.show()
# 
# 
# #for i in range(0,len(df)):
# =============================================================================
    


