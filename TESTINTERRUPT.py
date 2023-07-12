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

# Read the current state of the pin
while True:
    data = read_data()
    print(data)
    if data == 1 :
        break
    try:
        if math.isnan(data):
            print(data) 
    except:
        print("No data")

    
    
    
    