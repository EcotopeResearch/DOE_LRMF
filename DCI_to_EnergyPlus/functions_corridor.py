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

##### CORRIDOR SYSTEM EFFICIENCIES #######

def commonHeatingEfficiency(commonHeat, hvacCentralYN, CentralSys):

    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(commonHeat)):
        var.append('commonHeatingEfficiency')
    
    return var

def commonHeatingEfficiencyCurves1(commonHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(commonHeat)):
        var.append('commonHeatingEfficiencyCurves1')
        
    return var

def commonHeatingEfficiencyCurves2(commonHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(commonHeat)):
        var.append('commonHeatingEfficiencyCurves2')
        
    return var

def commonHeatingEfficiencyCurves3(commonHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(commonHeat)):
        var.append('commonHeatingEfficiencyCurves3')
        
    return var

def commonHeatingEfficiencyCurves4(commonHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(commonHeat)):
        var.append('commonHeatingEfficiencyCurves4')
        
    return var

def commonHeatingEfficiencyCurves5(commonHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(commonHeat)):
        var.append('commonHeatingEfficiencyCurves5')
        
    return var

def commonHeatingEfficiencyCurves6(commonHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(commonHeat)):
        var.append('commonHeatingEfficiencyCurves6')
        
    return var


def commonCoolEfficiency(commonCool, hvacCentralYN, CentralSys):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(commonCool)):
        var.append('commonCoolEfficiency')
    
    return var

def commonCoolingEfficiencyCurves1(commonCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(commonCool)):
        var.append('commonCoolingEfficiencyCurves1')
    
    return var

def commonCoolingEfficiencyCurves2(commonCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(commonCool)):
        var.append('commonCoolingEfficiencyCurves2')
    
    return var

def commonCoolingEfficiencyCurves3(commonCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(commonCool)):
        var.append('commonCoolingEfficiencyCurves3')
    
    return var

def commonCoolingEfficiencyCurves4(commonCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(commonCool)):
        var.append('commonCoolingEfficiencyCurves4')
    
    return var

def commonCoolingEfficiencyCurves5(commonCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(commonCool)):
        var.append('commonCoolingEfficiencyCurves5')
    
    return var

def commonVentilationFlowrate(ventCorridorErvYN, ventCorridorErvEff):
   
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(ventCorridorErvYN)):
        var.append('commonVentilationFlowrate')
    
    return var
    
def commonVentilationSP(ventCorridorErvYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(ventCorridorErvYN)):
        var.append('commonVentilationSP')
    
    return var

def commonHvacFanSP(commonHeat, commonCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(commonHeat)):
        var.append('commonHvacFanSP')
    
    return var

def commonHeatingSetpoint(df):

    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('commonHeatingSetpoint')
    
    return var

def commonCoolingSetpoint(df):

    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('commonCoolingSetpoint')
    
    return var

# LPD

def commonLpd(lpdCommon):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(lpdCommon)):
        var.append('commonLpd')
    
    return var