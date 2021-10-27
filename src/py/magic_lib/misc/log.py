import logging


def get_logger(name, level=None):
    if not level:
        level = 'DEBUG'

    # handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(filename)s#%(lineno)s#%(funcName)s() >> %(message)s')
    handler.setFormatter(formatter)

    # logger
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(eval("logging.{}".format(level)))
    return logger




