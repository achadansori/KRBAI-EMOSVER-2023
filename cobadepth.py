from navigation.rc import RCLib
import time
import navigation.imu as imu
import subprocess
import re
import struct
import smbus2


def read_data():
        I2C_ADDRESS = 8  # Alamat slave I2C Arduino
        bus = smbus2.SMBus(1)  # Inisialisasi I2C bus dengan nomor bus 1 pada Jetson Nano
        data_bytes = bus.read_i2c_block_data(I2C_ADDRESS, 0, 4)  # Membaca 4 byte data dari Arduino
        pressure_meter = struct.unpack('f', bytes(data_bytes))[0]  # Mengubah byte array menjadi float
        pressure_kpa = pressure_meter / 0.101972  # Konversi tekanan dari meter ke KPa
        return pressure_kpa

# Inisialisasi parameter PID
kp = 1  # Koefisien proporsional
ki = 0.5  # Koefisien integral
kd = 0.7  # Koefisien diferensial

# Inisialisasi variabel kontrol
integral = 0
prev_error = 0

# Inisialisasi target kedalaman yang diinginkan
target_depth = 4.0

rc = RCLib()

rc.arm()
time.sleep(1)

#for _ in range(5000):
for _ in range(3000):
    # Baca data kedalaman
    pressure = read_data()

    # Menghitung error kedalaman
    error = target_depth - pressure

    # Menghitung komponen kontrol PID
    proportional = kp * error
    integral += ki * error
    differential = kd * (error - prev_error)

    # Mendapatkan sinyal kontrol dari penjumlahan komponen PID
    control_signal = proportional + integral + differential

    # Mengatur batasan atas dan bawah untuk sinyal kontrol
    control_signal = max(min(control_signal, - 30), 30)  # Contoh batasan sinyal antara -100 hingga 100

    # Mengatur throttle berdasarkan sinyal kontrol
    throttle = 1450 - control_signal
    intThrottle = int(throttle)

    # Memperbarui error sebelum iterasi berikutnya
    prev_error = error

    pressure = read_data()
    print("Kedalaman: %.1f m" % pressure)

    print("Throttle PWM :", intThrottle)

    rc.raw('throttle', intThrottle)



rc.killall()
rc.disarm()
