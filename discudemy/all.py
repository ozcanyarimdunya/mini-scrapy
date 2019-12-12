from bs4 import BeautifulSoup

from base import BaseScrapper


class CourseScrapper(BaseScrapper):
    url = 'https://www.discudemy.com/all'
    filename = 'all.json'
    max_result = 100
    next_selector = 'ul.pagination3 li a'

    def get_next_url(self):
        try:
            return self.get_soup().select(self.get_next_selector())[-1].attrs.get('href')
        except:
            return

    def scrap(self, soup: BeautifulSoup):
        for course in soup.select('section.card'):
            language = course.select_one('label').get_text(strip=True)
            if language == 'Ads':
                return

            yield {
                'language': language,
                'link': course.select_one('a.card-header').attrs.get('href'),
                'title': course.select_one('a.card-header').get_text(strip=True),
                'date': course.select_one('.meta span.category').extract().get_text(strip=True),
                'price': course.select_one('.meta span').get_text(strip=True),
                'image': course.select_one('.image amp-img').attrs.get('src'),
                'description': course.select_one('.description').get_text(strip=True),
                'category': course.select_one('.catSpan').get_text(strip=True),
            }


if __name__ == '__main__':
    CourseScrapper()
