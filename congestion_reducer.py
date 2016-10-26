# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Wed Oct 26 13:32:10 2016

@author: kaku
###################### reducer code for congression condition #######################
# input data
    # origianl data: get from mapper: 4 features
        #ID,grid_num,time_num,speed
# output
    # average speed matrix
        # size: 48 x 10000
        # rows: grid index
        # col: time index
        # value: average speed 
"""

import sys
import numpy as np

all_aver_speed = []
time_interval = 30 # min
time_range = np.arange(0,24*60,time_interval)+time_interval/2
lon_range = 100 # 100 x 100 grids


#file = open('/home/kaku/Desktop/trail/grid_time_idex.csv')
##sys.stdin = open('/home/kaku/Desktop/trail/grid_time_idex.csv')
for time_idx in range(0,len(time_range)):
    one_avg_speed = np.empty(1,lon_range**2).reshape(lon_range**2)
    for grid_idx in range(0,lon_range**2):
        number = 0
        speed_add = 0
        for line in sys.stdin:
            data = line.strip().split(',')
            if eval(data[-2]) != time_idx:
                continue
            else:
                if eval(data[1]) == grid_idx:
                    number = number+1
                    speed = eval(data[-1])
                    speed_add = speed_add+speed
                else:
                    continue
        #no information
        if number == 0:
            speed_avg = -1
            one_avg_speed[grid_idx] = speed_avg
        else:
            speed_avg = speed_add/number
            one_avg_speed[grid_idx] = speed_avg
    print(one_avg_speed)

"""
for time_idx in range(0,len(time_range)):
    one_avg_speed = []
    for grid_idx in range(0,lon_range**2):
        number = 0
        speed_add = 0
        for line in sys.stdin:
            data = line.strip().split(',')
            if eval(data[-2]) != time_idx:
                continue
            else:
                if eval(data[1]) == grid_idx:
                    number = number+1
                    speed = eval(data[-1])
                    speed_add = speed_add+speed
                else:
                    continue
        #no information
        if number == 0:
            speed_avg = -1
            one_avg_speed.append(speed_avg)
        else:
            speed_avg = speed_add/number
            one_avg_speed.append(speed_avg)
    print(one_avg_speed)                    
"""   

    