from rc import RCLib
import time

rc = RCLib()

rc.arm()

rc.throttle('time', 4, -0.25)

rc.imu_turn(71)

des_time = 4
power = 0.5

#rc.forward('time', des_time, power)

rc.setmode('ALT_HOLD')

#rc.forward('time', 1, -0.3)

#rc.yaw('time', 10, 0)

rc.move_dist(295, 0.5)

#rc.imu_turn(241)

#rc.forward('time', des_time, power)

#rc.imu_turn(61)
