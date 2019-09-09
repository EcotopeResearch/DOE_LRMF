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

import numpy as np

def buildingName(sitex, runinput):
    
    # empty list to return  
    var = []

    # site ID + user input string    
    name = [str(x) + runinput for x in sitex]
    var = name
    return var

def slabBoundaryCondition(FndType):
    
    # empty list to return  
    var = []
    
    #for loop to walk through list of Foundation Types
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
    
    # lighting power of 180 W for all buildings
    for i in range(0, len(df)):
        var.append(180)
    
    return var

def unitDhwCoeffOn(centralDhwEffAvg, inunitDhwEffAvg):
    '''
    EnergyPlus Object
    WaterHeater:Mixed
    Input
    On Cycle Loss Coefficient to Ambient Temperature
    '''
    
    # empty list to return    
    var = []    
    
    # central of unit 0.5, 0.8
    for i in range(0, len(centralDhwEffAvg)):
        if centralDhwEffAvg[i] != 0 and inunitDhwEffAvg[i] == 0:
            var.append(0.5)
        elif inunitDhwEffAvg[i] != 0 and centralDhwEffAvg[i] == 0:
            var.append(0.8)
        else:
            print("ERROR IN DHW unitDhwCoeffOn")
    
    return var

def unitDhwCoeffOff(centralDhwEffAvg, inunitDhwEffAvg):
    
    '''
    EnergyPlus Object
    WaterHeater:Mixed
    Input
    Off Cycle Loss Coefficient to Ambient Temperature
    '''
    
    # empty list to return    
    var = []    
    
    # central of unit 0.5, 0.8
    for i in range(0, len(centralDhwEffAvg)):
        if centralDhwEffAvg[i] != 0 and inunitDhwEffAvg[i] == 0:
            var.append(0.5)
        elif inunitDhwEffAvg[i] != 0 and centralDhwEffAvg[i] == 0:
            var.append(0.8)
        else:
            print("ERROR IN DHW unitDhwCoeffOff")
    
    return var

def unitDhwThermEff(centralDhwEffAvg, inunitDhwEffAvg):
    '''
    EnergyPlus Object
    WaterHeater:Mixed
    Input
    Heater Thermal Efficiency
    '''
    
    # empty list to return    
    var = []    
    
    # central or unit eff
    for i in range(0, len(centralDhwEffAvg)):
        if centralDhwEffAvg[i] != 0 and inunitDhwEffAvg[i] == 0:
            var.append(centralDhwEffAvg[i])
        elif inunitDhwEffAvg[i] != 0 and centralDhwEffAvg[i] == 0:
            var.append(inunitDhwEffAvg[i])
        else:
            print("ERROR IN DHW unitDhwThermEff")
    
    return var

def lightingStairs(lpdIntStairwell):

    # empty list to return    
    var = []    
    
    # LPD stairs * 120 sf, 40 per floor
    for i in range(0, len(lpdIntStairwell)):
        var.append(lpdIntStairwell[i]*120)
    
    return var

def extPrkLights(lpdExtPrk):

    # empty list to return    
    var = []    
    
    # Ext Parking LPD * sf - same as basement
    for i in range(0, len(lpdExtPrk)):
        var.append(lpdExtPrk[i]*7800)
    
    return var

