#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:35:02 2016

@author: kaku
"""
import sys

old_label=0

for line in sys.stdin:
    data=line.strip().split(',')
    try:
        new_label=data[6]
        if new_label!=old_label:
            old_label=new_label
            print('{0},{1},{2},{3},{4}'.format(data[0],data[1],data[2],data[6],data[-2])) 
        else:
            continue
    except:
        continue

            
