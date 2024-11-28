import requests
from bs4 import BeautifulSoup

from data import ContentBase


class HabrComParser:
    def __init__(self):
        self.__base_url = 'https://habr.com'
        self.__articles_news_link = self.__base_url + '/ru/articles/'
        self.__posts_news_link = self.__base_url + '/ru/posts/'

    @staticmethod
    def get_soup(url: str) -> BeautifulSoup:
        """
        Метод делает из веб-страницы и возвращает объект BeautifulSoup для дальнейшего разбора.
        """
        return BeautifulSoup(requests.get(url).content, 'lxml')

    def get_new_content(self):
        post_list_html: BeautifulSoup = self.get_soup(self.__articles_news_link)

        post_links = [self.__base_url + item.get('href') for item in
                      post_list_html.body.find_all('a', 'tm-title__link')]

        result = []
        for link in post_links:
            try:
                post_html: BeautifulSoup = self.get_soup(link)
                post_title = post_html.body.find('h1', 'tm-title tm-title_h1').text.strip()
                tags = [span.text for a in post_html.body.find_all('a', 'tm-publication-hub__link') for span in
                        a.find_all('span')]
                tags = [tag for tag in tags if tag != '*']
                result.append(ContentBase(
                    link=link,
                    title=post_title,
                    source='habr',
                    tags=tags,
                ))

            except Exception as e:
                print(e, link)
        return result


if __name__ == "__main__":
    for post in HabrComParser().get_new_content():
        print(post.tags, post.title)
