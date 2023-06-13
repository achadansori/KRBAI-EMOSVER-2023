from navigation.rc import RCLib
import time
import navigation.imu as imu

rc = RCLib()

rc.setmode('MANUAL')
rc.arm()

time.sleep(5)

rc.raw('throttle', 1700)
time.sleep(3)
rc.raw('throttle', 1700)

rc.setmode('ALT_HOLD')

rc.raw('forward', 1700)
time.sleep(20)

rc.setmode('MANUAL')
rc.killall()
rc.disarm()