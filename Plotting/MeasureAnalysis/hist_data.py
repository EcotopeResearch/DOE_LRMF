# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:37:52 2019

@author: scott
"""

import pandas as pd

def hist_data():
    
    # bring in DCI for histograms
    dci = pd.read_csv('_stat_modeldata.csv')
    dci.fillna(0, inplace=True)
    
    
    # create dictionaries to store results for plotting
            
    IL4A_bsmtWallU = []
    IL4A_ceilingU = []
    IL4A_extWallU = []
    IL4A_slabU = []
    IL4A_windowU = []
    IL4A_windowSHGC = []
    
    WA4C_bsmtWallU = []
    WA4C_ceilingU = []
    WA4C_extWallU = []
    WA4C_slabU = []
    WA4C_windowU = []
    WA4C_windowSHGC = []
    
    OR4C_bsmtWallU = []
    OR4C_ceilingU = []
    OR4C_extWallU = []
    OR4C_slabU = []
    OR4C_windowU = []
    OR4C_windowSHGC = []
    
    IL5A_bsmtWallU = []
    IL5A_ceilingU = []
    IL5A_extWallU = []
    IL5A_slabU = []
    IL5A_windowU = []
    IL5A_windowSHGC = []
    
    WA5B_bsmtWallU = []
    WA5B_ceilingU = []
    WA5B_extWallU = []
    WA5B_slabU = []
    WA5B_windowU = []
    WA5B_windowSHGC = []
    
    OR5B_bsmtWallU = []
    OR5B_ceilingU = []
    OR5B_extWallU = []
    OR5B_slabU = []
    OR5B_windowU = []
    OR5B_windowSHGC = []
    
    MN6A_bsmtWallU = []
    MN6A_ceilingU = []
    MN6A_extWallU = []
    MN6A_slabU = []
    MN6A_windowU = []
    MN6A_windowSHGC = []
    
    MN7A_bsmtWallU = []
    MN7A_ceilingU = []
    MN7A_extWallU = []
    MN7A_slabU = []
    MN7A_windowU = []
    MN7A_windowSHGC = []
    
    
    for i in range(0,len(dci)):
        
        if dci.loc[i,'KeyCodeValue'] != 0:
            
            # if state and climate zone (matches weather file)
            if dci.loc[i,'State']=='Illinois' and dci.loc[i,'CZ']=='4A':
                
                if dci.loc[i,'KeyCodeName']=='GenWallAGU':
                    IL4A_extWallU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='BsmtWallU':
                    IL4A_bsmtWallU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='CeilingU':
                    IL4A_ceilingU.append(dci.loc[i,'KeyCodeValue'])
                            
                if dci.loc[i,'KeyCodeName']=='Fnd_f':
                    IL4A_slabU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='WindowU':
                    IL4A_windowU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='WindowSHGC':        
                    IL4A_windowSHGC.append(dci.loc[i,'KeyCodeValue'])
                
            if dci.loc[i,'State']=='Washington' and dci.loc[i,'CZ']=='4C':
              
                if dci.loc[i,'KeyCodeName']=='GenWallAGU':
                    WA4C_extWallU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='BsmtWallU':
                    WA4C_bsmtWallU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='CeilingU':
                    WA4C_ceilingU.append(dci.loc[i,'KeyCodeValue'])
                            
                if dci.loc[i,'KeyCodeName']=='Fnd_f':
                    WA4C_slabU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='WindowU':
                    WA4C_windowU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='WindowSHGC':        
                    WA4C_windowSHGC.append(dci.loc[i,'KeyCodeValue'])
        
                
            if dci.loc[i,'State']=='Oregon' and dci.loc[i,'CZ']=='4C':
                
                if dci.loc[i,'KeyCodeName']=='GenWallAGU':
                    OR4C_extWallU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='BsmtWallU':
                    OR4C_bsmtWallU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='CeilingU':
                    OR4C_ceilingU.append(dci.loc[i,'KeyCodeValue'])
                            
                if dci.loc[i,'KeyCodeName']=='Fnd_f':
                    OR4C_slabU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='WindowU':
                    OR4C_windowU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='WindowSHGC':        
                    OR4C_windowSHGC.append(dci.loc[i,'KeyCodeValue'])
                
            if dci.loc[i,'State']=='Illinois' and dci.loc[i,'CZ']=='5A':
        
                if dci.loc[i,'KeyCodeName']=='GenWallAGU':
                    IL5A_extWallU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='BsmtWallU':
                    IL5A_bsmtWallU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='CeilingU':
                    IL5A_ceilingU.append(dci.loc[i,'KeyCodeValue'])
                            
                if dci.loc[i,'KeyCodeName']=='Fnd_f':
                    IL5A_slabU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='WindowU':
                    IL5A_windowU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='WindowSHGC':        
                    IL5A_windowSHGC.append(dci.loc[i,'KeyCodeValue'])
                
            if dci.loc[i,'State']=='Washington' and dci.loc[i,'CZ']=='5B':
        
                if dci.loc[i,'KeyCodeName']=='GenWallAGU':
                    WA5B_extWallU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='BsmtWallU':
                    WA5B_bsmtWallU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='CeilingU':
                    WA5B_ceilingU.append(dci.loc[i,'KeyCodeValue'])
                            
                if dci.loc[i,'KeyCodeName']=='Fnd_f':
                    WA5B_slabU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='WindowU':
                    WA5B_windowU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='WindowSHGC':        
                    WA5B_windowSHGC.append(dci.loc[i,'KeyCodeValue'])
                
            if dci.loc[i,'State']=='Oregon' and dci.loc[i,'CZ']=='5B':
        
                if dci.loc[i,'KeyCodeName']=='GenWallAGU':
                    OR5B_extWallU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='BsmtWallU':
                    OR5B_bsmtWallU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='CeilingU':
                    OR5B_ceilingU.append(dci.loc[i,'KeyCodeValue'])
                            
                if dci.loc[i,'KeyCodeName']=='Fnd_f':
                    OR5B_slabU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='WindowU':
                    OR5B_windowU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='WindowSHGC':        
                    OR5B_windowSHGC.append(dci.loc[i,'KeyCodeValue'])
                
            if dci.loc[i,'State']=='Minnesota' and dci.loc[i,'CZ']=='6A':
        
                if dci.loc[i,'KeyCodeName']=='GenWallAGU':
                    MN6A_extWallU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='BsmtWallU':
                    MN6A_bsmtWallU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='CeilingU':
                    MN6A_ceilingU.append(dci.loc[i,'KeyCodeValue'])
                            
                if dci.loc[i,'KeyCodeName']=='Fnd_f':
                    MN6A_slabU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='WindowU':
                    MN6A_windowU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='WindowSHGC':        
                    MN6A_windowSHGC.append(dci.loc[i,'KeyCodeValue'])
        
        
            if dci.loc[i,'State']=='Minnesota' and dci.loc[i,'CZ']=='7A':
        
                if dci.loc[i,'KeyCodeName']=='GenWallAGU':
                    MN7A_extWallU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='BsmtWallU':
                    MN7A_bsmtWallU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='CeilingU':
                    MN7A_ceilingU.append(dci.loc[i,'KeyCodeValue'])
                            
                if dci.loc[i,'KeyCodeName']=='Fnd_f':
                    MN7A_slabU.append(dci.loc[i,'KeyCodeValue'])
                
                if dci.loc[i,'KeyCodeName']=='WindowU':
                    MN7A_windowU.append(dci.loc[i,'KeyCodeValue'])
                    
                if dci.loc[i,'KeyCodeName']=='WindowSHGC':        
                    MN7A_windowSHGC.append(dci.loc[i,'KeyCodeValue'])
            
    index = ['Basement Wall U-Value', 'Ceiling U-Value', 'Exterior Wall U-Value', 'Slab F-Value', 'Window U-Value', 'Window SHGC']
    
    d = {'IL4A': [IL4A_bsmtWallU, IL4A_ceilingU, IL4A_extWallU, IL4A_slabU, IL4A_windowU, IL4A_windowSHGC],
         'WA4C': [WA4C_bsmtWallU, WA4C_ceilingU, WA4C_extWallU, WA4C_slabU, WA4C_windowU, WA4C_windowSHGC],
         'OR4C': [OR4C_bsmtWallU, OR4C_ceilingU, OR4C_extWallU, OR4C_slabU, OR4C_windowU, OR4C_windowSHGC],
         'IL5A': [IL5A_bsmtWallU, IL5A_ceilingU, IL5A_extWallU, IL5A_slabU, IL5A_windowU, IL5A_windowSHGC], 
         'WA5B': [WA5B_bsmtWallU, WA5B_ceilingU, WA5B_extWallU, WA5B_slabU, WA5B_windowU, WA5B_windowSHGC],
         'OR5B': [OR5B_bsmtWallU, OR5B_ceilingU, OR5B_extWallU, OR5B_slabU, OR5B_windowU, OR5B_windowSHGC],
         'MN6A': [MN6A_bsmtWallU, MN6A_ceilingU, MN6A_extWallU, MN6A_slabU, MN6A_windowU, MN6A_windowSHGC],
         'MN7A': [MN7A_bsmtWallU, MN7A_ceilingU, MN7A_extWallU, MN7A_slabU, MN7A_windowU, MN7A_windowSHGC]
         }
    
    df = pd.DataFrame.from_dict(d)
    df['index'] = index
    df = df.set_index('index')

    return df

