# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 05:22:31 2019

This file was created as part of converting DCI outputs into EnergyPlus 
inputs. Each SEED model will have it's own function to create it's inputs, 
and store those inputs in a dataframe with columns that match the jEplus
input csv for export. Each function will be built on smaller functions
that control the calculation of DCI to EnergyPlus inputs.

Three files total:
    1) inputs_csv_creator
    2) dataframe_creator
    3) dci_to_energyplus

    
This is the dataframe_creator file, it's functions create dataframes that
match with EnergyPlus Inputs.
    
@author: scott
"""

import pandas as pd
from dci_to_energyplus import (buildingName, 
                               slabBoundaryCondition)

def commonBsmt_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    names = buildingName(df['sitex'])
    
    # create dataframe
    new_df = pd.DataFrame()
    new_df['names'] = names
    
    return new_df
    
def commonSlab_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    names = buildingName(df['sitex'])
    slabBC = slabBoundaryCondition(df['FndType'].tolist())
    
    # create dataframe
    new_df = pd.DataFrame()
    new_df['names'] = names
    new_df['slabBC'] = slabBC

    return new_df
    
def gardenBsmt_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    names = buildingName(df['sitex'])
    
    # create dataframe
    new_df = pd.DataFrame()
    new_df['names'] = names
    
    return new_df
    
def gardenSlab_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    names = buildingName(df['sitex'])
    
    # create dataframe
    new_df = pd.DataFrame()
    new_df['names'] = names
    
    return new_df
