# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 05:22:31 2019

This file was created as part of converting DCI outputs into EnergyPlus 
inputs. Each SEED model will have it's own function to create it's inputs, 
and store those inputs in a dataframe with columns that match the jEplus
input csv for export. Each function will be built on smaller functions
that control the calculation of DCI to EnergyPlus inputs.

Files Include
    1) inputs_csv_creator
    2) dataframe_creator
    3) function files

    
This is the inputs_csv_creator file, it generates the csv for energyplus.
    

@author: scott
"""

import pandas as pd
#from dci_to_energyplus import *
from dataframe_creator import (commonBsmt_inputs, commonSlab_inputs, 
                               gardenBsmt_inputs, gardenSlab_inputs)

df = pd.read_csv('ModelingInputs.csv')

# break the input df up into sub-dataframes that match the SEED models

# first by entry type
df_common = df.loc[df['EntrType']=='common entry']
df_garden = df.loc[df['EntrType']=='garden style']

# then by foundation
df_commonBsmt = df_common.loc[(df['FndType']=='unheatedbsmt') | 
        (df['FndType']=='heatedbsmt') |
        (df['FndType']=='unventedcrawlspace') |
        (df['FndType']=='ventedcrawlspace')]

df_commonSlab = df_common.loc[(df['FndType']=='slab') | 
        (df['FndType']=='commercialbelow')]

df_gardenBsmt = df_garden.loc[(df['FndType']=='unheatedbsmt') | 
        (df['FndType']=='heatedbsmt') |
        (df['FndType']=='unventedcrawlspace') |
        (df['FndType']=='ventedcrawlspace')]

df_gardenSlab = df_garden.loc[(df['FndType']=='slab') | 
        (df['FndType']=='commercialbelow')]


# use functions to generate the EnergyPlus Input dataframes
commonBsmt = commonBsmt_inputs(df_commonBsmt)
commonSlab = commonSlab_inputs(df_commonSlab)
gardenBsmt = gardenBsmt_inputs(df_gardenBsmt)
gardenSlab = gardenSlab_inputs(df_gardenSlab)

# final step! print to the inputs csv for parametric run
commonBsmt.to_csv('inputs_commonBsmt.csv')


