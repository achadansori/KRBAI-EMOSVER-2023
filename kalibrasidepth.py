from navigation.rc import RCLib
import time
import navigation.imu as imu


rc = RCLib()

rc.arm()

rc.raw('throttle', 1430)
time.sleep(20)


rc.killall()
rc.disarm()
