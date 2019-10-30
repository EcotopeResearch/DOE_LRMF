# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:48:39 2019

@author: scott
"""

import pandas as pd

def eui_data():
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
    
    
    # create dictionaries to store results for plotting
            
    IL4A_bsmtWallU_dict = {}
    IL4A_ceilingU_dict = {}
    IL4A_extWallU_dict = {}
    IL4A_slabU_dict = {}
    IL4A_windowU_dict = {}
    IL4A_windowSHGC_dict = {}
    
    WA4C_bsmtWallU_dict = {}
    WA4C_ceilingU_dict = {}
    WA4C_extWallU_dict = {}
    WA4C_slabU_dict = {}
    WA4C_windowU_dict = {}
    WA4C_windowSHGC_dict = {}
    
    OR4C_bsmtWallU_dict = {}
    OR4C_ceilingU_dict = {}
    OR4C_extWallU_dict = {}
    OR4C_slabU_dict = {}
    OR4C_windowU_dict = {}
    OR4C_windowSHGC_dict = {}
    
    IL5A_bsmtWallU_dict = {}
    IL5A_ceilingU_dict = {}
    IL5A_extWallU_dict = {}
    IL5A_slabU_dict = {}
    IL5A_windowU_dict = {}
    IL5A_windowSHGC_dict = {}
    
    WA5B_bsmtWallU_dict = {}
    WA5B_ceilingU_dict = {}
    WA5B_extWallU_dict = {}
    WA5B_slabU_dict = {}
    WA5B_windowU_dict = {}
    WA5B_windowSHGC_dict = {}
    
    OR5B_bsmtWallU_dict = {}
    OR5B_ceilingU_dict = {}
    OR5B_extWallU_dict = {}
    OR5B_slabU_dict = {}
    OR5B_windowU_dict = {}
    OR5B_windowSHGC_dict = {}
    
    MN6A_bsmtWallU_dict = {}
    MN6A_ceilingU_dict = {}
    MN6A_extWallU_dict = {}
    MN6A_slabU_dict = {}
    MN6A_windowU_dict = {}
    MN6A_windowSHGC_dict = {}
    
    MN7A_bsmtWallU_dict = {}
    MN7A_ceilingU_dict = {}
    MN7A_extWallU_dict = {}
    MN7A_slabU_dict = {}
    MN7A_windowU_dict = {}
    MN7A_windowSHGC_dict = {}
    
    
    for i in range(0, len(results)):
        
        # check weather file location - St. Louis
        if results.loc[i,'WeatherFile']=='USA_MO_St.Louis-Spirit.of.St.Louis.AP.724345_TMY3.epw':
    
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
                
        # check weather file location - Seattle
        if results.loc[i,'WeatherFile']=='USA_WA_Seattle-Tacoma.Intl.AP.727930_TMY3.epw':
    
            if 'Baseline' in results.loc[i,'@@NAME@@']:
                WA4C_baseline_EUI = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
    
            if 'bsmtWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA4C_bsmtWallU_dict[key] = value
    
            if 'ceilingU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA4C_ceilingU_dict[key] = value
    
            if 'extWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA4C_extWallU_dict[key] = value
                
            if 'slabF' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA4C_slabU_dict[key] = value
                
            if 'windowU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA4C_windowU_dict[key] = value
                
            if 'windowSHGC' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA4C_windowSHGC_dict[key] = value
    
        # check weather file location - Portland
        if results.loc[i,'WeatherFile']=='USA_OR_Portland.Intl.AP.726980_TMY3.epw':
    
            if 'Baseline' in results.loc[i,'@@NAME@@']:
                OR4C_baseline_EUI = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
    
            if 'bsmtWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR4C_bsmtWallU_dict[key] = value
    
            if 'ceilingU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR4C_ceilingU_dict[key] = value
    
            if 'extWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR4C_extWallU_dict[key] = value
                
            if 'slabF' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR4C_slabU_dict[key] = value
                
            if 'windowU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR4C_windowU_dict[key] = value
                
            if 'windowSHGC' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR4C_windowSHGC_dict[key] = value
    
        # check weather file location - Chicago
        if results.loc[i,'WeatherFile']=='USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw':
    
            if 'Baseline' in results.loc[i,'@@NAME@@']:
                IL5A_baseline_EUI = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
    
            if 'bsmtWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL5A_bsmtWallU_dict[key] = value
    
            if 'ceilingU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL5A_ceilingU_dict[key] = value
    
            if 'extWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL5A_extWallU_dict[key] = value
                
            if 'slabF' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL5A_slabU_dict[key] = value
                
            if 'windowU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL5A_windowU_dict[key] = value
                
            if 'windowSHGC' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                IL5A_windowSHGC_dict[key] = value
                
        # check weather file location - Spokane
        if results.loc[i,'WeatherFile']=='USA_WA_Spokane.Intl.AP.727850_TMY3.epw':
    
            if 'Baseline' in results.loc[i,'@@NAME@@']:
                WA5B_baseline_EUI = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
    
            if 'bsmtWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA5B_bsmtWallU_dict[key] = value
    
            if 'ceilingU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA5B_ceilingU_dict[key] = value
    
            if 'extWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA5B_extWallU_dict[key] = value
                
            if 'slabF' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA5B_slabU_dict[key] = value
                
            if 'windowU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA5B_windowU_dict[key] = value
                
            if 'windowSHGC' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                WA5B_windowSHGC_dict[key] = value            
    
        # check weather file location - Redmond
        if results.loc[i,'WeatherFile']=='USA_OR_Redmond-Roberts.Field.726835_TMY3.epw':
    
            if 'Baseline' in results.loc[i,'@@NAME@@']:
                OR5B_baseline_EUI = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
    
            if 'bsmtWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR5B_bsmtWallU_dict[key] = value
    
            if 'ceilingU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR5B_ceilingU_dict[key] = value
    
            if 'extWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR5B_extWallU_dict[key] = value
                
            if 'slabF' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR5B_slabU_dict[key] = value
                
            if 'windowU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR5B_windowU_dict[key] = value
                
            if 'windowSHGC' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                OR5B_windowSHGC_dict[key] = value
    
        # check weather file location - Minneapolis
        if results.loc[i,'WeatherFile']=='USA_MN_Minneapolis-St.Paul.Intl.AP.726580_TMY3.epw':
    
            if 'Baseline' in results.loc[i,'@@NAME@@']:
                MN6A_baseline_EUI = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
    
            if 'bsmtWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN6A_bsmtWallU_dict[key] = value
    
            if 'ceilingU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN6A_ceilingU_dict[key] = value
    
            if 'extWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN6A_extWallU_dict[key] = value
                
            if 'slabF' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN6A_slabU_dict[key] = value
                
            if 'windowU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN6A_windowU_dict[key] = value
                
            if 'windowSHGC' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN6A_windowSHGC_dict[key] = value
    
        # check weather file location - Bemidji
        if results.loc[i,'WeatherFile']=='USA_MN_Bemidji.Muni.AP.727550_TMY3.epw':
    
            if 'Baseline' in results.loc[i,'@@NAME@@']:
                MN7A_baseline_EUI = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
    
            if 'bsmtWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN7A_bsmtWallU_dict[key] = value
    
            if 'ceilingU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN7A_ceilingU_dict[key] = value
    
            if 'extWallU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN7A_extWallU_dict[key] = value
                
            if 'slabF' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN7A_slabU_dict[key] = value
                
            if 'windowU' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN7A_windowU_dict[key] = value
                
            if 'windowSHGC' in results.loc[i,'@@NAME@@']:
                key = d[results.loc[i,'@@NAME@@']]
                value = results.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000
                MN7A_windowSHGC_dict[key] = value
    
    
    
    ## create dataframes and normalize to a baseline of 0
    # IL4A
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
    
    # WA4C
    WA4C_bsmtWallU = pd.DataFrame.from_dict(WA4C_bsmtWallU_dict, orient='index')
    WA4C_bsmtWallU[0] = WA4C_bsmtWallU[0] - WA4C_baseline_EUI
    
    WA4C_ceilingU = pd.DataFrame.from_dict(WA4C_ceilingU_dict, orient='index')
    WA4C_ceilingU[0] = WA4C_ceilingU[0] - WA4C_baseline_EUI
    
    WA4C_extWallU = pd.DataFrame.from_dict(WA4C_extWallU_dict, orient='index')
    WA4C_extWallU[0] = WA4C_extWallU[0] - WA4C_baseline_EUI
    
    WA4C_slabU = pd.DataFrame.from_dict(WA4C_slabU_dict, orient='index')
    WA4C_slabU[0] = WA4C_slabU[0] - WA4C_baseline_EUI
    
    WA4C_windowU = pd.DataFrame.from_dict(WA4C_windowU_dict, orient='index')
    WA4C_windowU[0] = WA4C_windowU[0] - WA4C_baseline_EUI
    
    WA4C_windowSHGC = pd.DataFrame.from_dict(WA4C_windowSHGC_dict, orient='index')
    WA4C_windowSHGC[0] = WA4C_windowSHGC[0] - WA4C_baseline_EUI
    
    # OR4C
    OR4C_bsmtWallU = pd.DataFrame.from_dict(OR4C_bsmtWallU_dict, orient='index')
    OR4C_bsmtWallU[0] = OR4C_bsmtWallU[0] - OR4C_baseline_EUI
    
    OR4C_ceilingU = pd.DataFrame.from_dict(OR4C_ceilingU_dict, orient='index')
    OR4C_ceilingU[0] = OR4C_ceilingU[0] - OR4C_baseline_EUI
    
    OR4C_extWallU = pd.DataFrame.from_dict(OR4C_extWallU_dict, orient='index')
    OR4C_extWallU[0] = OR4C_extWallU[0] - OR4C_baseline_EUI
    
    OR4C_slabU = pd.DataFrame.from_dict(OR4C_slabU_dict, orient='index')
    OR4C_slabU[0] = OR4C_slabU[0] - OR4C_baseline_EUI
    
    OR4C_windowU = pd.DataFrame.from_dict(OR4C_windowU_dict, orient='index')
    OR4C_windowU[0] = OR4C_windowU[0] - OR4C_baseline_EUI
    
    OR4C_windowSHGC = pd.DataFrame.from_dict(OR4C_windowSHGC_dict, orient='index')
    OR4C_windowSHGC[0] = OR4C_windowSHGC[0] - OR4C_baseline_EUI
    
    # IL5A
    IL5A_bsmtWallU = pd.DataFrame.from_dict(IL5A_bsmtWallU_dict, orient='index')
    IL5A_bsmtWallU[0] = IL5A_bsmtWallU[0] - IL5A_baseline_EUI
    
    IL5A_ceilingU = pd.DataFrame.from_dict(IL5A_ceilingU_dict, orient='index')
    IL5A_ceilingU[0] = IL5A_ceilingU[0] - IL5A_baseline_EUI
    
    IL5A_extWallU = pd.DataFrame.from_dict(IL5A_extWallU_dict, orient='index')
    IL5A_extWallU[0] = IL5A_extWallU[0] - IL5A_baseline_EUI
    
    IL5A_slabU = pd.DataFrame.from_dict(IL5A_slabU_dict, orient='index')
    IL5A_slabU[0] = IL5A_slabU[0] - IL5A_baseline_EUI
    
    IL5A_windowU = pd.DataFrame.from_dict(IL5A_windowU_dict, orient='index')
    IL5A_windowU[0] = IL5A_windowU[0] - IL5A_baseline_EUI
    
    IL5A_windowSHGC = pd.DataFrame.from_dict(IL5A_windowSHGC_dict, orient='index')
    IL5A_windowSHGC[0] = IL5A_windowSHGC[0] - IL5A_baseline_EUI
    
    # WA5B
    WA5B_bsmtWallU = pd.DataFrame.from_dict(WA5B_bsmtWallU_dict, orient='index')
    WA5B_bsmtWallU[0] = WA5B_bsmtWallU[0] - WA5B_baseline_EUI
    
    WA5B_ceilingU = pd.DataFrame.from_dict(WA5B_ceilingU_dict, orient='index')
    WA5B_ceilingU[0] = WA5B_ceilingU[0] - WA5B_baseline_EUI
    
    WA5B_extWallU = pd.DataFrame.from_dict(WA5B_extWallU_dict, orient='index')
    WA5B_extWallU[0] = WA5B_extWallU[0] - WA5B_baseline_EUI
    
    WA5B_slabU = pd.DataFrame.from_dict(WA5B_slabU_dict, orient='index')
    WA5B_slabU[0] = WA5B_slabU[0] - WA5B_baseline_EUI
    
    WA5B_windowU = pd.DataFrame.from_dict(WA5B_windowU_dict, orient='index')
    WA5B_windowU[0] = WA5B_windowU[0] - WA5B_baseline_EUI
    
    WA5B_windowSHGC = pd.DataFrame.from_dict(WA5B_windowSHGC_dict, orient='index')
    WA5B_windowSHGC[0] = WA5B_windowSHGC[0] - WA5B_baseline_EUI
    
    # OR5B
    OR5B_bsmtWallU = pd.DataFrame.from_dict(OR5B_bsmtWallU_dict, orient='index')
    OR5B_bsmtWallU[0] = OR5B_bsmtWallU[0] - OR5B_baseline_EUI
    
    OR5B_ceilingU = pd.DataFrame.from_dict(OR5B_ceilingU_dict, orient='index')
    OR5B_ceilingU[0] = OR5B_ceilingU[0] - OR5B_baseline_EUI
    
    OR5B_extWallU = pd.DataFrame.from_dict(OR5B_extWallU_dict, orient='index')
    OR5B_extWallU[0] = OR5B_extWallU[0] - OR5B_baseline_EUI
    
    OR5B_slabU = pd.DataFrame.from_dict(OR5B_slabU_dict, orient='index')
    OR5B_slabU[0] = OR5B_slabU[0] - OR5B_baseline_EUI
    
    OR5B_windowU = pd.DataFrame.from_dict(OR5B_windowU_dict, orient='index')
    OR5B_windowU[0] = OR5B_windowU[0] - OR5B_baseline_EUI
    
    OR5B_windowSHGC = pd.DataFrame.from_dict(OR5B_windowSHGC_dict, orient='index')
    OR5B_windowSHGC[0] = OR5B_windowSHGC[0] - OR5B_baseline_EUI
    
    # MN6A
    MN6A_bsmtWallU = pd.DataFrame.from_dict(MN6A_bsmtWallU_dict, orient='index')
    MN6A_bsmtWallU[0] = MN6A_bsmtWallU[0] - MN6A_baseline_EUI
    
    MN6A_ceilingU = pd.DataFrame.from_dict(MN6A_ceilingU_dict, orient='index')
    MN6A_ceilingU[0] = MN6A_ceilingU[0] - MN6A_baseline_EUI
    
    MN6A_extWallU = pd.DataFrame.from_dict(MN6A_extWallU_dict, orient='index')
    MN6A_extWallU[0] = MN6A_extWallU[0] - MN6A_baseline_EUI
    
    MN6A_slabU = pd.DataFrame.from_dict(MN6A_slabU_dict, orient='index')
    MN6A_slabU[0] = MN6A_slabU[0] - MN6A_baseline_EUI
    
    MN6A_windowU = pd.DataFrame.from_dict(MN6A_windowU_dict, orient='index')
    MN6A_windowU[0] = MN6A_windowU[0] - MN6A_baseline_EUI
    
    MN6A_windowSHGC = pd.DataFrame.from_dict(MN6A_windowSHGC_dict, orient='index')
    MN6A_windowSHGC[0] = MN6A_windowSHGC[0] - MN6A_baseline_EUI
    
    # MN7A
    MN7A_bsmtWallU = pd.DataFrame.from_dict(MN7A_bsmtWallU_dict, orient='index')
    MN7A_bsmtWallU[0] = MN7A_bsmtWallU[0] - MN7A_baseline_EUI
    
    MN7A_ceilingU = pd.DataFrame.from_dict(MN7A_ceilingU_dict, orient='index')
    MN7A_ceilingU[0] = MN7A_ceilingU[0] - MN7A_baseline_EUI
    
    MN7A_extWallU = pd.DataFrame.from_dict(MN7A_extWallU_dict, orient='index')
    MN7A_extWallU[0] = MN7A_extWallU[0] - MN7A_baseline_EUI
    
    MN7A_slabU = pd.DataFrame.from_dict(MN7A_slabU_dict, orient='index')
    MN7A_slabU[0] = MN7A_slabU[0] - MN7A_baseline_EUI
    
    MN7A_windowU = pd.DataFrame.from_dict(MN7A_windowU_dict, orient='index')
    MN7A_windowU[0] = MN7A_windowU[0] - MN7A_baseline_EUI
    
    MN7A_windowSHGC = pd.DataFrame.from_dict(MN7A_windowSHGC_dict, orient='index')
    MN7A_windowSHGC[0] = MN7A_windowSHGC[0] - MN7A_baseline_EUI
    
    
    index = ['Baseline', 'Basement Wall U-Value', 'Ceiling U-Value', 'Exterior Wall U-Value', 'Slab F-Value', 'Window U-Value', 'Window SHGC']
    
    d = {'IL4A': [IL4A_baseline_EUI, IL4A_bsmtWallU, IL4A_ceilingU, IL4A_extWallU, IL4A_slabU, IL4A_windowU, IL4A_windowSHGC],
         'WA4C': [WA4C_baseline_EUI, WA4C_bsmtWallU, WA4C_ceilingU, WA4C_extWallU, WA4C_slabU, WA4C_windowU, WA4C_windowSHGC],
         'OR4C': [OR4C_baseline_EUI, OR4C_bsmtWallU, OR4C_ceilingU, OR4C_extWallU, OR4C_slabU, OR4C_windowU, OR4C_windowSHGC],
         'IL5A': [IL5A_baseline_EUI, IL5A_bsmtWallU, IL5A_ceilingU, IL5A_extWallU, IL5A_slabU, IL5A_windowU, IL5A_windowSHGC], 
         'WA5B': [WA5B_baseline_EUI, WA5B_bsmtWallU, WA5B_ceilingU, WA5B_extWallU, WA5B_slabU, WA5B_windowU, WA5B_windowSHGC],
         'OR5B': [OR5B_baseline_EUI, OR5B_bsmtWallU, OR5B_ceilingU, OR5B_extWallU, OR5B_slabU, OR5B_windowU, OR5B_windowSHGC],
         'MN6A': [MN6A_baseline_EUI, MN6A_bsmtWallU, MN6A_ceilingU, MN6A_extWallU, MN6A_slabU, MN6A_windowU, MN6A_windowSHGC],
         'MN7A': [MN7A_baseline_EUI, MN7A_bsmtWallU, MN7A_ceilingU, MN7A_extWallU, MN7A_slabU, MN7A_windowU, MN7A_windowSHGC]
         }
    
    df = pd.DataFrame.from_dict(d)
    df['index'] = index
    df = df.set_index('index')
    
    return df