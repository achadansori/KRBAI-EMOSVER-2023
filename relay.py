from navigation.rc import RCLib
import time

rc = RCLib()


rc.turn_relay_on()   # Menghidupkan relay
time.sleep(2)        # Contoh: Menunggu 2 detik
rc.turn_relay_off()  # Mematikan relay