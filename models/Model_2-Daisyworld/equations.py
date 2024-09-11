#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:25:35 2024

@author: jason
"""

import numpy as np
from matplotlib import pyplot as plt

#%% Temperature
alpha = np.linspace(0, 1, 101, endpoint=True)
I = np.linspace(550, 1650, 5, endpoint=True) # [W/m^2]

sigma = 5.6704e-8 # stefan-boltzmann constant
color_index = np.linspace(0, 1, len(I), endpoint=True)

for j in np.arange(0,len(I)):
    T = (I[j]*(1-alpha)/sigma)**0.25
    
    plt.plot(alpha, T-273.15, color=plt.cm.viridis(color_index[j]))

plt.ylabel('Temperature [$^\circ$C]')
plt.xlabel('Albedo')


#%% Growth rate
Tw = np.linspace(0, 50, 1001, endpoint=True)+273.15 # temperature [K]

Au = np.linspace(0, 1, 5, endpoint=True) # uncovered area

T0 = 273.15+22.5 # optimal temperature [K]

plt.figure()
for j in np.arange(0,len(Au)):
    gw = Au[j]*(1 - 0.003265*(T0-Tw)**2)

    gw[gw<0] = 0

    plt.plot(Tw-273.15, gw, color=plt.cm.viridis(Au[j]))

plt.ylabel('Growth rate [%]')
plt.xlabel('Temperature [$^\circ$C]')