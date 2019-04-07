import logging

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

    def build_filename(self):
        title = get_valid_filename(self.title)

        filename = '{}-{}'
        filename = filename.format(self.id, title)
        filename = filename[0:250]
        filename = filename + '.html'

        return filename
