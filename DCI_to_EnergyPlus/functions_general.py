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

from functions_switchers import (heat_cop_switcher, curve_heatCapFT_switcher, curve_HeatCapFFF_switcher,
                                 curve_HPACHeatEIRFT_switcher, curve_HPACHeatEIRFFF_switcher, cool_cop_switcher,
                                 curve_coolCapFT_switcher, curve_coolCapFFF_switcher, curve_HPACcoolEIRFT_switcher,
                                 curve_HPACcoolEIRFFF_switcher, curve_HPACCOOLPLFFPLR_switcher, curve_Defrost_EIR_FT_switcher)

##########################################
##### GENERAL BUILDING INFORMATION #######
##########################################

def runnumber(df):
    
    # empty list to return  
    var = []
    
    #for loop to walk through list of Foundation Types
    for i in range(0,len(df)):
        var.append(i+1)
        
    return var

def z1(df):
    
    # empty list to return  
    var = []
    
    #for loop to walk through list of Foundation Types
    for i in range(0,len(df)):
        var.append(0)
        
    return var

def z2(df):
    
    # empty list to return  
    var = []
    
    #for loop to walk through list of Foundation Types
    for i in range(0,len(df)):
        var.append(0)
        
    return var
    
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
        
        if lpdIntStairwell[i] != 0:    
            var.append(lpdIntStairwell[i]*120)
        else:
            var.append(30) # assumed value around .25 LPD
    
    return var

def extPrkLights(lpdExtPrk):

    # empty list to return    
    var = []    
    
    # Ext Parking LPD * sf - same as basement
    for i in range(0, len(lpdExtPrk)):
        var.append(lpdExtPrk[i]*7800)
    
    return var

###################################
##### EQUIPMENT PERFORMANCE #######
###################################

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
    '''
    EnergyPlus Object
    Coil:Heating:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_HeatCapFFF_switcher(unitHeat[i]))
        
    return var

def HeatingEfficiencyCurves3(unitHeat):
    '''
    EnergyPlus Object
    Coil:Heating:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_HPACHeatEIRFT_switcher(unitHeat[i]))
        
    return var

def HeatingEfficiencyCurves4(unitHeat):
    '''
    EnergyPlus Object
    Coil:Heating:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_HPACHeatEIRFFF_switcher(unitHeat[i]))
        
    return var

def HeatingEfficiencyCurves5(unitHeat):
    '''
    EnergyPlus Object
    Coil:Heating:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_HPACCOOLPLFFPLR_switcher(unitHeat[i]))
        
    return var

def HeatingEfficiencyCurves6(unitHeat):
    '''
    EnergyPlus Object
    Coil:Heating:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    

    # placeholder    
    for i in range(0, len(unitHeat)):
        var.append(curve_Defrost_EIR_FT_switcher(unitHeat[i]))
        
    return var

def CoolEfficiency(unitCool, centralSys):
    '''
    EnergyPlus Object
    Coil:Cooling:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(cool_cop_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves1(unitCool):
    '''
    EnergyPlus Object
    Coil:Cooling:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_coolCapFT_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves2(unitCool):
    '''
    EnergyPlus Object
    Coil:Cooling:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_coolCapFFF_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves3(unitCool):
    '''
    EnergyPlus Object
    Coil:Cooling:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_HPACcoolEIRFT_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves4(unitCool):
    '''
    EnergyPlus Object
    Coil:Cooling:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_HPACcoolEIRFFF_switcher(unitCool[i]))
    
    return var

def CoolingEfficiencyCurves5(unitCool):
    '''
    EnergyPlus Object
    Coil:Cooling:DX:SingleSpeed
    '''
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(unitCool)):
        var.append(curve_HPACCOOLPLFFPLR_switcher(unitCool[i]))
    
    return var
