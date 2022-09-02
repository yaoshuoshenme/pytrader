import logging
from common.constant import Constant
import os


class SimpleLog(object):

    _loggers = {}
    _error_path = os.path.join(Constant.conf_dir, "error.log")

    @staticmethod
    def get(file_name):
        """初始化logger
        """
        if file_name in SimpleLog._loggers:
            return SimpleLog._loggers[file_name]
        else:
            logger = logging.getLogger(file_name)
            logger.setLevel(logging.INFO)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # info handler
            info_handler = logging.StreamHandler()
            info_handler.setFormatter(formatter)
            info_handler.setLevel(logging.INFO)
            # error handler
            error_handler = logging.FileHandler(SimpleLog._error_path)
            error_handler.setFormatter(formatter)
            error_handler.setLevel(logging.ERROR)

            logger.addHandler(info_handler)
            logger.addHandler(error_handler)

            SimpleLog._loggers.setdefault(file_name, logger)
            return logger



