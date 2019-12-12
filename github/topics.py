from bs4 import BeautifulSoup

from base import BaseScrapper


class TopicScrapper(BaseScrapper):
    url = 'https://github.com/topics/python'
    filename = 'topics.json'

    def scrap(self, soup: BeautifulSoup):
        for topic in soup.select('article.border-bottom.border-gray-light.py-4'):
            yield {
                'title': topic.select_one('h3.f3 a').get_text(strip=True),
                'url': 'https://github.com' + topic.select_one('h3.f3 a').attrs.get('href'),
                'stars': topic.select_one('a.d-inline-block.link-gray').get_text(strip=True),
                'description': topic.select_one('.text-gray.mb-3.ws-normal').get_text(strip=True),
                'updated': topic.select_one('relative-time').attrs.get('datetime'),
            }


if __name__ == '__main__':
    TopicScrapper()
