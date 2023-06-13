from rc import RCLib
import time
import navigation.imu2 as imu2

rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

rc.throttle('time', 2, -0.25)

INIT_VAL = 73

rc.forward("time", 1, 0.5)
rc.imu_turn(INIT_VAL+90)
rc.forward("time", 1, 0.5)
