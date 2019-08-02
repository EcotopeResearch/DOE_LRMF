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


# ## Remove Existing Exterior:Lights from all idfs

# In[6]:


for i in range(0, len(idfs)):
    # create list for exterior lights
    existingExtLights = idfs[i].idfobjects['EXTERIOR:LIGHTS']

    #remove all items in exterior lights list
    for i in range(0, len(existingExtLights)):
        existingExtLights.remove(existingExtLights[0])


# ## Exterior:Lights for all idfs

# In[10]:


# add exterior:lights to all idfs
newExtLights = ['stairLights', 'intPrkLights', 'extPrkLights']

# loop through all idfs [4]
for j in range(0, len(idfs)):
    # loop through lights to add [3]
    for i in range(0, len(newExtLights)):
        
        # create a new thermostat control
        idfs[j].newidfobject('Exterior:Lights')

        # alter inputs to the newly crated idf object
        idfs[j].idfobjects['Exterior:Lights'][-1].Name = newExtLights[i]
        idfs[j].idfobjects['Exterior:Lights'][-1].Schedule_Name = 'ExteriorLightingProfile'
        idfs[j].idfobjects['Exterior:Lights'][-1].Design_Level = 500
        idfs[j].idfobjects['Exterior:Lights'][-1].EndUse_Subcategory = 'Exterior-Lights'


# ## Exterior:Lights for Garden idfs

# In[11]:


# add exterior:lights to all idfs
newExtLights = ['corrExtLights']

# loop through all idfs [4]
for j in range(0, len(garden)):
    # loop through lights to add [3]
    for i in range(0, len(newExtLights)):
        
        # create a new thermostat control
        garden[j].newidfobject('Exterior:Lights')

        # alter inputs to the newly crated idf object
        garden[j].idfobjects['Exterior:Lights'][-1].Name = newExtLights[i]
        garden[j].idfobjects['Exterior:Lights'][-1].Schedule_Name = 'ExteriorLightingProfile'
        garden[j].idfobjects['Exterior:Lights'][-1].Design_Level = 500
        garden[j].idfobjects['Exterior:Lights'][-1].EndUse_Subcategory = 'Exterior-Lights'


# In[13]:


[x.save() for x in idfs]


# In[ ]:





# In[ ]:




