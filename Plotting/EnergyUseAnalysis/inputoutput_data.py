# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:48:59 2019

@author: scott
"""

import pandas as pd

def inputoutput():

    commonBsmt_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\commonBsmt\\AllCombinedResults.csv'
    commonSlab_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\commonSlab\\AllCombinedResults.csv'
    gardenBsmt_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\gardenBsmt\\AllCombinedResults.csv'
    gardenSlab_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\jEplus\\results\\gardenSlab\\AllCombinedResults.csv'
    
    commonBsmt = pd.read_csv(commonBsmt_path)
    commonSlab = pd.read_csv(commonSlab_path)
    gardenBsmt = pd.read_csv(gardenBsmt_path)
    gardenSlab = pd.read_csv(gardenSlab_path)
    dfs = [commonBsmt, commonSlab, gardenBsmt, gardenSlab]
    
    
    # create lists for names
    names = []
    IL4A_names = []
    WA4C_names = []
    OR4C_names = []
    IL5A_names = []
    WA5B_names = []
    OR5B_names = []
    MN6A_names = []
    MN7A_names = []
    
    # create lists for energy usages
    eui = []
    intLtg = []
    extLtg = []
    appl = []
    intEq = []
    wtrht = []
    vent = []
    fans = []
    hvac = []
    cool = []
    heat = []    


    IL4A = []
    IL4A_intLtg = []
    IL4A_extLtg = []
    IL4A_appl = []
    IL4A_intEq = []
    IL4A_wtrht = []
    IL4A_vent = []
    IL4A_fans = []
    IL4A_hvac = []
    IL4A_cool = []
    IL4A_heat = []
    
    
    WA4C = []
    WA4C_intLtg = []
    WA4C_extLtg = []
    WA4C_appl = []
    WA4C_intEq = []
    WA4C_wtrht = []
    WA4C_vent = []
    WA4C_fans = []
    WA4C_hvac = []
    WA4C_cool = []
    WA4C_heat = []    
    
    OR4C = []
    OR4C_intLtg = []
    OR4C_extLtg = []
    OR4C_appl = []
    OR4C_intEq = []
    OR4C_wtrht = []
    OR4C_vent = []
    OR4C_fans = []
    OR4C_hvac = []
    OR4C_cool = []
    OR4C_heat = []
    
    IL5A = []
    IL5A_intLtg = []
    IL5A_extLtg = []
    IL5A_appl = []
    IL5A_intEq = []
    IL5A_wtrht = []
    IL5A_vent = []
    IL5A_fans = []
    IL5A_hvac = []
    IL5A_cool = []
    IL5A_heat = []   
    
    WA5B = []
    WA5B_intLtg = []
    WA5B_extLtg = []
    WA5B_appl = []
    WA5B_intEq = []
    WA5B_wtrht = []
    WA5B_vent = []
    WA5B_fans = []
    WA5B_hvac = []
    WA5B_cool = []
    WA5B_heat = []
    
    OR5B = []
    OR5B_intLtg = []
    OR5B_extLtg = []
    OR5B_appl = []
    OR5B_intEq = []
    OR5B_wtrht = []
    OR5B_vent = []
    OR5B_fans = []
    OR5B_hvac = []
    OR5B_cool = []
    OR5B_heat = []
    
    MN6A = []
    MN6A_intLtg = []
    MN6A_extLtg = []
    MN6A_appl = []
    MN6A_intEq = []
    MN6A_wtrht = []
    MN6A_vent = []
    MN6A_fans = []
    MN6A_hvac = []
    MN6A_cool = []
    MN6A_heat = []
    
    MN7A = []
    MN7A_intLtg = []
    MN7A_extLtg = []
    MN7A_appl = []
    MN7A_intEq = []
    MN7A_wtrht = []
    MN7A_vent = []
    MN7A_fans = []
    MN7A_hvac = []
    MN7A_cool = []
    MN7A_heat = []
    
    # create lists for multiple linear regression
    
    IL4A_unitCOP = []
    WA4C_unitCOP = []
    OR4C_unitCOP = []
    IL5A_unitCOP = []
    WA5B_unitCOP = []
    OR5B_unitCOP = []
    MN6A_unitCOP = []
    MN7A_unitCOP = []
    
    IL4A_dhwType = []
    WA4C_dhwType = []
    OR4C_dhwType = []
    IL5A_dhwType = []
    WA5B_dhwType = []
    OR5B_dhwType = []
    MN6A_dhwType = []
    MN7A_dhwType = []
    
    IL4A_dhwEff = []
    WA4C_dhwEff = []
    OR4C_dhwEff = []
    IL5A_dhwEff = []
    WA5B_dhwEff = []
    OR5B_dhwEff = []
    MN6A_dhwEff = []
    MN7A_dhwEff = []
    
    IL4A_unitLPD = []
    WA4C_unitLPD = []
    OR4C_unitLPD = []
    IL5A_unitLPD = []
    WA5B_unitLPD = []
    OR5B_unitLPD = []
    MN6A_unitLPD = []
    MN7A_unitLPD = []
    
    IL4A_unitFlow = []
    WA4C_unitFlow = []
    OR4C_unitFlow = []
    IL5A_unitFlow = []
    WA5B_unitFlow = []
    OR5B_unitFlow = []
    MN6A_unitFlow = []
    MN7A_unitFlow = []
    
    IL4A_unitSP = []
    WA4C_unitSP = []
    OR4C_unitSP = []
    IL5A_unitSP = []
    WA5B_unitSP = []
    OR5B_unitSP = []
    MN6A_unitSP = []
    MN7A_unitSP = []
    
    IL4A_unitHVACSP = []
    WA4C_unitHVACSP = []
    OR4C_unitHVACSP = []
    IL5A_unitHVACSP = []
    WA5B_unitHVACSP = []
    OR5B_unitHVACSP = []
    MN6A_unitHVACSP = []
    MN7A_unitHVACSP = []
    
    IL4A_wallU = []
    WA4C_wallU = []
    OR4C_wallU = []
    IL5A_wallU = []
    WA5B_wallU = []
    OR5B_wallU = []
    MN6A_wallU = []
    MN7A_wallU = []
    
    IL4A_ceilingU = []
    WA4C_ceilingU = []
    OR4C_ceilingU = []
    IL5A_ceilingU = []
    WA5B_ceilingU = []
    OR5B_ceilingU = []
    MN6A_ceilingU = []
    MN7A_ceilingU = []
    
    IL4A_slabU = []
    WA4C_slabU = []
    OR4C_slabU = []
    IL5A_slabU = []
    WA5B_slabU = []
    OR5B_slabU = []
    MN6A_slabU = []
    MN7A_slabU = []
    
    IL4A_windowU = []
    WA4C_windowU = []
    OR4C_windowU = []
    IL5A_windowU = []
    WA5B_windowU = []
    OR5B_windowU = []
    MN6A_windowU = []
    MN7A_windowU = []
    
    IL4A_SHGC = []
    WA4C_SHGC = []
    OR4C_SHGC = []
    IL5A_SHGC = []
    WA5B_SHGC = []
    OR5B_SHGC = []
    MN6A_SHGC = []
    MN7A_SHGC = []
    
    IL4A_strLtg = []
    WA4C_strLtg = []
    OR4C_strLtg = []
    IL5A_strLtg = []
    WA5B_strLtg = []
    OR5B_strLtg = []
    MN6A_strLtg = []
    MN7A_strLtg = []
    
    IL4A_prkLtg = []
    WA4C_prkLtg = []
    OR4C_prkLtg = []
    IL5A_prkLtg = []
    WA5B_prkLtg = []
    OR5B_prkLtg = []
    MN6A_prkLtg = []
    MN7A_prkLtg = []
    
    IL4A_extPrkLtg = []
    WA4C_extPrkLtg = []
    OR4C_extPrkLtg = []
    IL5A_extPrkLtg = []
    WA5B_extPrkLtg = []
    OR5B_extPrkLtg = []
    MN6A_extPrkLtg = []
    MN7A_extPrkLtg = []
    
    weather = []
    unitCOP = []
    dhwType = []
    dhwEff = []
    unitLPD = []
    unitFlow = []            
    unitSP = []
    unitHVACSP = []
    wallU = []
    ceilingU = []
    slabU = []
    windowU = []
    SHGC = []
    strLtg = []
    prkLtg = []
    extPrkLtg = []
    
    
    for i in range(0,len(dfs)):
        
        df = dfs[i]
        for i in range(0, len(df)):
            
            # climate zone plots
            
            # check weather file location - St. Louis
            if df.loc[i,'WeatherFile']=='USA_MO_St.Louis-Spirit.of.St.Louis.AP.724345_TMY3.epw':
                
                IL4A_names.append(df.loc[i,'@@NAME@@'])
                
                # energy usage
                IL4A.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_intLtg.append(df.loc[i,'c1: InteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_extLtg.append(df.loc[i,'c2: ExteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_appl.append(df.loc[i,'c3: Appl:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_intEq.append(df.loc[i,'c4: Misc:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_wtrht.append(df.loc[i,'c5: Water Heater:WaterSystems:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_vent.append(df.loc[i,'c6: Ventilation (simple):Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_fans.append(df.loc[i,'c7: General:Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_hvac.append(df.loc[i,'c8: Electricity:HVAC [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_cool.append(df.loc[i,'c9: Cooling:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL4A_heat.append(df.loc[i,'c10: Heating:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                
                # inputs for multi-var regression
                IL4A_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
                IL4A_dhwType.append(df.loc[i,'@@ONCOEF@@'])
                IL4A_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
                IL4A_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
                IL4A_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
                IL4A_unitSP.append(df.loc[i,'@@SPUNIT@@'])
                IL4A_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
                IL4A_wallU.append(df.loc[i,'@@WALLU@@'])
                IL4A_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
                IL4A_slabU.append(df.loc[i,'@@SLABU@@'])
                IL4A_windowU.append(df.loc[i,'@@WINU@@'])
                IL4A_SHGC.append(df.loc[i,'@@SHGC@@'])            
                IL4A_strLtg.append(df.loc[i,'@@LTGSTR@@'])
                IL4A_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
                IL4A_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
    
                
            # check weather file location - Seattle
            if df.loc[i,'WeatherFile']=='USA_WA_Seattle-Tacoma.Intl.AP.727930_TMY3.epw':
                
                WA4C_names.append(df.loc[i,'@@NAME@@'])
                
                WA4C.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_intLtg.append(df.loc[i,'c1: InteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_extLtg.append(df.loc[i,'c2: ExteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_appl.append(df.loc[i,'c3: Appl:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_intEq.append(df.loc[i,'c4: Misc:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_wtrht.append(df.loc[i,'c5: Water Heater:WaterSystems:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_vent.append(df.loc[i,'c6: Ventilation (simple):Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_fans.append(df.loc[i,'c7: General:Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_hvac.append(df.loc[i,'c8: Electricity:HVAC [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_cool.append(df.loc[i,'c9: Cooling:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA4C_heat.append(df.loc[i,'c10: Heating:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                
                # inputs for multi-var regression
                WA4C_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
                WA4C_dhwType.append(df.loc[i,'@@ONCOEF@@'])
                WA4C_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
                WA4C_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
                WA4C_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
                WA4C_unitSP.append(df.loc[i,'@@SPUNIT@@'])
                WA4C_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
                WA4C_wallU.append(df.loc[i,'@@WALLU@@'])
                WA4C_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
                WA4C_slabU.append(df.loc[i,'@@SLABU@@'])
                WA4C_windowU.append(df.loc[i,'@@WINU@@'])
                WA4C_SHGC.append(df.loc[i,'@@SHGC@@'])            
                WA4C_strLtg.append(df.loc[i,'@@LTGSTR@@'])
                WA4C_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
                WA4C_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
                
            # check weather file location - Portland
            if df.loc[i,'WeatherFile']=='USA_OR_Portland.Intl.AP.726980_TMY3.epw':
                
                OR4C_names.append(df.loc[i,'@@NAME@@'])
                
                OR4C.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_intLtg.append(df.loc[i,'c1: InteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_extLtg.append(df.loc[i,'c2: ExteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_appl.append(df.loc[i,'c3: Appl:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_intEq.append(df.loc[i,'c4: Misc:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_wtrht.append(df.loc[i,'c5: Water Heater:WaterSystems:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_vent.append(df.loc[i,'c6: Ventilation (simple):Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_fans.append(df.loc[i,'c7: General:Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_hvac.append(df.loc[i,'c8: Electricity:HVAC [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_cool.append(df.loc[i,'c9: Cooling:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR4C_heat.append(df.loc[i,'c10: Heating:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                
                # inputs for multi-var regression
                OR4C_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
                OR4C_dhwType.append(df.loc[i,'@@ONCOEF@@'])
                OR4C_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
                OR4C_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
                OR4C_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
                OR4C_unitSP.append(df.loc[i,'@@SPUNIT@@'])
                OR4C_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
                OR4C_wallU.append(df.loc[i,'@@WALLU@@'])
                OR4C_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
                OR4C_slabU.append(df.loc[i,'@@SLABU@@'])
                OR4C_windowU.append(df.loc[i,'@@WINU@@'])
                OR4C_SHGC.append(df.loc[i,'@@SHGC@@'])            
                OR4C_strLtg.append(df.loc[i,'@@LTGSTR@@'])
                OR4C_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
                OR4C_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
            
            # check weather file location - Chicago
            if df.loc[i,'WeatherFile']=='USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw':
                
                IL5A_names.append(df.loc[i,'@@NAME@@'])
                
                IL5A.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_intLtg.append(df.loc[i,'c1: InteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_extLtg.append(df.loc[i,'c2: ExteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_appl.append(df.loc[i,'c3: Appl:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_intEq.append(df.loc[i,'c4: Misc:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_wtrht.append(df.loc[i,'c5: Water Heater:WaterSystems:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_vent.append(df.loc[i,'c6: Ventilation (simple):Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_fans.append(df.loc[i,'c7: General:Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_hvac.append(df.loc[i,'c8: Electricity:HVAC [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_cool.append(df.loc[i,'c9: Cooling:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                IL5A_heat.append(df.loc[i,'c10: Heating:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                
                # inputs for multi-var regression
                IL5A_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
                IL5A_dhwType.append(df.loc[i,'@@ONCOEF@@'])
                IL5A_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
                IL5A_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
                IL5A_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
                IL5A_unitSP.append(df.loc[i,'@@SPUNIT@@'])
                IL5A_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
                IL5A_wallU.append(df.loc[i,'@@WALLU@@'])
                IL5A_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
                IL5A_slabU.append(df.loc[i,'@@SLABU@@'])
                IL5A_windowU.append(df.loc[i,'@@WINU@@'])
                IL5A_SHGC.append(df.loc[i,'@@SHGC@@'])            
                IL5A_strLtg.append(df.loc[i,'@@LTGSTR@@'])
                IL5A_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
                IL5A_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
                
            # check weather file location - Spokane
            if df.loc[i,'WeatherFile']=='USA_WA_Spokane.Intl.AP.727850_TMY3.epw':
                
                WA5B_names.append(df.loc[i,'@@NAME@@'])
                
                WA5B.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_intLtg.append(df.loc[i,'c1: InteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_extLtg.append(df.loc[i,'c2: ExteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_appl.append(df.loc[i,'c3: Appl:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_intEq.append(df.loc[i,'c4: Misc:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_wtrht.append(df.loc[i,'c5: Water Heater:WaterSystems:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_vent.append(df.loc[i,'c6: Ventilation (simple):Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_fans.append(df.loc[i,'c7: General:Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_hvac.append(df.loc[i,'c8: Electricity:HVAC [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_cool.append(df.loc[i,'c9: Cooling:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                WA5B_heat.append(df.loc[i,'c10: Heating:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                
                # inputs for multi-var regression
                WA5B_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
                WA5B_dhwType.append(df.loc[i,'@@ONCOEF@@'])
                WA5B_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
                WA5B_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
                WA5B_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
                WA5B_unitSP.append(df.loc[i,'@@SPUNIT@@'])
                WA5B_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
                WA5B_wallU.append(df.loc[i,'@@WALLU@@'])
                WA5B_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
                WA5B_slabU.append(df.loc[i,'@@SLABU@@'])
                WA5B_windowU.append(df.loc[i,'@@WINU@@'])
                WA5B_SHGC.append(df.loc[i,'@@SHGC@@'])            
                WA5B_strLtg.append(df.loc[i,'@@LTGSTR@@'])
                WA5B_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
                WA5B_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@']) 
                
            # check weather file location - Redmond
            if df.loc[i,'WeatherFile']=='USA_OR_Redmond-Roberts.Field.726835_TMY3.epw':
                
                OR5B_names.append(df.loc[i,'@@NAME@@'])
                
                OR5B.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_intLtg.append(df.loc[i,'c1: InteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_extLtg.append(df.loc[i,'c2: ExteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_appl.append(df.loc[i,'c3: Appl:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_intEq.append(df.loc[i,'c4: Misc:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_wtrht.append(df.loc[i,'c5: Water Heater:WaterSystems:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_vent.append(df.loc[i,'c6: Ventilation (simple):Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_fans.append(df.loc[i,'c7: General:Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_hvac.append(df.loc[i,'c8: Electricity:HVAC [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_cool.append(df.loc[i,'c9: Cooling:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                OR5B_heat.append(df.loc[i,'c10: Heating:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                
                # inputs for multi-var regression
                OR5B_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
                OR5B_dhwType.append(df.loc[i,'@@ONCOEF@@'])
                OR5B_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
                OR5B_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
                OR5B_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
                OR5B_unitSP.append(df.loc[i,'@@SPUNIT@@'])
                OR5B_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
                OR5B_wallU.append(df.loc[i,'@@WALLU@@'])
                OR5B_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
                OR5B_slabU.append(df.loc[i,'@@SLABU@@'])
                OR5B_windowU.append(df.loc[i,'@@WINU@@'])
                OR5B_SHGC.append(df.loc[i,'@@SHGC@@'])            
                OR5B_strLtg.append(df.loc[i,'@@LTGSTR@@'])
                OR5B_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
                OR5B_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
                
            # check weather file location - Minneapolis
            if df.loc[i,'WeatherFile']=='USA_MN_Minneapolis-St.Paul.Intl.AP.726580_TMY3.epw':
                
                MN6A_names.append(df.loc[i,'@@NAME@@'])
                
                MN6A.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_intLtg.append(df.loc[i,'c1: InteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_extLtg.append(df.loc[i,'c2: ExteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_appl.append(df.loc[i,'c3: Appl:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_intEq.append(df.loc[i,'c4: Misc:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_wtrht.append(df.loc[i,'c5: Water Heater:WaterSystems:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_vent.append(df.loc[i,'c6: Ventilation (simple):Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_fans.append(df.loc[i,'c7: General:Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_hvac.append(df.loc[i,'c8: Electricity:HVAC [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_cool.append(df.loc[i,'c9: Cooling:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN6A_heat.append(df.loc[i,'c10: Heating:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                
                # inputs for multi-var regression
                MN6A_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
                MN6A_dhwType.append(df.loc[i,'@@ONCOEF@@'])
                MN6A_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
                MN6A_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
                MN6A_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
                MN6A_unitSP.append(df.loc[i,'@@SPUNIT@@'])
                MN6A_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
                MN6A_wallU.append(df.loc[i,'@@WALLU@@'])
                MN6A_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
                MN6A_slabU.append(df.loc[i,'@@SLABU@@'])
                MN6A_windowU.append(df.loc[i,'@@WINU@@'])
                MN6A_SHGC.append(df.loc[i,'@@SHGC@@'])            
                MN6A_strLtg.append(df.loc[i,'@@LTGSTR@@'])
                MN6A_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
                MN6A_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
                
            # check weather file location - Bemidji
            if df.loc[i,'WeatherFile']=='USA_MN_Bemidji.Muni.AP.727550_TMY3.epw':
                
                MN7A_names.append(df.loc[i,'@@NAME@@'])
                
                MN7A.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_intLtg.append(df.loc[i,'c1: InteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_extLtg.append(df.loc[i,'c2: ExteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_appl.append(df.loc[i,'c3: Appl:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_intEq.append(df.loc[i,'c4: Misc:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_wtrht.append(df.loc[i,'c5: Water Heater:WaterSystems:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_vent.append(df.loc[i,'c6: Ventilation (simple):Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_fans.append(df.loc[i,'c7: General:Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_hvac.append(df.loc[i,'c8: Electricity:HVAC [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_cool.append(df.loc[i,'c9: Cooling:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
                MN7A_heat.append(df.loc[i,'c10: Heating:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
    
                # inputs for multi-var regression
                MN7A_unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
                MN7A_dhwType.append(df.loc[i,'@@ONCOEF@@'])
                MN7A_dhwEff.append(df.loc[i,'@@DHWCOP@@'])
                MN7A_unitLPD.append(df.loc[i,'@@UNITLPD@@'])
                MN7A_unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
                MN7A_unitSP.append(df.loc[i,'@@SPUNIT@@'])
                MN7A_unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])            
                MN7A_wallU.append(df.loc[i,'@@WALLU@@'])
                MN7A_ceilingU.append(df.loc[i,'@@CEILINGU@@'])
                MN7A_slabU.append(df.loc[i,'@@SLABU@@'])
                MN7A_windowU.append(df.loc[i,'@@WINU@@'])
                MN7A_SHGC.append(df.loc[i,'@@SHGC@@'])            
                MN7A_strLtg.append(df.loc[i,'@@LTGSTR@@'])
                MN7A_prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
                MN7A_extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
                
            ## inputs for multiple regression, assume linear
            
            # names
            names.append(df.loc[i,'@@NAME@@'])
            
            # dependent variable, reponse, dependent
            eui.append(df.loc[i,'c0: Electricity:Facility [J](RunPeriod)']*0.000947817/1000/31000)
            intLtg.append(df.loc[i,'c1: InteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
            extLtg.append(df.loc[i,'c2: ExteriorLights:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
            appl.append(df.loc[i,'c3: Appl:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
            intEq.append(df.loc[i,'c4: Misc:InteriorEquipment:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
            wtrht.append(df.loc[i,'c5: Water Heater:WaterSystems:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
            vent.append(df.loc[i,'c6: Ventilation (simple):Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
            fans.append(df.loc[i,'c7: General:Fans:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
            hvac.append(df.loc[i,'c8: Electricity:HVAC [J](RunPeriod)']*0.000947817/1000/31000)
            cool.append(df.loc[i,'c9: Cooling:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
            heat.append(df.loc[i,'c10: Heating:Electricity [J](RunPeriod)']*0.000947817/1000/31000)
            
            # explanatory variables, covariates, independent
            weather.append(df.loc[i,'WeatherFile'])
            unitCOP.append(df.loc[i,'@@UNITHTCOP@@'])
            dhwType.append(df.loc[i,'@@ONCOEF@@'])
            dhwEff.append(df.loc[i,'@@DHWCOP@@'])
            unitLPD.append(df.loc[i,'@@UNITLPD@@'])
            unitFlow.append(df.loc[i,'@@FLOWUNIT@@'])            
            unitSP.append(df.loc[i,'@@SPUNIT@@'])
            unitHVACSP.append(df.loc[i,'@@SPHVACUNIT@@'])
            wallU.append(df.loc[i,'@@WALLU@@'])
            ceilingU.append(df.loc[i,'@@CEILINGU@@'])
            slabU.append(df.loc[i,'@@SLABU@@'])
            windowU.append(df.loc[i,'@@WINU@@'])
            SHGC.append(df.loc[i,'@@SHGC@@'])            
            strLtg.append(df.loc[i,'@@LTGSTR@@'])
            prkLtg.append(df.loc[i,'@@LTGINTPKG@@'])
            extPrkLtg.append(df.loc[i,'@@LTGEXTPKG@@'])
        
    index = ['names', 'eui', 'intLtg', 'extLtg', 'appl', 'intEq', 'wtrht', 'vent', 'fans', 'hvac', 'cool', 'heat', 
             'unitCOP', 'dhwType', 'dhwEff', 'unitLPD', 'unitFlow', 'unitSP', 'unitHVACSP', 'wallU', 'ceilingU', 'slabU', 'windowU', 'SHGC', 'strLtg', 'prkLtg', 'extPrkLtg']
    
    d = {'All States': [names, eui, intLtg, extLtg, appl, intEq, wtrht, vent, fans, hvac, cool, heat,
                        unitCOP, dhwType, dhwEff, unitLPD, unitFlow, unitSP, unitHVACSP, wallU, ceilingU, slabU, windowU, SHGC, strLtg, prkLtg, extPrkLtg],
         
         'IL4A': [IL4A_names ,IL4A, IL4A_intLtg, IL4A_extLtg, IL4A_appl, IL4A_intEq, IL4A_wtrht, IL4A_vent, IL4A_fans, IL4A_hvac, IL4A_cool, IL4A_heat,
                  IL4A_unitCOP, IL4A_dhwType, IL4A_dhwEff, IL4A_unitLPD, IL4A_unitFlow, IL4A_unitSP, IL4A_unitHVACSP, IL4A_wallU, IL4A_ceilingU, IL4A_slabU, IL4A_windowU, IL4A_SHGC, IL4A_strLtg, IL4A_prkLtg, IL4A_extPrkLtg],
                  
         'WA4C': [WA4C_names, WA4C, WA4C_intLtg, WA4C_extLtg, WA4C_appl, WA4C_intEq, WA4C_wtrht, WA4C_vent, WA4C_fans, WA4C_hvac, WA4C_cool, WA4C_heat,
                  WA4C_unitCOP, WA4C_dhwType, WA4C_dhwEff, WA4C_unitLPD, WA4C_unitFlow, WA4C_unitSP, WA4C_unitHVACSP, WA4C_wallU, WA4C_ceilingU, WA4C_slabU, WA4C_windowU, WA4C_SHGC, WA4C_strLtg, WA4C_prkLtg, WA4C_extPrkLtg],
                  
         'OR4C': [OR4C_names, OR4C, OR4C_intLtg, OR4C_extLtg, OR4C_appl, OR4C_intEq, OR4C_wtrht, OR4C_vent, OR4C_fans, OR4C_hvac, OR4C_cool, OR4C_heat,
                  OR4C_unitCOP, OR4C_dhwType, OR4C_dhwEff, OR4C_unitLPD, OR4C_unitFlow, OR4C_unitSP, OR4C_unitHVACSP, OR4C_wallU, OR4C_ceilingU, OR4C_slabU, OR4C_windowU,OR4C_SHGC, OR4C_strLtg, OR4C_prkLtg, OR4C_extPrkLtg],
    
         'IL5A': [IL5A_names, IL5A, IL5A_intLtg, IL5A_extLtg, IL5A_appl, IL5A_intEq, IL5A_wtrht, IL5A_vent, IL5A_fans, IL5A_hvac, IL5A_cool, IL5A_heat,
                  IL5A_unitCOP, IL5A_dhwType, IL5A_dhwEff, IL5A_unitLPD, IL5A_unitFlow, IL5A_unitSP, IL5A_unitHVACSP, IL5A_wallU, IL5A_ceilingU, IL5A_slabU, IL5A_windowU,IL5A_SHGC, IL5A_strLtg, IL5A_prkLtg, IL5A_extPrkLtg],
         
         'WA5B': [WA5B_names, WA5B, WA5B_intLtg, WA5B_extLtg, WA5B_appl, WA5B_intEq, WA5B_wtrht, WA5B_vent, WA5B_fans, WA5B_hvac, WA5B_cool, WA5B_heat,
                  WA5B_unitCOP, WA5B_dhwType, WA5B_dhwEff, WA5B_unitLPD, WA5B_unitFlow, WA5B_unitSP, WA5B_unitHVACSP, WA5B_wallU, WA5B_ceilingU, WA5B_slabU, WA5B_windowU, WA5B_SHGC, WA5B_strLtg, WA5B_prkLtg, WA5B_extPrkLtg],
         
         'OR5B': [OR5B_names, OR5B, OR5B_intLtg, OR5B_extLtg, OR5B_appl, OR5B_intEq, OR5B_wtrht, OR5B_vent, OR5B_fans, OR5B_hvac, OR5B_cool, OR5B_heat,
                  OR5B_unitCOP, OR5B_dhwType, OR5B_dhwEff, OR5B_unitLPD, OR5B_unitFlow, OR5B_unitSP, OR5B_unitHVACSP, OR5B_wallU, OR5B_ceilingU, OR5B_slabU, OR5B_windowU,OR5B_SHGC, OR5B_strLtg, OR5B_prkLtg, OR5B_extPrkLtg],
         
         'MN6A': [MN6A_names, MN6A, MN6A_intLtg, MN6A_extLtg, MN6A_appl, MN6A_intEq, MN6A_wtrht, MN6A_vent, MN6A_fans, MN6A_hvac, MN6A_cool, MN6A_heat,
                  MN6A_unitCOP, MN6A_dhwType, MN6A_dhwEff, MN6A_unitLPD, MN6A_unitFlow, MN6A_unitSP, MN6A_unitHVACSP, MN6A_wallU, MN6A_ceilingU, MN6A_slabU, MN6A_windowU, MN6A_SHGC, MN6A_strLtg, MN6A_prkLtg, MN6A_extPrkLtg],
         
         'MN7A': [MN7A_names, MN7A, MN7A_intLtg, MN7A_extLtg, MN7A_appl, MN7A_intEq, MN7A_wtrht, MN7A_vent, MN7A_fans, MN7A_hvac, MN7A_cool, MN7A_heat,
                  MN7A_unitCOP, MN7A_dhwType, MN7A_dhwEff, MN7A_unitLPD, MN7A_unitFlow, MN7A_unitSP, MN7A_unitHVACSP, MN7A_wallU, MN7A_ceilingU, MN7A_slabU, MN7A_windowU,MN7A_SHGC, MN7A_strLtg, MN7A_prkLtg, MN7A_extPrkLtg]
         }
    
    df = pd.DataFrame.from_dict(d)
    df['index'] = index
    df = df.set_index('index')
    
    return df