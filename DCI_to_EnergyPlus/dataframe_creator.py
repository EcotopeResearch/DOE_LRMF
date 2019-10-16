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

from functions_general import (HeatingEfficiency, HeatingEfficiencyCurves1, HeatingEfficiencyCurves2,
                               HeatingEfficiencyCurves3, HeatingEfficiencyCurves4, HeatingEfficiencyCurves5,
                               HeatingEfficiencyCurves6, CoolEfficiency,
                               CoolingEfficiencyCurves1, CoolingEfficiencyCurves2, CoolingEfficiencyCurves3,
                               CoolingEfficiencyCurves4, CoolingEfficiencyCurves5,buildingName, slabBoundaryCondition, exteriorCorrLights, 
                               unitDhwCoeffOn, unitDhwCoeffOff, unitDhwThermEff, lightingStairs,
                               extPrkLights, runnumber, z1, z2, WinterDB, SummerDB, SummerWB, Latitude, Longitude)

from functions_bsmt import (bsmtVentilationFlowrate, bsmtVentilationSP,
                            bsmtHvacFanSP, bsmtHeatingSetpoint, bsmtCoolingSetpoint, bsmtLpd)

from functions_constructions import (bsmtWallCond, extWallCond, ceilingCond,
                                     slabCond, windowU, windowSHGC, floorCond)

from functions_corridor import (commonLpd, commonVentilationFlowrate,
                                commonVentilationSP, commonHvacFanSP, commonHeatingSetpoint,
                                commonCoolingSetpoint)

from functions_unit import (unitLpd, unitVentilationFlowrate, unitVentilationSP,
                            unitHvacFanSP, unitHeatingSetpoint, unitCoolingSetpoint)

def commonBsmt_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    v1 = runnumber(df)
    v2 = z1(df['CZ'], df['State'])
    v3 = z2(df)
    buildingNameVar = buildingName(df['sitex'], df['CZ'])
    unitHeatingEfficiencyVar = HeatingEfficiency(df['inunit_heat'], df['Central_Sys'])
    unitHeatingEfficiencyCurves1Var = HeatingEfficiencyCurves1(df['inunit_heat'])
    unitHeatingEfficiencyCurves2Var = HeatingEfficiencyCurves2(df['inunit_heat'])
    unitHeatingEfficiencyCurves3Var = HeatingEfficiencyCurves3(df['inunit_heat'])
    unitHeatingEfficiencyCurves4Var = HeatingEfficiencyCurves4(df['inunit_heat'])
    unitHeatingEfficiencyCurves5Var = HeatingEfficiencyCurves5(df['inunit_heat'])
    unitHeatingEfficiencyCurves6Var = HeatingEfficiencyCurves6(df['inunit_heat'])
    unitCoolEfficiencyVar = CoolEfficiency(df['inunit_cool'], df['BLANK'])
    unitCoolingEfficiencyCurves1Var = CoolingEfficiencyCurves1(df['inunit_cool'])
    unitCoolingEfficiencyCurves2Var = CoolingEfficiencyCurves2(df['inunit_cool'])
    unitCoolingEfficiencyCurves3Var = CoolingEfficiencyCurves3(df['inunit_cool'])
    unitCoolingEfficiencyCurves4Var = CoolingEfficiencyCurves4(df['inunit_cool'])
    unitCoolingEfficiencyCurves5Var = CoolingEfficiencyCurves5(df['inunit_cool'])
    unitDhwCoeffOnVar = unitDhwCoeffOn(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwCoeffOffVar = unitDhwCoeffOff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwThermEffVar = unitDhwThermEff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitLpdVar = unitLpd(df['LPD_unit'])
    unitVentilationFlowrateVar = unitVentilationFlowrate(df['Ventcentral_YN'] ,df['Vent_inuniterv_YN'] ,df['Vent_inunit_erveff'])
    unitVentilationSPVar = unitVentilationSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    unitHvacFanSPVar = unitHvacFanSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    extWallCondVar = extWallCond(df['wtmn_GenlWallU'], df['State'])
    ceilingCondVar = ceilingCond(df['wtmn_CeilingU'], df['State'])
    slabCondVar = slabCond(df['Fnd_wtmn_u'], df['Fnd_wtmn_f'], df['State'] )
    windowUVar = windowU(df['wtmn_WindowU'], df['State'], df['CZ'])
    windowSHGCVar = windowSHGC(df['wtmn_WindowSHGC'])
    lightingStairsVar = lightingStairs(df['LPD_IntStairwell'])
    bsmtLpdVar = bsmtLpd(df['LPD_IntPk_common'], df['FndType'])
    extPrkLightsVar = extPrkLights(df['LPD_ExtPk'])
    unitHeatingSetpointVar = unitHeatingSetpoint(df['BLANK'])
    unitCoolingSetpointVar = unitCoolingSetpoint(df['BLANK'])
    corrHeatingEfficiencyVar = HeatingEfficiency(df['common_heat'], df['Central_Sys'])
    corrHeatingEfficiencyCurves1Var = HeatingEfficiencyCurves1(df['common_heat'])
    corrHeatingEfficiencyCurves2Var = HeatingEfficiencyCurves2(df['common_heat'])
    corrHeatingEfficiencyCurves3Var = HeatingEfficiencyCurves3(df['common_heat'])
    corrHeatingEfficiencyCurves4Var = HeatingEfficiencyCurves4(df['common_heat'])
    corrHeatingEfficiencyCurves5Var = HeatingEfficiencyCurves5(df['common_heat'])
    corrHeatingEfficiencyCurves6Var = HeatingEfficiencyCurves6(df['common_heat'])
    corrCoolEfficiencyVar = CoolEfficiency(df['common_cool'], df['BLANK'])
    corrCoolingEfficiencyCurves1Var = CoolingEfficiencyCurves1(df['common_cool'])
    corrCoolingEfficiencyCurves2Var = CoolingEfficiencyCurves2(df['common_cool'])
    corrCoolingEfficiencyCurves3Var = CoolingEfficiencyCurves3(df['common_cool'])
    corrCoolingEfficiencyCurves4Var = CoolingEfficiencyCurves4(df['common_cool'])
    corrCoolingEfficiencyCurves5Var = CoolingEfficiencyCurves5(df['common_cool'])
    commonLpdVar = commonLpd(df['LPD_IntCorridor'])
    commonVentilationFlowrateVar = commonVentilationFlowrate(df['Ventcentral_YN'] ,df['Vent_corridorerv_YN'] ,df['Vent_corridor_erveff'])
    commonVentilationSPVar = commonVentilationSP(df['Ventcentral_YN'], df['Vent_corridorerv_YN'])
    commonHvacFanSPVar = commonHvacFanSP(df['Ventcentral_YN'], df['Vent_corridorerv_YN'])
    commonHeatingSetpointVar = commonHeatingSetpoint(df['BLANK'])
    commonCoolingSetpointVar = commonCoolingSetpoint(df['BLANK'])
    HeatingEfficiencyVar = HeatingEfficiency(df['Heat_bsmt_type'], df['Central_Sys'])
    bsmtHeatingEfficiencyCurves1Var = HeatingEfficiencyCurves1(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves2Var = HeatingEfficiencyCurves2(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves3Var = HeatingEfficiencyCurves3(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves4Var = HeatingEfficiencyCurves4(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves5Var = HeatingEfficiencyCurves5(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves6Var = HeatingEfficiencyCurves6(df['Heat_bsmt_type'])
    bsmtCoolEfficiencyVar = CoolEfficiency(df['BLANK'], df['BLANK'])
    bsmtCoolingEfficiencyCurves1Var = CoolingEfficiencyCurves1(df['BLANK'])
    bsmtCoolingEfficiencyCurves2Var = CoolingEfficiencyCurves2(df['BLANK'])
    bsmtCoolingEfficiencyCurves3Var = CoolingEfficiencyCurves3(df['BLANK'])
    bsmtCoolingEfficiencyCurves4Var = CoolingEfficiencyCurves4(df['BLANK'])
    bsmtCoolingEfficiencyCurves5Var = CoolingEfficiencyCurves5(df['BLANK'])
    bsmtVentilationFlowrateVar = bsmtVentilationFlowrate(df['Vent_bsmt_YN'] ,df['Vent_bsmterv_YN'] ,df['Vent_bsmt_erveff']  ,df['LPD_IntPk_common'])
    bsmtVentilationSPVar = bsmtVentilationSP(df['Vent_bsmterv_YN'])
    bsmtHvacFanSPVar = bsmtHvacFanSP(df['Vent_bsmterv_YN'])
    bsmtWallCondVar = bsmtWallCond(df['BsmtWallU'], df['CZ'])
    floorCondVar = floorCond(df['BsmtFloorU'], df['CZ'])
    bsmtHeatingSetpointVar = bsmtHeatingSetpoint(df['Heat_bsmt_YN'])
    bsmtCoolingSetpointVar = bsmtCoolingSetpoint(df['Heat_bsmt_YN'])
    winterDbVar = WinterDB(df['CZ'], df['State'])
    summerDbVar = SummerDB(df['CZ'], df['State'])
    summerWbVar = SummerWB(df['CZ'], df['State'])
    longitudeVar = Longitude(df['CZ'], df['State'])
    latitudeVar = Latitude(df['CZ'], df['State'])
    
    # create dataframe
    new_df = pd.DataFrame()
    
    # assign new dataframe with values created in above functions
    new_df['v1'] = v1
    new_df['v2'] = v2
    new_df['v3'] = v3
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
    new_df['Corridor heating efficiency (COP)'] = corrHeatingEfficiencyVar
    new_df['Corridor heating efficiency curves1'] = corrHeatingEfficiencyCurves1Var
    new_df['Corridor heating efficiency curves2'] = corrHeatingEfficiencyCurves2Var
    new_df['Corridor heating efficiency curves3'] = corrHeatingEfficiencyCurves3Var
    new_df['Corridor heating efficiency curves4'] = corrHeatingEfficiencyCurves4Var
    new_df['Corridor heating efficiency curves5'] = corrHeatingEfficiencyCurves5Var
    new_df['Corridor heating efficiency curves6'] = corrHeatingEfficiencyCurves6Var
    new_df['Corridor cooling efficiency (COP)'] = corrCoolEfficiencyVar
    new_df['Corridor cooling efficiency curves1'] = corrCoolingEfficiencyCurves1Var
    new_df['Corridor cooling efficiency curves2'] = corrCoolingEfficiencyCurves2Var
    new_df['Corridor cooling efficiency curves3'] = corrCoolingEfficiencyCurves3Var
    new_df['Corridor cooling efficiency curves4'] = corrCoolingEfficiencyCurves4Var
    new_df['Corridor cooling efficiency curves5'] = corrCoolingEfficiencyCurves5Var
    new_df['Corridor LPD (W/sf)'] = commonLpdVar
    new_df['Corridor Ventilation Flowrate [m3/s]'] = commonVentilationFlowrateVar
    new_df['Corridor Ventilation SP [Pa]'] = commonVentilationSPVar
    new_df['Corridor HVAC Fan SP [Pa]'] = commonHvacFanSPVar
    new_df['Corridor heating setpoint temp [C]'] = commonHeatingSetpointVar
    new_df['Corridor cooling setpoint temp [C]'] = commonCoolingSetpointVar
    new_df['Bsmt heating efficiency (COP)'] = HeatingEfficiencyVar
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
    new_df['WinterDB'] = winterDbVar
    new_df['SummerDB'] = summerDbVar
    new_df['SummerWB'] = summerWbVar
    new_df['Latitude'] = latitudeVar
    new_df['Longitude'] = longitudeVar

    return new_df
    
def commonSlab_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    v1 = runnumber(df)
    v2 = z1(df['CZ'], df['State'])
    v3 = z2(df)
    buildingNameVar = buildingName(df['sitex'], df['CZ'])
    unitHeatingEfficiencyVar = HeatingEfficiency(df['inunit_heat'], df['Central_Sys'])
    unitHeatingEfficiencyCurves1Var = HeatingEfficiencyCurves1(df['inunit_heat'])
    unitHeatingEfficiencyCurves2Var = HeatingEfficiencyCurves2(df['inunit_heat'])
    unitHeatingEfficiencyCurves3Var = HeatingEfficiencyCurves3(df['inunit_heat'])
    unitHeatingEfficiencyCurves4Var = HeatingEfficiencyCurves4(df['inunit_heat'])
    unitHeatingEfficiencyCurves5Var = HeatingEfficiencyCurves5(df['inunit_heat'])
    unitHeatingEfficiencyCurves6Var = HeatingEfficiencyCurves6(df['inunit_heat'])
    unitCoolEfficiencyVar = CoolEfficiency(df['inunit_cool'], df['BLANK'])
    unitCoolingEfficiencyCurves1Var = CoolingEfficiencyCurves1(df['inunit_cool'])
    unitCoolingEfficiencyCurves2Var = CoolingEfficiencyCurves2(df['inunit_cool'])
    unitCoolingEfficiencyCurves3Var = CoolingEfficiencyCurves3(df['inunit_cool'])
    unitCoolingEfficiencyCurves4Var = CoolingEfficiencyCurves4(df['inunit_cool'])
    unitCoolingEfficiencyCurves5Var = CoolingEfficiencyCurves5(df['inunit_cool'])
    unitDhwCoeffOnVar = unitDhwCoeffOn(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwCoeffOffVar = unitDhwCoeffOff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwThermEffVar = unitDhwThermEff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitLpdVar = unitLpd(df['LPD_unit'])
    unitVentilationFlowrateVar = unitVentilationFlowrate(df['Ventcentral_YN'] ,df['Vent_inuniterv_YN'] ,df['Vent_inunit_erveff'])
    unitVentilationSPVar = unitVentilationSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    unitHvacFanSPVar = unitHvacFanSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    extWallCondVar = extWallCond(df['wtmn_GenlWallU'], df['State'])
    ceilingCondVar = ceilingCond(df['wtmn_CeilingU'], df['State'])
    slabCondVar = slabCond(df['Fnd_wtmn_u'], df['Fnd_wtmn_f'], df['State'])
    windowUVar = windowU(df['wtmn_WindowU'], df['State'], df['CZ'])
    windowSHGCVar = windowSHGC(df['wtmn_WindowSHGC'])
    lightingStairsVar = lightingStairs(df['LPD_IntStairwell'])
    bsmtLpdVar = bsmtLpd(df['LPD_IntPk_common'], df['FndType'])
    extPrkLightsVar = extPrkLights(df['LPD_ExtPk'])
    unitHeatingSetpointVar = unitHeatingSetpoint(df['BLANK'])
    unitCoolingSetpointVar = unitCoolingSetpoint(df['BLANK'])
    corrHeatingEfficiencyVar = HeatingEfficiency(df['common_heat'], df['Central_Sys'])
    corrHeatingEfficiencyCurves1Var = HeatingEfficiencyCurves1(df['common_heat'])
    corrHeatingEfficiencyCurves2Var = HeatingEfficiencyCurves2(df['common_heat'])
    corrHeatingEfficiencyCurves3Var = HeatingEfficiencyCurves3(df['common_heat'])
    corrHeatingEfficiencyCurves4Var = HeatingEfficiencyCurves4(df['common_heat'])
    corrHeatingEfficiencyCurves5Var = HeatingEfficiencyCurves5(df['common_heat'])
    corrHeatingEfficiencyCurves6Var = HeatingEfficiencyCurves6(df['common_heat'])
    corrCoolEfficiencyVar = CoolEfficiency(df['common_cool'], df['BLANK'])
    corrCoolingEfficiencyCurves1Var = CoolingEfficiencyCurves1(df['common_cool'])
    corrCoolingEfficiencyCurves2Var = CoolingEfficiencyCurves2(df['common_cool'])
    corrCoolingEfficiencyCurves3Var = CoolingEfficiencyCurves3(df['common_cool'])
    corrCoolingEfficiencyCurves4Var = CoolingEfficiencyCurves4(df['common_cool'])
    corrCoolingEfficiencyCurves5Var = CoolingEfficiencyCurves5(df['common_cool'])
    commonLpdVar = commonLpd(df['LPD_IntCorridor'])
    commonVentilationFlowrateVar = commonVentilationFlowrate(df['Ventcentral_YN'] ,df['Vent_corridorerv_YN'] ,df['Vent_corridor_erveff'])
    commonVentilationSPVar = commonVentilationSP(df['Ventcentral_YN'], df['Vent_corridorerv_YN'])
    commonHvacFanSPVar = commonHvacFanSP(df['Ventcentral_YN'], df['Vent_corridorerv_YN'])
    commonHeatingSetpointVar = commonHeatingSetpoint(df['BLANK'])
    commonCoolingSetpointVar = commonCoolingSetpoint(df['BLANK'])
    winterDbVar = WinterDB(df['CZ'], df['State'])
    summerDbVar = SummerDB(df['CZ'], df['State'])
    summerWbVar = SummerWB(df['CZ'], df['State'])
    longitudeVar = Longitude(df['CZ'], df['State'])
    latitudeVar = Latitude(df['CZ'], df['State'])


    # create dataframe
    new_df = pd.DataFrame()
    
    # assign new dataframe with values created in above functions
    new_df['v1'] = v1
    new_df['v2'] = v2
    new_df['v3'] = v3
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
    new_df['Corridor heating efficiency (COP)'] = corrHeatingEfficiencyVar
    new_df['Corridor heating efficiency curves1'] = corrHeatingEfficiencyCurves1Var
    new_df['Corridor heating efficiency curves2'] = corrHeatingEfficiencyCurves2Var
    new_df['Corridor heating efficiency curves3'] = corrHeatingEfficiencyCurves3Var
    new_df['Corridor heating efficiency curves4'] = corrHeatingEfficiencyCurves4Var
    new_df['Corridor heating efficiency curves5'] = corrHeatingEfficiencyCurves5Var
    new_df['Corridor heating efficiency curves6'] = corrHeatingEfficiencyCurves6Var
    new_df['Corridor cooling efficiency (COP)'] = corrCoolEfficiencyVar
    new_df['Corridor cooling efficiency curves1'] = corrCoolingEfficiencyCurves1Var
    new_df['Corridor cooling efficiency curves2'] = corrCoolingEfficiencyCurves2Var
    new_df['Corridor cooling efficiency curves3'] = corrCoolingEfficiencyCurves3Var
    new_df['Corridor cooling efficiency curves4'] = corrCoolingEfficiencyCurves4Var
    new_df['Corridor cooling efficiency curves5'] = corrCoolingEfficiencyCurves5Var
    new_df['Corridor LPD (W/sf)'] = commonLpdVar
    new_df['Corridor Ventilation Flowrate [m3/s]'] = commonVentilationFlowrateVar
    new_df['Corridor Ventilation SP [Pa]'] = commonVentilationSPVar
    new_df['Corridor HVAC Fan SP [Pa]'] = commonHvacFanSPVar
    new_df['Corridor heating setpoint temp [C]'] = commonHeatingSetpointVar
    new_df['Corridor cooling setpoint temp [C]'] = commonCoolingSetpointVar
    new_df['WinterDB'] = winterDbVar
    new_df['SummerDB'] = summerDbVar
    new_df['SummerWB'] = summerWbVar
    new_df['Latitude'] = latitudeVar
    new_df['Longitude'] = longitudeVar


    return new_df
    
def gardenBsmt_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    v1 = runnumber(df)
    v2 = z1(df['CZ'], df['State'])
    v3 = z2(df)
    buildingNameVar = buildingName(df['sitex'], df['CZ'])
    unitHeatingEfficiencyVar = HeatingEfficiency(df['inunit_heat'], df['Central_Sys'])
    unitHeatingEfficiencyCurves1Var = HeatingEfficiencyCurves1(df['inunit_heat'])
    unitHeatingEfficiencyCurves2Var = HeatingEfficiencyCurves2(df['inunit_heat'])
    unitHeatingEfficiencyCurves3Var = HeatingEfficiencyCurves3(df['inunit_heat'])
    unitHeatingEfficiencyCurves4Var = HeatingEfficiencyCurves4(df['inunit_heat'])
    unitHeatingEfficiencyCurves5Var = HeatingEfficiencyCurves5(df['inunit_heat'])
    unitHeatingEfficiencyCurves6Var = HeatingEfficiencyCurves6(df['inunit_heat'])
    unitCoolEfficiencyVar = CoolEfficiency(df['inunit_cool'], df['BLANK'])
    unitCoolingEfficiencyCurves1Var = CoolingEfficiencyCurves1(df['inunit_cool'])
    unitCoolingEfficiencyCurves2Var = CoolingEfficiencyCurves2(df['inunit_cool'])
    unitCoolingEfficiencyCurves3Var = CoolingEfficiencyCurves3(df['inunit_cool'])
    unitCoolingEfficiencyCurves4Var = CoolingEfficiencyCurves4(df['inunit_cool'])
    unitCoolingEfficiencyCurves5Var = CoolingEfficiencyCurves5(df['inunit_cool'])
    unitDhwCoeffOnVar = unitDhwCoeffOn(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwCoeffOffVar = unitDhwCoeffOff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwThermEffVar = unitDhwThermEff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitLpdVar = unitLpd(df['LPD_unit'])
    unitVentilationFlowrateVar = unitVentilationFlowrate(df['Ventcentral_YN'] ,df['Vent_inuniterv_YN'] ,df['Vent_inunit_erveff'])
    unitVentilationSPVar = unitVentilationSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    unitHvacFanSPVar = unitHvacFanSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    extWallCondVar = extWallCond(df['wtmn_GenlWallU'], df['State'])
    ceilingCondVar = ceilingCond(df['wtmn_CeilingU'], df['State'])
    slabCondVar = slabCond(df['Fnd_wtmn_u'], df['Fnd_wtmn_f'], df['State'])
    windowUVar = windowU(df['wtmn_WindowU'], df['State'], df['CZ'])
    windowSHGCVar = windowSHGC(df['wtmn_WindowSHGC'])
    lightingStairsVar = lightingStairs(df['LPD_IntStairwell'])
    bsmtLpdVar = bsmtLpd(df['LPD_IntPk_common'], df['FndType'])
    extPrkLightsVar = extPrkLights(df['LPD_ExtPk'])
    unitHeatingSetpointVar = unitHeatingSetpoint(df['BLANK'])
    unitCoolingSetpointVar = unitCoolingSetpoint(df['BLANK'])
    exteriorCorrLightsVar = exteriorCorrLights(df)
    HeatingEfficiencyVar = HeatingEfficiency(df['Heat_bsmt_type'], df['Central_Sys'])
    bsmtHeatingEfficiencyCurves1Var = HeatingEfficiencyCurves1(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves2Var = HeatingEfficiencyCurves2(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves3Var = HeatingEfficiencyCurves3(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves4Var = HeatingEfficiencyCurves4(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves5Var = HeatingEfficiencyCurves5(df['Heat_bsmt_type'])
    bsmtHeatingEfficiencyCurves6Var = HeatingEfficiencyCurves6(df['Heat_bsmt_type'])
    bsmtCoolEfficiencyVar = CoolEfficiency(df['BLANK'], df['BLANK'])
    bsmtCoolingEfficiencyCurves1Var = CoolingEfficiencyCurves1(df['BLANK'])
    bsmtCoolingEfficiencyCurves2Var = CoolingEfficiencyCurves2(df['BLANK'])
    bsmtCoolingEfficiencyCurves3Var = CoolingEfficiencyCurves3(df['BLANK'])
    bsmtCoolingEfficiencyCurves4Var = CoolingEfficiencyCurves4(df['BLANK'])
    bsmtCoolingEfficiencyCurves5Var = CoolingEfficiencyCurves5(df['BLANK'])
    bsmtVentilationFlowrateVar = bsmtVentilationFlowrate(df['Vent_bsmt_YN'] ,df['Vent_bsmterv_YN'] ,df['Vent_bsmt_erveff']  ,df['LPD_IntPk_common'])
    bsmtVentilationSPVar = bsmtVentilationSP(df['Vent_bsmterv_YN'])
    bsmtHvacFanSPVar = bsmtHvacFanSP(df['Vent_bsmterv_YN'])
    bsmtWallCondVar = bsmtWallCond(df['BsmtWallU'], df['CZ'])
    floorCondVar = floorCond(df['BsmtFloorU'], df['CZ'])
    bsmtHeatingSetpointVar = bsmtHeatingSetpoint(df['Heat_bsmt_YN'])
    bsmtCoolingSetpointVar = bsmtCoolingSetpoint(df['Heat_bsmt_YN'])
    winterDbVar = WinterDB(df['CZ'], df['State'])
    summerDbVar = SummerDB(df['CZ'], df['State'])
    summerWbVar = SummerWB(df['CZ'], df['State'])
    longitudeVar = Longitude(df['CZ'], df['State'])
    latitudeVar = Latitude(df['CZ'], df['State'])

    
    # create dataframe
    new_df = pd.DataFrame()
    
    # assign new dataframe with values created in above functions
    new_df['v1'] = v1
    new_df['v2'] = v2
    new_df['v3'] = v3
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
    new_df['Exterior corridor Lights [W]'] = exteriorCorrLightsVar
    new_df['Bsmt heating efficiency (COP)'] = HeatingEfficiencyVar
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
    new_df['WinterDB'] = winterDbVar
    new_df['SummerDB'] = summerDbVar
    new_df['SummerWB'] = summerWbVar
    new_df['Latitude'] = latitudeVar
    new_df['Longitude'] = longitudeVar

    return new_df
    
def gardenSlab_inputs(df):
    
    # pass column from dci df column to function, return E+ df column
    v1 = runnumber(df)
    v2 = z1(df['CZ'], df['State'])
    v3 = z2(df)
    buildingNameVar = buildingName(df['sitex'], df['CZ'])
    unitHeatingEfficiencyVar = HeatingEfficiency(df['inunit_heat'], df['Central_Sys'])
    unitHeatingEfficiencyCurves1Var = HeatingEfficiencyCurves1(df['inunit_heat'])
    unitHeatingEfficiencyCurves2Var = HeatingEfficiencyCurves2(df['inunit_heat'])
    unitHeatingEfficiencyCurves3Var = HeatingEfficiencyCurves3(df['inunit_heat'])
    unitHeatingEfficiencyCurves4Var = HeatingEfficiencyCurves4(df['inunit_heat'])
    unitHeatingEfficiencyCurves5Var = HeatingEfficiencyCurves5(df['inunit_heat'])
    unitHeatingEfficiencyCurves6Var = HeatingEfficiencyCurves6(df['inunit_heat'])
    unitCoolEfficiencyVar = CoolEfficiency(df['inunit_cool'], df['BLANK'])
    unitCoolingEfficiencyCurves1Var = CoolingEfficiencyCurves1(df['inunit_cool'])
    unitCoolingEfficiencyCurves2Var = CoolingEfficiencyCurves2(df['inunit_cool'])
    unitCoolingEfficiencyCurves3Var = CoolingEfficiencyCurves3(df['inunit_cool'])
    unitCoolingEfficiencyCurves4Var = CoolingEfficiencyCurves4(df['inunit_cool'])
    unitCoolingEfficiencyCurves5Var = CoolingEfficiencyCurves5(df['inunit_cool'])
    unitDhwCoeffOnVar = unitDhwCoeffOn(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwCoeffOffVar = unitDhwCoeffOff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitDhwThermEffVar = unitDhwThermEff(df['centraldhweff_avg'], df['inunitdhweff_avg'])
    unitLpdVar = unitLpd(df['LPD_unit'])
    unitVentilationFlowrateVar = unitVentilationFlowrate(df['Ventcentral_YN'] ,df['Vent_inuniterv_YN'] ,df['Vent_inunit_erveff'])
    unitVentilationSPVar = unitVentilationSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    unitHvacFanSPVar = unitHvacFanSP(df['Ventcentral_YN'], df['Vent_inuniterv_YN'])
    extWallCondVar = extWallCond(df['wtmn_GenlWallU'], df['State'])
    ceilingCondVar = ceilingCond(df['wtmn_CeilingU'], df['State'])
    slabCondVar = slabCond(df['Fnd_wtmn_u'], df['Fnd_wtmn_f'], df['State'])
    windowUVar = windowU(df['wtmn_WindowU'], df['State'], df['CZ'])
    windowSHGCVar = windowSHGC(df['wtmn_WindowSHGC'])
    lightingStairsVar = lightingStairs(df['LPD_IntStairwell'])
    bsmtLpdVar = bsmtLpd(df['LPD_IntPk_common'], df['FndType'])
    extPrkLightsVar = extPrkLights(df['LPD_ExtPk'])
    unitHeatingSetpointVar = unitHeatingSetpoint(df['BLANK'])
    unitCoolingSetpointVar = unitCoolingSetpoint(df['BLANK'])
    exteriorCorrLightsVar = exteriorCorrLights(df)
    winterDbVar = WinterDB(df['CZ'], df['State'])
    summerDbVar = SummerDB(df['CZ'], df['State'])
    summerWbVar = SummerWB(df['CZ'], df['State'])
    longitudeVar = Longitude(df['CZ'], df['State'])
    latitudeVar = Latitude(df['CZ'], df['State'])

    
    # create dataframe
    new_df = pd.DataFrame()
    
    # assign new dataframe with values created in above functions
    new_df['v1'] = v1
    new_df['v2'] = v2
    new_df['v3'] = v3
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
    new_df['Exterior corridor Lights [W]'] = exteriorCorrLightsVar
    new_df['WinterDB'] = winterDbVar
    new_df['SummerDB'] = summerDbVar
    new_df['SummerWB'] = summerWbVar
    new_df['Latitude'] = latitudeVar
    new_df['Longitude'] = longitudeVar
    
    return new_df
