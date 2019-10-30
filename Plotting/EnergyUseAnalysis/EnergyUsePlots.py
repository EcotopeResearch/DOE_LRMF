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
from inputoutput_data import inputoutput

# gather data from results
df = inputoutput()


commonBsmt_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\commonBsmt\\AllCombinedResults.csv'
commonSlab_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\commonSlab\\AllCombinedResults.csv'
gardenBsmt_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\gardenBsmt\\AllCombinedResults.csv'
gardenSlab_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\gardenSlab\\AllCombinedResults.csv'

commonBsmt = pd.read_csv(commonBsmt_path)
commonSlab = pd.read_csv(commonSlab_path)
gardenBsmt = pd.read_csv(gardenBsmt_path)
gardenSlab = pd.read_csv(gardenSlab_path)
dfs = [commonBsmt, commonSlab, gardenBsmt, gardenSlab]


# create lists for different climate zones.
IL4A = []
WA4C = []
OR4C = []
IL5A = []
WA5B = []
OR5B = []
MN6A = []
MN7A = []

# create lists for multiple linear regression

IL4A_unitCOP = []
WA4C_unitCOP = []
OR4C_unitCOP = []
IL5A_unitCOP = []
WA5B_unitCOP = []
OR5B_unitCOP = []
MN6A_unitCOP = []
MN7A_unitCOP = []

IL4A_dhwType = []
WA4C_dhwType = []
OR4C_dhwType = []
IL5A_dhwType = []
WA5B_dhwType = []
OR5B_dhwType = []
MN6A_dhwType = []
MN7A_dhwType = []

IL4A_dhwEff = []
WA4C_dhwEff = []
OR4C_dhwEff = []
IL5A_dhwEff = []
WA5B_dhwEff = []
OR5B_dhwEff = []
MN6A_dhwEff = []
MN7A_dhwEff = []

IL4A_unitLPD = []
WA4C_unitLPD = []
OR4C_unitLPD = []
IL5A_unitLPD = []
WA5B_unitLPD = []
OR5B_unitLPD = []
MN6A_unitLPD = []
MN7A_unitLPD = []

IL4A_unitFlow = []
WA4C_unitFlow = []
OR4C_unitFlow = []
IL5A_unitFlow = []
WA5B_unitFlow = []
OR5B_unitFlow = []
MN6A_unitFlow = []
MN7A_unitFlow = []

IL4A_unitSP = []
WA4C_unitSP = []
OR4C_unitSP = []
IL5A_unitSP = []
WA5B_unitSP = []
OR5B_unitSP = []
MN6A_unitSP = []
MN7A_unitSP = []

IL4A_unitHVACSP = []
WA4C_unitHVACSP = []
OR4C_unitHVACSP = []
IL5A_unitHVACSP = []
WA5B_unitHVACSP = []
OR5B_unitHVACSP = []
MN6A_unitHVACSP = []
MN7A_unitHVACSP = []

IL4A_wallU = []
WA4C_wallU = []
OR4C_wallU = []
IL5A_wallU = []
WA5B_wallU = []
OR5B_wallU = []
MN6A_wallU = []
MN7A_wallU = []

IL4A_ceilingU = []
WA4C_ceilingU = []
OR4C_ceilingU = []
IL5A_ceilingU = []
WA5B_ceilingU = []
OR5B_ceilingU = []
MN6A_ceilingU = []
MN7A_ceilingU = []

IL4A_slabU = []
WA4C_slabU = []
OR4C_slabU = []
IL5A_slabU = []
WA5B_slabU = []
OR5B_slabU = []
MN6A_slabU = []
MN7A_slabU = []

IL4A_windowU = []
WA4C_windowU = []
OR4C_windowU = []
IL5A_windowU = []
WA5B_windowU = []
OR5B_windowU = []
MN6A_windowU = []
MN7A_windowU = []

IL4A_SHGC = []
WA4C_SHGC = []
OR4C_SHGC = []
IL5A_SHGC = []
WA5B_SHGC = []
OR5B_SHGC = []
MN6A_SHGC = []
MN7A_SHGC = []

IL4A_strLtg = []
WA4C_strLtg = []
OR4C_strLtg = []
IL5A_strLtg = []
WA5B_strLtg = []
OR5B_strLtg = []
MN6A_strLtg = []
MN7A_strLtg = []

IL4A_prkLtg = []
WA4C_prkLtg = []
OR4C_prkLtg = []
IL5A_prkLtg = []
WA5B_prkLtg = []
OR5B_prkLtg = []
MN6A_prkLtg = []
MN7A_prkLtg = []

IL4A_extPrkLtg = []
WA4C_extPrkLtg = []
OR4C_extPrkLtg = []
IL5A_extPrkLtg = []
WA5B_extPrkLtg = []
OR5B_extPrkLtg = []
MN6A_extPrkLtg = []
MN7A_extPrkLtg = []

eui = []
weather = []
unitCOP = []
dhwType = []
dhwEff = []
unitLPD = []
unitFlow = []            
unitSP = []
unitHVACSP = []
wallU = []
ceilingU = []
slabU = []
windowU = []
SHGC = []
strLtg = []
prkLtg = []
extPrkLtg = []


for i in range(0,len(dfs)):
    
    df = dfs[i]
    for i in range(0, len(df)):
        
        # climate zone plots
        
        # check weather file location - St. Louis
        if df.loc[i,'WeatherFile']=='USA_MO_St.Louis-Spirit.of.St.Louis.AP.724345_TMY3.epw':
            # energy usage
            IL4A.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
            
            # inputs for multi-var regression
            IL4A_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
            IL4A_dhwType.append(df.loc[i,'@@ONCOEF@@'])
            IL4A_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
            IL4A_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
            IL4A_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
            IL4A_unitSP.append(df.loc[i,'@@SPUNIT@@'])
            IL4A_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
            IL4A_wallU.append(df.loc[i,'@@WALLU@@'])
            IL4A_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
            IL4A_slabU.append(df.loc[i,'@@SLABU@@'])
            IL4A_windowU.append(df.loc[i,'@@WINU@@'])
            IL4A_SHGC.append(df.loc[i,'@@SHGC@@'])            
            IL4A_strLtg.append(df.loc[i,'@@LTGSTR@@'])
            IL4A_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
            IL4A_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])

            
        # check weather file location - Seattle
        if df.loc[i,'WeatherFile']=='USA_WA_Seattle-Tacoma.Intl.AP.727930_TMY3.epw':
            WA4C.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
            
            # inputs for multi-var regression
            WA4C_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
            WA4C_dhwType.append(df.loc[i,'@@ONCOEF@@'])
            WA4C_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
            WA4C_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
            WA4C_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
            WA4C_unitSP.append(df.loc[i,'@@SPUNIT@@'])
            WA4C_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
            WA4C_wallU.append(df.loc[i,'@@WALLU@@'])
            WA4C_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
            WA4C_slabU.append(df.loc[i,'@@SLABU@@'])
            WA4C_windowU.append(df.loc[i,'@@WINU@@'])
            WA4C_SHGC.append(df.loc[i,'@@SHGC@@'])            
            WA4C_strLtg.append(df.loc[i,'@@LTGSTR@@'])
            WA4C_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
            WA4C_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
            
        # check weather file location - Portland
        if df.loc[i,'WeatherFile']=='USA_OR_Portland.Intl.AP.726980_TMY3.epw':
            OR4C.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
            
            # inputs for multi-var regression
            OR4C_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
            OR4C_dhwType.append(df.loc[i,'@@ONCOEF@@'])
            OR4C_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
            OR4C_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
            OR4C_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
            OR4C_unitSP.append(df.loc[i,'@@SPUNIT@@'])
            OR4C_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
            OR4C_wallU.append(df.loc[i,'@@WALLU@@'])
            OR4C_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
            OR4C_slabU.append(df.loc[i,'@@SLABU@@'])
            OR4C_windowU.append(df.loc[i,'@@WINU@@'])
            OR4C_SHGC.append(df.loc[i,'@@SHGC@@'])            
            OR4C_strLtg.append(df.loc[i,'@@LTGSTR@@'])
            OR4C_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
            OR4C_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
        
        # check weather file location - Chicago
        if df.loc[i,'WeatherFile']=='USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw':
            IL5A.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
            
            # inputs for multi-var regression
            IL5A_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
            IL5A_dhwType.append(df.loc[i,'@@ONCOEF@@'])
            IL5A_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
            IL5A_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
            IL5A_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
            IL5A_unitSP.append(df.loc[i,'@@SPUNIT@@'])
            IL5A_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
            IL5A_wallU.append(df.loc[i,'@@WALLU@@'])
            IL5A_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
            IL5A_slabU.append(df.loc[i,'@@SLABU@@'])
            IL5A_windowU.append(df.loc[i,'@@WINU@@'])
            IL5A_SHGC.append(df.loc[i,'@@SHGC@@'])            
            IL5A_strLtg.append(df.loc[i,'@@LTGSTR@@'])
            IL5A_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
            IL5A_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
            
        # check weather file location - Spokane
        if df.loc[i,'WeatherFile']=='USA_WA_Spokane.Intl.AP.727850_TMY3.epw':
            WA5B.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
            
            # inputs for multi-var regression
            WA5B_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
            WA5B_dhwType.append(df.loc[i,'@@ONCOEF@@'])
            WA5B_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
            WA5B_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
            WA5B_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
            WA5B_unitSP.append(df.loc[i,'@@SPUNIT@@'])
            WA5B_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
            WA5B_wallU.append(df.loc[i,'@@WALLU@@'])
            WA5B_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
            WA5B_slabU.append(df.loc[i,'@@SLABU@@'])
            WA5B_windowU.append(df.loc[i,'@@WINU@@'])
            WA5B_SHGC.append(df.loc[i,'@@SHGC@@'])            
            WA5B_strLtg.append(df.loc[i,'@@LTGSTR@@'])
            WA5B_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
            WA5B_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@']) 
            
        # check weather file location - Redmond
        if df.loc[i,'WeatherFile']=='USA_OR_Redmond-Roberts.Field.726835_TMY3.epw':
            OR5B.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
            
            # inputs for multi-var regression
            OR5B_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
            OR5B_dhwType.append(df.loc[i,'@@ONCOEF@@'])
            OR5B_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
            OR5B_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
            OR5B_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
            OR5B_unitSP.append(df.loc[i,'@@SPUNIT@@'])
            OR5B_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
            OR5B_wallU.append(df.loc[i,'@@WALLU@@'])
            OR5B_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
            OR5B_slabU.append(df.loc[i,'@@SLABU@@'])
            OR5B_windowU.append(df.loc[i,'@@WINU@@'])
            OR5B_SHGC.append(df.loc[i,'@@SHGC@@'])            
            OR5B_strLtg.append(df.loc[i,'@@LTGSTR@@'])
            OR5B_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
            OR5B_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
            
        # check weather file location - Minneapolis
        if df.loc[i,'WeatherFile']=='USA_MN_Minneapolis-St.Paul.Intl.AP.726580_TMY3.epw':
            MN6A.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
            
            # inputs for multi-var regression
            MN6A_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
            MN6A_dhwType.append(df.loc[i,'@@ONCOEF@@'])
            MN6A_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
            MN6A_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
            MN6A_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
            MN6A_unitSP.append(df.loc[i,'@@SPUNIT@@'])
            MN6A_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
            MN6A_wallU.append(df.loc[i,'@@WALLU@@'])
            MN6A_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
            MN6A_slabU.append(df.loc[i,'@@SLABU@@'])
            MN6A_windowU.append(df.loc[i,'@@WINU@@'])
            MN6A_SHGC.append(df.loc[i,'@@SHGC@@'])            
            MN6A_strLtg.append(df.loc[i,'@@LTGSTR@@'])
            MN6A_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
            MN6A_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
            
        # check weather file location - Bemidji
        if df.loc[i,'WeatherFile']=='USA_MN_Bemidji.Muni.AP.727550_TMY3.epw':
            MN7A.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)

            # inputs for multi-var regression
            MN7A_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
            MN7A_dhwType.append(df.loc[i,'@@ONCOEF@@'])
            MN7A_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
            MN7A_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
            MN7A_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
            MN7A_unitSP.append(df.loc[i,'@@SPUNIT@@'])
            MN7A_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
            MN7A_wallU.append(df.loc[i,'@@WALLU@@'])
            MN7A_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
            MN7A_slabU.append(df.loc[i,'@@SLABU@@'])
            MN7A_windowU.append(df.loc[i,'@@WINU@@'])
            MN7A_SHGC.append(df.loc[i,'@@SHGC@@'])            
            MN7A_strLtg.append(df.loc[i,'@@LTGSTR@@'])
            MN7A_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
            MN7A_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
            
        ## inputs for multiple regression, assume linear
        
        # dependent variable, reponse, dependent
        eui.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
        
        # explanatory variables, covariates, independent
        weather.append(df.loc[i,'WeatherFile'])
        unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
        dhwType.append(df.loc[i,'@@ONCOEF@@'])
        dhwEff.append(df.loc[i,'@@DHWCOP@@'])
        unitLPD.append(df.loc[i,'@@UNITLPD@@'])
        unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
        unitSP.append(df.loc[i,'@@SPUNIT@@'])
        unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])
        wallU.append(df.loc[i,'@@WALLU@@'])
        ceilingU.append(df.loc[i,'@@CEILINGU@@'])
        slabU.append(df.loc[i,'@@SLABU@@'])
        windowU.append(df.loc[i,'@@WINU@@'])
        SHGC.append(df.loc[i,'@@SHGC@@'])            
        strLtg.append(df.loc[i,'@@LTGSTR@@'])
        prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
        extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
    
index = ['eui', 'unitCOP', 'dhwType', 'dhwEff', 'unitLPD', 
         'unitFlow', 'unitSP', 'unitHVACSP', 'wallU', 'ceilingU', 'slabU', 'windowU',
         'SHGC', 'strLtg', 'prkLtg', 'extPrkLtg']

d = {'total': [eui, unitCOP, dhwType, dhwEff, unitLPD, 
         unitFlow, unitSP, unitHVACSP, wallU, ceilingU, slabU, windowU,
         SHGC, strLtg, prkLtg, extPrkLtg],
     
     'IL4A': [IL4A, IL4A_unitCOP, IL4A_dhwType, IL4A_dhwEff, IL4A_unitLPD, 
         IL4A_unitFlow, IL4A_unitSP, IL4A_unitHVACSP, IL4A_wallU, IL4A_ceilingU, IL4A_slabU, IL4A_windowU,
         IL4A_SHGC, IL4A_strLtg, IL4A_prkLtg, IL4A_extPrkLtg],
              
     'WA4C': [WA4C, WA4C_unitCOP, WA4C_dhwType, WA4C_dhwEff, WA4C_unitLPD, 
         WA4C_unitFlow, WA4C_unitSP, WA4C_unitHVACSP, WA4C_wallU, WA4C_ceilingU, WA4C_slabU, WA4C_windowU,
         WA4C_SHGC, WA4C_strLtg, WA4C_prkLtg, WA4C_extPrkLtg],
              
     'OR4C': [IL4A, OR4C_unitCOP, OR4C_dhwType, OR4C_dhwEff, OR4C_unitLPD, 
         OR4C_unitFlow, OR4C_unitSP, OR4C_unitHVACSP, OR4C_wallU, OR4C_ceilingU, OR4C_slabU, OR4C_windowU,
         OR4C_SHGC, OR4C_strLtg, OR4C_prkLtg, OR4C_extPrkLtg],

     'IL5A': [IL5A, IL5A_unitCOP, IL5A_dhwType, IL5A_dhwEff, IL5A_unitLPD, 
         IL5A_unitFlow, IL5A_unitSP, IL5A_unitHVACSP, IL5A_wallU, IL5A_ceilingU, IL5A_slabU, IL5A_windowU,
         IL5A_SHGC, IL5A_strLtg, IL5A_prkLtg, IL5A_extPrkLtg],
     
     'WA5B': [WA5B, WA5B_unitCOP, WA5B_dhwType, WA5B_dhwEff, WA5B_unitLPD, 
         WA5B_unitFlow, WA5B_unitSP, WA5B_unitHVACSP, WA5B_wallU, WA5B_ceilingU, WA5B_slabU, WA5B_windowU,
         WA5B_SHGC, WA5B_strLtg, WA5B_prkLtg, WA5B_extPrkLtg],
     
     'OR5B': [OR5B, OR5B_unitCOP, OR5B_dhwType, OR5B_dhwEff, OR5B_unitLPD, 
         OR5B_unitFlow, OR5B_unitSP, OR5B_unitHVACSP, OR5B_wallU, OR5B_ceilingU, OR5B_slabU, OR5B_windowU,
         OR5B_SHGC, OR5B_strLtg, OR5B_prkLtg, OR5B_extPrkLtg],
     
     'MN6A': [MN6A, MN6A_unitCOP, MN6A_dhwType, MN6A_dhwEff, MN6A_unitLPD, 
         MN6A_unitFlow, MN6A_unitSP, MN6A_unitHVACSP, MN6A_wallU, MN6A_ceilingU, MN6A_slabU, MN6A_windowU,
         MN6A_SHGC, MN6A_strLtg, MN6A_prkLtg, MN6A_extPrkLtg],
     
     'MN7A': [MN7A, MN7A_unitCOP, MN7A_dhwType, MN7A_dhwEff, MN7A_unitLPD, 
         MN7A_unitFlow, MN7A_unitSP, MN7A_unitHVACSP, MN7A_wallU, MN7A_ceilingU, MN7A_slabU, MN7A_windowU,
         MN7A_SHGC, MN7A_strLtg, MN7A_prkLtg, MN7A_extPrkLtg]
     }

df = pd.DataFrame.from_dict(d)
df['index'] = index
df = df.set_index('index')

    
    
# climate zone plots
# =============================================================================
# ax = sns.distplot(IL4A, hist=True, kde=True, norm_hist=False)
# plt.show()
# ax = sns.distplot(WA4C, hist=True, kde=True, norm_hist=False, bins=8)
# plt.show()
# ax = sns.distplot(OR4C, hist=True, kde=True, norm_hist=False, bins=8)
# plt.show()
# ax = sns.distplot(IL5A, hist=True, kde=True, norm_hist=False)
# plt.show()
# ax = sns.distplot(WA5B, hist=True, kde=True, norm_hist=False)
# plt.show()
# ax = sns.distplot(OR5B, hist=True, kde=True, norm_hist=False, bins=8)
# plt.show()
# ax = sns.distplot(MN6A, hist=True, kde=True, norm_hist=False, bins=8)
# plt.show()
# ax = sns.distplot(MN7A, hist=True, kde=True, norm_hist=False)
# plt.show()
# =============================================================================

### PLOT HISTOGRAMS
ax = sns.distplot(eui, hist=True, kde=False, norm_hist=False)
plt.show()

WA = WA4C + WA5B
ax = sns.distplot(WA, hist=True, kde=False, norm_hist=False)
plt.show()

OR = OR4C + OR5B
ax = sns.distplot(OR, hist=True, kde=False, norm_hist=False)
plt.show()

IL = IL4A + IL5A
ax = sns.distplot(IL, hist=True, kde=False, norm_hist=False)
plt.show()

MN = MN6A + MN7A
ax = sns.distplot(MN, hist=True, kde=False, norm_hist=False)
plt.show()


### PERFORM MULTI-VAR LINEAR REGRESSION
# import packages
import numpy as np
import statsmodels.api as sm
import sys 

# inputs
title = 'Regression Analysis'
covars = [unitCOP, dhwType, dhwEff, unitLPD, unitFlow,
          unitSP, unitHVACSP, wallU] # covars used

energy = eui

# saving txt exports
stdoutOrigin=sys.stdout 
sys.stdout = open(title + ".txt", "w")

rng = [(max(x) - min(x)) for x in covars] # calculate range for each covar
var = []

for i in range(0, len(energy)):
    # regression on mech systems
    var.append([x[i] for x in covars])
    
    
x = np.array(var)
y = np.array(energy)

x, y = np.array(x), np.array(y)

# run regression
model = sm.OLS(y,x)
results = model.fit()

# parse results
coef = results.params # COEF
std_err = results.bse # STD ERROR
norm_coef = coef * rng

# print results
print(results.summary())

print()
print('Normalized Coefficients')
print(norm_coef)


sys.stdout.close()
sys.stdout=stdoutOrigin






