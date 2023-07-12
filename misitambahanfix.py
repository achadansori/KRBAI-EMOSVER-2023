from navigation.rc import RCLib
import time
import navigation.imu as imu
import subprocess
import re
import struct
import smbus2
import math

def read_data():
        I2C_ADDRESS = 8  # Alamat slave I2C Arduino
        bus = smbus2.SMBus(1)  # Inisialisasi I2C bus dengan nomor bus 1 pada Jetson Nano
        data_bytes = bus.read_i2c_block_data(I2C_ADDRESS, 0, 4)  # Membaca 4 byte data dari Arduino
        data = struct.unpack('f', bytes(data_bytes))[0]
        return data

cpp_process = subprocess.Popen(['./vision'], stdout=subprocess.PIPE)

rc = RCLib()

rc.arm()

rc.raw('throttle', 1440)
time.sleep(3)
rc.raw('forward', 1580)

for _ in range(1400):
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
