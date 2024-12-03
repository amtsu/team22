from datetime import datetime
import requests
from bs4 import BeautifulSoup

from data import ContentBase

class AutoRuParser:
    BASE_URL = 'https://auto.ru'

    def __init__(self):
        """
        Инициализация парсера для Auto.ru.
        """
        self.__sections = {
            'Новости': '/mag/theme/news/',
            'Тесты': '/mag/theme/tests/',
            'Видео': '/mag/theme/video/',
            'Разбор': '/mag/theme/razbor/',
            'Игры': '/mag/theme/games/',
            'Подборки': '/mag/theme/lists/',
            'Учебник': '/mag/theme/uchebnik/',
            'Про бизнес': '/mag/theme/pro_business/',
        }

    @staticmethod
    def __parse_auto_section(url, section_tag):
        """
        Парсит заголовки новостей из указанного раздела Auto.ru.
        """
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            # Изменяем поиск элементов под структуру Auto.ru
            news_blocks = soup.find_all('a', class_='ArticleItem')

            news_list = []
            for block in news_blocks:
                title = block.find('h3', class_='ArticleItem__title').get_text(strip=True)
                link = block['href']
                news_list.append((title, link, section_tag))
            return news_list
        else:
            print(f"Ошибка доступа к сайту: {response.status_code}")
        return []

    def __parse_auto_news(self):
        """
        Парсит новости из всех разделов Auto.ru.
        """
        all_news = []
        for tag, url in self.__sections.items():
            news = self.__parse_auto_section(self.BASE_URL + url, tag)
            all_news.extend(news)
        return all_news

    def get_new_content(self):
        """
        Сбор новостей из всех разделов, их вывод с проверкой на дублирование.
        """
        news_data = self.__parse_auto_news()
        result = []

        # Обработка новостей и проверка на дублирование
        for news in news_data:
            title, url, tag = news

            result.append(ContentBase(
                link=url,
                title=title,
                source='auto_ru',
                tags=[tag],
            ))

        return result

if __name__ == "__main__":
    content_list = AutoRuParser().get_new_content()
    for i, item in enumerate(content_list, 1):
        print(item.title, item.link, item.date_time, item.status)
