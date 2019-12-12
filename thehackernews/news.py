from bs4 import BeautifulSoup

from base import BaseScrapper


class TheHackerNewsScrapper(BaseScrapper):
    url = 'https://thehackernews.com/'
    next_selector = '.blog-pager-older-link-mobile'
    filename = 'news.json'
    max_result = 5

    def scrap(self, soup: BeautifulSoup):
        print('Current page: {}/{}'.format(self.get_current_page(), '~'), end='\r')
        for post in soup.select('.body-post'):
            yield {
                'url': post.select_one('.story-link').attrs.get('href'),
                'img': post.select_one('img.home-img-src').attrs.get('data-src'),
                'title': post.select_one('h2.home-title').get_text(strip=True),
                'description': post.select_one('.home-desc').get_text(strip=True),
            }


if __name__ == '__main__':
    TheHackerNewsScrapper()
