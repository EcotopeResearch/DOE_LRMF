# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:48:39 2019

@author: scott
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def df_restructure():
    
    param_path = "C:\\Users\\scott\\github\\DOE_LRMF\\DCI_to_EnergyPlus\\MeasureAnalysis\\"
    
    # bring in results as dataframe
    results = pd.read_csv('AllCombinedResults.csv')
    
    # bring in run name references from excel
    bsmtWallU = pd.read_excel(param_path+'bsmtWallU.xlsx')
    ceilingU = pd.read_excel(param_path+'ceilingU.xlsx')
    extWallU = pd.read_excel(param_path+'extWallU.xlsx')
    slabU = pd.read_excel(param_path+'slabU.xlsx')
    windowU = pd.read_excel(param_path+'windowU.xlsx')
    windowSHGC = pd.read_excel(param_path+'windowSHGC.xlsx')
    
    # create list of dataframes
    run_names = [bsmtWallU, ceilingU, extWallU, slabU, windowU, windowSHGC]
    
    ## loop through list to create dictionary of attributes for results plotting
    
    # create empty dictionary
    d = {}
    
    # loop and creat dictionary
    for i in range(0, len(run_names)):
        df = run_names[i]
        
        for i in range(0, len(df)):
            
            key = df.loc[i,'name']
            value = df.loc[i, 'ipu']
        
            d[key] = value
        
    # break out dataframe by weather file, and by @@NAME@@ to make line plots. 
    # plot U value (or F-value) vs. EUI (1 sig-fig)
    
    
    # create dfs to store results for plotting
    IL4A_bsmtWallU_dict = {}
    IL4A_ceilingU_dict = {}
    IL4A_extWallU_dict = {}
    IL4A_slabU_dict = {}
    IL4A_windowU_dict = {}
    IL4A_windowSHGC_dict = {}
    
    for i in range(0, len(results)):
        
        # check weather file location
        if results.loc[i,'WeatherFile']=='USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw':
    
            if 'Baseline' in results.loc[i,'@@NAME@@']:
                IL4A_baseline_EUI = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
    
            if 'bsmtWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL4A_bsmtWallU_dict[key] = value
    
            if 'ceilingU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL4A_ceilingU_dict[key] = value
    
            if 'extWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL4A_extWallU_dict[key] = value
                
            if 'slabF' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL4A_slabU_dict[key] = value
                
            if 'windowU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL4A_windowU_dict[key] = value
                
            if 'windowSHGC' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL4A_windowSHGC_dict[key] = value
    
    
    # create dataframes and normalize to a baseline of 0
    IL4A_bsmtWallU = pd.DataFrame.from_dict(IL4A_bsmtWallU_dict, orient='index')
    IL4A_bsmtWallU[0] = IL4A_bsmtWallU[0] - IL4A_baseline_EUI
    
    IL4A_ceilingU = pd.DataFrame.from_dict(IL4A_ceilingU_dict, orient='index')
    IL4A_ceilingU[0] = IL4A_ceilingU[0] - IL4A_baseline_EUI
    
    IL4A_extWallU = pd.DataFrame.from_dict(IL4A_extWallU_dict, orient='index')
    IL4A_extWallU[0] = IL4A_extWallU[0] - IL4A_baseline_EUI
    
    IL4A_slabU = pd.DataFrame.from_dict(IL4A_slabU_dict, orient='index')
    IL4A_slabU[0] = IL4A_slabU[0] - IL4A_baseline_EUI
    
    IL4A_windowU = pd.DataFrame.from_dict(IL4A_windowU_dict, orient='index')
    IL4A_windowU[0] = IL4A_windowU[0] - IL4A_baseline_EUI
    
    IL4A_windowSHGC = pd.DataFrame.from_dict(IL4A_windowSHGC_dict, orient='index')
    IL4A_windowSHGC[0] = IL4A_windowSHGC[0] - IL4A_baseline_EUI