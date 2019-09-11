# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:48:03 2019

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

################################
##### CORRIDOR FUNCTIONS #######
################################

def commonVentilationFlowrate(ventCentralYN, ventCorridorErvYN, ventCorridorErvEff):
    '''
    EnergyPlus Object
    ZoneVentilation:DesignFlowRate
    '''
    # unit airflow [m3/s]
    flowrate = 0.051 # about 108 cfm, from 0.06 cfm/sf
    avgERV = 0.6
    
    # empty list to return    
    var = []    
    
    # loop through rows
    for i in range(0, len(ventCorridorErvYN)):
        
        # if ERV reduce flowrate
        if ventCorridorErvYN[i] == 'Yes':
            if ventCorridorErvEff[i] != 0:
                var.append(flowrate*(1-(float(ventCorridorErvEff[i])/100)))
            else:
                var.append(flowrate*(1-avgERV))
        # otherwist apply normal flowrate
        else:
            var.append(flowrate)
        
    return var

def commonVentilationSP(ventCentralYN, ventCorridorErvYN):
    
    # empty list to return    
    var = []    
    unit = 62.21 # units are pa, equal to 0.25" 
    central = 248.84 # units are pa, equal to 0.25"
    erv = 62.21 # units are pa, equal to 0.25"
    
    
    # static pressure
    for i in range(0, len(ventCorridorErvYN)):
        if ventCorridorErvYN[i] == 'Yes' and ventCentralYN[i] == 'Yes':
            var.append(unit + central + erv)
        elif ventCorridorErvYN[i] == 'Yes' and ventCentralYN[i] == 'No':
            var.append(unit + erv)
        elif ventCorridorErvYN[i] == 'No' and ventCentralYN[i] == 'Yes':
            var.append(unit + central)
        elif ventCorridorErvYN[i] == 'No' and ventCentralYN[i] == 'No':
            var.append(unit)
        else:
            print('ERROR IN unitVentilationSP')
    
    return var

def commonHvacFanSP(ventCentralYN, ventCorridorErvYN):
    
    # empty list to return    
    var = []    
    
    
    unit = 62.21 # units are pa, equal to 0.25" 
    erv = 62.21 # units are pa, equal to 0.25"
    
    
    # static pressure, central systems are covered above
    for i in range(0, len(ventCorridorErvYN)):
        if ventCorridorErvYN[i] == 'Yes' and ventCentralYN[i] == 'Yes':
            var.append(unit)
        elif ventCorridorErvYN[i] == 'Yes' and ventCentralYN[i] == 'No':
            var.append(unit + erv)
        elif ventCorridorErvYN[i] == 'No' and ventCentralYN[i] == 'Yes':
            var.append(unit)
        elif ventCorridorErvYN[i] == 'No' and ventCentralYN[i] == 'No':
            var.append(unit)
        else:
            print('ERROR IN unitVentilationSP')
    
    return var

def commonHeatingSetpoint(df):

    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append(20) # in °C
    
    return var

def commonCoolingSetpoint(df):

    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append(22.2222) # in °C
    
    return var

# LPD

def commonLpd(lpdCommon):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(lpdCommon)):
        var.append(lpdCommon[i])
    
    return var