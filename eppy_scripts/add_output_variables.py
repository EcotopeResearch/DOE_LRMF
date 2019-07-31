"""
Created on Wed Jul 31 13:14:27 2019

@author: scott
"""


# In[1]:


import numpy as np
import pandas as pd
import sys

from eppy import hvacbuilder
from eppy import modeleditor
from eppy.modeleditor import IDF


# In[2]:


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


# In[4]:


#define paths
idf_path = 'C:\\Users\\scott\\github\\DOE_LRMF\\SEED_Models\\common_hp_slab_IECC_2012_V8.7.idf'

#make connections
idf = eppy_connection(idf_path)


# ## Add Zone Mean Air Temperature

# In[ ]:


# use eppy to get a list of Zone Names
zones = idf.idfobjects['ZONE']
zoneNames = [x.Name for x in zones]


# In[ ]:


#add Zone Mean Air Temperature for corridors
keyValue = zoneNames
variableName = 'Zone Mean Air Temperature'
reportingFrequency = 'hourly'


for i in range(0, len(keyValue)):

    # create a idf object
    idf.newidfobject('Output:Variable')

    # alter inputs to the newly crated idf object
    idf.idfobjects['Output:Variable'][-1].Key_Value = keyValue[i]
    idf.idfobjects['Output:Variable'][-1].Variable_Name = variableName
    idf.idfobjects['Output:Variable'][-1].Reporting_Frequency = reportingFrequency

idf.save()


# ## Add Surface Inside Face Conduction Heat Gain Rate

# In[ ]:


#add Surface Inside Face Conduction Heat Gain Rate
keyValue = ['Wall_ldb_1.unit2_FrontRow_BottomFloor', 'Wall_ldb_1.unit2_FrontRow_MiddleFloor', 'Wall_ldb_1.unit2_FrontRow_TopFloor']
variableName = 'Surface Inside Face Conduction Heat Gain Rate'
reportingFrequency = 'hourly'


for i in range(0, len(keyValue)):

    # create a idf object
    idf.newidfobject('Output:Variable')

    # alter inputs to the newly created idf object
    idf.idfobjects['Output:Variable'][-1].Key_Value = keyValue[i]
    idf.idfobjects['Output:Variable'][-1].Variable_Name = variableName
    idf.idfobjects['Output:Variable'][-1].Reporting_Frequency = reportingFrequency

idf.save()


# ## Add Cooling Coil Total Cooling Energy

# In[ ]:


# use eppy to get a list of Cooling Coil Names
coolingCoil = idf.idfobjects['Coil:Cooling:DX:SingleSpeed']
coolingCoilNames = [x.Name for x in coolingCoil]


# In[ ]:


#add Cooling Coil Total Cooling Energy for corridors
keyValue = coolingCoilNames
variableName1 = 'Cooling Coil Total Cooling Energy'
variableName2 = 'Cooling Coil Electric Energy'
reportingFrequency = 'hourly'


for i in range(0, len(keyValue)):

    # create a idf object
    idf.newidfobject('Output:Variable')

    # alter inputs to the newly created idf object
    idf.idfobjects['Output:Variable'][-1].Key_Value = keyValue[i]
    idf.idfobjects['Output:Variable'][-1].Variable_Name = variableName1
    idf.idfobjects['Output:Variable'][-1].Reporting_Frequency = reportingFrequency

    # create a idf object
    idf.newidfobject('Output:Variable')

    # alter inputs to the newly created idf object
    idf.idfobjects['Output:Variable'][-1].Key_Value = keyValue[i]
    idf.idfobjects['Output:Variable'][-1].Variable_Name = variableName2
    idf.idfobjects['Output:Variable'][-1].Reporting_Frequency = reportingFrequency

idf.save()

# ## Add Heating Coil Total Heating Energy to Corridor HPs

# In[ ]:


# use eppy to get a list of Heating Coil Names
heatingCoil = idf.idfobjects['Coil:Heating:DX:SingleSpeed']
heatingCoilNames = [x.Name for x in heatingCoil]


# In[ ]:


#add Heating Coil Total Cooling Energy
keyValue = heatingCoilNames
variableName1 = 'Heating Coil Total Heating Energy'
variableName2 = 'Heating Coil Electric Energy'
reportingFrequency = 'hourly'

for i in range(0, len(keyValue)):

    # create a idf object
    idf.newidfobject('Output:Variable')

    # alter inputs to the newly created idf object
    idf.idfobjects['Output:Variable'][-1].Key_Value = keyValue[i]
    idf.idfobjects['Output:Variable'][-1].Variable_Name = variableName1
    idf.idfobjects['Output:Variable'][-1].Reporting_Frequency = reportingFrequency
    
    # create a idf object
    idf.newidfobject('Output:Variable')

    # alter inputs to the newly created idf object
    idf.idfobjects['Output:Variable'][-1].Key_Value = keyValue[i]
    idf.idfobjects['Output:Variable'][-1].Variable_Name = variableName2
    idf.idfobjects['Output:Variable'][-1].Reporting_Frequency = reportingFrequency

idf.save()


# In[ ]:

# use eppy to get a list of Electric Heating Coil Names
heatingCoil = idf.idfobjects['Coil:Heating:Electric']
heatingCoilNames = [x.Name for x in heatingCoil]

#add Electric Heating Coil Energy Usage
keyValue = heatingCoilNames
variableName1 = 'Heating Coil Total Heating Energy'
variableName2 = 'Heating Coil Electric Energy'
reportingFrequency = 'hourly'

for i in range(0, len(keyValue)):

    # create a idf object
    idf.newidfobject('Output:Variable')

    # alter inputs to the newly created idf object
    idf.idfobjects['Output:Variable'][-1].Key_Value = keyValue[i]
    idf.idfobjects['Output:Variable'][-1].Variable_Name = variableName1
    idf.idfobjects['Output:Variable'][-1].Reporting_Frequency = reportingFrequency
    
    # create a idf object
    idf.newidfobject('Output:Variable')

    # alter inputs to the newly created idf object
    idf.idfobjects['Output:Variable'][-1].Key_Value = keyValue[i]
    idf.idfobjects['Output:Variable'][-1].Variable_Name = variableName2
    idf.idfobjects['Output:Variable'][-1].Reporting_Frequency = reportingFrequency

idf.save()
