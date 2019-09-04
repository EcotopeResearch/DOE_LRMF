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

    
This is the dataframe_creator file, it's functions create dataframes that
match with EnergyPlus Inputs.
    
@author: scott
"""

import pandas as pd

from functions_general import (buildingName, slabBoundaryCondition, exteriorCorrLights, 
                               unitDhwCoeffOn, unitDhwCoeffOff, unitDhwThermEff, lightingStairs,
                               extPrkLights)

from functions_bsmt import (bsmtHeatingEfficiency, bsmtHeatingEfficiencyCurves1, bsmtHeatingEfficiencyCurves2,
                            bsmtHeatingEfficiencyCurves3, bsmtHeatingEfficiencyCurves4, bsmtHeatingEfficiencyCurves5,
                            bsmtHeatingEfficiencyCurves6, bsmtCoolEfficiency,
                            bsmtCoolingEfficiencyCurves1, bsmtCoolingEfficiencyCurves2, bsmtCoolingEfficiencyCurves3,
                            bsmtCoolingEfficiencyCurves4, bsmtCoolingEfficiencyCurves5,
                            bsmtVentilationFlowrate, bsmtVentilationSP,
                            bsmtHvacFanSP, bsmtHeatingSetpoint, bsmtCoolingSetpoint, bsmtLpd)

from functions_constructions import (bsmtWallCond, extWallCond, ceilingCond,
                                     slabCond, windowU, windowSHGC, floorCond)

from functions_corridor import (commonHeatingEfficiency, commonHeatingEfficiencyCurves1, commonHeatingEfficiencyCurves2, 
                                commonHeatingEfficiencyCurves3, commonHeatingEfficiencyCurves4, commonHeatingEfficiencyCurves5,
                                commonHeatingEfficiencyCurves6, commonCoolEfficiency,
                                commonCoolingEfficiencyCurves1, commonCoolingEfficiencyCurves2, commonCoolingEfficiencyCurves3,
                                commonCoolingEfficiencyCurves4, commonCoolingEfficiencyCurves5, commonLpd, commonVentilationFlowrate,
                                commonVentilationSP, commonHvacFanSP, commonHeatingSetpoint,
                                commonCoolingSetpoint)

from functions_unit import (unitHeatingEfficiency, unitHeatingEfficiencyCurves1, unitHeatingEfficiencyCurves2,
                            unitHeatingEfficiencyCurves3, unitHeatingEfficiencyCurves4, unitHeatingEfficiencyCurves5,
                            unitHeatingEfficiencyCurves6, unitCoolEfficiency,
                            unitCoolingEfficiencyCurves1, unitCoolingEfficiencyCurves2, unitCoolingEfficiencyCurves3,
                            unitCoolingEfficiencyCurves4, unitCoolingEfficiencyCurves5, 
                            unitLpd, unitVentilationFlowrate, unitVentilationSP,
                            unitHvacFanSP, unitHeatingSetpoint, unitCoolingSetpoint)

def commonBsmt_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    buildingNameVar = buildingName(df['sitex'])
    unitHeatingEfficiencyVar = unitHeatingEfficiency(df['inunit_heat'], df['HVACcentral_YN'])
    unitHeatingEfficiencyCurves1Var = unitHeatingEfficiencyCurves1(df['inunit_heat'])
    unitHeatingEfficiencyCurves2Var = unitHeatingEfficiencyCurves2(df['inunit_heat'])
    unitHeatingEfficiencyCurves3Var = unitHeatingEfficiencyCurves3(df['inunit_heat'])
    unitHeatingEfficiencyCurves4Var = unitHeatingEfficiencyCurves4(df['inunit_heat'])
    unitHeatingEfficiencyCurves5Var = unitHeatingEfficiencyCurves5(df['inunit_heat'])
    unitHeatingEfficiencyCurves6Var = unitHeatingEfficiencyCurves6(df['inunit_heat'])
    unitCoolEfficiencyVar = unitCoolEfficiency(df['inunit_cool'], df['HVACcentral_YN'])
    unitCoolingEfficiencyCurves1Var = unitCoolingEfficiencyCurves1(df['inunit_cool'])
    unitCoolingEfficiencyCurves2Var = unitCoolingEfficiencyCurves2(df['inunit_cool'])
    unitCoolingEfficiencyCurves3Var = unitCoolingEfficiencyCurves3(df['inunit_cool'])
    unitCoolingEfficiencyCurves4Var = unitCoolingEfficiencyCurves4(df['inunit_cool'])
    unitCoolingEfficiencyCurves5Var = unitCoolingEfficiencyCurves5(df['inunit_cool'])
    unitDhwCoeffOnVar = unitDhwCoeffOn(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwCoeffOffVar = unitDhwCoeffOff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwThermEffVar = unitDhwThermEff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitLpdVar = unitLpd(df['LPD_unit'])
    unitVentilationFlowrateVar = unitVentilationFlowrate(df['Ventcentral_YN'] ,df['Vent_inuniterv_YN'] ,df['Vent_inunit_erveff'])
    unitVentilationSPVar = unitVentilationSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    unitHvacFanSPVar = unitHvacFanSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    extWallCondVar = extWallCond(df['wtmn_GenlWallU'])
    ceilingCondVar = ceilingCond(df['wtmn_CeilingU'])
    slabCondVar = slabCond(df['Fnd_wtmn_u'], df['Fnd_wtmn_f'])
    windowUVar = windowU(df['wtmn_WindowU'])
    windowSHGCVar = windowSHGC(df['wtmn_WindowSHGC'])
    lightingStairsVar = lightingStairs(df['LPD_IntStairwell'])
    bsmtLpdVar = bsmtLpd(df['LPD_IntPk_common'])
    extPrkLightsVar = extPrkLights(df['LPD_ExtPk'])
    unitHeatingSetpointVar = unitHeatingSetpoint(df)
    unitCoolingSetpointVar = unitCoolingSetpoint(df)
    commonHeatingEfficiencyVar = commonHeatingEfficiency(df['common_heat'] ,df['HVACcentral_YN'] ,df['Central_Sys'])
    commonHeatingEfficiencyCurves1Var = commonHeatingEfficiencyCurves1(df['common_heat'])
    commonHeatingEfficiencyCurves2Var = commonHeatingEfficiencyCurves2(df['common_heat'])
    commonHeatingEfficiencyCurves3Var = commonHeatingEfficiencyCurves3(df['common_heat'])
    commonHeatingEfficiencyCurves4Var = commonHeatingEfficiencyCurves4(df['common_heat'])
    commonHeatingEfficiencyCurves5Var = commonHeatingEfficiencyCurves5(df['common_heat'])
    commonHeatingEfficiencyCurves6Var = commonHeatingEfficiencyCurves6(df['common_heat'])
    commonCoolEfficiencyVar = commonCoolEfficiency(df['common_cool'] ,df['HVACcentral_YN'] ,df['Central_Sys'])
    commonCoolingEfficiencyCurves1Var = commonCoolingEfficiencyCurves1(df['common_cool'])
    commonCoolingEfficiencyCurves2Var = commonCoolingEfficiencyCurves2(df['common_cool'])
    commonCoolingEfficiencyCurves3Var = commonCoolingEfficiencyCurves3(df['common_cool'])
    commonCoolingEfficiencyCurves4Var = commonCoolingEfficiencyCurves4(df['common_cool'])
    commonCoolingEfficiencyCurves5Var = commonCoolingEfficiencyCurves5(df['common_cool'])
    commonLpdVar = commonLpd(df['LPD_IntCorridor'])
    commonVentilationFlowrateVar = commonVentilationFlowrate(df['Vent_corridorerv_YN'], df['Vent_corridor_erveff'])
    commonVentilationSPVar = commonVentilationSP(df['Vent_corridorerv_YN'])
    commonHvacFanSPVar = commonHvacFanSP(df['common_heat'], df['common_cool'])
    commonHeatingSetpointVar = commonHeatingSetpoint(df)
    commonCoolingSetpointVar = commonCoolingSetpoint(df)
    bsmtHeatingEfficiencyVar = bsmtHeatingEfficiency(df['Heat_bsmt_type'] ,df['HVACcentral_YN'] ,df['Central_Sys'])
    bsmtHeatingEfficiencyCurves1Var = bsmtHeatingEfficiencyCurves1(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves2Var = bsmtHeatingEfficiencyCurves2(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves3Var = bsmtHeatingEfficiencyCurves3(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves4Var = bsmtHeatingEfficiencyCurves4(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves5Var = bsmtHeatingEfficiencyCurves5(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves6Var = bsmtHeatingEfficiencyCurves6(df['Heat_bsmt_type'])
    bsmtCoolEfficiencyVar = bsmtCoolEfficiency(df)
    bsmtCoolingEfficiencyCurves1Var = bsmtCoolingEfficiencyCurves1(df)
    bsmtCoolingEfficiencyCurves2Var = bsmtCoolingEfficiencyCurves2(df)
    bsmtCoolingEfficiencyCurves3Var = bsmtCoolingEfficiencyCurves3(df)
    bsmtCoolingEfficiencyCurves4Var = bsmtCoolingEfficiencyCurves4(df)
    bsmtCoolingEfficiencyCurves5Var = bsmtCoolingEfficiencyCurves5(df)
    bsmtVentilationFlowrateVar = bsmtVentilationFlowrate(df['Vent_bsmterv_YN'] ,df['Vent_bsmt_erveff'] ,df['LPD_IntPk_common']  ,df['Vent_bsmt_YN'])
    bsmtVentilationSPVar = bsmtVentilationSP(df['Vent_bsmterv_YN'] ,df['LPD_IntPk_common'] ,df['Vent_bsmt_YN'])
    bsmtHvacFanSPVar = bsmtHvacFanSP(df['Heat_bsmt_type'])
    bsmtWallCondVar = bsmtWallCond(df['BsmtWallU'])
    floorCondVar = floorCond(df['BsmtFloorU'])
    bsmtHeatingSetpointVar = bsmtHeatingSetpoint(df['FndType'], df['Heat_bsmt_YN'])
    bsmtCoolingSetpointVar = bsmtCoolingSetpoint(df['FndType'], df['Heat_bsmt_YN'])


    # create dataframe
    new_df = pd.DataFrame()
    
    # assign new dataframe with values created in above functions
    new_df['Building Name'] = buildingNameVar
    new_df['Unit heating efficiency (COP)'] = unitHeatingEfficiencyVar
    new_df['Unit heating efficiency curves1'] = unitHeatingEfficiencyCurves1Var
    new_df['Unit heating efficiency curves2'] = unitHeatingEfficiencyCurves2Var
    new_df['Unit heating efficiency curves3'] = unitHeatingEfficiencyCurves3Var
    new_df['Unit heating efficiency curves4'] = unitHeatingEfficiencyCurves4Var
    new_df['Unit heating efficiency curves5'] = unitHeatingEfficiencyCurves5Var
    new_df['Unit heating efficiency curves6'] = unitHeatingEfficiencyCurves6Var
    new_df['Unit cooling efficiency (COP)'] = unitCoolEfficiencyVar
    new_df['Unit cooling efficiency curves1'] = unitCoolingEfficiencyCurves1Var
    new_df['Unit cooling efficiency curves2'] = unitCoolingEfficiencyCurves2Var
    new_df['Unit cooling efficiency curves3'] = unitCoolingEfficiencyCurves3Var
    new_df['Unit cooling efficiency curves4'] = unitCoolingEfficiencyCurves4Var
    new_df['Unit cooling efficiency curves5'] = unitCoolingEfficiencyCurves5Var
    new_df['Unit DHW Loss Coefficient - ON'] = unitDhwCoeffOnVar
    new_df['Unit DHW Loss Coefficient - OFF'] = unitDhwCoeffOffVar
    new_df['Unit DHW Thermal Efficiency'] = unitDhwThermEffVar
    new_df['Unit LPD [W/sf]'] = unitLpdVar
    new_df['Unit Ventilation Flowrate [m3/s]'] = unitVentilationFlowrateVar
    new_df['Unit Ventilation SP [Pa]'] = unitVentilationSPVar
    new_df['Unit HVAC Fan SP [Pa]'] = unitHvacFanSPVar
    new_df['Exterior Wall Insulation Conductivity [W/m*K]'] = extWallCondVar
    new_df['Ceiling Insulation Conductivity [W/m*K]'] = ceilingCondVar
    new_df['Slab Insulation Conductivity [W/m*K]'] = slabCondVar
    new_df['Windows Ufactor [W/m2*K]'] = windowUVar
    new_df['Windows SHGC'] = windowSHGCVar
    new_df['Lighting Stairwell [W]'] = lightingStairsVar
    new_df['Internal Parking Lights [W]'] = bsmtLpdVar
    new_df['External Parking Lights [W]'] = extPrkLightsVar
    new_df['Unit heating setpoint temp [C]'] = unitHeatingSetpointVar
    new_df['Unit cooling setpoint temp [C]'] = unitCoolingSetpointVar
    new_df['Corridor heating efficiency (COP)'] = commonHeatingEfficiencyVar
    new_df['Corridor heating efficiency curves1'] = commonHeatingEfficiencyCurves1Var
    new_df['Corridor heating efficiency curves2'] = commonHeatingEfficiencyCurves2Var
    new_df['Corridor heating efficiency curves3'] = commonHeatingEfficiencyCurves3Var
    new_df['Corridor heating efficiency curves4'] = commonHeatingEfficiencyCurves4Var
    new_df['Corridor heating efficiency curves5'] = commonHeatingEfficiencyCurves5Var
    new_df['Corridor heating efficiency curves6'] = commonHeatingEfficiencyCurves6Var
    new_df['Corridor cooling efficiency (COP)'] = commonCoolEfficiencyVar
    new_df['Corridor cooling efficiency curves1'] = commonCoolingEfficiencyCurves1Var
    new_df['Corridor cooling efficiency curves2'] = commonCoolingEfficiencyCurves2Var
    new_df['Corridor cooling efficiency curves3'] = commonCoolingEfficiencyCurves3Var
    new_df['Corridor cooling efficiency curves4'] = commonCoolingEfficiencyCurves4Var
    new_df['Corridor cooling efficiency curves5'] = commonCoolingEfficiencyCurves5Var
    new_df['Corridor LPD (W/sf)'] = commonLpdVar
    new_df['Corridor Ventilation Flowrate [m3/s]'] = commonVentilationFlowrateVar
    new_df['Corridor Ventilation SP [Pa]'] = commonVentilationSPVar
    new_df['Corridor HVAC Fan SP [Pa]'] = commonHvacFanSPVar
    new_df['Corridor heating setpoint temp [C]'] = commonHeatingSetpointVar
    new_df['Corridor cooling setpoint temp [C]'] = commonCoolingSetpointVar
    new_df['Bsmt heating efficiency (COP)'] = bsmtHeatingEfficiencyVar
    new_df['Bsmt Heating efficiency curves1'] = bsmtHeatingEfficiencyCurves1Var
    new_df['Bsmt Heating efficiency curves2'] = bsmtHeatingEfficiencyCurves2Var
    new_df['Bsmt Heating efficiency curves3'] = bsmtHeatingEfficiencyCurves3Var
    new_df['Bsmt Heating efficiency curves4'] = bsmtHeatingEfficiencyCurves4Var
    new_df['Bsmt Heating efficiency curves5'] = bsmtHeatingEfficiencyCurves5Var
    new_df['Bsmt Heating efficiency curves6'] = bsmtHeatingEfficiencyCurves6Var
    new_df['Bsmt cooling efficiency (COP)'] = bsmtCoolEfficiencyVar
    new_df['Bsmt cooling efficiency curves1'] = bsmtCoolingEfficiencyCurves1Var
    new_df['Bsmt cooling efficiency curves2'] = bsmtCoolingEfficiencyCurves2Var
    new_df['Bsmt cooling efficiency curves3'] = bsmtCoolingEfficiencyCurves3Var
    new_df['Bsmt cooling efficiency curves4'] = bsmtCoolingEfficiencyCurves4Var
    new_df['Bsmt cooling efficiency curves5'] = bsmtCoolingEfficiencyCurves5Var
    new_df['Bsmt Ventilation Flowrate [m3/s]'] = bsmtVentilationFlowrateVar
    new_df['Bsmt Ventilation SP [Pa]'] = bsmtVentilationSPVar
    new_df['Bsmt HVAC Fan SP [Pa]'] = bsmtHvacFanSPVar
    new_df['Bsmt Wall Insulation Conductivity [W/m*K]'] = bsmtWallCondVar
    new_df['Floor Insulation Conductivity [W/m*K]'] = floorCondVar
    new_df['Bsmt heating setpoint temp [C]'] = bsmtHeatingSetpointVar
    new_df['Bsmt cooling setpoint temp [C]'] = bsmtCoolingSetpointVar



    return new_df
    
def commonSlab_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    names = buildingName(df['sitex'])
    slabBC = slabBoundaryCondition(df['FndType'].tolist())
    
    # create dataframe
    new_df = pd.DataFrame()
    new_df['names'] = names
    new_df['slabBC'] = slabBC

    return new_df
    
def gardenBsmt_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    names = buildingName(df['sitex'])
    
    # create dataframe
    new_df = pd.DataFrame()
    new_df['names'] = names
    
    return new_df
    
def gardenSlab_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    names = buildingName(df['sitex'])
    
    # create dataframe
    new_df = pd.DataFrame()
    new_df['names'] = names
    
    return new_df
