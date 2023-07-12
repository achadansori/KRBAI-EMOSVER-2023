import struct
import smbus2

I2C_ADDRESS = 8  # Alamat slave I2C Arduino

def read_data():
    bus = smbus2.SMBus(1)  # Inisialisasi I2C bus dengan nomor bus 1 pada Jetson Nano
    data_bytes = bus.read_i2c_block_data(I2C_ADDRESS, 0, 4)  # Membaca 4 byte data dari Arduino
    pressure_meter = struct.unpack('f', bytes(data_bytes))[0]  # Mengubah byte array menjadi float
    pressure_kpa = pressure_meter / 0.101972  # Konversi tekanan dari meter ke KPa
    return pressure_kpa

while True:
    pressure = read_data()
    print("Kedalaman: %.1f m" % pressure)
