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

from designDays import (SeattleDD)

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

def z1(cz, st): #weather switcher
    
    # empty list to return  
    var = []
    
    #for loop to walk through list of Foundation Types
    for i in range(0,len(cz)):
        
        if cz[i] == '4A':
            var.append('USA_MO_St.Louis-Spirit.of.St.Louis.AP.724345_TMY3.epw')
        elif cz[i] == '4C' and st[i] == 'WA':
            var.append('USA_WA_Seattle-Tacoma.Intl.AP.727930_TMY3.epw')
        elif cz[i] == '4C' and st[i] == 'OR':
            var.append('USA_OR_Portland.Intl.AP.726980_TMY3.epw')
        elif cz[i] == '5A':
            var.append('USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw')            
        elif cz[i] == '5B' and st[i] == 'WA':
            var.append('USA_WA_Spokane.Intl.AP.727850_TMY3.epw')            
        elif cz[i] == '5B' and st[i] == 'OR':
            var.append('USA_OR_Redmond-Roberts.Field.726835_TMY3.epw')   
        elif cz[i] == '6A':
            var.append('USA_MN_Minneapolis-St.Paul.Intl.AP.726580_TMY3.epw')
        elif cz[i] == '7A':
            var.append('USA_MN_Bemidji.Muni.AP.727550_TMY3.epw')
        else:
            print('No climate zone could not identify weather file')
            var.append()
        
    return var

def z2(df):
    
    # empty list to return  
    var = []
    
    #for loop to walk through list of Foundation Types
    for i in range(0,len(df)):
        var.append(0)
        
    return var
    
def buildingName(sitex, cz):
    
    # empty list to return  
    var = []
    

    # site ID + user input string    
    for i in range(0,len(sitex)):
        var.append(str(cz[i])+'_'+str(sitex[i]))

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
            var.append(125) # Estimated thermal loss for recirc
        elif inunitDhwEffAvg[i] != 0 and centralDhwEffAvg[i] == 0:
            var.append(1)
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
            var.append(125) # estimated thermal loss for recirc
        elif inunitDhwEffAvg[i] != 0 and centralDhwEffAvg[i] == 0:
            var.append(1)
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
            var.append(84) # use code baseline of 0.7 
    
    return var

def extPrkLights(lpdExtPrk):

    # empty list to return    
    var = []    
    
    # Ext Parking LPD * sf - same as basement
    # no if for code baseline, assume no parking if zero
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
    
    for i in range(0, len(unitCool)):
        var.append(curve_HPACCOOLPLFFPLR_switcher(unitCool[i]))
    
    return var

###################################
#####     DESIGN DAYS       #######
###################################

def WinterDB(cz, st):
    '''
    EnergyPlus Object
    SizingPeriod:DesignDay
    '''
    # empty list
    var=[]
    
    for i in range(0, len(cz)):
        if cz[i] == "4A":
            var.append(-15)
        elif cz[i] == "4C" and st[i] == 'WA':
            var.append(-4.2)
        elif cz[i] == "4C" and st[i] == 'OR':
            var.append(-4.5)
        elif cz[i] == "5A":
            var.append(-20)                        
        elif cz[i] == "5B" and st[i] == 'WA':
            var.append(-16)
        elif cz[i] == "5B" and st[i] == 'OR':
            var.append(-14.8)
        elif cz[i] == "6A":
            var.append(-25.2)
        elif cz[i] == "7A":
            var.append(-30.4)
        else:
            print("unknown climate zone")
                                                    
    return var

def SummerDB(cz, st):
    '''
    EnergyPlus Object
    SizingPeriod:DesignDay
    '''
    # empty list
    var=[]
    
    for i in range(0, len(cz)):
        if cz[i] == "4A":
            var.append(35.1)
        elif cz[i] == "4C" and st[i] == 'WA':
            var.append(29.4)
        elif cz[i] == "4C" and st[i] == 'OR':
            var.append(32.9)
        elif cz[i] == "5A":
            var.append(33.3)                        
        elif cz[i] == "5B" and st[i] == 'WA':
            var.append(33.8)
        elif cz[i] == "5B" and st[i] == 'OR':
            var.append(33.8)
        elif cz[i] == "6A":
            var.append(32.8)
        elif cz[i] == "7A":
            var.append(31)
        else:
            print("unknown climate zone")
                                                    
    return var

def SummerWB(cz, st):
    '''
    EnergyPlus Object
    SizingPeriod:DesignDay
    '''
    # empty list
    var=[]
    
    for i in range(0, len(cz)):
        if cz[i] == "4A":
            var.append(25.1)
        elif cz[i] == "4C" and st[i] == 'WA':
            var.append(19.7)
        elif cz[i] == "4C" and st[i] == 'OR':
            var.append(18.3)
        elif cz[i] == "5A":
            var.append(23.7)                        
        elif cz[i] == "5B" and st[i] == 'WA':
            var.append(17.2)
        elif cz[i] == "5B" and st[i] == 'OR':
            var.append(16.6)
        elif cz[i] == "6A":
            var.append(23)
        elif cz[i] == "7A":
            var.append(21.6)
        else:
            print("unknown climate zone")
                                                    
    return var

def Latitude(cz, st):
    '''
    EnergyPlus Object
    SizingPeriod:DesignDay
    '''
    # empty list
    var=[]
    
    for i in range(0, len(cz)):
        if cz[i] == "4A":
            var.append(38.65)
        elif cz[i] == "4C" and st[i] == 'WA':
            var.append(47.47)
        elif cz[i] == "4C" and st[i] == 'OR':
            var.append(45.60)
        elif cz[i] == "5A":
            var.append(41.98)                        
        elif cz[i] == "5B" and st[i] == 'WA':
            var.append(47.49)
        elif cz[i] == "5B" and st[i] == 'OR':
            var.append(44.25)
        elif cz[i] == "6A":
            var.append(44.88)
        elif cz[i] == "7A":
            var.append(47.50)
        else:
            print("unknown climate zone")
                                                    
    return var

def Longitude(cz, st):
    '''
    EnergyPlus Object
    SizingPeriod:DesignDay
    '''
    # empty list
    var=[]
    
    for i in range(0, len(cz)):
        if cz[i] == "4A":
            var.append(-90.65)
        elif cz[i] == "4C" and st[i] == 'WA':
            var.append(-122.32)
        elif cz[i] == "4C" and st[i] == 'OR':
            var.append(-122.62)
        elif cz[i] == "5A":
            var.append( -87.92)                        
        elif cz[i] == "5B" and st[i] == 'WA':
            var.append(-117.59)
        elif cz[i] == "5B" and st[i] == 'OR':
            var.append(-121.17)
        elif cz[i] == "6A":
            var.append(-93.23)
        elif cz[i] == "7A":
            var.append(-94.93)
        else:
            print("unknown climate zone")
                                                    
    return var

