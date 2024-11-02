import requests
from bs4 import BeautifulSoup

from config import DB_NAME
from db_managers.content_manager import ContentDatabaseManager


class TrialSportRuParser:
    """
    Класс содержит методы для парсинга контента с сайта.
    """

    def __init__(self, db_path: str):
        self.__db_path = db_path
        self.__base_url = 'https://trial-sport.ru'

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
        # получаем HTML-страницу при помощи метода get_soup
        post_list_html: BeautifulSoup = self.__get_soup(self.__base_url + '/news.php')
        # парсим с этой страницы ссылки на все статьи
        post_links = [self.__base_url + article.find('a').get('href') for article in
                      post_list_html.body.find_all('div', 'article')]

        for link in post_links:  # пробегаемся циклом по каждой ссылке
            try:
                # получаем HTML-страницу при помощи метода get_soup
                post_html: BeautifulSoup = self.__get_soup(link)
                # парсим название страницы
                post_title = post_html.body.find('h2').text.strip()
                # парсим теги со страницы
                tags = [tag.text for item in post_html.body.find_all('p', 'lite') for tag in item.find_all('a')]
                # преобразуем список тегов в строку, указав их через запятую
                tags = ','.join(tags)

                if not tags:  # выбрасываем исключение, если на странице нет тегов
                    raise ValueError('Статья без тегов не нужна!')

                # записываем все в базу данных
                with ContentDatabaseManager('content_trial_sport_ru', self.__db_path) as db:
                    db.add_content(post_title, link, 'trial-sport', tags)

            except Exception as e:  # выводим в консоль информацию о нерабочих ссылках
                print(e, link)


if __name__ == "__main__":
    TrialSportRuParser('../' + DB_NAME).get_new_content()
