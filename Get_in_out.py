# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:23:26 2016
# Target:
	find out get in out location,time,ID

# Format of each line in orignal CSV file:
# IMEI,Latitude,Longitude,speed,direaction,acceleration,meter,time(unix),data_source(8,9),time
# (normal),error  of Taxi data(11 features)

@author: kaku
"""

import numpy as np
import pandas as pd
import os,csv

data_path=os.path.join('..','data','trajectory')
data_0724_path=os.path.join(data_path,'gps_20140724_imei.csv')
result_path=os.path.join('..','result')

######################read all the line of .csv#####################
def read_data(path):
    features=[]
    file=open(path,'r')
    while(1):
        line=file.readline()
        if line=='':
            break
        else:
            line=line.strip().split(',')
            if len(line)!=10:
                continue
            else:
                features.append(line)
    return features
######################mine out ID, lat, long, meter, time################    

def read_meter(data):
    meter_datas=[]
    for m in range(0,len(data)):
        ID=data[m][0]
        lat=data[m][1]
        long=data[m][2]
        meter=data[m][6]
        time=data[m][-1]
        meter_data=[ID,lat,long,meter,time]
        meter_datas.append(meter_data)
    return meter_datas
######################## record get in and out Index ##############

def find_change(data):
    old_status='0'
    get_in=[]
    get_out=[]
    for m in range(0,len(data)):
        meter=data[m][3]
        if meter==old_status:
            continue
        else:
            if meter!=old_status and meter=='1':
                get_in.append(m)
                old_status='1'
            else:
                get_out.append(m)
                old_status='0'
    return get_in,get_out
    
####################### find out location ##############################################

def find_location(get_in,get_out,meter):
    get_in_locations=[]
    get_out_locations=[]
    for m in range(0,len(get_in)):
        lat=meter[get_in[m]][1]
        long=meter[get_in[m]][2]
        get_in_location=[float(lat),float(long)]
        get_in_locations.append(get_in_location)
    for m in range(0,len(get_out)):
        lat=meter[get_out[m]][1]
        long=meter[get_out[m]][2]
        get_out_location=[float(lat),float(long)]
        get_out_locations.append(get_out_location)    
    return get_in_locations,get_out_locations
    
def csv_make(path,name,data):
    with open(os.path.join(path,name),'w') as f:
        writer=csv.writer(f)
        writer.writerows(data)


raw=read_data(data_0724_path)
meter=read_meter(raw)
get_in,get_out=find_change(meter)
get_in_loc,get_out_loc=find_location(get_in,get_out,meter)
csv_make(result_path,'get_in_loc.csv',get_in_loc)
csv_make(result_path,'get_out_loc.csv',get_out_loc)
    
