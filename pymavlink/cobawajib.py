from navigation.rc import RCLib
from navigation.ac import ACLib
import time
import navigation.imu as imu

rc = RCLib()
ac = ACLib()


rc.setmode('MANUAL')

rc.arm()

print(rc.getDeg())

# depth hold and go down
rc.setmode('ALT_HOLD')
rc.throttle("time", DEPTH_SEC, -0.25)

# align with the origin 
rc.imu_turn(START)

rc.forward("time", 10, 0.32)
leftAlign(2400)
#rc.imu_turn(START)
rc.forward("time", 5, 0.32)
leftAlign(2000)
rc.imu_turn(START)
rc.forward("time", 5, 0.32)
leftAlign(1500)
rc.imu_turn(START)
rc.forward("time", 5, 0.32)
leftAlign(1500)
rc.forward("time", 5, 0.32)
leftAlign(3500)

rc.imu_turn(85)
rc.forward("time", 15, 0.25)
rc.imu_turn(85)
rightAlign(2500)
rc.imu_turn(85)
rc.forward("time", 8, 0.32)
rightAlign(2500)
rc.imu_turn(80)
rc.throttle("time", 1, -0.25)
rc.forward("time", 3, 0.35)
rightAlign(2500)
rc.imu_turn(80)
rc.forward("time", 15, 0.32)

rc.close()
