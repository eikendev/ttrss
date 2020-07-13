import atexit
import json
import logging
import requests

from urllib.parse import urljoin

from .article import TTRssArticle
from .exception import TTRssException

logger = logging.getLogger("ttrss")


class TTRssClient:
    def __init__(self, url, username, password):
        self.url = urljoin(url, 'api/')
        self.username = username
        self.password = password
        self.session_id = None

    def __enter__(self):
        self.login()
        return self

    def __exit__(self, _type, _value, _traceback):
        self.logout()

    def _perform_json_request(self, data, retries=5):
        data_json = json.dumps(data)
        success = False

        for _ in range(0, retries):
            try:
                r = requests.post(self.url, data=data_json)
                r.raise_for_status()
                success = True
            except requests.exceptions.RequestException:
                pass

        if not success:
            raise TTRssException('HTTP request not successful.')

        try:
            data = r.json()
        except ValueError:
            raise TTRssException('Received invalid JSON.')

        return data

    def login(self):
        if self.session_id is not None:
            return

        data = dict(
            op='login',
            user=self.username,
            password=self.password,
        )
        data = self._perform_json_request(data)

        if data['status'] != 0:
            raise TTRssException('Login not successful.')

        self.session_id = data['content']['session_id']
        atexit.register(self.logout)

    def logout(self):
        if self.session_id is None:
            return

        data = dict(
            op='logout',
            sid=self.session_id,
        )
        data = self._perform_json_request(data)

        self.session_id = None

    def get_unread_articles(self):
        if self.session_id is None:
            raise TTRssException('Client is missing session_id.')

        articles = list()

        per_page = 200
        offset = 0
        last_len = per_page

        while last_len == per_page:
            data = dict(
                op='getHeadlines',
                sid=self.session_id,
                feed_id=-4,
                limit=per_page,
                skip=offset,
                show_content=True,
                view_mode='unread',
                include_attachments=False,
                include_nested=True,
                order_by='feed_dates',
                include_header=False,
            )
            data = self._perform_json_request(data)
            new_articles = data['content']
            new_articles = [TTRssArticle(source) for source in new_articles]

            last_len = len(new_articles)
            offset += last_len
            articles += new_articles

        return articles
