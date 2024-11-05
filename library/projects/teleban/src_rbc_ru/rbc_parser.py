import requests
from bs4 import BeautifulSoup
from config import DB_NAME
from db_managers/content_manager import ContentDatabaseManager

class RbcNewsParser:
    def __init__(self):
        self.__base_url = 'https://www.rbc.ru'
        self.__sections = {
            '/economics': 'economics',
            '/politics': 'politics',
            '/business': 'business',
            '/technology_and_media': 'technology_and_media'
        }
        # Путь к базе данных
        self.db_name = 'teleban.sqlite3'

    @staticmethod
    def __get_soup(url: str) -> BeautifulSoup:
        """
        Получает страницу и возвращает объект BeautifulSoup для парсинга.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            raise Exception(f"Ошибка доступа к {url}: {response.status_code}")

    def __parse_section(self, section_url: str, section_tag: str):
        """
        Парсит заголовки и ссылки из раздела и возвращает их.
        """
        full_url = self.__base_url + section_url
        soup = self.__get_soup(full_url)

        news_blocks = soup.find_all('a', class_='item__link')

        news_list = []
        for block in news_blocks:
            title = block.get_text(strip=True)
            link = block['href']
            news_list.append([title, link, section_tag])

        return news_list

    def get_all_news(self):
        """
        Парсит все разделы и возвращает список новостей с тегами.
        """
        all_news = []
        for section_url, section_tag in self.__sections.items():
            try:
                news = self.__parse_section(section_url, section_tag)
                all_news.extend(news)
            except Exception as e:
                print(f"Ошибка при парсинге раздела {section_tag}: {e}")

        return all_news

    def get_new_content(self):
        """
        Собирает новые новости из всех разделов и выводит их.
        """
        print("Сбор новых новостей...")
        new_content = self.get_all_news()

        # Пример обработки — вывод новостей
        for i, news in enumerate(new_content, 1):
            print(f"{i}. Заголовок: {news[0]}\nСсылка: {news[1]}\nТег: {news[2]}\n")

        # Сохранение новостей в базу данных
        self.save_to_db(new_content)

    def save_to_db(self, news_list):
        """
        Сохраняет собранные новости в базу данных SQLite.
        """
        try:
            with ContentDatabaseManager('content_sports_ru', self.__db_path) as db:
                db.add_content(post_title, link, source, tags)


        except Exception as e:
            print(e, link)


if __name__ == "__main__":
    parser = RbcNewsParser()
    parser.get_new_content()  # Сбор и сохранение новых новостей
