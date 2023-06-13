import nav_interface_recv
import logging
import time

nav_i = nav_interface_recv.Nav_recv_intf(5005, "nav_recv.log", logging.DEBUG)

nav_i.start()
time.sleep(5)
print("After nav_i.start")
nav_i.stop()
nav_data = nav_i.get_nav_data()
print("Nav Data %s", nav_data)
nav_i.join()
