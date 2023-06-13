import time

# Import mavutil
from pymavlink import mavutil

master = mavutil.mavlink_connection('/dev/ttyTHS1', baud=57600)

master.wait_heartbeat()

def getDeg() :
    while True:
        try:

            att_val = master.recv_match(type='ATTITUDE').to_dict()
            roll = ((180/3.14159265358618)* att_val['yaw'])

            if roll < 0:

                return 360 + roll

            if roll > 0:

                return(roll)
            
#        print(master.recv_match(type='HOME_POSITION').to_dict())
#        dict = master.recv_match(type='RAW_IMU').to_dict()
#        print('xmag: ', dict['xmag'], 'ymag: ', dict['ymag'], 'zmag: ', dict['zmag'])
        except:
            pass
        time.sleep(0.1)

print(getDeg())
