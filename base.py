import json
import requests
from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup


class BaseScrapper:
    url = None
    format = 'json'
    next_selector = None
    filename = None
    max_page = 100

    __metaclass__ = ABCMeta

    def __init__(self):
        if not getattr(self, '_data', None):
            self._data = []
        if not getattr(self, '_current_page', None):
            self._current_page = 1

        scrapped_data = list(self.scrap(self.get_soup()))
        self._data.extend(scrapped_data)

        if self.get_next_url():
            if self._current_page != self.max_page:
                self.url = self.get_next_url()
                self._current_page += self._current_page
                self.reproduce(url=self.url, current_page=self._current_page)

        if self.filename:
            self.save2file()

    def get_url(self):
        assert self.url is not None, (
            'You must set `url`.'
        )
        return self.url

    def get_next_selector(self):
        assert self.next_selector is not None, (
            'You must set `next_selector`.'
        )
        return self.next_selector

    def get_filename(self):
        assert self.filename is not None, (
            'You must set `filename`.'
        )
        return self.filename

    def perform_request(self):
        return requests.get(self.get_url())

    def get_html(self):
        return self.perform_request().content

    def get_soup(self):
        return BeautifulSoup(self.get_html(), "html.parser")

    def get_next_url(self):
        try:
            return self.get_soup().select_one(self.get_next_selector()).attrs.get('href')
        except:
            return

    def get_current_page(self):
        return self._current_page

    def get_data(self):
        if self.format == 'json':
            return json.dumps(self._data, ensure_ascii=False)
        return self._data

    @classmethod
    def reproduce(cls, url, current_page):
        cls.url = url
        cls._current_page = current_page
        return cls()

    def save2file(self):
        with open(self.get_filename(), 'w') as fp:
            fp.write(self.get_data())

    @abstractmethod
    def scrap(self, soup: BeautifulSoup):
        ...
