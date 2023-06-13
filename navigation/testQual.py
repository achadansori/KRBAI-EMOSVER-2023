from rc import RCLib
import time
import navigation.imu2 as imu2

rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()


rc.throttle('time', 2, -0.25)



#INIT_VAL = 73

#rc.forward("time", 9, 0.5)
#rc.imu_turn(INIT_VAL+90)
#rc.imu_turn(INIT_VAL+90)
#rc.forward("time", 1.5, 0.5)
#rc.setmode('ALT_HOLD')
#rc.imu_turn(INIT_VAL+181)
#rc.setmode('ALT_HOLD')
#rc.forward("time", 8, 0.5)

print(rc.getDeg())

#rc.yaw('time', 10, 0)
#time.sleep(10)

rc.setmode('ALT_HOLD')
rc.yaw("imu", 90, 0.10)
rc.yaw("time", 2, 0)

print("----------")
print(rc.getDeg())

#time.sleep(5)
