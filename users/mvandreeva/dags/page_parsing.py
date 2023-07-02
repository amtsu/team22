"""
Парсер для сайта застройщика 'CapitalGroup', проект 'Триколор'
"""
import urllib
import urllib.request
from bs4 import BeautifulSoup

class PageParser:
    """
    Производит открытие страницы, её первичную обработку
    """

    def __init__(self, url: str):
        self.__url = url
        self.__page = ""

    def open_page(self):
        """
        Открывает страницу
        """
        try:
            with urllib.request.urlopen(self.__url) as page:
                self.__page = page.read()
        except (urllib.request.HTTPError, urllib.request.URLError):
            print("Error url =", self.__url)
        return self.__page

    def use_b_soup(self):
        """
        Создает объект класса BeautifulSoup
        """
        b_soup = BeautifulSoup(self.open_page(), features="html.parser")
        return b_soup
