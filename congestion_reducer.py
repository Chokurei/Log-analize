#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:41:51 2016

@author: kaku
###################### reducer code for congression condition #######################
# input data
    # origianl data: get from mapper: 3 features
        #time_id, grid_id, speed
# output
    # time_id, grid_id, avg_spped, num_of_records
"""

import sys

old_grid_id = None
old_time_id = None
avg_speed = None
num_of_records = 0
sum_of_speed = 0

for line in sys.stdin:
    data_mapped = line.strip().split(',')
    try:
        assert len(data_mapped) == 3
        time_id= data_mapped[0]
        grid_id= data_mapped[1]
        
        if time_id == old_time_id:
            if grid_id == old_grid_id:
                num_of_records += 1
                sum_of_speed += float(data_mapped[2])
            elif grid_id != old_grid_id:
                avg_speed = round(sum_of_speed/num_of_records)
                print('{0},{1},{2},{3}'.format(grid_id,time_id,avg_speed,num_of_records))
                old_grid_id =grid_id                
                num_of_records = 0
                sum_of_speed = 0
                num_of_records +=1
                sum_of_speed += float(data_mapped[2])
            else:
                continue
            
        elif old_time_id != None:
            print('{0},{1},{2},{3}'.format(grid_id,time_id,avg_speed,num_of_records))
            old_time_id = time_id
            old_grid_id = grid_id            
            num_of_records = 0
            sum_of_speed = 0
            num_of_records +=1
            sum_of_speed +=float(data_mapped[2])
            
        else:
            old_time_id = time_id
            old_grid_id = grid_id
            num_of_records += 1
            sum_of_speed += float(data_mapped[2])
            continue
    except:
        continue

##The final line, if time_id == old_time_id and grid_id == old_grid_id, also need to be output
if time_id == old_time_id and grid_id == old_grid_id:
    avg_speed = round(sum_of_speed/num_of_records)
    print('{0},{1},{2},{3}'.format(grid_id,time_id,avg_speed,num_of_records))
    
