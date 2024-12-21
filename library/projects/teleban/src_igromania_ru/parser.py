import logging

import requests
from bs4 import BeautifulSoup

from data import ContentBase
from src_igromania_ru.text_data import IGROMANIA_SECTIONS

logging.basicConfig(level=logging.ERROR)


class IgromaniaRuParser:
    """
    Класс для парсинга контента с сайта igromania.ru.
    """
    BASE_URL = 'https://www.igromania.ru'

    def __init__(self):
        self.source = 'igromania'
        self.sections = IGROMANIA_SECTIONS

    @staticmethod
    def __get_soup(url: str) -> BeautifulSoup:
        """
        Возвращает объект BeautifulSoup для указанного URL.
        """
        response = requests.get(url)
        response.raise_for_status()  # Проверка статуса ответа
        return BeautifulSoup(response.content, 'lxml')

    def __fetch_post_data(self, tag: str, slug: str) -> list[ContentBase]:
        """
        Получает список ссылок на статьи с указанной страницы.
        """
        result = []
        link = self.BASE_URL + slug

        try:
            post_list_html: BeautifulSoup = self.__get_soup(link)
            posts = post_list_html.find_all('div', 'ShelfCard_card__GrWrN')
            links = [post.find_next('a').get('href') for post in posts]
            titles = [post.find_next('a').text for post in posts]
            # tag_elements = [post.find_next('div', 'ShelfCard_cardFooter__tkRln') for post in posts]
            # tags = [a.text.removeprefix('#').split('#') for a in tag_elements]
        except Exception as err:
            print(err, link)
        else:
            for post in zip(links, titles):
                result.append(ContentBase(
                    link=self.BASE_URL + post[0],
                    title=post[1],
                    source=self.source,
                    tags=[tag],
                ))

        return result

    def get_new_content(self):
        result = []
        for tag, slug in self.sections.items():
            result.extend(self.__fetch_post_data(tag, slug))
        return result


if __name__ == "__main__":
    test_list = []
    for i in IgromaniaRuParser().get_new_content():
        print(i.source, i.link, '\n', i.title, '\n', i.tags, '\n')
