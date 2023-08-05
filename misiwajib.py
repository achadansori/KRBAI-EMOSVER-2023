from navigation.rc import RCLib
import time
import navigation.imu as imu
import serial

# Buka koneksi Serial dengan Arduino Uno
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

rc = RCLib()

def read_data():
    data = ser.readline().decode().strip()
    return data

if __name__ == "__main__":
    try:
        while True:
            # Baca data dari Arduino Uno
            data = read_data()

            # Proses data jika diperlukan
            if data:
                channel_values = data.split(",")  # Pisahkan data berdasarkan koma
                if len(channel_values) == 6:
                    ch1Value = int(channel_values[0])
                    ch2Value = int(channel_values[1])
                    ch3Value = int(channel_values[2])
                    ch4Value = int(channel_values[3])
                    ch5Value = int(channel_values[4])
                    ch6Value = int(channel_values[5]) 

                    rc.arm()


                    if ch5Value > 1900:
                        rc.arm()
                        #AUTO NIH BOSS
                        rc.raw('forward', 1800)
                        if ch6Value > 1900:
                            rc.disarm()
                            break
                        print("auto1")
                        time.sleep(1)

                            
                    else:
                        rc.raw('forward', ch2Value)
                        rc.raw('lateral', ch1Value)
                        rc.raw('yaw', ch4Value)
                        
    except :
        print("No data")

rc.killall()
rc.disarm()

#sudo usermod -a -G dialout penship
#sudo chown :dialout /dev/ttyTHS1
#sudo chmod g+rw /dev/ttyTHS1