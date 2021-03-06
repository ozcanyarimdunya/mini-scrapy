from bs4 import BeautifulSoup

from base import BaseScrapper


class RealPythonScrapper(BaseScrapper):
    url = 'https://realpython.com'
    filename = 'all.json'

    def scrap(self, soup: BeautifulSoup):
        for lesson in soup.select('.card.border-0'):
            yield {
                'link': self.url + lesson.select_one('a').attrs.get('href'),
                'image': lesson.select_one('a img').attrs.get('src'),
                'text': lesson.select_one('.card-title').get_text(strip=True),
                'date': lesson.select_one('.text-muted span').get_text(strip=True),
            }


if __name__ == '__main__':
    RealPythonScrapper()
