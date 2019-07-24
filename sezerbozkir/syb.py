from base import BaseScrapper


class SybScrapper(BaseScrapper):
    url = 'https://www.sezerbozkir.com/'
    next_selector = '.nav-previous a'
    as_json = True
    save_as_file = True
    filename = 'syb.json'
    follow = True
    max_result = 5

    def scrap(self, soup):
        for post in soup.select('.type-post'):
            date = post.select_one('.entry-meta .date-meta a')
            yield {
                'url': post.select_one('.entry-title a').attrs.get('href'),
                'title': post.select_one('.entry-title a').get_text(strip=True),
                'htmlContent': str(post.select_one('.entry-content')),
                'date': date.get_text(strip=True) if date else None,
            }


if __name__ == '__main__':
    SybScrapper()
