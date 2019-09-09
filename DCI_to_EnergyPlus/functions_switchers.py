# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:24:46 2019

@author: scott
"""

# SWITCHER FUNCTIONS #

# heating curves

heating_cop = {'elecres':1, 'gasfurnace':0.8, 'hydronic baseboard (gas boiler)':0.75,'PTHP':2.5,
               'Split system HP':2.5,'water source HP':2.5,'water source HP (gas boiler)':0.7, 0:'No Heating'}

curve_heatCapFT = {'elecres':'flatHeatCapFT', 'gasfurnace':'flatHeatCapFT', 'hydronic baseboard (gas boiler)':'flatHeatCapFT','PTHP':'HPACHeatCapFT',
                   'Split system HP':'HPACHeatCapFT','water source HP':'HPACHeatCapFT','water source HP (gas boiler)':'HPACHeatCapFT', 0:'No Heating'}

curve_HeatCapFFF = {'elecres':'flatHeatCapFFF', 'gasfurnace':'flatHeatCapFFF', 'hydronic baseboard (gas boiler)':'flatHeatCapFFF','PTHP':'HPACHeatCapFFF',
                   'Split system HP':'HPACHeatCapFFF','water source HP':'HPACHeatCapFFF','water source HP (gas boiler)':'HPACHeatCapFFF', 0:'No Heating'}

curve_HPACHeatEIRFT = {'elecres':'flatHPACHeatEIRFT', 'gasfurnace':'flatHPACHeatEIRFT', 'hydronic baseboard (gas boiler)':'flatHPACHeatEIRFT','PTHP':'HPACHPACHeatEIRFT',
                   'Split system HP':'HPACHPACHeatEIRFT','water source HP':'HPACHPACHeatEIRFT','water source HP (gas boiler)':'HPACHPACHeatEIRFT', 0:'No Heating'}

curve_HPACHeatEIRFFF = {'elecres':'flatHPACHeatEIRFFF', 'gasfurnace':'flatHPACHeatEIRFFF', 'hydronic baseboard (gas boiler)':'flatHPACHeatEIRFFF','PTHP':'HPACHPACHeatEIRFFF',
                   'Split system HP':'HPACHPACHeatEIRFFF','water source HP':'HPACHPACHeatEIRFFF','water source HP (gas boiler)':'HPACHPACHeatEIRFFF', 0:'No Heating'}

def heat_cop_switcher(argument):
    switcher = heating_cop
    return(switcher.get(argument, "Invalid Equipment Type"))

def curve_heatCapFT_switcher(argument):
    switcher = curve_heatCapFT
    return(switcher.get(argument, "Invalid Curve Type"))
    
def curve_HeatCapFFF_switcher(argument):
    switcher = curve_HeatCapFFF
    return(switcher.get(argument, "Invalid Curve Type"))
    
def curve_HPACHeatEIRFT_switcher(argument):
    switcher = curve_HPACHeatEIRFT
    return(switcher.get(argument, "Invalid Curve Type"))
    
def curve_HPACHeatEIRFFF_switcher(argument):
    switcher = curve_HPACHeatEIRFFF
    return(switcher.get(argument, "Invalid Curve Type"))
    
# cooling curves

cooling_cop = {'PTHP':2.5, 'Split system HP':2.5, 'Split system AC':2, 'PTAC':2, 'water source HP':1.2, 'Win AC':2, 0:'No Cooling'}

curve_coolCapFT = {'PTHP':'HPACcoolCapFT', 'Split system HP':'HPACcoolCapFT', 'Split system AC':'HPACcoolCapFT',
                   'water source HP':'HPACcoolCapFT','Win AC':'HPACcoolCapFT', 'PTAC':'HPACcoolCapFT', 0:'No Cooling'}

curve_coolCapFFF = {'PTHP':'HPACcoolCapFFF', 'Split system HP':'HPACcoolCapFFF', 'Split system AC':'HPACcoolCapFFF',
                   'water source HP':'HPACcoolCapFFF','Win AC':'HPACcoolCapFFF', 'PTAC':'HPACcoolCapFFF',  0:'No Cooling'}

curve_HPACcoolEIRFT = {'PTHP':'HPACHPACcoolEIRFT', 'Split system HP':'HPACHPACcoolEIRFT', 'Split system AC':'HPACHPACcoolEIRFT',
                   'water source HP':'HPACHPACcoolEIRFT','Win AC':'HPACHPACcoolEIRFT', 'PTAC':'HPACHPACcoolEIRFT',  0:'No Cooling'}

curve_HPACcoolEIRFFF = {'PTHP':'HPACHPACcoolEIRFFF', 'Split system HP':'HPACHPACcoolEIRFFF', 'Split system AC':'HPACHPACcoolEIRFFF',
                   'water source HP':'HPACHPACcoolEIRFFF','Win AC':'HPACHPACcoolEIRFFF', 'PTAC':'HPACHPACcoolEIRFFF',  0:'No Cooling'}

def cool_cop_switcher(argument):
    switcher = cooling_cop
    return(switcher.get(argument, "Invalid Equipment Type"))

def curve_coolCapFT_switcher(argument):
    switcher = curve_coolCapFT
    return(switcher.get(argument, "Invalid Curve Type"))
    
def curve_coolCapFFF_switcher(argument):
    switcher = curve_coolCapFFF
    return(switcher.get(argument, "Invalid Curve Type"))
    
def curve_HPACcoolEIRFT_switcher(argument):
    switcher = curve_HPACcoolEIRFT
    return(switcher.get(argument, "Invalid Curve Type"))
    
def curve_HPACcoolEIRFFF_switcher(argument):
    switcher = curve_HPACcoolEIRFFF
    return(switcher.get(argument, "Invalid Curve Type"))

# Part Load Corrilation and defrost

curve_HPACCOOLPLFFPLR = {'elecres':'flatHPACCOOLPLFFPLR', 'gasfurnace':'flatHPACCOOLPLFFPLR', 'hydronic baseboard (gas boiler)':'flatHPACCOOLPLFFPLR',
                         'PTHP':'HPACHPACCOOLPLFFPLR','Split system HP':'HPACHPACCOOLPLFFPLR','water source HP':'HPACHPACCOOLPLFFPLR',
                         'water source HP (gas boiler)':'HPACHPACCOOLPLFFPLR','Split system AC':'HPACHPACCOOLPLFFPLR',
                         'Win AC':'HPACHPACCOOLPLFFPLR', 'PTAC':'HPACHPACCOOLPLFFPLR',  0:'No Cooling/Heating'}

curve_Defrost_EIR_FT = {'elecres':'flatDefrost_EIR_FT', 'gasfurnace':'flatDefrost_EIR_FT', 'hydronic baseboard (gas boiler)':'flatDefrost_EIR_FT','PTHP':'HPACDefrost_EIR_FT',
                   'Split system HP':'HPACDefrost_EIR_FT','water source HP':'HPACDefrost_EIR_FT','water source HP (gas boiler)':'HPACDefrost_EIR_FT', 0:'No Heating'}
    
def curve_HPACCOOLPLFFPLR_switcher(argument):
    switcher = curve_HPACCOOLPLFFPLR
    return(switcher.get(argument, "Invalid Curve Type"))
    
def curve_Defrost_EIR_FT_switcher(argument):
    switcher = curve_Defrost_EIR_FT
    return(switcher.get(argument, "Invalid Curve Type"))