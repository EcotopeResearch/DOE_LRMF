# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:49:25 2019

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

##### BASEMENT SYSTEM EFFICIENCIES #######

def bsmtHeatingEfficiency(heatBsmtType, HVACcentral_YN, centralSys):

    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(heatBsmtType)):
        var.append('bsmtHeatingEfficiency')
    
    return var

def bsmtHeatingEfficiencyCurves1(heatBsmtType):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(heatBsmtType)):
        var.append('bsmtHeatingEfficiencyCurves1')
        
    return var

def bsmtHeatingEfficiencyCurves2(heatBsmtType):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(heatBsmtType)):
        var.append('bsmtHeatingEfficiencyCurves2')
        
    return var

def bsmtHeatingEfficiencyCurves3(heatBsmtType):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(heatBsmtType)):
        var.append('bsmtHeatingEfficiencyCurves3')
        
    return var

def bsmtHeatingEfficiencyCurves4(heatBsmtType):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(heatBsmtType)):
        var.append('bsmtHeatingEfficiencyCurves4')
        
    return var

def bsmtHeatingEfficiencyCurves5(heatBsmtType):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(heatBsmtType)):
        var.append('bsmtHeatingEfficiencyCurves5')
        
    return var

def bsmtHeatingEfficiencyCurves6(heatBsmtType):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(heatBsmtType)):
        var.append('bsmtHeatingEfficiencyCurves6')
        
    return var

def bsmtCoolEfficiency(df):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('bsmtCoolEfficiency')
    
    return var

def bsmtCoolingEfficiencyCurves1(df):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('bsmtCoolingEfficiencyCurves1')
    
    return var

def bsmtCoolingEfficiencyCurves2(df):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('bsmtCoolingEfficiencyCurves2')
    
    return var

def bsmtCoolingEfficiencyCurves3(df):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('bsmtCoolingEfficiencyCurves3')
    
    return var

def bsmtCoolingEfficiencyCurves4(df):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('bsmtCoolingEfficiencyCurves4')
    
    return var

def bsmtCoolingEfficiencyCurves5(df):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('bsmtCoolingEfficiencyCurves5')
    
    return var

def bsmtVentilationFlowrate(ventBsemtErvYN, ventBsemtErvEff, lpdIntPkCommon, ventBsmtYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(ventBsemtErvYN)):
        var.append('bsmtVentilationFlowrate')
    
    return var

def bsmtVentilationSP(ventBsemtErvYN, lpdIntPkCommon, ventBsmtYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(ventBsemtErvYN)):
        var.append('bsmtVentilationFlowrate')
    
    return var

def bsmtHvacFanSP(heatBsmtType):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(heatBsmtType)):
        var.append('bsmtHvacFanSP')
    
    return var

# BASEMENT SETPOINTS

def bsmtHeatingSetpoint(FndType, heatBsmtYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(FndType)):
        var.append('bsmtHeatingSetpoint')
    
    return var

def bsmtCoolingSetpoint(FndType, heatBsmtYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(FndType)):
        var.append('bsmtCoolingSetpoint')
    
    return var

def bsmtLpd(intPrkLpd):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(intPrkLpd)):
        var.append('bsmtLpd')
    
    return var


