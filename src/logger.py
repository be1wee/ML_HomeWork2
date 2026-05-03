import logging
import os
from logging.handlers import RotatingFileHandler

class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, log_file='./data/log_file.log'):
        if hasattr(self, 'initialized'):
            return
        self.initialized = True
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        self.logger = logging.getLogger('CarNumberApp')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=5)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger

app_logger = Logger().get_logger()