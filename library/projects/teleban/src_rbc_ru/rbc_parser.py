import requests
from bs4 import BeautifulSoup
from config import DB_NAME

class RbcNewsParser:
    def __init__(self, db_path: str):
        """
        Инициализация парсера РБК.
        """
        self.__db_path = db_path
        self.__base_url = 'https://www.rbc.ru'
        self.__economics_url = self.__base_url + '/economics'
        self.__politics_url = self.__base_url + '/politics'
        self.__business_url = self.__base_url + '/business'
        self.__tech_media_url = self.__base_url + '/technology_and_media'
        self.__sections = {
            'Экономика': self.__economics_url,
            'Политика': self.__politics_url,
            'Бизнес': self.__business_url,
            'Технологии и медиа': self.__tech_media_url,
        }

    def __parse_rbc_section(self, url, section_tag):
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
                news_list.append([title, link, section_tag])
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
            print("Парсинг раздела " + tag + "...")
            news = self.__parse_rbc_section(url, tag)
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

            # Проверяем, существует ли ссылка уже в списке result
            existing_item = next((item for item in result if item[1] == url), None)
            if existing_item:
                # Если ссылка существует, добавляем тег, если его ещё нет
                if tag not in existing_item[3]:
                    existing_item[3] += ',' + tag
            else:
                # Если ссылка не найдена, добавляем новую запись
                result.append([title, url, 'rbc', tag])

        # Финальный вывод
        for i, item in enumerate(result, 1):
            print(str(i) + ". Заголовок: " + item[0] + "\nСсылка: " + item[1] + "\nТег: " + item[3] + "\n")

        #print(result)

        return result


if __name__ == "__main__":
    RbcNewsParser(DB_NAME).get_new_content()
