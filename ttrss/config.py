import logging
import os

from configparser import ConfigParser
from pathlib import Path

from .exception import TTRssConfigurationException

logger = logging.getLogger("ttrss")


def load_config(path):
    config = ConfigParser(interpolation=None)
    config.read(path)

    return config


def _get_config_base() -> Path:
    default = '~/.config'
    path = os.getenv('XDG_CONFIG_HOME', default)

    path = Path(path)
    path = path.expanduser().resolve()

    if not path.is_dir():
        msg = 'Could not find configuration file.'
        logger.error(msg)
        exit(1)

    return path


def get_config_path() -> Path:
    directory = 'ttrss'
    filename = 'config.ini'

    base = _get_config_base()
    path = base / directory / filename

    return path


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
