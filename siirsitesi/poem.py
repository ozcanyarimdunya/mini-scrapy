from bs4 import BeautifulSoup

from base import BaseScrapper


class PoetristScrapper(BaseScrapper):
    url = 'http://siir.sitesi.web.tr/nazim-hikmet/yasamaya-dair-1-2-3.html'
    as_json = True
    save_as_file = True
    filename = 'poem.json'

    def scrap(self, soup: BeautifulSoup):
        yield {
            'name': soup.select_one('.text p').get_text()
        }


if __name__ == '__main__':
    PoetristScrapper()
