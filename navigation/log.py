import logging, time
from io import StringIO
CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0

class LogLib:

    def __init__(self, name='log'):
        try: 
           self._stream = StringIO.StringIO()
           self._formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
           self._logger = logging.getLogger()
           self._handler = logging.StreamHandler(self._stream)
           self._handler.setFormatter(self._formatter)
           self._logger.addHandler(self._handler)
           self._name = name

        except Exception as e:
            print(e)
        
    # This function is responsible for sending RC channel overrides
    def setLevel(self, level):
           self._logger.setLevel(level)
        
    def critical(self, msg ):
          self._logger.critical(msg)

    def error(self, msg ):
          self._logger.error(msg)

    def warning (self, msg ):
          self._logger.warning (msg)

    def info(self, msg ):
          self._logger.info(msg)

    def debug(self, msg ):
          self._logger.debug(msg)

    def flush(self):
          fileName = self._name + '_' + str(time.localtime().tm_mon) + '_' + str(time.localtime().tm_mday) \
             + '_' + str(time.localtime().tm_hour) + '_' + str(time.localtime().tm_min) \
             + '_' + str(time.localtime().tm_sec) + '.txt'
          with open(fileName, 'w') as f:
             f.write(self._stream.getvalue())
