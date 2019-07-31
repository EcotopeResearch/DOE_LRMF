"""
Created on Wed Jul 31 13:14:27 2019

@author: scott
"""

# In[2]:


import numpy as np
import pandas as pd
import sys

from eppy import hvacbuilder
from eppy import modeleditor
from eppy.modeleditor import IDF


# In[3]:


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

#add lights for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new thermostat control
    idf.newidfobject('Lights')

    # alter inputs to the newly crated idf object
    idf.idfobjects['Lights'][-1].Name = ('Corridor Lights Lighting_' + newZones[i])
    idf.idfobjects['Lights'][-1].Zone_or_ZoneList_Name = newZones[i]
    idf.idfobjects['Lights'][-1].Schedule_Name = 'LightingProfile_EELighting'
    idf.idfobjects['Lights'][-1].Design_Level_Calculation_Method = 'Watts/Area'
    idf.idfobjects['Lights'][-1].Watts_per_Zone_Floor_Area = 0.288
    idf.idfobjects['Lights'][-1].Return_Air_Fraction = 0
    idf.idfobjects['Lights'][-1].Fraction_Radiant = 0.6
    idf.idfobjects['Lights'][-1].Fraction_Visible = 0.2
    idf.idfobjects['Lights'][-1].Fraction_Replaceable = 0

idf.save()


# ## Add ZoneVentilation:DesignFlowRate

# In[7]:


#add lights for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new thermostat control
    idf.newidfobject('ZoneVentilation:DesignFlowRate')

    # alter inputs to the newly crated idf object
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Name = ('Ventilation_' + newZones[i])
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Zone_or_ZoneList_Name = newZones[i]
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Schedule_Name = 'always_avail'
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Design_Flow_Rate = 'Flow/Zone'
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Design_Flow_Rate = 0.0212524794559365
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Ventilation_Type = 'Exhaust'
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Fan_Pressure_Rise = 0
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Fan_Total_Efficiency = 1
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Constant_Term_Coefficient = 1
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Temperature_Term_Coefficient = 0
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Velocity_Term_Coefficient = 0
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Velocity_Squared_Term_Coefficient = 0
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Minimum_Indoor_Temperature = -100
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Maximum_Indoor_Temperature = 100
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Delta_Temperature = -100
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Minimum_Outdoor_Temperature = -100
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Maximum_Outdoor_Temperature = 100
    idf.idfobjects['ZoneVentilation:DesignFlowRate'][-1].Maximum_Wind_Speed = 40   
    
idf.save()


# ## Add Coil:Heating:DX:SingleSpeed

# In[8]:


#add zone thermostat control for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new thermostat control
    idf.newidfobject('Coil:Heating:DX:SingleSpeed')
    
    # alter inputs to the newly crated idf object
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Name = ('Main DX Heating Coil_' + newZones[i])
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Availability_Schedule_Name = 'always_avail'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Gross_Rated_Heating_Capacity = 'autosize'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Gross_Rated_Heating_COP = 3.63216498787731
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Rated_Air_Flow_Rate = 'autosize'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Air_Inlet_Node_Name = ('Heating Coil Air Inlet Node_' + newZones[i])
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Air_Outlet_Node_Name = ('Supp Heating Coil Air Inlet Node_' + newZones[i])
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Heating_Capacity_Function_of_Temperature_Curve_Name = 'HPACHeatCapFT'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Heating_Capacity_Function_of_Flow_Fraction_Curve_Name = 'HPACHeatCapFFF'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Energy_Input_Ratio_Function_of_Temperature_Curve_Name = 'HPACHeatEIRFT'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name = 'HPACHeatEIRFFF'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Part_Load_Fraction_Correlation_Curve_Name = 'HPACCOOLPLFFPLR'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Defrost_Energy_Input_Ratio_Function_of_Temperature_Curve_Name = 'Defrost_EIR_FT'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation = -17.78
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Maximum_Outdoor_DryBulb_Temperature_for_Defrost_Operation = 5
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Crankcase_Heater_Capacity = 200
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater_Operation = 10
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Defrost_Strategy = 'ReverseCycle'
    idf.idfobjects['Coil:Heating:DX:SingleSpeed'][-1].Defrost_Control = 'OnDemand'

idf.save()    


# ## Add Coil:Cooling:DX:SingleSpeed

# In[9]:


#add zone thermostat control for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new thermostat control
    idf.newidfobject('Coil:Cooling:DX:SingleSpeed')
    
    # alter inputs to the newly crated idf object
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Name = ('DX Cooling Coil_' + newZones[i])
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Availability_Schedule_Name = 'always_avail'
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Gross_Rated_Total_Cooling_Capacity = 'autosize'
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Gross_Rated_Sensible_Heat_Ratio = 'autosize'
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Gross_Rated_Cooling_COP = 3.97008850025305
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Rated_Air_Flow_Rate = 'autosize'
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Air_Inlet_Node_Name = ('Cooling Coil Air Inlet Node_' + newZones[i])
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Air_Outlet_Node_Name = ('Heating Coil Air Inlet Node_' + newZones[i])
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Total_Cooling_Capacity_Function_of_Temperature_Curve_Name = 'HPACCoolCapFT'
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Total_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name = 'HPACCoolCapFFF'
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Energy_Input_Ratio_Function_of_Temperature_Curve_Name = 'HPACCOOLEIRFT'
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name = 'HPACCOOLEIRFFF'
    idf.idfobjects['Coil:Cooling:DX:SingleSpeed'][-1].Part_Load_Fraction_Correlation_Curve_Name = 'HPACCOOLPLFFPLR'
    
idf.save()


# ## Add Coil:Heating:Electric

# In[10]:


#add zone thermostat control for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new thermostat control
    idf.newidfobject('Coil:Heating:Electric')
    
    # alter inputs to the newly crated idf object
    idf.idfobjects['Coil:Heating:Electric'][-1].Name = ('Supp Heating Coil_' + newZones[i])
    idf.idfobjects['Coil:Heating:Electric'][-1].Availability_Schedule_Name = 'always_avail'
    idf.idfobjects['Coil:Heating:Electric'][-1].Efficiency = 1
    idf.idfobjects['Coil:Heating:Electric'][-1].Nominal_Capacity = 'autosize'
    idf.idfobjects['Coil:Heating:Electric'][-1].Air_Inlet_Node_Name = ('Supp Heating Coil Air Inlet Node_' + newZones[i])
    idf.idfobjects['Coil:Heating:Electric'][-1].Air_Outlet_Node_Name = ('Air Loop Outlet Node_' + newZones[i])
    
idf.save()


# ## Add AirLoopHVAC:UnitaryHeatPump:AirToAir 

# In[11]:


#add zone thermostat control for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new thermostat control
    idf.newidfobject('AirLoopHVAC:UnitaryHeatPump:AirToAir')

    # alter inputs to the newly crated idf object
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Name = ('Heat Pump_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Availability_Schedule_Name = 'always_avail'
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Air_Inlet_Node_Name = ('Air Loop Inlet node_' + newZones[i]) # added in air loop
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Air_Outlet_Node_Name = ('Air Loop Outlet node_' + newZones[i]) # added in air loop
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Cooling_Supply_Air_Flow_Rate = 'autosize'
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Heating_Supply_Air_Flow_Rate = 'autosize'
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].No_Load_Supply_Air_Flow_Rate = 0
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Controlling_Zone_or_Thermostat_Location = newZones[i]
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Supply_Air_Fan_Object_Type = 'Fan:OnOff'
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Supply_Air_Fan_Name = ('Supply Fan_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Heating_Coil_Object_Type = 'Coil:Heating:DX:SingleSpeed' # needs add
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Heating_Coil_Name = ('Main DX Heating Coil_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Cooling_Coil_Object_Type = 'Coil:Cooling:DX:SingleSpeed' #needs add
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Cooling_Coil_Name = ('Dx Cooling Coil_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Supplemental_Heating_Coil_Object_Type = 'Coil:Heating:Electric' # needs add
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Supplemental_Heating_Coil_Name = ('Supp Heating Coil_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Maximum_Supply_Air_Temperature_from_Supplemental_Heater = 50
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Maximum_Outdoor_DryBulb_Temperature_for_Supplemental_Heater_Operation = 10
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Fan_Placement = 'BlowThrough'
    idf.idfobjects['AirLoopHVAC:UnitaryHeatPump:AirToAir'][-1].Supply_Air_Fan_Operating_Mode_Schedule_Name = 'fan_cycle'

idf.save()


# ## Add AirTerminal:SingleDuct:Uncontrolled

# In[12]:


#add zone thermostat control for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new thermostat control
    idf.newidfobject('AirTerminal:SingleDuct:Uncontrolled')

    # alter inputs to the newly crated idf object
    idf.idfobjects['AirTerminal:SingleDuct:Uncontrolled'][-1].Name = ('ZoneDirectAir_' + newZones[i])
    idf.idfobjects['AirTerminal:SingleDuct:Uncontrolled'][-1].Availability_Schedule_Name = 'always_avail'
    idf.idfobjects['AirTerminal:SingleDuct:Uncontrolled'][-1].Zone_Supply_Air_Node_Name = ('Zone Inlet Node_' + newZones[i])
    idf.idfobjects['AirTerminal:SingleDuct:Uncontrolled'][-1].Maximum_Air_Flow_Rate = ('autosize')


# ## Add ZoneHVAC:EquipmentConnections

# In[13]:


#add zone ZoneHVAC:EquipmentConnections for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new ZoneHVAC:EquipmentConnections
    idf.newidfobject('ZoneHVAC:EquipmentConnections')

    # alter inputs to the newly crated idf object
    idf.idfobjects['ZoneHVAC:EquipmentConnections'][-1].Zone_Name = newZones[i]
    idf.idfobjects['ZoneHVAC:EquipmentConnections'][-1].Zone_Conditioning_Equipment_List_Name = ('ZONEEQUIPMENT_' + newZones[i])
    idf.idfobjects['ZoneHVAC:EquipmentConnections'][-1].Zone_Air_Inlet_Node_or_NodeList_Name = ('zone inlet nodes_' + newZones[i])
    idf.idfobjects['ZoneHVAC:EquipmentConnections'][-1].Zone_Air_Node_Name = ('Zone Node_' + newZones[i])
    idf.idfobjects['ZoneHVAC:EquipmentConnections'][-1].Zone_Return_Air_Node_Name = ('Zone Outlet Node_' + newZones[i])
    
idf.save() 


# ## Add Fan:OnOff

# In[14]:


#add zone Fan:OnOff for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new Fan:OnOff
    idf.newidfobject('Fan:OnOff')

    # alter inputs to the newly crated idf object
    idf.idfobjects['Fan:OnOff'][-1].Name = ('Supply Fan_' + newZones[i])
    idf.idfobjects['Fan:OnOff'][-1].Availability_Schedule_Name = 'always_avail'
    idf.idfobjects['Fan:OnOff'][-1].Fan_Total_Efficiency = 0.377
    idf.idfobjects['Fan:OnOff'][-1].Pressure_Rise = 400
    idf.idfobjects['Fan:OnOff'][-1].Maximum_Flow_Rate = 'autosize'
    idf.idfobjects['Fan:OnOff'][-1].Motor_Efficiency = 0.65
    idf.idfobjects['Fan:OnOff'][-1].Motor_In_Airstream_Fraction = 1
    idf.idfobjects['Fan:OnOff'][-1].Air_Inlet_Node_Name = ('air loop inlet node_' + newZones[i])
    idf.idfobjects['Fan:OnOff'][-1].Air_Outlet_Node_Name = ('cooling coil air inlet node_' + newZones[i])
    idf.idfobjects['Fan:OnOff'][-1].EndUse_Subcategory = 'General'
    
idf.save()


# ## Add ZoneHVAC:EquipmentList

# In[15]:


#add zone thermostat control for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new thermostat control
    idf.newidfobject('ZoneHVAC:EquipmentList')

    # alter inputs to the newly crated idf object
    idf.idfobjects['ZoneHVAC:EquipmentList'][-1].Name = ('ZONEEQUIPMENT_' + newZones[i])
    idf.idfobjects['ZoneHVAC:EquipmentList'][-1].Zone_Equipment_1_Object_Type = 'AirTerminal:SingleDuct:Uncontrolled'
    idf.idfobjects['ZoneHVAC:EquipmentList'][-1].Zone_Equipment_1_Name = ('ZoneDirectAir_' + newZones[i])
    idf.idfobjects['ZoneHVAC:EquipmentList'][-1].Zone_Equipment_1_Cooling_Sequence = 1
    idf.idfobjects['ZoneHVAC:EquipmentList'][-1].Zone_Equipment_1_Heating_or_NoLoad_Sequence = 1


# ## Add AirLoopHVAC 

# In[16]:


#add zone AirLoopHVAC for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new AirLoopHVAC
    idf.newidfobject('AirLoopHVAC')

    # alter inputs to the newly crated idf object
    idf.idfobjects['AirLoopHVAC'][-1].Name = ('Central System_' + newZones[i])
    idf.idfobjects['AirLoopHVAC'][-1].Availability_Manager_List_Name = 'availability list'
    idf.idfobjects['AirLoopHVAC'][-1].Design_Supply_Air_Flow_Rate = 'autosize'
    idf.idfobjects['AirLoopHVAC'][-1].Branch_List_Name = ('Air Loop Branches_' + newZones[i])
    idf.idfobjects['AirLoopHVAC'][-1].Supply_Side_Inlet_Node_Name = ('Air Loop Inlet Node_' + newZones[i])
    idf.idfobjects['AirLoopHVAC'][-1].Demand_Side_Outlet_Node_Name = ('Return Air Mixer Outlet_' + newZones[i])
    idf.idfobjects['AirLoopHVAC'][-1].Demand_Side_Inlet_Node_Names = ('Zone Equipment Inlet Node_' + newZones[i])
    idf.idfobjects['AirLoopHVAC'][-1].Supply_Side_Outlet_Node_Names = ('Air Loop Outlet Node_' + newZones[i])

    
idf.save()


# ## Add AirLoopHVAC:ZoneSplitter

# In[17]:


#add zone AirLoopHVAC:ZoneSplitter for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new AirLoopHVAC:ZoneSplitter
    idf.newidfobject('AirLoopHVAC:ZoneSplitter')

    # alter inputs to the newly crated idf object
    idf.idfobjects['AirLoopHVAC:ZoneSplitter'][-1].Name = ('Zone Supply Air Splitter_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:ZoneSplitter'][-1].Inlet_Node_Name = ('Zone Equipment Inlet Node_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:ZoneSplitter'][-1].Outlet_1_Node_Name = ('Zone Inlet Node_' + newZones[i])
    
idf.save()    


# ## Add AirLoopHVAC:SupplyPath

# In[18]:


#add zone AirLoopHVAC:SupplyPath for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new AirLoopHVAC
    idf.newidfobject('AirLoopHVAC:SupplyPath')

    # alter inputs to the newly crated idf object
    idf.idfobjects['AirLoopHVAC:SupplyPath'][-1].Name = ('SupplyPath_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:SupplyPath'][-1].Supply_Air_Path_Inlet_Node_Name = ('Zone Equipment Inlet Node_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:SupplyPath'][-1].Component_1_Object_Type = 'AirLoopHVAC:ZoneSplitter'
    idf.idfobjects['AirLoopHVAC:SupplyPath'][-1].Component_1_Name = ('Zone Supply Air Splitter_' + newZones[i])

idf.save()


# ## Add AirLoopHVAC:ZoneMixer

# In[19]:


#add zone AirLoopHVAC:ZoneMixer for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new AirLoopHVAC:ZoneMixer
    idf.newidfobject('AirLoopHVAC:ZoneMixer')

    # alter inputs to the newly crated idf object
    idf.idfobjects['AirLoopHVAC:ZoneMixer'][-1].Name = ('Zone Return Air Mixer_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:ZoneMixer'][-1].Outlet_Node_Name = ('Return Air Mixer Outlet_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:ZoneMixer'][-1].Inlet_1_Node_Name = ('Zone Outlet Node_' + newZones[i])
    
idf.save()


# ## Add AirLoopHVAC:ReturnPath

# In[20]:


#add zone AirLoopHVAC:ReturnPath for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new AirLoopHVAC:ReturnPath
    idf.newidfobject('AirLoopHVAC:ReturnPath')

    # alter inputs to the newly crated idf object
    idf.idfobjects['AirLoopHVAC:ReturnPath'][-1].Name = ('ReturnPath_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:ReturnPath'][-1].Return_Air_Path_Outlet_Node_Name = ('Return Air Mixer Outlet_' + newZones[i])
    idf.idfobjects['AirLoopHVAC:ReturnPath'][-1].Component_1_Object_Type = 'AirLoopHVAC:ZoneMixer'
    idf.idfobjects['AirLoopHVAC:ReturnPath'][-1].Component_1_Name = ('Zone Return Air Mixer_' + newZones[i])
    
idf.save()


# ## Add Branch

# In[21]:


#add zone Branch for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new Branch
    idf.newidfobject('Branch')

    # alter inputs to the newly crated idf object
    idf.idfobjects['Branch'][-1].Name = ('Air Loop Main Branch_' + newZones[i])
    idf.idfobjects['Branch'][-1].Component_1_Object_Type = 'AirLoopHVAC:UnitaryHeatPump:AirtoAir'
    idf.idfobjects['Branch'][-1].Component_1_Name = ('Heat Pump_' + newZones[i])
    idf.idfobjects['Branch'][-1].Component_1_Inlet_Node_Name = ('Air Loop Inlet Node_' + newZones[i])
    idf.idfobjects['Branch'][-1].Component_1_Outlet_Node_Name = ('Air Loop Outlet Node_' + newZones[i])
    
idf.save()


# ## Add BranchList

# In[22]:


#add zone BranchList for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new BranchList
    idf.newidfobject('BranchList')

    # alter inputs to the newly crated idf object
    idf.idfobjects['BranchList'][-1].Name = ('Air Loop Branches_' + newZones[i])
    idf.idfobjects['BranchList'][-1].Branch_1_Name = ('Air Loop Main Branch_' + newZones[i])
    
idf.save()


# ## Add NodeList

# In[23]:


#add zone NodeList for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new NodeList
    idf.newidfobject('NodeList')

    # alter inputs to the newly crated idf object
    idf.idfobjects['NodeList'][-1].Name = ('Zone Inlet Nodes_' + newZones[i])
    idf.idfobjects['NodeList'][-1].Node_1_Name = ('Zone Inlet Node_' + newZones[i])
    
idf.save()


# ## Add Zone Control: Thermostats

# In[24]:


#add zone thermostat control for corridors
newZones = ['G Corridor', 'M Corridor', 'T Corridor']

for i in range(0, len(newZones)):
    
    # create a new thermostat control
    idf.newidfobject('ZoneControl:Thermostat')

    # alter inputs to the newly crated idf object
    idf.idfobjects['ZoneControl:Thermostat'][-1].Name = ('Zone Thermostat_' + newZones[i])
    idf.idfobjects['ZoneControl:Thermostat'][-1].Zone_or_ZoneList_Name = newZones[i]
    idf.idfobjects['ZoneControl:Thermostat'][-1].Control_Type_Schedule_Name = 'zone_control_type'
    idf.idfobjects['ZoneControl:Thermostat'][-1].Control_1_Object_Type = 'ThermostatSetpoint:DualSetpoint'
    idf.idfobjects['ZoneControl:Thermostat'][-1].Control_1_Name = 'thermostat_living Dual SP Control'

idf.save()

