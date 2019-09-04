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

def unitHeatingEfficiencyCurves1(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append('unitHeatingEfficiencyCurves1')
        
    return var

def unitHeatingEfficiencyCurves2(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append('unitHeatingEfficiencyCurves2')
        
    return var

def unitHeatingEfficiencyCurves3(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append('unitHeatingEfficiencyCurves3')
        
    return var

def unitHeatingEfficiencyCurves4(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append('unitHeatingEfficiencyCurves4')
        
    return var

def unitHeatingEfficiencyCurves5(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append('unitHeatingEfficiencyCurves5')
        
    return var

def unitHeatingEfficiencyCurves6(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append('unitHeatingEfficiencyCurves6')
        
    return var

def unitCoolEfficiency(unitCool, centralSys):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append('unitCoolEfficiency')
    
    return var

def unitCoolingEfficiencyCurves1(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append('unitCoolingEfficiencyCurves1')
    
    return var

def unitCoolingEfficiencyCurves2(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append('unitCoolingEfficiencyCurves2')
    
    return var

def unitCoolingEfficiencyCurves3(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append('unitCoolingEfficiencyCurves3')
    
    return var

def unitCoolingEfficiencyCurves4(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append('unitCoolingEfficiencyCurves4')
    
    return var

def unitCoolingEfficiencyCurves5(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append('unitCoolingEfficiencyCurves5')
    
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

def unitHvacFanSP(unitheat, ventUnitErvYN):
    
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
    
    
    
    