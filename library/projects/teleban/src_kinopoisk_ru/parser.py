import requests
from bs4 import BeautifulSoup

from text_data import KINOPOISK_RU_DICTIONARY


# пока не работает
class KinopoiskRuParser:
    """
    Класс содержит методы для парсинга контента с сайта.
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.__base_url = 'https://www.kinopoisk.ru'

    @staticmethod
    def __get_soup(url: str) -> BeautifulSoup:
        """
        Метод делает из веб-страницы и возвращает объект BeautifulSoup для дальнейшего разбора.
        """
        return BeautifulSoup(requests.get(url).content, 'lxml')

    def get_new_content(self, link):
        """
        Метод получает ссылки на все статьи, их заголовки и теги.
        Записывает все в БД.
        """
        post_list_html: BeautifulSoup = self.__get_soup(link)
        # парсим с этой страницы ссылки на все статьи
        post_links = [self.__base_url + article.get('href') for article in
                      post_list_html.body.find_all('a', 'rHg73hUuhIU9jiVJ6itV')]
        print(8, post_links)
        return post_links

        # for link in post_links:  # пробегаемся циклом по каждой ссылке
        #     try:
        #         # получаем HTML-страницу при помощи метода get_soup
        #         post_html: BeautifulSoup = self.__get_soup(link)
        #         # парсим название страницы
        #         post_title = post_html.body.find('span').text.strip()
        #         print(post_title)
        #         # парсим теги со страницы
        #
        #
        #
        #         tags = [tag.text for item in post_html.body.find_all('p', 'lite') for tag in item.find_all('a')]
        #         # преобразуем список тегов в строку, указав их через запятую
        #         tags = ','.join(tags)
        #
        #         if not tags:  # выбрасываем исключение, если на странице нет тегов
        #             raise ValueError('Статья без тегов не нужна!')
        #
        #         # записываем все в базу данных
        #         with ContentDatabaseManager('content_kinopoisk_ru', self.__db_path) as db:
        #             db.add_content(post_title, link, 'kinopoisk', tags)
        #
        #     except Exception as e:  # выводим в консоль информацию о нерабочих ссылках
        #         print(e, link)

    def get_all_news(self):
        for val in KINOPOISK_RU_DICTIONARY.values():
            link = self.__base_url + val
            print(link)
            post_list = self.get_new_content(link)
            print(post_list)


if __name__ == "__main__":
    KinopoiskRuParser('test_kino').get_all_news()
