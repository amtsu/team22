import requests
from bs4 import BeautifulSoup
#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB_NAME
from db_managers.content_manager import ContentDatabaseManager
class HabrComParser:
    def __init__(self, db_path: str):
        self.__db_path = db_path
        self.__base_url = 'https://habr.com'
        self.__articles_news_link = self.__base_url + '/ru/articles/'
        self.__posts_news_link = self.__base_url + '/ru/posts/'
    @staticmethod
    def get_soup(url: str) -> BeautifulSoup:
        """
        Метод делает из веб-страницы и возвращает объект BeautifulSoup для дальнейшего разбора.
        """
        return BeautifulSoup(requests.get(url).content, 'lxml')

    def get_new_content(self):
        post_list_html: BeautifulSoup = self.get_soup(self.__articles_news_link)

        post_links = [self.__base_url + item.get('href') for item in post_list_html.body.find_all('a', 'tm-title__link')]
        #print(post_links)
        for link in post_links:
            try:
                print('!-------!')
                post_html: BeautifulSoup = self.get_soup(link)
                post_title = post_html.body.find('h1', 'tm-title tm-title_h1').text.strip()
                print(post_title)
                #tags = [item.text for item in post_html.body.find_all('span', 'tags-list-item__title')]
                tags = [span.text for a in post_html.body.find_all('a', 'tm-publication-hub__link') for span in
                        a.find_all('span')]
                tags = ','.join(tags)
                print(tags)

                with ContentDatabaseManager('content_habr_com', self.__db_path) as db:
                    db.add_content(post_title, link, 'habr', tags)

            except Exception as e:
                print(e, link)

if __name__ == "__main__":
    HabrComParser('../' + DB_NAME).get_new_content()