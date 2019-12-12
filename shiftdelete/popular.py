from bs4 import BeautifulSoup

from base import BaseScrapper


class PopularScrapper(BaseScrapper):
    url = 'https://shiftdelete.net/enler-haber'
    filename = 'popular.json'

    def scrap(self, soup: BeautifulSoup):
        for article in soup.select('li.newone'):
            yield {
                'img': article.select_one('img.u-photo').attrs.get('src'),
                'title': article.select_one('em.p-name').get_text(strip=True),
                'description': article.select_one('p.e-description').get_text(strip=True),
            }


if __name__ == '__main__':
    PopularScrapper()
