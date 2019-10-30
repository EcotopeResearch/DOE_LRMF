# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:08:12 2019

@author: scott
"""

import plotly.graph_objects as go
from inputoutput_data import inputoutput

# print path
path = "C:\\Users\\scott\\github\\DOE_LRMF\\Plotting\\EnergyUseAnalysis\\barPlots\\"

# gather data from results
df = inputoutput()

# lists
cz = ['All States', 'IL4A', 'WA4C', 'OR4C', 'IL5A', 'WA5B', 'OR5B', 'MN6A', 'MN7A']
states = {'Washington':['WA4C','WA5B'], 'Oregon':['OR4C','OR5B'], 'Illinois':['IL4A','IL5A'], 'Minnesota':['MN6A', 'MN7A']} 

# loop through climate zones

for i in  range(0, len(cz)):

    labels = df[cz[i]]['names']
    
    # lighting
    intLtg = df[cz[i]]['intLtg'] # interior lighting
    extLtg = df[cz[i]]['extLtg'] # exterior lighting
    ltg = intLtg + extLtg
    
    # appliances
    appl = df[cz[i]]['appl'] # appliances
    intEq = df[cz[i]]['intEq'] # interior equipment
    eqp = appl + intEq
    
    
    # hot water
    wtrht = df[cz[i]]['wtrht'] # water heating
    
    # fans and ventilation
    vent = df[cz[i]]['vent'] # ventilation
    fans = df[cz[i]]['fans'] # fans
    fanVent = vent + fans
    
    # hvac equipment
    cool = df[cz[i]]['cool'] # space cooling
    heat = df[cz[i]]['heat'] # space heating
    
    
    x = labels
    
    # columns
    fig = go.Figure(go.Bar(x =x, y=ltg, name='Lighting'))
    fig = go.Figure(go.Bar(x =x, y=eqp, name='Appliances and Equipment'))
    fig.add_trace(go.Bar(x=x, y=wtrht, name='Hot Water'))
    fig.add_trace(go.Bar(x=x, y=fanVent, name='Fans and Ventilation'))
    fig.add_trace(go.Bar(x=x, y=cool, name='Cooling'))
    fig.add_trace(go.Bar(x=x, y=heat, name='Heating'))
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
    
    # for 
    #plotly.offline.plot(fig)
    
    # print
    fig.write_image(path + cz[i] + ".jpeg")
    fig.write_html(path + cz[i] + ".html")

for state in states:
    czs = states[state]

    labels = df[czs[0]]['names']
    labels.extend(df[czs[1]]['names'])
    print(labels)
    
    # lighting
    intLtg = df[czs[0]]['intLtg']
    intLtg.extend(df[czs[1]]['intLtg']) # interior lighting
    extLtg = df[czs[0]]['extLtg']
    extLtg.extend(df[czs[1]]['extLtg']) # exterior lighting
    ltg = intLtg + extLtg
    
    # appliances
    appl = df[czs[0]]['appl']
    appl.extend(df[czs[1]]['appl']) # appliances
    intEq = df[czs[0]]['intEq']
    intEq.extend(df[czs[1]]['intEq']) # interior equipment
    eqp = appl + intEq
    
    
    # hot water
    wtrht = df[cz[0]]['wtrht']
    wtrht.extend(df[cz[1]]['wtrht']) # water heating
    
    # fans and ventilation
    vent = df[cz[0]]['vent']
    vent.extend(df[cz[1]]['vent']) # ventilation
    fans = df[cz[0]]['fans']
    fans.extend(df[cz[1]]['fans']) # fans
    fanVent = vent + fans
    
    # hvac equipment
    cool = df[cz[0]]['cool']
    cool.extend(df[cz[1]]['cool']) # space cooling
    heat = df[cz[0]]['heat']
    heat.extend(df[cz[1]]['heat']) # space heating
    
    
    x = labels
    
    # columns
    fig = go.Figure(go.Bar(x =x, y=ltg, name='Lighting'))
    fig = go.Figure(go.Bar(x =x, y=eqp, name='Appliances and Equipment'))
    fig.add_trace(go.Bar(x=x, y=wtrht, name='Hot Water'))
    fig.add_trace(go.Bar(x=x, y=fanVent, name='Fans and Ventilation'))
    fig.add_trace(go.Bar(x=x, y=cool, name='Cooling'))
    fig.add_trace(go.Bar(x=x, y=heat, name='Heating'))
    
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
    
    # for 
    #plotly.offline.plot(fig)
    
    # print
    fig.write_image(path + state + ".jpeg")
    fig.write_html(path + state + ".html")
