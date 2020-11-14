# utf-8
import logging
import logging.handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

rf_handler = logging.handlers.TimedRotatingFileHandler('info.log', when='midnight', interval=1, backupCount=7,
                                                       atTime=datetime.time(0, 0, 0, 0), encoding='utf-8')
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# 使用StreamHandler输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log', encoding='utf-8')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(ch)
logger.addHandler(f_handler)


def record_log(level, message):  # 有6个等级，分别是debug, info, warning,error,critical
    if level == 'DEBUG':
        logger.log(logging.DEBUG, message)
    elif level == 'INFO':
        logger.log(logging.INFO, message)
    elif level == 'WARNING':
        logger.log(logging.WARNING, message)
    elif level == 'ERROR':
        logger.log(logging.ERROR, message)
    elif level == 'CRITICAL':
        logger.log(logging.CRITICAL, message)
