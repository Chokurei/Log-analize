# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Wed Oct 26 10:38:21 2016

@author: kaku

##################### mapper code for congression condition ############ 
#input
    # original data: 11 features
        #IMEI,Latitude,Longitude,speed,direaction,acceleration,meter,time(unix),data_source(8,9),time,other
#output
    # filtered features after mapper: 4 features
        #ID,grid_num,time_num,speed
    # grid_idx=lon_idx*30+lat_idx
        #Bangkok coordinate
            #lon_w,lon_e=100.40,100.70
            #lat_s,lat_n=13.60,13.90
            #split into 100x100 grid
    # time_idx 
        #split 1 day(1440min) into interval = 30 min
"""

import sys
import numpy as np
from datetime import datetime 

#Bangkok coordinate
lon_w,lon_e = 100.40,100.70
lat_s,lat_n = 13.60,13.90
#grid_interval
grid_size = 100
grid_interval = (lon_e-lon_w)/grid_size
lon_range = np.linspace(lon_w,lon_e,grid_size)+grid_interval/2
lat_range = np.linspace(lat_s,lat_n,grid_size)+grid_interval/2
#time interval
time_interval = 30 # min
time_range = np.arange(0,24*60,time_interval)+time_interval/2

def get_grid_idx(lon,lat):
    lon=float(lon)
    lat=float(lat)
    #in lon range
    if min(abs(lon-lon_range))<=grid_interval:
        lon_idx = np.argmin(abs(lon-lon_range))
        #in lat range        
        if min(abs(lat-lat_range))<=grid_interval:
            lat_idx = np.argmin(abs(lat-lat_range))
            grid_idx = lon_idx*grid_size+lat_idx
            return grid_idx
        # out of lat range
        else:
            return -1
    #out of lon range
    else:
        return -1

def get_time_idx(time):
    time = datetime.fromtimestamp(time)
    h,m = time.hour, time.minute
    # only use hour and min    
    time = h*60+m
    time_idx = np.argmin(abs(time-time_range))
    return time_idx
    
for line in sys.stdin:
    data = line.strip().split(',')
    try:
        assert len(data) == 11
        lat,lon = data[1],data[2]
        grid_idx = get_grid_idx(lon,lat)
        if grid_idx == -1:
            continue
        else:               
            time = int(data[-4])            
            time_idx = get_time_idx(time)
            print('{0},{1},{2},{3}'.format(data[0],grid_idx,time_idx,data[3]))
        continue
    except:
        continue
        
        
        
        
        
        
        
        
        
        
        
        



