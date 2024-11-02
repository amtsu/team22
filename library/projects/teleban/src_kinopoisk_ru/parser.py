import requests
from bs4 import BeautifulSoup

from config import DB_NAME
from db_managers.content_manager import ContentDatabaseManager

class KinopoiskRuParser:
    """
    Класс содержит методы для парсинга контента с сайта.
    """

    def __init__(self, db_path: str):
        self.__db_path = db_path
        self.__base_url = 'https://www.kinopoisk.ru/media/'

    @staticmethod
    def __get_soup(url: str) -> BeautifulSoup:
        """
        Метод делает из веб-страницы и возвращает объект BeautifulSoup для дальнейшего разбора.
        """
        return BeautifulSoup(requests.get(url).content, 'lxml')

    def get_new_content(self):
        """
        Метод получает ссылки на все статьи, их заголовки и теги.
        Записывает все в БД.
        """
        post_list_html: BeautifulSoup = self.__get_soup(self.__base_url)
        post_links = [self.__base_url + article.find('a').get('href') for article in
                      post_list_html.body.find_all('class', 'article')]
        print(post_links,5)


if __name__ == "__main__":
    KinopoiskRuParser('../' + DB_NAME).get_new_content()