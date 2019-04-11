import configparser
import logging
import os

from pathlib import Path

from .exception import TTRssConfigurationException

logger = logging.getLogger("ttrss")


def load_config(path):
    msg = "Loading configuration '{}'."
    logger.debug(msg.format(path))

    config = configparser.ConfigParser(interpolation=None)

    try:
        config.read(path)
    except configparser.Error:
        msg = "Cannot load configuration '{}'."
        logger.error(msg.format(path))
        exit(1)

    return config


def get_default_config_file():
    msg = 'Loading default configuration file.'
    logger.debug(msg)

    subdirectory = 'ttrss'
    filename = 'config.ini'

    base = '~/.config'
    base = os.getenv('XDG_CONFIG_HOME', base)
    base = Path(base)
    base = base.expanduser()
    base = base.resolve()

    config = base / subdirectory / filename

    return config


def get_root_dir(path: str) -> Path:
    if path is None:
        msg = 'Invalid root directory.'
        raise TTRssConfigurationException(msg)

    path = Path(path)
    path = path.expanduser().resolve()

    if not path.exists():
        path.mkdir(parents=True)

    if not path.is_dir():
        msg = 'Root directory path is not a directory.'
        raise TTRssConfigurationException(msg)

    return path
