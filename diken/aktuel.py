import requests
from bs4 import BeautifulSoup

from base import BaseScrapper


class DikenScrapper(BaseScrapper):
    url = 'http://www.diken.com.tr'
    filename = 'aktuel.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
    }

    def perform_request(self):
        return requests.get(self.get_url(), headers=self.headers)

    def scrap(self, soup: BeautifulSoup):
        for lesson in soup.select('article.category-aktuel'):
            yield {
                'link': lesson.select_one('header a').attrs.get('href'),
                'image': lesson.select_one('a img').attrs.get('src'),
                'text': lesson.select_one('header a').get_text(strip=True),
            }


if __name__ == '__main__':
    DikenScrapper()
