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


def siu_to_ipu(arg):
    """
    AEI FUNCTION: IP to SI u-value conversion
    Location: aei_conversions.py module of aei package
    """
    return arg * 0.1761183515

def ipu_to_siu(arg):
    """
    AEI FUNCTION: IP to SI u-value conversion
    Location: aei_conversions.py module of aei package
    """
    return arg * 5.678

##### CONSTRUCTION CONDUCTIVITY ######

def bsmtWallCond(bsmtWallU, cz):
    '''
    EnergyPlus Object
    Material
    Input
    Conductivity
    '''
    
    # initial SEED model values
    k_i = 0.05966275 # initial insulation thermal conductivity [W/m*K]
    t_i = 0.0889 # insulation thickness [m]
    # starting u-value
    u_i = 0.549441 # construction u-value [W/m2*K]
    
    # equation #1
    # calculate resistance of everything except the insulation  
    res_o = (1/u_i) - (t_i/k_i) # resistance other materials [m2*k/W]
    
    # empty list to return    
    var = []    
    
    # loop through all bsmt wall u-values in DCI outputs
    # convert u-values to metric units
    for i in range(0, len(bsmtWallU)):
        # convert bsmt wall u-values from imperial units to metric units. 
        if ipu_to_siu(bsmtWallU[i]) == 0:
            
            ### IF THE VALUE IS ZERO WE NEED TO REPLACE WITH THE CODE MINIMUM ###
            ### THIS WILL ALSO DEPEND ON LOCATION, FUNCTIONALITY TO ADD ###
            
            if cz[i] == '4A':
                u = ipu_to_siu(0.059) # replace with code minimum if = 0
            else:
                u = ipu_to_siu(0.05)
            
        else:
            u = ipu_to_siu(bsmtWallU[i]) # target u-value
        
        # equation #2, list operation
        # calculate new thermal conductivity of insulation
        k = t_i / ((1/u)-res_o)
        
        var.append(k)
    
    return var

def floorCond(BsmtFloorU, cz):
    '''
    EnergyPlus Object
    Material
    Input
    Conductivity
    '''
    
    # initial SEED model values
    k_i = 0.0485233 # initial insulation thermal conductivity [W/m*K]
    t_i = 0.23495 # insulation thickness [m]
    # starting u-value
    u_i = 0.184182 # construction u-value [W/m2*K]
    
    # equation #1
    # calculate resistance of everything except the insulation  
    res_o = (1/u_i) - (t_i/k_i) # resistance other materials [m2*k/W]
    
    # empty list to return    
    var = []    
    
    # loop through all bsmt wall u-values in DCI outputs
    # convert u-values to metric units
    for i in range(0, len(BsmtFloorU)):
        # convert bsmt wall u-values from imperial units to metric units. 
        if ipu_to_siu(BsmtFloorU[i]) == 0:
            ### IF THE VALUE IS ZERO WE NEED TO REPLACE WITH THE CODE MINIMUM ###
            ### THIS WILL ALSO DEPEND ON LOCATION, FUNCTIONALITY TO ADD ###
            
            if cz[i] == '7A':
                u = ipu_to_siu(0.028) 
            elif cz[i] == '4A':
                u = ipu_to_siu(0.047)
            else:
                u = ipu_to_siu(0.033)
                
        else:
            u = ipu_to_siu(BsmtFloorU[i]) # target u-value
        
        # equation #2, list operation
        # calculate new thermal conductivity of insulation
        k = t_i / ((1/u)-res_o)
        
        var.append(k)
    
    return var

def extWallCond(wtmnGenWallU, st):
    '''
    EnergyPlus Object
    Material
    Input
    Conductivity
    '''
    
    # initial SEED model values
    k_i = 0.05966275 # initial insulation thermal conductivity [W/m*K]
    t_i = 0.1397 # insulation thickness [m]
    # starting u-value
    u_i = 0.367494 # construction u-value [W/m2*K]
    
    # equation #1
    # calculate resistance of everything except the insulation  
    res_o = (1/u_i) - (t_i/k_i) # resistance other materials [m2*k/W]
    
    # empty list to return    
    var = []    
    
    # loop through all bsmt wall u-values in DCI outputs
    # convert u-values to metric units
    for i in range(0, len(wtmnGenWallU)):
        # convert bsmt wall u-values from imperial units to metric units. 
        if ipu_to_siu(wtmnGenWallU[i]) == 0:
            ### IF THE VALUE IS ZERO WE NEED TO REPLACE WITH THE CODE MINIMUM ###
            ### THIS WILL ALSO DEPEND ON LOCATION, FUNCTIONALITY TO ADD ###
            
            if st[i] == 'OR':
                u = ipu_to_siu(0.06)
            elif st[i] == 'MN':
                u = ipu_to_siu(0.48)
            else:
                u = ipu_to_siu(0.57)

        else:
            u = ipu_to_siu(wtmnGenWallU[i]) # target u-value
        
        # equation #2, list operation
        # calculate new thermal conductivity of insulation
        k = t_i / ((1/u)-res_o)
        
        var.append(k)
    
    return var


def ceilingCond(wtmnCeilingU, st):
    # initial SEED model values
    k_i = 0.0617176 # initial insulation thermal conductivity [W/m*K]
    t_i = 0.447738918260194 # insulation thickness [m]
    # starting u-value
    u_i = 0.136352 # construction u-value [W/m2*K]
    
    # equation #1
    # calculate resistance of everything except the insulation  
    res_o = (1/u_i) - (t_i/k_i) # resistance other materials [m2*k/W]
    
    # empty list to return    
    var = []    
    
    # loop through all bsmt wall u-values in DCI outputs
    # convert u-values to metric units
    for i in range(0, len(wtmnCeilingU)):
        # convert bsmt wall u-values from imperial units to metric units. 
        if ipu_to_siu(wtmnCeilingU[i]) == 0:
            ### IF THE VALUE IS ZERO WE NEED TO REPLACE WITH THE CODE MINIMUM ###
            ### THIS WILL ALSO DEPEND ON LOCATION, FUNCTIONALITY TO ADD ###
            ### USING 0.5 AS PLACEHOLDER ###
            
            if st[i] == 'OR':
                u = ipu_to_siu(0.031)
            else:
                u = ipu_to_siu(0.026)
        
        else:
            u = ipu_to_siu(wtmnCeilingU[i]) # target u-value
        
        # equation #2, list operation
        # calculate new thermal conductivity of insulation
        k = t_i / ((1/u)-res_o)
        
        var.append(k)
    
    return var


def slabCond(fndWtmnU, FndWtmnF, st):
    # initial SEED model values
    k_i = 0.0485233 # initial insulation thermal conductivity [W/m*K]
    t_i = 0.23495 # insulation thickness [m]
    # starting u-value
    u_i = 0.184182 # construction u-value [W/m2*K]
    
    # equation #1
    # calculate resistance of everything except the insulation  
    res_o = (1/u_i) - (t_i/k_i) # resistance other materials [m2*k/W]
    
    ## loop through and calculate whether u val or f val or none
    slbU = []
    for i in range(0,len(FndWtmnF)):
        if FndWtmnF[i] !=0:
            slbU.append(float(FndWtmnF[i])*0.0474)
        elif fndWtmnU[i] !=0:
            slbU.append(fndWtmnU[i])
        else:
            slbU.append(0.05) ##THIS WILL NEED TO BE REPLACED WITH THE CODE MIN
    
    # empty list to return    
    var = []    
    
    # loop through all bsmt wall u-values in DCI outputs
    # convert u-values to metric units
    for i in range(0, len(slbU)):
        # convert bsmt wall u-values from imperial units to metric units. 
        if ipu_to_siu(slbU[i]) == 0:
            ### IF THE VALUE IS ZERO WE NEED TO REPLACE WITH THE CODE MINIMUM ###
            ### THIS WILL ALSO DEPEND ON LOCATION, FUNCTIONALITY TO ADD ###
            
            if st[i] == 'MN':
                u = ipu_to_siu(0.52)
            else:
                u = ipu_to_siu(0.54)
                
        else:
            u = ipu_to_siu(slbU[i]) # target u-value
        
        # equation #2, list operation
        # calculate new thermal conductivity of insulation
        k = t_i / ((1/u)-res_o)
        
        var.append(k)
    
    return var

def windowU(wtmnWindowU, st, cz):
    
    # empty list to return    
    var = []    
    
    # placeholder
    for i in range(0, len(wtmnWindowU)):
        
        if ipu_to_siu(wtmnWindowU[i]) == 0:
            if st[i] == 'OR':
                u_start = ipu_to_siu(0.35) # replace with code minimum if = 0
            elif cz[i] == '4A':
                u_start = ipu_to_siu(0.35)
            else:
                u_start = ipu_to_siu(0.32)
        
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
            shgc = 0.4 # code min
        else:
            shgc = wtmnWindowSHGC[i] 
        
        var.append(shgc)
    
    return var









