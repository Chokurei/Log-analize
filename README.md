# Log-analize
==========================================================================================
The project in G-spase

## 1. Get in and out
------------------------------------------------------------------------------------------
### 1. Get_in_out.py

Non-distributed way 

Target: find out get in out location,time,ID

Format of each line in orignal CSV file:

IMEI,Latitude,Longitude,speed,direaction,acceleration,meter,time(unix),data_source(8,9),time
(normal),error of Taxi data(11 features)
### 2. 20161025_maper.py
 Distributed way, using hadoop

Mapper procedure
### 3. 20161025_reducer.py
Distributed way, using hadoop

Reducer procedure

Note:

    for line in sys.stdin:

## 2. Congestion analyse
------------------------------------------------------------------------------------------
Analyze congestion condition in Bangkok
### 1. congestion_mapper.py

input

    *original data: 11 features:
        #IMEI,Latitude,Longitude,speed,direaction,acceleration,meter,time(unix),data_source(8,9),time,other
        
output

    *filtered features after mapper: 4 features:
        ID,grid_num,time_num,speed
        
    *grid_idx=lon_idx*30+lat_idx:
        #Bangkok coordinate:
            #lon_w,lon_e=100.40,100.70
            #lat_s,lat_n=13.60,13.90
            #split into 100x100 grid
            
    *time_idx:
        split 1 day(1440min) into interval = 30 min
### 2. congestion_reducer.py
input data

    * origianl data: get from mapper: 4 features
        #ID,grid_num,time_num,speed
output

    * average speed matrix
        # size: 48 x 10000
        # rows: grid index
        # col: time index
        # value: average speed 

