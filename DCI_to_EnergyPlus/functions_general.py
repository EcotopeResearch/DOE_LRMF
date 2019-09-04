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

    
This is a function file, it's functions are common individual 
calculations for getting from the DCI outputs to the EnergyPlus inputs.

@author: scott
"""

##### GENERAL BUILDING INFORMATION #######

def buildingName(sitex):
    
    # empty list to return  
    var = []
    
    # add more info, discuss with Hyunwoo
    var = sitex
    return var

def slabBoundaryCondition(FndType):
    
    # empty list to return  
    var = []
    
    for i in range(0,len(FndType)):
        if FndType[i] == 'slab':
            var.append('Ground')
        elif FndType[i] == 'commercialbelow':
            var.append('Adiabatic')
        else:
            print('ERROR in slab boundary condition category')
            return
    
    return var    

def exteriorCorrLights(df):
    
    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(df)):
        var.append('exteriorCorrLights')
    
    return var

def unitDhwCoeffOn(centralDhwEffAvg, inunitDhwEffAvg):
    
    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(centralDhwEffAvg)):
        var.append('unitDhwCoeffOn')
    
    return var

def unitDhwCoeffOff(centralDhwEffAvg, inunitDhwEffAvg):
    
    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(centralDhwEffAvg)):
        var.append('unitDhwCoeffOff')
    
    return var

def unitDhwThermEff(centralDhwEffAvg, inunitDhwEffAvg):
    
    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(centralDhwEffAvg)):
        var.append('unitDhwThermEff')
    
    return var

def lightingStairs(lpdIntStairwell):

    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(lpdIntStairwell)):
        var.append('lightingStairs')
    
    return var

def extPrkLights(lpdExtPrk):

    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(lpdExtPrk)):
        var.append('extPrkLights')
    
    return var

