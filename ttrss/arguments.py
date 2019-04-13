import logging

from argparse import ArgumentParser

from .exception import TTRssArgumentException

logger = logging.getLogger("ttrss")


def parse_arguments():
    method_choices = [
        "synchronize",
    ]

    parser = ArgumentParser(
        prog="ttrss",
        description="A tool for synchronizing feeds from a Tiny Tiny RSS server."
    )
    parser.add_argument("method", type=str, choices=method_choices,
                        help="Method to run.")
    parser.add_argument("-v", "--debug", action="store_true",
                        help="Print debug information.")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Print errors and warnings only.")
    parser.add_argument("-c", "--config-file", type=str,
                        help="File to read configuration from.")
    parser.add_argument("--directory", type=str,
                        help="Directory to use for synchronization.")
    parser.add_argument("--url", type=str,
                        help="Root URL of the ttrss instance.")
    parser.add_argument("--username", type=str,
                        help="Username for the ttrss instance.")
    parser.add_argument("--keyring-service", type=str,
                        help="Service name to retrieve the password for.")

    args = parser.parse_args()

    if args.debug and args.quiet:
        msg = 'Cannot be quiet in debug mode.'
        raise TTRssArgumentException(msg)

    return args
