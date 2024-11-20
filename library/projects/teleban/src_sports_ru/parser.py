import logging
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from data import ContentBase

logging.basicConfig(level=logging.ERROR)


class SportsRuParser:
    """
    Класс для парсинга контента с сайта sports.ru.
    """
    BASE_URL = 'https://www.sports.ru'

    def __init__(self):
        self.sports_sections = {
            'sports_nba': f"{self.BASE_URL}/basketball/tournament/nba/",
            'sports_nfl': f"{self.BASE_URL}/amfootball/tournament/nfl/",
            'sports_nhl': f"{self.BASE_URL}/hockey/tournament/nhl/"
        }

    @staticmethod
    def __get_soup(url: str) -> BeautifulSoup:
        """
        Возвращает объект BeautifulSoup для указанного URL.
        """
        response = requests.get(url)
        response.raise_for_status()  # Проверка статуса ответа
        return BeautifulSoup(response.content, 'lxml')

    def __fetch_news_links(self, news_link: str) -> list[str]:
        """
        Получает список ссылок на статьи с указанной страницы.
        """
        soup = self.__get_soup(news_link)
        return [
            f"{self.BASE_URL}{element.get('href')}"
            for element in soup.find_all('a', class_='short-text')
        ]

    def __parse_article(self, link: str, source: str) -> ContentBase:
        """
        Парсит статью и создает объект ContentBase.
        """
        soup = self.__get_soup(link)
        title = soup.find('h1', class_='document-header__title').text.strip()
        tags = [tag.text for tag in soup.find_all('span', class_='tags-list-item__title')]

        return ContentBase(
            title=title,
            link=link,
            source=source,
            tags=tags,
            date_time=datetime.now(),
            status=False
        )

    def __news_feed_parsing(self, news_link: str, source: str) -> list[ContentBase]:
        """
        Парсит новости с указанной ссылки и возвращает список объектов ContentBase.
        """
        news_links = self.__fetch_news_links(news_link)
        result = []

        for link in news_links:
            try:
                result.append(self.__parse_article(link, source))
            except Exception as e:
                logging.error(f"Ошибка при обработке ссылки {link}: {e}")

        return result

    def get_new_content(self) -> list[ContentBase]:
        """
        Собирает и возвращает все новости со всех указанных источников.
        """
        result = []

        for source, link in self.sports_sections.items():
            result.extend(self.__news_feed_parsing(link, source))

        return result


if __name__ == "__main__":
    for article in SportsRuParser().get_new_content():
        print(article.source, article.title)
