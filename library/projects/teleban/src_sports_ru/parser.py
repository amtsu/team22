import requests
from bs4 import BeautifulSoup

from config import DB_NAME
from db_managers.content_manager import ContentDatabaseManager


class SportsRuParser:
    def __init__(self, db_path: str):
        self.__db_path = db_path
        self.__base_url = 'https://www.sports.ru'
        self.__nba_news_link = self.__base_url + '/basketball/tournament/nba/'
        self.__nfl_news_link = self.__base_url + '/amfootball/tournament/nfl/'
        self.__nhl_news_link = self.__base_url + '/hockey/tournament/nhl/'

    @staticmethod
    def __get_soup(url: str) -> BeautifulSoup:
        """
        Метод делает из веб-страницы объект BeautifulSoup и возвращает его для дальнейшего разбора.
        """
        return BeautifulSoup(requests.get(url).content, 'lxml')

    def __news_feed_parsing(self, news_link: str, source: str):
        """
        Метод принимает относительную ссылку для сайта sports.ru и записывает новости с этой страницы в БД.
        """
        post_list_html: BeautifulSoup = self.__get_soup(news_link)
        post_links = [self.__base_url + item.get('href') for item in post_list_html.body.find_all('a', 'short-text')]

        for link in post_links:
            try:
                post_html: BeautifulSoup = self.__get_soup(link)
                post_title = post_html.body.find('h1', 'document-header__title').text.strip()
                tags = [item.text for item in post_html.body.find_all('span', 'tags-list-item__title')]
                tags = ','.join(tags)

                with ContentDatabaseManager('content_sports_ru', self.__db_path) as db:
                    db.add_content(post_title, link, source, tags)

            except Exception as e:
                print(e, link)

    def get_new_content(self):
        self.__news_feed_parsing(self.__nba_news_link, 'sports_nba')
        self.__news_feed_parsing(self.__nfl_news_link, 'sports_nfl')
        self.__news_feed_parsing(self.__nhl_news_link, 'sports_nhl')


if __name__ == "__main__":
    SportsRuParser('../' + DB_NAME).get_new_content()
