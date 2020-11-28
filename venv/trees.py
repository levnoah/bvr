#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:42:29 2020

@author: rachlin
"""

#%%  Where are the trees in Boston?

import json
import numpy as np
import matplotlib.pyplot as plt


with open('datasets/trees.geojson', 'r') as trees_file:
    trees = json.load(trees_file)
    
# Spyder will crash if we try to pretty-print this data!



#%%

def map_to_array(coords, bndry, size=(1000,1000)):
    """ Map gps (lon,lat) coordinates to
    array coordinates based on the bounderies given as 
    (minlon, minlat, maxlon, maxlat) and the size 
    (height, width) of the array. Return array coordinates. """
    lon,lat = coords
    minlon, minlat, maxlon, maxlat = bndry
    height,width = size
    i = height - (lat - minlat) / (maxlat - minlat) * height
    j = (lon - minlon) / (maxlon - minlon) * width 
    return (int(i),int(j))
 
    
#%%
    
# (minlon, minlat, maxlon, maxlat)    
boston = (-71.2, 42.2, -70.9, 42.4 )
northeastern = (-71.12, 42.32, -71.05, 42.36)



#%% Now we plot the trees!


shape = (1000,1000)
arr = np.zeros(shape=shape)

for f in trees['features']:
    gps = tuple(f['geometry']['coordinates'])
    i,j = map_to_array(gps, boston, shape)
    if i>0 and i<shape[0] and j>0 and j<shape[1]:
        arr[i][j] = 1

plt.figure(figsize=(10,10))
plt.grid()
plt.imshow(arr, cmap='viridis')
plt.show()