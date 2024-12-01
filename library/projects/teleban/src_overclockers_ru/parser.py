import logging
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from data import ContentBase
from src_overclockers_ru.text_data import OVERCLOCKERS_SECTIONS

logging.basicConfig(level=logging.ERROR)


class OverclockersRuParser:
    """
    Класс для парсинга контента с overclockers.ru.
    """
    BASE_URL = 'https://overclockers.ru'

    def __init__(self):
        self.source = 'overclockers'
        self.__sections = OVERCLOCKERS_SECTIONS

    @staticmethod
    def __get_soup(url: str) -> BeautifulSoup | None:
        """
        Возвращает объект BeautifulSoup для указанного URL.
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при подключении: {e}")
            return None

    def __fetch_article_links(self, news_url: str) -> list[tuple]:
        """
        Получает список ссылок на статьи.
        """
        soup = self.__get_soup(news_url)
        result = [
            (
                f"{self.BASE_URL}{article.find('a').get('href')}",
                article.find('a').text.strip()
            )
            for article in soup.find_all('div', class_='event')
        ]

        return result

    def get_new_content(self) -> list[ContentBase]:
        """
        Собирает все статьи с сайта и возвращает список объектов ContentBase.
        """
        result = []
        for tag, url in OVERCLOCKERS_SECTIONS.items():

            try:
                article_links = self.__fetch_article_links(self.BASE_URL + url)
                for link, title in article_links:
                    obj = ContentBase(
                        title=title,
                        link=link,
                        source=self.source,
                        tags=[tag],
                        date_time=datetime.now(),
                        status=False
                    )
                    try:
                        result.append(obj)
                    except Exception as e:
                        logging.error(f"Ошибка при обработке статьи {link}: {e}")
            except Exception as e:
                logging.error(f"Ошибка при получении списка статей: {e}")

        return result


if __name__ == "__main__":
    for article in OverclockersRuParser().get_new_content():
        print(article.source, article.tags, article.title, article.link)
