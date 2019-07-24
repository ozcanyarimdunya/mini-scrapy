from bs4 import BeautifulSoup

from base import BaseScrapper


class StreamingScrapper(BaseScrapper):
    base_url = 'https://www.tvyayinakisi.com'
    url = base_url + '/yayinda-olanlar'
    as_json = True
    save_as_file = True
    filename = 'streaming.json'

    def scrap(self, soup: BeautifulSoup):
        for channel in soup.select('a.channel-card'):
            yield {
                'url': channel.attrs.get('href'),
                'logo': channel.select_one('.logo img').attrs.get('src'),
                'name': channel.select_one('.name span').get_text(strip=True),
                'time': channel.select_one('p.time').get_text(strip=True),
                'type': channel.select_one('p.type').get_text(strip=True),

            }


if __name__ == '__main__':
    StreamingScrapper()
