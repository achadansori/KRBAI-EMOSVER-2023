from navigation.rc import RCLib
import time
import navigation.imu as imu

rc = RCLib()

rc.arm()
rc.raw('throttle', 1400)
time.sleep(3)
rc.raw('forward', 1800)
time.sleep(2)
rc.raw('throttle', 1420)
time.sleep(2)
rc.raw('throttle', 1445)


time.sleep(11)



rc.raw('forward', 1500)
time.sleep(2)


rc.killall()
rc.disarm()