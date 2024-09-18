import requests
from bs4 import BeautifulSoup

from db_managers.content_manager import ContentDatabaseManager

URL_NBA_NEWS = 'https://www.sports.ru/basketball/tournament/nba/'


class SportsRuParser:
    def __init__(self, source_link):
        self.__link = source_link

    @staticmethod
    def get_soup(url: str) -> BeautifulSoup:
        """
        Метод делает из веб-страницы и возвращает объект BeautifulSoup для дальнейшего разбора.
        """
        return BeautifulSoup(requests.get(url).content, 'lxml')

    def get_new_content(self):
        post_list_html: BeautifulSoup = self.get_soup(self.__link)
        post_links = [item.get('href') for item in post_list_html.body.find_all('a', 'short-text')]

        for link in post_links:
            try:
                post_html: BeautifulSoup = self.get_soup(link)
                post_title = post_html.body.find('h1', 'document-header__title').text.strip()
                tags = [item.text for item in post_html.body.find_all('span', 'tags-list-item__title')]
                tags = ','.join(tags)

                with ContentDatabaseManager('content_sports_ru') as db:
                    db.add_content(post_title, link, tags)

            except Exception as e:
                print(e, link)


if __name__ == "__main__":
    SportsRuParser(URL_NBA_NEWS).get_new_content()
