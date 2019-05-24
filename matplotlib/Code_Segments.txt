#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<Description>

Created on Thu Oct 18 15:09:37 2018
@author: Richard Boyne rmb115@ic.ac.uk
"""

# %%

import matplotlib as mpl
import matplotlib.pyplot as plt

# %%

# close and clear all
plt.clf()
plt.close('all')

# %%

# set matplotlib preferences - report
mpl.rcdefaults()
plt.rc('axes', titlesize=20, labelsize=20)
plt.rc('axes.formatter', limits=[-4, 4])
plt.rc('ytick', labelsize=15)
plt.rc('xtick', labelsize=15)
plt.rc('lines', linewidth=2, markersize=7)
plt.rc('figure', figsize=(9, 9))
# print(plt.rcParams) # all parameters

# %%

## simple example plot
#fig, ax = plt.subplots()
#ax.plot(x, func_1(x), 'r-', label='y(t)')
#ax.set(xlabel='time (s)', ylabel='height (m)')
#
## 3d example plot
#fig1 = plt.figure('*******')
#ax1 = fig1.add_subplot(111, projection='3d')
#
#ax1.scatter( surv['reprod_threash'], surv['reprod_number'], surv['grow_percent'],
#		   c = 'b', marker = 'o' , label = 'Survived' )
#ax1.scatter( died['reprod_threash'], died['reprod_number'], died['grow_percent'],
#		   c = 'r',marker = 'o', label =  'Died')
#
#ax1.legend()
#ax1.set( xlabel = 'reprod_threash', ylabel = 'reprod_number', zlabel = 'grow_percent' )
#fig1.suptitle('Agent Parameter Space')