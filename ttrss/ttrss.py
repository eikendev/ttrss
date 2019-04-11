import keyring
import logging
import sys

from functools import partial
from pathlib import Path

from .arguments import parse_arguments
from .client import TTRssClient
from .config import load_config, get_default_config_file, get_root_dir
from .exception import TTRssArgumentException, TTRssConfigurationException
from .methods import synchronize

logger = logging.getLogger("ttrss")


def setup_logger(logger: logging.Logger) -> None:
    fmt = '%(asctime)s [%(levelname)s] %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    level = logging.INFO

    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(sh)


def execute_method(method: str, path: Path, client: TTRssClient) -> None:
    msg = "Executing method: '{}'.".format(method)
    logger.debug(msg)

    methods = {
        'synchronize': partial(synchronize, path=path),
    }

    try:
        method = methods[method]
    except KeyError:
        logger.error('Method does not exist.')
        exit(1)

    try:
        method(client)
    except KeyboardInterrupt:
        msg = 'Received keyboard interrupt.'
        logger.info(msg)


def main():
    setup_logger(logger)

    try:
        args = parse_arguments()
    except TTRssArgumentException as e:
        msg = 'Failed to parse arguments: ' + str(e)
        logger.error(msg)
        exit(1)

    if args.debug:
        logger.setLevel(logging.DEBUG)
        msg = 'Application is running in debug mode.'
        logger.debug(msg)
    elif args.quiet:
        logger.setLevel(logging.WARNING)

    config_file = args.config_file

    if config_file is None:
        config_file = get_default_config_file()

    config = load_config(config_file)

    logger.info('Starting TTRss.')

    def load_parameter(required, conf_section, conf_name, arg_name):
        arg = getattr(args, arg_name, None)

        if arg is not None:
            return arg

        conf = config.get(conf_section, conf_name, fallback=None)

        if not required:
            return conf
        else:
            msg = "Required argument not provided: '{}'."
            logger.error(msg.format(arg_name))
            exit(1)

    directory = load_parameter(True, 'GENERAL', 'RootDir', 'directory')
    url = load_parameter(True, 'GENERAL', 'Url', 'url')
    username = load_parameter(True, 'GENERAL', 'Username', 'username')
    keyring_service = load_parameter(True, 'GENERAL', 'KeyringService', 'keyring_service')

    try:
        directory = get_root_dir(directory)
    except TTRssConfigurationException as e:
        msg = 'Initialization not successful: ' + str(e)
        logger.error(msg)
        exit(1)

    try:
        password = keyring.get_password(keyring_service, username)
    except keyring.errors.KeyringError:
        logger.error('No password given.')
        exit(1)

    with TTRssClient(url, username, password) as client:
        execute_method(args.method, directory, client)
