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
    



##### VENTILATION FUNCTIONS #######
    
### SHOULD BE MADE FLEXIBLE TO WORK FOR COMMON, BASEMENT, AND CORRIDOR. 

#### NOT USING VENT CENTRALYN
def unitVentilationFlowrate(ventCentralYN, ventUnitErvYN, ventUnitErvEff):
    '''
    EnergyPlus Object
    ZoneVentilation:DesignFlowRate
    '''
    # unit airflow [m3/s]
    flowrate = 0.0212524794559365 # about 45 cfm, from PNNL model
    avgERV = 0.6
    
    # empty list to return    
    var = []    
    
    # loop through rows
    for i in range(0, len(ventUnitErvYN)):
        
        # if ERV reduce flowrate
        if ventUnitErvYN[i] == 'Yes':
            if ventUnitErvEff[i] != 0:
                var.append(flowrate*(1-(float(ventUnitErvEff[i])/100)))
            else:
                var.append(flowrate*(1-avgERV))
        # otherwist apply normal flowrate
        else:
            var.append(flowrate)
    
    return var

def unitVentilationSP(ventCentralYN, ventUnitErvYN):
    
    # empty list to return    
    var = []    
    unit = 62.21 # units are pa, equal to 0.25" 
    central = 248.84 # units are pa, equal to 1"
    erv = 62.21 # units are pa, equal to 0.25"
    
    
    # static pressure
    for i in range(0, len(ventUnitErvYN)):
        if ventUnitErvYN[i] == 'Yes' and ventCentralYN[i] == 'Yes':
            var.append(unit + central + erv)
        elif ventUnitErvYN[i] == 'Yes' and ventCentralYN[i] == 'No':
            var.append(unit + erv)
        elif ventUnitErvYN[i] == 'No' and ventCentralYN[i] == 'Yes':
            var.append(unit + central)
        elif ventUnitErvYN[i] == 'No' and ventCentralYN[i] == 'No':
            var.append(unit)
        else:
            var.append(unit + central + erv)
            print('No unitVentilationSP in DCI')
    
    return var

# add central ventilation
def unitHvacFanSP(ventCentralYN, ventUnitErvYN):
    
    # empty list to return    
    var = []    
    
    
    unit = 62.21 # units are pa, equal to 0.25" 
    erv = 62.21 # units are pa, equal to 0.25"
    
    
    # static pressure, central systems are covered above
    for i in range(0, len(ventUnitErvYN)):
        if ventUnitErvYN[i] == 'Yes' and ventCentralYN[i] == 'Yes':
            var.append(unit)
        elif ventUnitErvYN[i] == 'Yes' and ventCentralYN[i] == 'No':
            var.append(unit + erv)
        elif ventUnitErvYN[i] == 'No' and ventCentralYN[i] == 'Yes':
            var.append(unit)
        elif ventUnitErvYN[i] == 'No' and ventCentralYN[i] == 'No':
            var.append(unit)
        else:
            var.append(unit)
            print('No unitVentilationSP from DCI')
    
    return var

# UNIT SETPOINT TEMPERATURES

def unitHeatingSetpoint(df):

    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append(20) # in °C
    
    return var

def unitCoolingSetpoint(df):

    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(df)):
        var.append(22.2222) # in °C
    
    return var

# LPD

def unitLpd(lpdUnit):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(lpdUnit)):
        if lpdUnit[i] != 0:
            var.append(lpdUnit[i])
        else: 
            var.append(0.5)
            print('No Unit LPD from DCI')
    return var
    
    
    
    