# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:52:16 2019

@author: scott

Plot results from measure analysis run. 

1072 runs for Measure Analysis to create EUI maps for 
different building components

"""

import seaborn as sns
import matplotlib.pyplot as plt

# separate script that restructures jEplus and dci outputs for plotting
from eui_data import eui_data
from hist_data import hist_data

# plot path
path = 'C:\\Users\\scott\\github\\DOE_LRMF\\Plotting\\MeasureAnalysis\\plots\\'

# pull in dataframes from csv through data formatter scripts
eui_df = eui_data()
hist_df = hist_data()


# baseline dictionary
base_dict = {'Basement Wall U-Value': 0.05, 'Ceiling U-Value': 0.026, 'Exterior Wall U-Value': 0.057, 
             'Slab U-Value': 0.54, 'Window U-Value': 0.4, 'Window SHGC': 0.4}

# plot dataframes
row = ['Baseline', 'Basement Wall U-Value', 'Ceiling U-Value', 'Exterior Wall U-Value', 'Slab U-Value', 'Window U-Value', 'Window SHGC']
col = ['IL4A','WA4C','OR4C','IL5A','WA5B','OR5B','MN6A','MN7A']

## loop through eui dataframe rows 1 to len, all columns for plots
# i for columns
# j for rows

for i in range(0,8):
    for j in range(1,7):
        
        # set up figure object for subplots
        fig, ax = plt.subplots()
        
        # create line plot
        ax.set(xlabel='U Value', ylabel='EUI Delta')    
        sns.lineplot(data=eui_df[col[i]][row[j]], legend=False, ax = ax)
        
        # create hist plot
        if len(hist_df[col[i]][row[j]]) > 5:
            ax2 = ax.twinx()
            ax2.set(ylabel='Building Quantity')  
            sns.distplot(hist_df[col[i]][row[j]], hist=True, kde=False, norm_hist=False, color='orange', ax = ax2)


        plt.axvline(base_dict[row[j]], 0, 5, linestyle=':', color='red', label='Code Baseline')
        ax.set_title(str(col[i])+' '+str(row[j]))
    
        name = str(col[i])+'_'+str(row[j])+'.png'
        
        plt.savefig(path + name)
        plt.show()
        





