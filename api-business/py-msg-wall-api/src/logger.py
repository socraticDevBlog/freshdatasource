import datetime
import time
import logging
import os


class Logger:

    LOWEST_VERBOSITY = logging.ERROR
    DEBUG_VERBOSITY = logging.DEBUG
    TIMESTAMP_SYNTAX = "%Y%m%d-%H%M%S"
    LOG_FILE = 'log_'
    FILE_TYPE = '.out'
    
    def __init__(self, program_name, verbosity=LOWEST_VERBOSITY):
        timestamp = time.strftime(self.TIMESTAMP_SYNTAX)
        log_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs')
        log_file_name = os.path.join(log_directory, self.LOG_FILE + timestamp  + self.FILE_TYPE)

        logging.basicConfig(filename=log_file_name, 
                            level=verbosity
                            )

        logging.critical('Log for program %s' % program_name)

        now = str(datetime.datetime.today())
        logging.critical('Execution date = %s' % now)

    def debug(self, arg):
        logging.debug(arg)

    def error(self, arg):
        now =  str(datetime.datetime.today())
        logging.error(now + ' ' + arg)
    