# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:50:38 2019

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


def ipu_to_siu(arg):
    """
    AEI FUNCTION: IP to SI u-value conversion
    Location: aei_conversions.py module of aei package
    """
    return arg * 5.678263337

##### CONSTRUCTION CONDUCTIVITY ######

def bsmtWallCond(bsmtWallU):
    '''
    EnergyPlus Object
    Material
    Input
    Conductivity
    '''
    
    # SEED model conductivity
    bsmtwall_consol_layer = 0.05966275 # [W/m*K]
    u_start = 0.549441 # [W/m*K]
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(bsmtWallU)):
        
        if ipu_to_siu(bsmtWallU[i]) == 0:
            u_start = 0.50 # replace with code minimum if = 0
        else:
            u_start = ipu_to_siu(bsmtWallU[i]) 
        
        u_const = ipu_to_siu(u_start) # convert to si
        u_material = u_const - (u_start - bsmtwall_consol_layer) # calculate new material u-value
        
        var.append(u_material)
    
    return var

def floorCond(BsmtFloorU):
    '''
    EnergyPlus Object
    Material
    Input
    Conductivity
    '''
    
    # SEED model conductivity
    floor_consol_layer = 0.0485233 # [W/m*K]
    u_start = 0.184182 # [W/m*K]
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(BsmtFloorU)):
        
        if ipu_to_siu(BsmtFloorU[i]) == 0:
            u_start = 0.50 # replace with code minimum if = 0
        else:
            u_start = ipu_to_siu(BsmtFloorU[i]) 
        
        u_const = ipu_to_siu(u_start) # convert to si
        u_material = u_const - (u_start - floor_consol_layer) # calculate new material u-value
        
        var.append(u_material)
    
    return var

def extWallCond(wtmnGenWallU):
    # SEED model conductivity
    wall_consol_layer = 0.05966275 # [W/m*K]
    u_start = 0.367494 # [W/m*K]
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(wtmnGenWallU)):
        
        if ipu_to_siu(wtmnGenWallU[i]) == 0:
            u_start = 0.50 # replace with code minimum if = 0
        else:
            u_start = ipu_to_siu(wtmnGenWallU[i]) 
        
        u_const = ipu_to_siu(u_start) # convert to si
        u_material = u_const - (u_start - wall_consol_layer) # calculate new material u-value
        
        var.append(u_material)
    
    return var

def ceilingCond(wtmnCeilingU):
    # SEED model conductivity
    ceil_consol_layer = 0.136352 # [W/m*K]
    u_start = 0.549441 # [W/m*K]
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(wtmnCeilingU)):
        
        if ipu_to_siu(wtmnCeilingU[i]) == 0:
            u_start = 0.50 # replace with code minimum if = 0
        else:
            u_start = ipu_to_siu(wtmnCeilingU[i]) 
        
        u_const = ipu_to_siu(u_start) # convert to si
        u_material = u_const - (u_start - ceil_consol_layer) # calculate new material u-value
        
        var.append(u_material)
    
    return var

def slabCond(fndWtmnU, FndWtmnF):
    # SEED model conductivity
    slab_consol_layer = 0.0485233 # [W/m*K]
    u_start = 0.184182 # [W/m*K]
    
    # empty list to return    
    var = []    
    
    for i in range(0, len(fndWtmnU)):  
        
        # from reported u-value
        if fndWtmnU[i] != 0:                   
            u_start = ipu_to_siu(fndWtmnU[i])         
        # from reported f-factor
        elif FndWtmnF[i] !=0:
            u_start = ipu_to_siu(0.1556*fndWtmnU[i]) 
        # if nothing reported
        else:
            u_start = 0.50
        
        u_const = ipu_to_siu(u_start) # convert to si
        u_material = u_const - (u_start - slab_consol_layer) # calculate new material u-value
    
        var.append(u_material)
    
    return var

def windowU(wtmnWindowU):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(wtmnWindowU)):
        
        if ipu_to_siu(wtmnWindowU[i]) == 0:
            u_start = ipu_to_siu(0.50) # replace with code minimum if = 0
        else:
            u_start = ipu_to_siu(wtmnWindowU[i]) 
        
        u_window = u_start # convert to si
        
        var.append(u_window)
    
    return var

def windowSHGC(wtmnWindowSHGC):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(wtmnWindowSHGC)):
        
        if wtmnWindowSHGC[i] == 0:
            shgc = 0.50 # replace with code minimum if = 0
        else:
            shgc = wtmnWindowSHGC[i] 
        
        var.append(shgc)
    
    return var









