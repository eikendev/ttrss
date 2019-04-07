import logging
import re

logger = logging.getLogger("ttrss")


# https://github.com/django/django/blob/master/django/utils/text.py
def get_valid_filename(s):
    s_old = s

    s = str(s)
    s = s.strip()
    s = re.sub(r'\s{2,}', ' ', s)
    s = s.replace(' ', '_')
    s = re.sub(r'(?u)[^-\w.]', '', s)
    s = s.lower()

    logger.debug("Got valid filename '%s' from '%s'.", s, s_old)

    return s
