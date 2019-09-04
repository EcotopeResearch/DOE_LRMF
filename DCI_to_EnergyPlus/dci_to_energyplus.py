# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 05:22:31 2019

This file was created as part of converting DCI outputs into EnergyPlus 
inputs. Each SEED model will have it's own function to create it's inputs, 
and store those inputs in a dataframe with columns that match the jEplus
input csv for export. Each function will be built on smaller functions
that control the calculation of DCI to EnergyPlus inputs.

Three files total:
    1) inputs_csv_creator
    2) dataframe_creator
    3) dci_to_energyplus

    
This is the dci_to_energyplus file, it's functions area individual 
calculations for getting from the DCI outputs to the EnergyPlus inputs.

@author: scott
"""

##### GENERAL BUILDING INFORMATION #######

def buildingName(sitex):
    
    # empty list to return  
    var = []
    
    # add more info, discuss with Hyunwoo
    var = sitex
    return var

def slabBoundaryCondition(FndType):
    
    # empty list to return  
    var = []
    
    for i in range(0,len(FndType)):
        if FndType[i] == 'slab':
            var.append('Ground')
        elif FndType[i] == 'commercialbelow':
            var.append('Adiabatic')
        else:
            print('ERROR in slab boundary condition category')
            return
    
    return var    
