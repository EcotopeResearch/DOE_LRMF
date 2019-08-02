#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import sys

from eppy import hvacbuilder
from eppy import modeleditor
from eppy.modeleditor import IDF


# In[2]:


# this function determines what idf version and connects the idd for eppy
def eppy_connection(idffile):
    fp = open(idffile)
    lines=fp.readlines()
    vers = ""
    vers = vers.join(lines[2:12])
    vers
    if vers.find('8.7') != -1:
        print('Using EnergyPlus version 8.7')
        iddfile = 'C:\\EnergyPlusV8-7-0\\Energy+.idd'
        IDF.setiddname(iddfile)
        idf = IDF(idffile)
        return idf
    elif vers.find('8.8') != -1:
        print('Using EnergyPlus version 8.8')
        iddfile = 'C:\\EnergyPlusV8-8-0\\Energy+.idd'
        IDF.setiddname(iddfile)
        idf = IDF(idffile)
        return idf
    elif vers.find('8.9') != -1:
        print('Using EnergyPlus version 8.9')
        iddfile = 'C:\\EnergyPlusV8-9-0\\Energy+.idd'
        IDF.setiddname(iddfile)
        idf = IDF(idffile)
        return idf
    elif vers.find('9.0') != -1:
        print('Using EnergyPlus version 9.0.1')
        iddfile = 'C:\\EnergyPlusV9-0-1\\Energy+.idd'
        IDF.setiddname(iddfile)
        idf = IDF(idffile)
        return idf
    else:
        print('IDF Type not found on line 3')


# In[3]:


#define paths
commonSlab_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\SEED_Models\\common_hp_slab_IECC_2012_V8.7.idf'
commonBsmt_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\SEED_Models\\common_hp_heatedbsmtIECC_2012_V8.7.idf'
gardenSlab_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\SEED_Models\\garden_hp_slab_IECC_2012_V8.7.idf'
gardenBsmt_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\SEED_Models\\garden_hp_heatedbsmtIECC_2012_V8.7.idf'

#make connections
commonSlab = eppy_connection(commonSlab_path)
commonBsmt = eppy_connection(commonBsmt_path)
gardenSlab = eppy_connection(gardenSlab_path)
gardenBsmt = eppy_connection(gardenBsmt_path)

# create groups
idfs = [commonSlab, commonBsmt, gardenSlab, gardenBsmt]
common = [commonSlab, commonBsmt]
garden = [gardenSlab, gardenBsmt]
bsmt = [commonBsmt, gardenBsmt]
slab = [commonSlab, gardenSlab]


# ## Alter Name of Unit Schedule:Compact

# In[6]:


# loop through all idfs [4]
for j in range(0, len(idfs)):
    ## change name of temperature setpoint schedule that applies to units
    # identify schedules
    sch = idfs[j].idfobjects['SCHEDULE:COMPACT']
    heating_sch_unit = [x for x in sch if x.Name == 'heating_sch'][0]
    cooling_sch_unit = [x for x in sch if x.Name == 'cooling_sch'][0]

    # set new names
    heating_sch_unit.Name = 'heating_sch_unit'
    cooling_sch_unit.Name = 'cooling_sch_unit'
    
    ## change referenced schedule
    thermostat = idfs[j].idfobjects['ThermostatSetpoint:DualSetpoint']
    thermostat_unit = [x for x in thermostat if x.Name == 'thermostat_living Dual SP Control'][0]

    thermostat_unit.Heating_Setpoint_Temperature_Schedule_Name = 'heating_sch_unit'
    thermostat_unit.Cooling_Setpoint_Temperature_Schedule_Name = 'cooling_sch_unit'


# ## Add Corridor Temperature Control

# In[7]:


# add exterior:lights to all idfs
newCompactSch = ['heating_sch_corr', 'cooling_sch_corr']
corrThermostats = ['Zone Thermostat_G Corridor', 'Zone Thermostat_M Corridor', 'Zone Thermostat_T Corridor']

# loop through all idfs [4]
for j in range(0, len(common)):
    
    # add new thermostat
    common[j].newidfobject('ThermostatSetpoint:DualSetpoint')
    
    common[j].idfobjects['ThermostatSetpoint:DualSetpoint'][-1].Name = 'thermostat_corr Dual SP Control'
    common[j].idfobjects['ThermostatSetpoint:DualSetpoint'][-1].Heating_Setpoint_Temperature_Schedule_Name = newCompactSch[0]
    common[j].idfobjects['ThermostatSetpoint:DualSetpoint'][-1].Cooling_Setpoint_Temperature_Schedule_Name = newCompactSch[1]
    
    # loop through lights to add [3]
    for i in range(0, len(newCompactSch)):
        
        # create a new schedule
        common[j].newidfobject('SCHEDULE:COMPACT')
        
        # alter inputs for newly created idf object
        common[j].idfobjects['SCHEDULE:COMPACT'][-1].Name = newCompactSch[i]
        common[j].idfobjects['SCHEDULE:COMPACT'][-1].Schedule_Type_Limits_Name = 'Temperature'
        common[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_1 = 'Through: 12/31'
        common[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_2 = 'For: AllDays'
        common[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_3 = 'Until: 24:00'
        if i == 0:
            common[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_4 = '22.22'
        else:
            common[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_4 = '23.88'


# ### Modify Corridor Temperature Controls

# In[8]:


corrThermostats = ['Zone Thermostat_G Corridor', 'Zone Thermostat_M Corridor', 'Zone Thermostat_T Corridor']

# loop through idfs with enclosed corridors
for j in range(0, len(common)):
    
    # loop through ZoneControl:Thermostats for corridors
    for i in range(0, len(corrThermostats)):
        # create list of ZoneControl:Thermostats, pick ZoneControl:Thermostat that matches corridor
        zoneControl = common[j].idfobjects['ZoneControl:Thermostat']
        zoneControlCorr = [x for x in zoneControl if x.Name == corrThermostats[i]][0]
        
        # alter input to correct thermostat control
        zoneControlCorr.Control_1_Name = 'thermostat_corr Dual SP Control'


# ## Add Basement Temperature Control

# In[9]:


# add exterior:lights to all idfs
newCompactSch = ['heating_sch_bsmt', 'cooling_sch_bsmt']

# loop through all idfs [4]
for j in range(0, len(bsmt)):
    
    # add new thermostat
    bsmt[j].newidfobject('ThermostatSetpoint:DualSetpoint')
    
    bsmt[j].idfobjects['ThermostatSetpoint:DualSetpoint'][-1].Name = 'thermostat_corr Dual SP Control'
    bsmt[j].idfobjects['ThermostatSetpoint:DualSetpoint'][-1].Heating_Setpoint_Temperature_Schedule_Name = newCompactSch[0]
    bsmt[j].idfobjects['ThermostatSetpoint:DualSetpoint'][-1].Cooling_Setpoint_Temperature_Schedule_Name = newCompactSch[1]
    
    # loop through lights to add [3]
    for i in range(0, len(newCompactSch)):
        
        # create a new schedule
        bsmt[j].newidfobject('SCHEDULE:COMPACT')
        
        # alter inputs for newly created idf object
        bsmt[j].idfobjects['SCHEDULE:COMPACT'][-1].Name = newCompactSch[i]
        bsmt[j].idfobjects['SCHEDULE:COMPACT'][-1].Schedule_Type_Limits_Name = 'Temperature'
        bsmt[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_1 = 'Through: 12/31'
        bsmt[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_2 = 'For: AllDays'
        bsmt[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_3 = 'Until: 24:00'
        if i == 0:
            common[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_4 = '22.22'
        else:
            common[j].idfobjects['SCHEDULE:COMPACT'][-1].Field_4 = '23.88'
        


# ### Modify Basement Temperature Control

# In[10]:


bsmtThermostats = ['Zone Thermostat_unitheatedbsmt']

# loop through idfs with heated basements
for j in range(0, len(bsmt)):
    
    # loop through ZoneControl:Thermostats for bsmts
    for i in range(0, len(bsmtThermostats)):
        # create list of ZoneControl:Thermostats, pick ZoneControl:Thermostat that matches bsmt
        zoneControl = bsmt[j].idfobjects['ZoneControl:Thermostat']
        zoneControlBsmt = [x for x in zoneControl if x.Name == bsmtThermostats[i]][0]
        
        # alter input to correct thermostat control
        zoneControlBsmt.Control_1_Name = 'thermostat_bsmt Dual SP Control'


# In[11]:


## save idfs
[x.save() for x in idfs]


# In[ ]:




