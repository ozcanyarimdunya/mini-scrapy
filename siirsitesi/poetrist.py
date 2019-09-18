from bs4 import BeautifulSoup

from base import BaseScrapper


class PoetristScrapper(BaseScrapper):
    url = 'http://siir.sitesi.web.tr/sairler.html'
    as_json = True
    save_as_file = True
    filename = 'poetrist.json'

    def scrap(self, soup: BeautifulSoup):
        for poetrist in soup.select('.siir'):
            yield {
                'name': poetrist.select_one('a').get_text(strip=True),
                'link': poetrist.select_one('a').attrs.get('href'),
            }


if __name__ == '__main__':
    PoetristScrapper()
