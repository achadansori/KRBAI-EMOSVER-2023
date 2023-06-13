from rc import RCLib
import time

rc = RCLib()

rc.arm()

rc.throttle('time', 4, -0.25)

rc.imu_turn(63)

rc.move_dist(265, 0.5)

