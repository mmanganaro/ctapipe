#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
plot atmo trans table

@author: Johan Bregeon
"""

# @TODO plot wavelenght line in RGB colors
# * https://stackoverflow.com/questions/44959955/matplotlib-color-under-curve-based-on-spectral-color
# * make similar to ctapipe/tools/plot_charge_resolution.py
#

from traitlets import Unicode
from ctapipe.utils import get_dataset
from matplotlib import pyplot as plt
from ctapipe.atmosphere.atmo_trans import readAtmoTrans

# JB - doesn't understand traitlets...
# set CTAPIPE_SVC_PATH to a path containing the file below
#input_path = Unicode(get_dataset('atm_trans_2150_1_10_0_0_2150.dat'), allow_none=True,
#                     help='Path to the atmospheric profile file, e.g.'
#                          'atm_trans_2150_1_10_0_0_2150.dat').tag(config=True)

input_path = get_dataset('atm_trans_2150_1_10_0_0_2150.dat')
header, obs_alt, altitudes, opt_depth, extinction =\
        readAtmoTrans(input_path)

fig = plt.figure(figsize=(20, 8))
ax  = fig.add_subplot(111)
#ax_l = self.fig.add_subplot(121)
#ax_r = self.fig.add_subplot(122)

# plot 2 reference wave lengths

wl355, = ax.plot(altitudes,opt_depth[355], color='blue')
wl532, = ax.plot(altitudes,opt_depth[532], color='green')
legend_handles = [wl355, wl532]
legend_labels = ["355", "532"]

# scan wave lengths
for wl in range(200, 999, 50):
    print(wl)
    leg, = ax.plot(altitudes,opt_depth[wl], lw=0.75, ls='--')
    legend_handles.append(leg)
    legend_labels.append(str(wl))
    

plt.title('Atmospheric Transmission Table')
ax.set_xlabel("Altitudes")
ax.set_xbound(0, 20000)
ax.set_ylabel("Optical Depth")
ax.set_ybound(0, 1)

ax.legend(legend_handles, legend_labels,
          bbox_to_anchor=(1.02, 1.), loc=2,
          borderaxespad=0., fontsize=10)
plt.show()