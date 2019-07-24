from bs4 import BeautifulSoup

from base import BaseScrapper


class GamesScrapper(BaseScrapper):
    url = 'https://shiftdelete.net/oyun'
    filename = 'games.json'
    save_as_file = True
    as_json = True
    follow = True
    next_selector = 'li.arrow.last a'
    max_result = 5  # None

    def scrap(self, soup: BeautifulSoup):
        print('Current page: {}/{}'.format(self.current_page, '~'), end='\r')
        for article in soup.select('li.full.h-card'):
            yield {
                'img': article.select_one('img.u-photo').attrs['src'],
                'date': article.select_one('i.dt-published').get_text(strip=True),
                'title': article.select_one('em.p-name').get_text(strip=True),
                'description': article.select_one('p.e-description').get_text(strip=True),
            }


if __name__ == '__main__':
    GamesScrapper()
