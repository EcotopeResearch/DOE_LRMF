# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:56:15 2019

@author: scott
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from inputoutput_data import inputoutput
import plotly.express as px

# gather data from results
df = inputoutput()

### STACKED HISTOGRAMS

# =============================================================================
# # All Buildings
# hist_df = pd.DataFrame()
# hist_df['eui'] = df['All States']['EUI']
# fig = px.histogram(hist_df, x="EUI", nbins=20)
# 
# fig.show()
# 
# # Washington
# hist_df = pd.DataFrame()
# hist_df['eui'] = df['All States']['EUI']
# fig = px.histogram(hist_df, x="EUI", nbins=20)
# 
# fig.show()
# 
# =============================================================================


### PLOT HISTOGRAMS - PMFs
ax = sns.distplot(df['All States']['eui'], hist=True, kde=True, norm_hist=False).set_title("All States")
plt.xlabel('EUI')
plt.ylabel('PMF')
plt.show()

WA = df['WA4C']['eui'] 
WA.extend(df['WA5B']['eui'])
ax = sns.distplot(WA, hist=True, kde=True, norm_hist=False).set_title("Washington ")
plt.xlabel('EUI')
plt.ylabel('PMF')
plt.show()

OR = df['OR4C']['eui']
OR.extend(df['OR5B']['eui'])
ax = sns.distplot(OR, hist=True, kde=True, norm_hist=False).set_title("Oregon")
plt.xlabel('EUI')
plt.ylabel('PMF')
plt.show()

IL = df['IL4A']['eui'] + df['IL5A']['eui']
ax = sns.distplot(IL, hist=True, kde=True, norm_hist=False).set_title("Illinois")
plt.xlabel('EUI')
plt.ylabel('PMF')
plt.show()

MN = df['MN6A']['eui'] + df['MN7A']['eui']
ax = sns.distplot(MN, hist=True, kde=True, norm_hist=False).set_title("Minnesota")
plt.xlabel('EUI')
plt.ylabel('PMF')
plt.show()

