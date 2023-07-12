import subprocess
import re
import Jetson.GPIO as GPIO
import smbus


# Set up I2C bus
bus = smbus.SMBus(1)
address = 0x08

# Set up GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

# Read data from I2C device
def read_i2c():
    GPIO.output(3, GPIO.HIGH)
    data = bus.read_byte(address)
    GPIO.output(3, GPIO.LOW)
    return data

# Spawn the C++ program as a subprocess
cpp_process = subprocess.Popen(['./vision'], stdout=subprocess.PIPE)

while True:
    output = cpp_process.stdout.readline().decode().strip()
    value = read_i2c()
    print("Received value: ", value)
    
    to_convert = re.findall('[0-9]+', output)
    try:
        converted = int(to_convert[0])
    except IndexError:
        #print("Index out of range!")
        continue
    
    print("Yaw PWM :", converted)