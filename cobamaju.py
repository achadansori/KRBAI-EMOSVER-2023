from navigation.rc import RCLib
import time
import navigation.imu as imu

rc = RCLib()

rc.arm()
rc.raw('throttle', 1380)
time.sleep(2)
rc.raw('forward', 1600)
time.sleep(2)
rc.raw('throttle', 1400)
time.sleep(2)
rc.raw('throttle', 1425)


#Maju
time.sleep(15)

rc.raw('forward', 1500)
time.sleep(2)


rc.killall()
rc.disarm()