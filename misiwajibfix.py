from navigation.rc import RCLib
import time
import navigation.imu as imu
import subprocess
import re
import struct
import smbus2
import math
rc = RCLib()

def read_data():
        I2C_ADDRESS = 8  # Alamat slave I2C Arduino
        bus = smbus2.SMBus(1)  # Inisialisasi I2C bus dengan nomor bus 1 pada Jetson Nano
        data_bytes = bus.read_i2c_block_data(I2C_ADDRESS, 0, 4)  # Membaca 4 byte data dari Arduino
        data = struct.unpack('f', bytes(data_bytes))[0]
        return data

rc.arm()

time.sleep(5)
rc.raw('throttle', 1400)
time.sleep(3)
rc.raw('forward', 1800)
time.sleep(2)
rc.raw('throttle', 1420)
time.sleep(2)
rc.raw('throttle', 1445)

for _ in range(11):
    print("FOR")
    data = read_data()
    print(data)
    if data == 1 :
        rc.killall()
        rc.disarm()
        break
    try:
        if math.isnan(data):
            print(data) 
    except:
        print("No data")
    rc.raw('forward', 1800)
    rc.raw('throttle', 1445)
    time.sleep(1)



rc.raw('forward', 1500)
time.sleep(2)

rc.killall()
rc.disarm()