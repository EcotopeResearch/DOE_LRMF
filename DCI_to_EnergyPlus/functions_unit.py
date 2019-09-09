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
    
from functions_switchers import (heat_cop_switcher, curve_heatCapFT_switcher, curve_HeatCapFFF_switcher,
                                 curve_HPACHeatEIRFT_switcher, curve_HPACHeatEIRFFF_switcher, cool_cop_switcher,
                                 curve_coolCapFT_switcher, curve_coolCapFFF_switcher, curve_HPACcoolEIRFT_switcher,
                                 curve_HPACcoolEIRFFF_switcher, curve_HPACCOOLPLFFPLR_switcher, curve_Defrost_EIR_FT_switcher)

##### UNIT SYSTEM EFFICIENCIES #######

def HeatingEfficiency(unitHeat, centralSys):
    '''
    EnergyPlus Object
    Coil:Heating:DX:SingleSpeed
    Input
    Gross Rated Heating COP
    '''
    
    # empty list to return    
    var = []    
    
    # place holder
    for i in range(0, len(unitHeat)):
        var.append(heat_cop_switcher(unitHeat[i]))
    
    return var

def HeatingEfficiencyCurves1(unitHeat):
    '''
    EnergyPlus Object
    Coil:Heating:DX:SingleSpeed
    Input
    Heating Capacity Function of Temperature Curve Name
    '''

    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_heatCapFT_switcher(unitHeat[i]))
        
    return var

def HeatingEfficiencyCurves2(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_HeatCapFFF_switcher(unitHeat[i]))
        
    return var

def HeatingEfficiencyCurves3(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_HPACHeatEIRFT_switcher(unitHeat[i]))
        
    return var

def HeatingEfficiencyCurves4(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_HPACHeatEIRFFF_switcher(unitHeat[i]))
        
    return var

def HeatingEfficiencyCurves5(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_HPACCOOLPLFFPLR_switcher(unitHeat[i]))
        
    return var

def HeatingEfficiencyCurves6(unitHeat):
    
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_Defrost_EIR_FT_switcher(unitHeat[i]))
        
    return var

def CoolEfficiency(unitCool, centralSys):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(cool_cop_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves1(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_coolCapFT_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves2(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_coolCapFFF_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves3(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_HPACcoolEIRFT_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves4(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_HPACcoolEIRFFF_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves5(unitCool):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_HPACCOOLPLFFPLR_switcher(unitCool[i]))
    
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
    
    
    
    