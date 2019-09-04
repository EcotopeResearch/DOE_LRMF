# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:47:12 2019

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

##### UNIT SYSTEM EFFICIENCIES #######

def unitHeatingEfficiency(unitHeat, centralSys):

    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(unitHeat)):
        var.append('unitHeatingEfficiency')
    
    return var

def unitHeatingEfficiencyCurves(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append('unitHeatingEfficiencyCurves')
        
    return var

def unitCoolEfficiency(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append('unitCoolEfficiency')
    
    return var

def unitCoolingEfficiencyCurves(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append('unitCoolingEfficiencyCurves')
    
    return var

def unitVentilationFlowrate(ventUnitErvYN, ventUnitErvEff, ventCentralYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(ventUnitErvYN)):
        var.append('unitVentilationFlowrate')
    
    return var

def unitVentilationSP(ventUnitErvYN, ventCentralYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(ventUnitErvYN)):
        var.append('unitVentilationFlowrate')
    
    return var

def unitHvacFanSP(unitheat):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitheat)):
        var.append('unitHvacFanSP')
    
    return var

# UNIT SETPOINT TEMPERATURES

def unitHeatingSetpoint(df):

    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('unitHeatingSetpoint')
    
    return var

def unitCoolingSetpoint(df):

    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('unitCoolingSetpoint')
    
    return var

# LPD

def unitLpd(lpdUnit):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(lpdUnit)):
        var.append('unitLpd')
    
    return var
    
    
    
    