# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:58:05 2019

@author: scott
"""

### PERFORM MULTI-VAR LINEAR REGRESSION
# import packages
from inputoutput_data import inputoutput

import numpy as np
import statsmodels.api as sm
import sys 


# filepath to save text files
path = 'C:\\Users\\scott\\github\\DOE_LRMF\\Plotting\\EnergyUseAnalysis\\regressions\\'

# gather data from results
df = inputoutput()

# inputs
ra = 'Regression Analysis - '

# leave out SHGC because not enough surveys actually included it.   
runs = {'All Variables':['unitCOP', 'dhwType', 'dhwEff', 'unitLPD', 
                         'wallU', 'ceilingU', 'slabU', 'windowU'], 
        'Mechanical':['unitCOP', 'dhwType', 'dhwEff'], 
        'Constructions':['wallU', 'ceilingU', 'slabU', 'windowU', 'SHGC'],
        'All Variables2':['unitCOP', 'dhwType', 'dhwEff', 
                          'ceilingU', 'SHGC'], 
        'Mechanical2':['unitCOP', 'dhwType'], 
        'Constructions2':['ceilingU', 'SHGC']}

keys = ['All Variables','Mechanical','Constructions',
        'All Variables2','Mechanical2','Constructions2']

for i in range(0, len(keys)):
    key = keys[i]

    # saving txt exports
    stdoutOrigin=sys.stdout 
    sys.stdout = open(path + key + ".txt", "w")
    
    print('The variables used in this regression are:')
    for i in range (0, len(runs[key])):
        print(runs[key][i])
    
    covars = df['All States'][runs[key]]
    energy = df['All States']['eui']
    
    rng = [(max(x) - min(x)) for x in covars] # calculate range for each covar
    var = []
    
    for i in range(0, len(energy)):
        # regression on mech systems
        var.append([x[i] for x in covars])
        
        
    x = np.array(var)
    y = np.array(energy)
    
    x, y = np.array(x), np.array(y)
    
    # run regression
    model = sm.OLS(y,x)
    results = model.fit()
    
    # parse results
    coef = results.params # COEF
    std_err = results.bse # STD ERROR
    norm_coef = coef * rng
    
    # print results
    print(results.summary())
    
    print()
    print('Normalized Coefficients')
    print(norm_coef)
    
    
    sys.stdout.close()
    sys.stdout=stdoutOrigin