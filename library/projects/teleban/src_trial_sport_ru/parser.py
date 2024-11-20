import logging
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from data import ContentBase

logging.basicConfig(level=logging.ERROR)


class TrialSportRuParser:
    """
    Класс для парсинга контента с сайта trial-sport.ru.
    """
    BASE_URL = 'https://trial-sport.ru'
    NEWS_URL = f"{BASE_URL}/news.php"

    def __init__(self):
        self.source = 'trial-sport'

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
        soup = self.__get_soup(self.NEWS_URL)
        return [
            f"{self.BASE_URL}{article.find('a').get('href')}"
            for article in soup.find_all('div', class_='article')
        ]

    def __parse_article(self, link: str) -> ContentBase:
        """
        Парсит статью и возвращает объект ContentBase.
        """
        soup = self.__get_soup(link)
        title = soup.find('h2').text.strip()
        tags = [tag.text for item in soup.find_all('p', class_='lite') for tag in item.find_all('a')]

        if not tags:
            raise ValueError("Статья без тегов пропущена.")

        return ContentBase(
            title=title,
            link=link,
            source=self.source,
            tags=tags,
            date_time=datetime.now(),
            status=False
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
    for article in TrialSportRuParser().get_new_content():
        print(article.source, article.title, article.tags, article.link)
