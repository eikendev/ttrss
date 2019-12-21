import logging
import os

from .util import get_valid_filename

logger = logging.getLogger("ttrss")


class TTRssArticle:
    def __init__(self, source):
        self.author = source['author']
        self.content = source['content']
        self.feed_id = source['feed_id']
        self.feed_title = source['feed_title']
        self.id = source['id']
        self.link = source['link']
        self.title = source['title']

    def build_filename(self, path):
        title = get_valid_filename(self.title)

        max_length = os.statvfs(path).f_namemax - len('.html')

        filename = '{}-{}'
        filename = filename.format(self.id, title)
        filename = filename[0:max_length]
        filename = filename + '.html'

        msg = "Final filename is '{}'.".format(filename)
        logger.debug(msg)

        return filename
