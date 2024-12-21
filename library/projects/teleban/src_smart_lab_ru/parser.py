import logging
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from data import ContentBase

logging.basicConfig(level=logging.ERROR)


class SmartLabRuParser:
    """
    Класс для парсинга контента с сайта smart-lab.ru.
    """
    BASE_URL = 'https://smart-lab.ru'

    def __init__(self):
        self.source = 'smart_lab'
        self.news_url = f"{self.BASE_URL}/news"

    @staticmethod
    def __get_soup(url: str) -> BeautifulSoup:
        """
        Возвращает объект BeautifulSoup для указанного URL.
        """
        response = requests.get(url)
        response.raise_for_status()  # Проверка статуса ответа
        return BeautifulSoup(response.content, 'lxml')

    def __fetch_article_links(self) -> list[str]:
        """
        Получает список ссылок на статьи с главной страницы новостей.
        """
        soup = self.__get_soup(self.news_url)
        result = [
            f"{self.BASE_URL}{article.find('a').get('href')}"
            for article in soup.find_all('div', class_='inside')
        ]
        return result

    def __parse_article(self, link: str) -> ContentBase:
        """
        Парсит пост и возвращает объект ContentBase.
        """
        soup = self.__get_soup(link)
        title = soup.find('h1').find_next('span').text.strip()
        tags = [tag.text for item in soup.find_all('ul', class_='tags') for tag in item.find_all('a')]

        return ContentBase(
            title=title,
            link=link,
            source=self.source,
            tags=tags,
        )

    def get_new_content(self) -> list[ContentBase]:
        """
        Собирает все статьи с сайта и возвращает список объектов ContentBase.
        """
        result = []
        try:
            article_links = self.__fetch_article_links()

            for link in article_links:
                try:
                    result.append(self.__parse_article(link))
                except Exception as e:
                    logging.error(f"Ошибка при обработке статьи {link}: {e}")
        except Exception as e:
            logging.error(f"Ошибка при получении списка статей: {e}")

        return result


if __name__ == "__main__":
    for post in SmartLabRuParser().get_new_content():
        print(post.source, post.link, '\n', post.title, '\n', post.tags, '\n')
