from rc import RCLib
import time
import navigation.imu2 as imu2

rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

#print(rc.getDeg())

#time.sleep(5)

rc.throttle('time', 2, -0.25)

rc.setmode('ALT_HOLD')

#time.sleep(0.5)
#x = 0
#while (x < 12):
#    rc.getDeg()
#    x = x+1


#INIT_VAL = rc.getDeg()
INIT_VAL = 73

#rc.imu_turn(63)
#rc.setmode('ALT_HOLD')
rc.forward("time", 8, 0.5)
#rc.setmode('ALT_HOLD')
rc.imu_turn(INIT_VAL+90)
#rc.setmode('ALT_HOLD')
rc.forward("time", 1, 0.25)
#rc.setmode('ALT_HOLD')
rc.imu_turn(INIT_VAL+181)
#rc.setmode('ALT_HOLD')
rc.forward("time", 2, 0.5)
rc.imu_turn(INIT_VAL+181)
rc.forward("time", 2, 0.5)
rc.imu_turn(INIT_VAL+181)
rc.forward("time", 2, 0.5)
rc.imu_turn(INIT_VAL+181)

#rc.setmode('ALT_HOLD')
#rc.setmode('ALT_HOLD')

#rc.imu_turn(227)
#rc.setmode('ALT_HOLD')


#rc.forward('time', 1.5, -0.4)

print(rc.getDeg())

#rc.yaw('time', 10, 0)
#time.sleep(10)

print("----------")
print(rc.getDeg())

#time.sleep(5)
