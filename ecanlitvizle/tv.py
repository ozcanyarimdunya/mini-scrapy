from bs4 import BeautifulSoup

from base import BaseScrapper


class TvScrapper(BaseScrapper):
    url = 'https://www.ecanlitvizle.live/tv/tv'
    filename = 'tv.json'
    next_selector = 'span.current'

    def get_next_url(self):
        try:
            return self.get_soup().select_one(self.get_next_selector()).next_sibling.attrs.get('href')
        except:
            return

    def scrap(self, soup: BeautifulSoup):
        print('Current page: {}/{}'.format(self.get_current_page(), '~'), end='\r')
        for channel in soup.select('ul.kanallar li'):
            yield {
                'title': channel.select_one('.kanallaradi').get_text(strip=True),
                'logo': channel.select_one('.kanallarlogo img').attrs.get('src'),
                'url': channel.select_one('a').attrs.get('href'),
            }


if __name__ == '__main__':
    TvScrapper()
