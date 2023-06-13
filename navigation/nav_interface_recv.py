import socket
import time
import json
import threading
import logging

class Nav_recv_intf(threading.Thread):

    def __init__(self, server_port, log_file, log_level):
        threading.Thread.__init__(self)

        self._server_ip = "0.0.0.0"
        self._server_port = server_port
        self._log_file = log_file
        self._log_level = log_level
        self._stop = False
        self._nav_data = {}

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.setblocking(0)
        self._sock.bind((self._server_ip, self._server_port))
        FORMAT = '%(asctime)-15s %(message)s'
        logging.basicConfig(filename=self._log_file,level=self._log_level, format=FORMAT)
        logging.info('nav_interface initialized with log file %s', self._log_file)

    def __del__(self):
        self._sock.close()

    def stop(self):
        self._stop = True

    def get_nav_data(self):
        return self._nav_data

    def run(self):
        while not self._stop:
            try:
                data, addr = self._sock.recvfrom(1024) # buffer size is 1024 bytes
                logging.debug("received message: %s", data)
                y = json.loads(data)
                self._nav_data = y
            except socket.error as err:
                time.sleep(0.1)
