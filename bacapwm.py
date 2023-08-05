import serial
import time

# Buka koneksi Serial dengan Arduino Uno
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

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

                    print("Ch1:", ch1Value)
                    print("Ch2:", ch2Value)
                    print("Ch3:", ch3Value)
                    print("Ch4:", ch4Value)
                    print("Ch5:", ch5Value)
                    print("Ch6:", ch6Value)
                    print("")

            time.sleep(0.1)

    except KeyboardInterrupt:
        # Tutup koneksi saat program dihentikan
        ser.close()
        print("Program dihentikan.")
