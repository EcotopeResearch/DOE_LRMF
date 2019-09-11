# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:24:46 2019

@author: scott
"""

# SWITCHER FUNCTIONS #

# heating curves

heating_cop = {'elecres':1, 'gasfurnace':0.8, 'hydronic baseboard (gas boiler)':0.75,'PTHP':2.5,
               'Split system HP':2.5,'water source HP':0.8,'water source HP (gas boiler)':0.7, 0:1000}

curve_heatCapFT = {'elecres':'ConstantCubic', 'gasfurnace':'ConstantCubic', 'hydronic baseboard (gas boiler)':'ConstantCubic','PTHP':'HPACHeatCapFT',
                   'Split system HP':'HPACHeatCapFT','water source HP':'ConstantCubic','water source HP (gas boiler)':'ConstantCubic', 0:'ConstantCubic'}

curve_HeatCapFFF = {'elecres':'ConstantCubic', 'gasfurnace':'ConstantCubic', 'hydronic baseboard (gas boiler)':'ConstantCubic','PTHP':'HPACHeatCapFFF',
                   'Split system HP':'HPACHeatCapFFF','water source HP':'ConstantCubic','water source HP (gas boiler)':'ConstantCubic', 0:'ConstantCubic'}

curve_HPACHeatEIRFT = {'elecres':'ConstantCubic', 'gasfurnace':'ConstantCubic', 'hydronic baseboard (gas boiler)':'ConstantCubic','PTHP':'HPACHeatEIRFT',
                   'Split system HP':'HPACHeatEIRFT','water source HP':'ConstantCubic','water source HP (gas boiler)':'ConstantCubic', 0:'ConstantCubic'}

curve_HPACHeatEIRFFF = {'elecres':'ConstantCubic', 'gasfurnace':'ConstantCubic', 'hydronic baseboard (gas boiler)':'ConstantCubic','PTHP':'HPACHeatEIRFFF',
                   'Split system HP':'HPACHeatEIRFFF','water source HP':'ConstantCubic','water source HP (gas boiler)':'ConstantCubic', 0:'ConstantCubic'}

def heat_cop_switcher(argument):
    switcher = heating_cop
    var = switcher.get(argument, "InvalidEquipmentType")
    
    if var == "InvalidEquipmentType":
        print("WARNING InvalidEquipmentType")
        var = 1
    
    return(var)

def curve_heatCapFT_switcher(argument):
    switcher = curve_heatCapFT
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'ConstantCubic'
    
    return(var)
    
def curve_HeatCapFFF_switcher(argument):
    switcher = curve_HeatCapFFF
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'ConstantCubic'
    
    return(var)
    
def curve_HPACHeatEIRFT_switcher(argument):
    switcher = curve_HPACHeatEIRFT
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'ConstantCubic'
    
    return(var)
    
def curve_HPACHeatEIRFFF_switcher(argument):
    switcher = curve_HPACHeatEIRFFF
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'ConstantCubic'
    
    return(var)
    
# cooling curves

cooling_cop = {'PTHP':2.5, 'Split system HP':2.5, 'Split system AC':2, 'PTAC':2, 'water source HP':1.8, 'Win AC':2, 0:1000}

curve_coolCapFT = {'PTHP':'HPACcoolCapFT', 'Split system HP':'HPACcoolCapFT', 'Split system AC':'HPACcoolCapFT',
                   'water source HP':'HPACcoolCapFT','Win AC':'HPACcoolCapFT', 'PTAC':'HPACcoolCapFT', 0:'HPACcoolCapFT'}

curve_coolCapFFF = {'PTHP':'HPACcoolCapFFF', 'Split system HP':'HPACcoolCapFFF', 'Split system AC':'HPACcoolCapFFF',
                   'water source HP':'HPACcoolCapFFF','Win AC':'HPACcoolCapFFF', 'PTAC':'HPACcoolCapFFF',  0:'HPACcoolCapFFF'}

curve_HPACcoolEIRFT = {'PTHP':'HPACCOOLEIRFT', 'Split system HP':'HPACCOOLEIRFT', 'Split system AC':'HPACCOOLEIRFT',
                   'water source HP':'HPACCOOLEIRFT','Win AC':'HPACCOOLEIRFT', 'PTAC':'HPACCOOLEIRFT',  0:'HPACCOOLEIRFT'}

curve_HPACcoolEIRFFF = {'PTHP':'HPACcoolEIRFFF', 'Split system HP':'HPACcoolEIRFFF', 'Split system AC':'HPACcoolEIRFFF',
                   'water source HP':'HPACcoolEIRFFF','Win AC':'HPACcoolEIRFFF', 'PTAC':'HPACcoolEIRFFF',  0:'HPACcoolEIRFFF'}

def cool_cop_switcher(argument):
    switcher = cooling_cop
    var = switcher.get(argument, "InvalidEquipmentType")
    
    if var == "InvalidEquipmentType":
        print("WARNING InvalidEquipmentType")
        var = 1
    
    return(var)

def curve_coolCapFT_switcher(argument):
    switcher = curve_coolCapFT
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'HPACcoolCapFT'
    
    return(var)
    
def curve_coolCapFFF_switcher(argument):
    switcher = curve_coolCapFFF
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'HPACcoolCapFFF'
    
    return(var)
    
def curve_HPACcoolEIRFT_switcher(argument):
    switcher = curve_HPACcoolEIRFT
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'HPACCOOLEIRFT'
    
    return(var)
    
def curve_HPACcoolEIRFFF_switcher(argument):
    switcher = curve_HPACcoolEIRFFF
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'HPACcoolEIRFFF'
    
    return(var)

# Part Load Corrilation and defrost

curve_HPACCOOLPLFFPLR = {'elecres':'ConstantCubic', 'gasfurnace':'ConstantCubic', 'hydronic baseboard (gas boiler)':'ConstantCubic',
                         'PTHP':'HPACCOOLPLFFPLR','Split system HP':'HPACCOOLPLFFPLR','water source HP':'HPACCOOLPLFFPLR',
                         'water source HP (gas boiler)':'ConstantCubic','Split system AC':'HPACCOOLPLFFPLR',
                         'Win AC':'HPACCOOLPLFFPLR', 'PTAC':'HPACCOOLPLFFPLR',  0:'HPACCOOLPLFFPLR'}

curve_Defrost_EIR_FT = {'elecres':'Defrost_EIR_FT', 'gasfurnace':'Defrost_EIR_FT', 'hydronic baseboard (gas boiler)':'Defrost_EIR_FT','PTHP':'Defrost_EIR_FT',
                   'Split system HP':'Defrost_EIR_FT','water source HP':'Defrost_EIR_FT','water source HP (gas boiler)':'Defrost_EIR_FT', 0:'Defrost_EIR_FT'}
    
def curve_HPACCOOLPLFFPLR_switcher(argument):
    switcher = curve_HPACCOOLPLFFPLR
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'HPACCOOLPLFFPLR'
    
    return(var)

    
def curve_Defrost_EIR_FT_switcher(argument):
    switcher = curve_Defrost_EIR_FT
    var = switcher.get(argument, "InvalidCurveType")
    
    if var == "InvalidCurveType":
        print("WARNING InvalidCurveType")
        var = 'HPACDefrost_EIR_FT'
    
    return(var)