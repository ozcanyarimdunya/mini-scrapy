from bs4 import BeautifulSoup

from base import BaseScrapper


class TrendingScrapper(BaseScrapper):
    base_url = 'https://github.com'
    url = base_url + '/trending'
    as_json = True
    save_as_file = True
    filename = 'trending.json'

    def scrap(self, soup: BeautifulSoup):
        for trend in soup.select('article.Box-row'):
            title = trend.select_one('h1.lh-condensed a').get_text(strip=True)
            url = self.base_url + trend.select_one('h1.lh-condensed a').attrs.get('href')
            stars = trend.select_one('a.muted-link.d-inline-block.mr-3').get_text(strip=True)
            language = trend.find('span', {'itemprop': 'programmingLanguage'})
            language = language.get_text(strip=True) if language else None
            description = trend.select_one('p.col-9.text-gray.my-1.pr-4').get_text(strip=True)
            today_star = trend.select_one('span.d-inline-block.float-sm-right').get_text(strip=True)

            yield {
                'title': title,
                'url': url,
                'stars': stars,
                'language': language,
                'description': description,
                'today_star': today_star,
            }


if __name__ == '__main__':
    TrendingScrapper()
