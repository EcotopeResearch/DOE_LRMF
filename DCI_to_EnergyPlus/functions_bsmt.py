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

def bsmtVentilationFlowrate(ventBsmtYN, ventBsemtErvYN, ventBsemtErvEff, lpdIntPkCommon):
    
    # basement airflow [m3/s]
    flowrate = 0.22 # about 468 cfm, from 0.06 cfm/sf
    avgERV = 0.6
    
    # empty list to return    
    var = []    
    
    # loop through rows
    for i in range(0, len(ventBsemtErvYN)):
        
        # if ventilation
        if ventBsmtYN[i] == 'Yes':
            # if ERV reduce flowrate
            if ventBsemtErvEff[i] == 'Yes':
                if ventBsemtErvEff[i] != 0:
                    var.append(flowrate*(1-(float(ventBsemtErvEff[i])/100)))
                else:
                    var.append(flowrate*(1-avgERV))
            # otherwist apply normal flowrate
            else:
                var.append(flowrate)
        else:
            var.append(0.01) # no flow, about 20 cfm
        
    return var

def bsmtVentilationSP(ventBsemtErvYN):
    
    # empty list to return    
    var = []    
    central = 62.21 # units are pa, equal to 0.25"
    erv = 62.21 # units are pa, equal to 0.25"
    
    
    # static pressure
    for i in range(0, len(ventBsemtErvYN)):
        if ventBsemtErvYN[i] == 'Yes':
            var.append(central + erv)
        elif ventBsemtErvYN[i] == 'No':
            var.append(central)
        else:
            var.append(central)
            print('No bsmtVentilationSP info in DCI')
    
    return var

def bsmtHvacFanSP(ventBsemtErvYN):
    
    # empty list to return    
    var = []        
    
    # static pressure
    for i in range(0, len(ventBsemtErvYN)):
        var.append(24.884) # 0.1", it's just one system 
    
    return var

# BASEMENT SETPOINTS

def bsmtHeatingSetpoint(heatBsmtYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(heatBsmtYN)):
        if heatBsmtYN[i] == 'Yes':
            var.append(15.5) # in °C
        else:
            var.append(15) # in °C
    
    return var

def bsmtCoolingSetpoint(heatBsmtYN):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(heatBsmtYN)):
        var.append(27) # in °C
    
    return var

def bsmtLpd(intPrkLpd, FndType):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(intPrkLpd)):
        if intPrkLpd[i] != 0:
            var.append(intPrkLpd[i] * 7800) # LPD * area
        else:
            if FndType[i] == 'ventedcrawlspace':    
                var.append(0)
            elif FndType[i] == 'unheatedbsmt':
                var.append(0)
            elif FndType[i] == 'unventedcrawlspace':
                var.append(0)
            elif FndType[i] == 'heatedbsmt':
                var.append(0.2 * 7800) # 0.2 for bsmt * area for interior parking
            else:
                var.append(0)
                print('No bsmtLpd in DCI')
            
    return var


