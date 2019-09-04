# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:47:12 2019

@author: scott
"""

##### UNIT SYSTEM EFFICIENCIES #######

def unitHeatingEfficiency(heatunitType, centralSys):

    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(heatunitType)):
        var.append('unitHeatingEfficiency')
    
    return var

def unitHeatingEfficiencyCurves(heatunitType):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(heatunitType)):
        var.append('unitHeatingEfficiencyCurves')
        
    return var

def unitCoolEfficiency(df):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('unitCoolEfficiency')
    
    return var

def unitCoolingEfficiencyCurves(df):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append('unitCoolingEfficiencyCurves')
    
    return var

def unitVentilationSP(ventBsemtErvYN, lpdIntPkunit, ventunitYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(ventBsemtErvYN)):
        var.append('unitVentilationFlowrate')
    
    return var

def unitHvacFanSP(heatunitType):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(heatunitType)):
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