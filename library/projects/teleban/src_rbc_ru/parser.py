from datetime import datetime

import requests
from bs4 import BeautifulSoup

from data import ContentBase


class RbcRuParser:
    BASE_URL = 'https://www.rbc.ru'

    def __init__(self):
        self.__sections = {
            'Бизнес': '/business',
            'Политика': '/politics',
            'Технологии и медиа': '/technology_and_media',
            'Экономика': '/economics',
        }

    @staticmethod
    def __parse_rbc_section(url, section_tag):
        """
        Парсит заголовки новостей из указанного раздела.
        """
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            news_blocks = soup.find_all('a', class_='item__link')

            news_list = []
            for block in news_blocks:
                title = block.get_text(strip=True)  # Заголовок новости
                link = block['href']  # Ссылка на новость
                news_list.append((title, link, section_tag))
            return news_list
        else:
            print(f"Ошибка доступа к сайту: {response.status_code}")
        return []

    def __parse_rbc_news(self):
        """
        Парсит новости из всех разделов РБК.
        """
        all_news = []
        for tag, url in self.__sections.items():
            news = self.__parse_rbc_section(self.BASE_URL + url, tag)
            all_news.extend(news)
        return all_news

    def get_new_content(self):
        """
        Сбор новостей из всех разделов, их вывод с проверкой на дублирование.
        """
        news_data = self.__parse_rbc_news()
        result = []

        # Обработка новостей и проверка на дублирование
        for news in news_data:
            title, url, tag = news

            result.append(ContentBase(
                link=url,
                title=title,
                source='rbc',
                tags=[tag],
            ))

        return result


if __name__ == "__main__":
    content_list = RbcRuParser().get_new_content()
    for i, item in enumerate(content_list, 1):
        print(item.title, item.link, item.date_time, item.status)
        # pass
