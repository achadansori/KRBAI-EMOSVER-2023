import json
import socket
import logging

class Nav_send_intf:

    def __init__(self, server_ip, server_port, log_file, log_level):
        self._server_ip = server_ip
        self._server_port = server_port
        self._log_file = log_file
        self._log_level = log_level

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

        FORMAT = '%(asctime)-15s %(message)s'
        logging.basicConfig(filename=self._log_file,level=self._log_level, format=FORMAT)
        logging.info('nav_interface initialized with log file %s', self._log_file)



    def send_cv_data(self, target_id ,x, y, z, roll, pitch, yaw, width, height, confidence):
   
        logging.info('send_cv_data target_id=%d x=%d y=%d z=%d roll=%d pitch=%d yaw=%d width=%d height=%d confidence=%d', target_id, x, y, z, roll, pitch, yaw, width, height, confidence)
        cv_data_json = {}
        cv_data_json['Target_ID'] = target_id
        cv_data_json['X'] = x
        cv_data_json['Y'] = y
        cv_data_json['Z'] = z
        cv_data_json['Roll'] = roll
        cv_data_json['Pitch'] = pitch
        cv_data_json['Yaw'] = yaw
        cv_data_json['Width'] = width
        cv_data_json['Height'] = height
        cv_data_json['Confidence'] = confidence
    
        message = json.dumps(cv_data_json)
    
        logging.info("message:%s", message)

        self._sock.sendto(message, (self._server_ip, self._server_port))

        
        logging.info("sent cv data to nav")
