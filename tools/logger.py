import logging


def get_logger(name: str) -> logging.Logger:
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.FATAL)

    handler = logging.StreamHandler()
    handler.setLevel(logging.FATAL)

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
