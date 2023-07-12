from navigation.rc import RCLib
import time
import navigation.imu as imu

rc = RCLib()

rc.arm()

rc.raw('forward', 1600)
time.sleep(10)


rc.killall()
rc.disarm()