# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:23:47 2019

@author: scott
"""

from functions_constructions import(floorCond, 
                                    extWallCond, 
                                    ceilingCond, 
                                    slabCond, 
                                    windowU, 
                                    bsmtWallCond)

# exterior wall

s0 = 0.057
s1 = 0.2
inc = 0.01

start = extWallCond([s0], '')[0]
end = extWallCond([s1], '')[0]
rows = ((s1-s0)/inc)
length = (end - start)/rows

print('Ext. Wall')
print(start)
print(end)
print(rows)
print(length)
print()

# ceiling insulation

s0 = 0.026
s1 = 0.2
inc = 0.01

start = ceilingCond([s0], '')[0]
end = ceilingCond([s1], '')[0]
rows = ((s1-s0)/inc)
length = (end - start)/rows

print('Ceiling Wall')
print(start)
print(end)
print(rows)
print(length)
print()

# slab insulation slabCond(fndWtmnU, FndWtmnF, st)

s0 = 0.54
s1 = 0.7
inc = 0.05

start = slabCond('', [s0], '')[0]
end = slabCond('', [s1], '')[0]
rows = ((s1-s0)/inc)
length = (end - start)/rows

print('Slab')
print(start)
print(end)
print(rows)
print(length)
print()

# WindowU

s0 = 0.1
s1 = 1.6
inc = 0.05

start = windowU([s0], '', '')[0]
end = windowU([s1], '', '')[0]
rows = ((s1-s0)/inc)
length = (end - start)/rows

print('WindowU')
print(start)
print(end)
print(rows)
print(length)
print()

# basement wall

s0 = 0.01
s1 = 0.5
inc = 0.05

start = bsmtWallCond([s0], '')[0]
end = bsmtWallCond([s1], '')[0]
rows = ((s1-s0)/inc)
length = (end - start)/rows

print('Basement Wall')
print(start)
print(end)
print(rows)
print(length)
print()

# floor insulation

s0 = 0.01
s1 = 0.2
inc = 0.05

start = floorCond([s0], '')[0]
end = floorCond([s1], '')[0]
rows = ((s1-s0)/inc)
length = (end - start)/rows

print('Floor')
print(start)
print(end)
print(rows)
print(length)
print()
