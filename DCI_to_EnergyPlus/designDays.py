# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:11:13 2019

@author: scott

design day text objects
"""

SeattleDD = (  
"""
Site:Location,
    Seattle Seattle Tacoma Intl A_WA_USA Design_Conditions,    !- Name
    47.47,                    !- Latitude
    -122.32,                  !- Longitude
    -8,                       !- Time Zone
    122;                      !- Elevation

SizingPeriod:DesignDay,
    Seattle Seattle Tacoma Intl A Ann Htg 99.6% Condns DB,    !- Name
    12,                       !- Month
    21,                       !- Day of Month
    WinterDesignDay,          !- Day Type
    @@WDB@@,                     !- Maximum DryBulb Temperature
    0,                        !- Daily DryBulb Temperature Range
    ,                         !- DryBulb Temperature Range Modifier Type
    ,                         !- DryBulb Temperature Range Modifier Day Schedule Name
    Wetbulb,                  !- Humidity Condition Type
    -4.2,                     !- Wetbulb or DewPoint at Maximum DryBulb
    ,                         !- Humidity Condition Day Schedule Name
    ,                         !- Humidity Ratio at Maximum DryBulb
    ,                         !- Enthalpy at Maximum DryBulb
    ,                         !- Daily WetBulb Temperature Range
    99868,                    !- Barometric Pressure
    4.3,                      !- Wind Speed
    20,                       !- Wind Direction
    No,                       !- Rain Indicator
    No,                       !- Snow Indicator
    No,                       !- Daylight Saving Time Indicator
    ASHRAEClearSky,           !- Solar Model Indicator
    ,                         !- Beam Solar Day Schedule Name
    ,                         !- Diffuse Solar Day Schedule Name
    ,                         !- ASHRAE Clear Sky Optical Depth for Beam Irradiance taub
    ,                         !- ASHRAE Clear Sky Optical Depth for Diffuse Irradiance taud
    0;                        !- Sky Clearness

SizingPeriod:DesignDay,
    Seattle Seattle Tacoma Intl A Ann Clg .4% Condns DB=>MWB,    !- Name
    8,                        !- Month
    21,                       !- Day of Month
    SummerDesignDay,          !- Day Type
    @@SDB@@,                     !- Maximum DryBulb Temperature
    10.4,                     !- Daily DryBulb Temperature Range
    ,                         !- DryBulb Temperature Range Modifier Type
    ,                         !- DryBulb Temperature Range Modifier Day Schedule Name
    Wetbulb,                  !- Humidity Condition Type
    @@SWB@@,                     !- Wetbulb or DewPoint at Maximum DryBulb
    ,                         !- Humidity Condition Day Schedule Name
    ,                         !- Humidity Ratio at Maximum DryBulb
    ,                         !- Enthalpy at Maximum DryBulb
    ,                         !- Daily WetBulb Temperature Range
    99868,                    !- Barometric Pressure
    4.2,                      !- Wind Speed
    350,                      !- Wind Direction
    No,                       !- Rain Indicator
    No,                       !- Snow Indicator
    No,                       !- Daylight Saving Time Indicator
    ASHRAEClearSky,           !- Solar Model Indicator
    ,                         !- Beam Solar Day Schedule Name
    ,                         !- Diffuse Solar Day Schedule Name
    ,                         !- ASHRAE Clear Sky Optical Depth for Beam Irradiance taub
    ,                         !- ASHRAE Clear Sky Optical Depth for Diffuse Irradiance taud
    1;                        !- Sky Clearness
"""
)

