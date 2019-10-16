# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:23:47 2019

@author: scott
"""

import math
import pandas as pd

from functions_constructions import(floorCond, 
                                    extWallCond, 
                                    ceilingCond, 
                                    slabCond, 
                                    windowU, 
                                    bsmtWallCond)

### EXTERIOR WALL ###

s0 = 0.005
s1 = 0.2
inc = 0.005

rows = int(math.ceil((s1-s0)/inc))

extWallU_siu = []
extWallU_ipu = []

for i in range(0, rows):
    val = extWallCond([s0 + inc*i],'')[0]
    extWallU_ipu.append(round(s0 + inc*i,3)) 
    extWallU_siu.append(round(val,3))
     

# create dataframe
extWallU = pd.DataFrame()
# store values in dataframe
extWallU['extWallU_siu']=extWallU_siu
extWallU['extWallU_ipu']=extWallU_ipu
# export to csv
extWallU.to_csv('MeasureAnalysis//extWallU.csv')


### CEILING ###

s0 = 0.005
s1 = 0.1
inc = 0.005

rows = int(math.ceil((s1-s0)/inc))

ceilingU_siu = []
ceilingU_ipu = []

for i in range(0, rows):
    val = ceilingCond([s0 + inc*i],'')[0]
    ceilingU_ipu.append(round(s0 + inc*i,3)) 
    ceilingU_siu.append(round(val,3))

#create dataframe
ceilingU = pd.DataFrame()
# store values in dataframe
ceilingU['ceilingU_siu']=ceilingU_siu
ceilingU['ceilingU_ipu']=ceilingU_ipu
#export csv
ceilingU.to_csv('MeasureAnalysis//ceilingU.csv')


### Foundation ###

s0 = 0.1
s1 = 1.0
inc = 0.05

start = slabCond('', [s0], '')[0]
end = slabCond('', [s1], '')[0]
rows = int(math.ceil((s1-s0)/inc))

slabU_siu = []
slabF_ipu = []

for i in range(0, rows):
    val = slabCond('', [s0 + inc*i], '')[0]
    slabF_ipu.append(round(s0 + inc*i,3)) 
    slabU_siu.append(round(val,3))

    
#create dataframe
slabU = pd.DataFrame()
# store values in dataframe
slabU['slabU_siu']=slabU_siu
slabU['slabF_ipu']=slabF_ipu
#export csv
slabU.to_csv('MeasureAnalysis//slabU.csv')


### WINDOW U ###

s0 = 0.1
s1 = 1.0
inc = 0.05

rows = int(math.ceil((s1-s0)/inc))

windowU_siu = []
windowU_ipu = []

for i in range(0, rows):
    val = windowU([s0 + inc*i], '', '')[0]
    windowU_ipu.append(round(s0 + inc*i,3))
    windowU_siu.append(round(val,3))

#create dataframe
windowU = pd.DataFrame()
# store values in dataframe
windowU['windowU_siu']=windowU_siu
windowU['windowU_ipu']=windowU_ipu
#export csv
windowU.to_csv('MeasureAnalysis//windowU.csv')

### BASEMENT WALL ###

s0 = 0.01
s1 = 0.15
inc = 0.005

rows = int(math.ceil((s1-s0)/inc))

bsmtWallU_siu = []
bsmtWallU_ipu = []

for i in range(0, rows):
    val = bsmtWallCond([s0 + inc*i],'')[0]
    bsmtWallU_ipu.append(round(s0 + inc*i,3)) 
    bsmtWallU_siu.append(round(val,3))
 

    
#create dataframe
bsmtWallU = pd.DataFrame()
# store values in dataframe
bsmtWallU['bsmtWallU_siu']=bsmtWallU_siu
bsmtWallU['bsmtWallU_ipu']=bsmtWallU_ipu
#export csv
bsmtWallU.to_csv('MeasureAnalysis//bsmtWallU.csv')

### FLOOR ###

s0 = 0.01
s1 = 0.6
inc = 0.05

rows = int(math.ceil((s1-s0)/inc))

floorU_siu = []
floorU_ipu = []

for i in range(0, rows):
    val = floorCond([s0 + inc*i],'')[0]
    floorU_ipu.append(round(s0 + inc*i,3)) 
    floorU_siu.append(round(val,3))

    
#create dataframe
floorU = pd.DataFrame()
# store values in dataframe
floorU['floorU_siu']=floorU_siu
floorU['floorU_ipu']=floorU_ipu
#export csv
floorU.to_csv('MeasureAnalysis//floorU.csv')
