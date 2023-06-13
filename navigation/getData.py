from rc import RCLib
import time
import navigation.imu2 as imu2
from pymavlink import mavutil
import math

master = mavutil.mavlink_connection('/dev/ttyTHS1', baud=57600)

master.wait_heartbeat()

while(True):
    try:
        att_val = master.recv_match(type='ATTITUDE').to_dict()
        #print(att_val)
        yaw = att_val['yaw']
        yaw_deg = math.floor(yaw * (180/3.141592))
        print(yaw_deg)
        #rc.getAllData()
    except:
        pass
                
