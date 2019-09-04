# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:50:38 2019

This file was created as part of converting DCI outputs into EnergyPlus 
inputs. Each SEED model will have it's own function to create it's inputs, 
and store those inputs in a dataframe with columns that match the jEplus
input csv for export. Each function will be built on smaller functions
that control the calculation of DCI to EnergyPlus inputs.

Files Include
    1) inputs_csv_creator
    2) dataframe_creator
    3) function files

    
This is a function file, it's functions are common individual 
calculations for getting from the DCI outputs to the EnergyPlus inputs.

@author: scott
"""

##### CONSTRUCTION CONDUCTIVITY ######

def bsmtWallCond(bsmtWallU):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(bsmtWallU)):
        var.append('bsmtWallCond')
    
    return var

def floorCond(BsmtFloorU):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(BsmtFloorU)):
        var.append('floorCond')
    
    return var

def extWallCond(wtmnGenWallU):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(wtmnGenWallU)):
        var.append('extWallCond')
    
    return var

def ceilingCond(wtmnCeilingU):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(wtmnCeilingU)):
        var.append('ceilingCond')
    
    return var

def slabCond(fndWtmnU, FndWtmnF):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(fndWtmnU)):
        var.append('slabCond')
    
    return var














