from bs4 import BeautifulSoup

from base import BaseScrapper


class RatingScrapper(BaseScrapper):
    base_url = 'https://www.tvyayinakisi.com'
    url = base_url + '/reyting'
    as_json = True
    save_as_file = True
    filename = 'rating.json'

    def scrap(self, soup: BeautifulSoup):
        for rating in soup.select('tbody#total tr'):
            td_list = rating.select('td')
            yield {
                'order': td_list[0].get_text(strip=True),
                'title': td_list[1].get_text(strip=True),
                'channel': td_list[2].get_text(strip=True),
                'date': td_list[3].get_text(strip=True),
                'startDate': td_list[4].get_text(strip=True),
                'endDate': td_list[5].get_text(strip=True),
                'category': td_list[6].get_text(strip=True),
                'rtg': td_list[7].get_text(strip=True),
                'share': td_list[8].get_text(strip=True),
            }


if __name__ == '__main__':
    RatingScrapper()
