import logging
import re

from pathlib import Path

from .article import TTRssArticle
from .client import TTRssClient
from .exception import TTRssException

logger = logging.getLogger("ttrss")


def synchronize(client: TTRssClient, path: Path) -> None:
    logger.debug('Synchronizing unread feeds.')

    local = set()
    indexfile = path / '.index'
    countfile = path / '.count'

    def line_to_id(line: str) -> str:
        line = re.match(r'(\d+),.*', line)
        line = line.group(1)
        line = int(line)

        return line

    if indexfile.exists():
        if not indexfile.is_file():
            msg = 'Cannot create index file.'
            raise TTRssException(msg)
        else:
            with open(indexfile, 'r') as f:
                local = f.readlines()

            local = [line_to_id(l) for l in local]
            local = set(local)

    articles = client.get_unread_articles()
    articles = {a.id: a for a in articles}

    msg = 'Received %d unread articles.'
    logger.debug(msg, len(articles))

    remote = [a_id for a_id in articles]
    remote = set(remote)

    to_remove = local - remote
    to_add = remote - local

    msg = 'There are %d obsolete and %d new articles.'
    logger.info(msg, len(to_remove), len(to_add))

    line = str(len(remote)) + "\n"

    with open(countfile, 'w') as f:
        f.write(line)

    if len(to_remove) == 0 and len(to_add) == 0:
        msg = 'No more modifictions are necessary.'
        logger.info(msg)
        exit(0)

    # Remove all obsolete articles.
    for a_id in to_remove:
        pattern = str(a_id) + '-*.html'

        for a_path in path.glob(pattern):
            if not a_path.is_file():
                msg = 'Cannot remove missing %s.'
                logger.warning(msg, a_path)
            else:
                a_path.unlink()

    # Add all new articles.
    for a_id in to_add:
        article = articles[a_id]

        a_path = article.build_filename()
        a_path = path / a_path

        if a_path.exists():
            msg = 'Cannot write existing %s.'
            logger.warning(msg, a_path)
        else:
            content = article.content

            if len(content) == 0:
                content = article.link

            with open(a_path, 'w') as f:
                f.write(content)

    def build_index_line(article: TTRssArticle) -> str:
        a_path = article.build_filename()

        line = "{},{}\n"
        line = line.format(article.id, a_path)

        return line

    lines = [build_index_line(articles[a]) for a in remote]

    with open(indexfile, 'w') as f:
        f.writelines(lines)
