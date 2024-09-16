import requests
from bs4 import BeautifulSoup

from config import DB_NAME
from db_managers.content_manager import ContentDatabaseManager

BASE_URL = 'https://trial-sport.ru'


class SportsRuParser:
    """
    Класс содержит методы для парсинга контента с сайта.
    """

    def __init__(self, source_link):
        self.__link = source_link

    @staticmethod
    def get_soup(url: str) -> BeautifulSoup:
        """
        Метод делает из веб-страницы и возвращает объект BeautifulSoup для дальнейшего разбора.
        """
        return BeautifulSoup(requests.get(url).content, 'lxml')

    def get_new_content(self):
        """
        Метод получает ссылки на все статьи, их заголовки и теги.
        Записывает все в БД.
        """
        # получаем HTML-страницу при помощи метода get_soup
        post_list_html: BeautifulSoup = self.get_soup(self.__link + '/news.php')
        # парсим с этой страницы ссылки на все статьи
        post_links = [article.find('a').get('href') for article in post_list_html.body.find_all('div', 'article')]

        for link in post_links:  # пробегаемся циклом по каждой ссылке
            try:
                # получаем HTML-страницу при помощи метода get_soup
                post_html: BeautifulSoup = self.get_soup(BASE_URL + link)
                # парсим название страницы
                post_title = post_html.body.find('h2').text.strip()
                # парсим теги со страницы
                tags = [[tag.text for tag in item.find_all('a')] for item in post_html.body.find_all('p', 'lite')]
                # преобразуем список тегов в строку, указав их через запятую
                tags = ','.join(tags[0])

                if not tags:  # выбрасываем исключение, если на странице нет тегов
                    raise ValueError('Статья без тегов не нужна!')

                # записываем все в базу данных
                with ContentDatabaseManager('content_trial_sport_ru', '../' + DB_NAME) as db:
                    db.add_content(post_title, link, tags)

            except Exception as e:  # выводим в консоль информацию о нерабочих ссылках
                print(e, link)


if __name__ == "__main__":
    SportsRuParser(BASE_URL).get_new_content()
