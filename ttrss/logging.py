import logging
import sys


def setup_logger(logger: logging.Logger) -> None:
    fmt = '%(asctime)s [%(levelname)s] %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    level = logging.INFO

    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(sh)
