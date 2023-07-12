from navigation.rc import RCLib
import time
import navigation.imu as imu
import subprocess
import re

cpp_process = subprocess.Popen(['./vision'], stdout=subprocess.PIPE)

rc = RCLib()

rc.arm()

rc.raw('throttle', 1445)
time.sleep(3)
rc.raw('forward', 1570)

for _ in range(2000):
    output = cpp_process.stdout.readline().decode().strip()
    
    to_convert = re.findall('[0-9]+', output)
    try:
        converted = int(to_convert[0])
    except IndexError:
        #print("Index out of range!")
        continue
    
    print("Yaw PWM :", converted)

    rc.raw('yaw', converted)

rc.raw('forward', 1500)
time.sleep(2)

rc.killall()
rc.disarm()
