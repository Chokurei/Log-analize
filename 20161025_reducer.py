#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:57:21 2016

@author: kaku
"""

import sys

for line in sys.stdin:
    data=line.strip().split(',')
    if len(data)==5:
        print('{0},{1},{2},{3},{4}'.format(data[0],data[1],data[2],data[3],data[4])) 

        
