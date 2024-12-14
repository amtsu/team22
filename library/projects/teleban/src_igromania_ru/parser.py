import logging
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from data import ContentBase

from text_data import IGROMANIA_RU_DICTIONARY

logging.basicConfig(level=logging.ERROR)

class IgromaniaRuParser:
    """
    Класс для парсинга контента с сайта igromania.ru.
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.__base_url = 'https://www.igromania.ru/'

    @staticmethod
    def __get_soup(url: str) -> BeautifulSoup:
        """
        Возвращает объект BeautifulSoup для указанного URL.
        """
        response = requests.get(url)
        response.raise_for_status()  # Проверка статуса ответа
        return BeautifulSoup(response.content, 'lxml')

    def get_new_content(self, link):
        """
        Метод получает ссылки на все статьи, их заголовки и теги.
        Записывает все в БД.
        """
        post_list_html: BeautifulSoup = self.__get_soup(link)
        # парсим с этой страницы ссылки на все статьи
        post_links = [self.__base_url + article.get('href') for article in
                      post_list_html.body.find_all('h3', 'ShelfCard_cardLink__mSxdR')]
        print(8, post_links)
        return post_links

    def get_all_news(self):
        for val in IGROMANIA_RU_DICTIONARY.values():
            link = self.__base_url + val
            print(link)
            post_list = self.get_new_content(link)
            print(post_list)

    if __name__ == "__main__":
        IgromaniaRuParser('test_igromania').get_all_news()