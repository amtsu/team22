#!/usr/local/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib
import urllib.request

"""
Парсер для сайта застройщика "ПИК"
"""

class PagePerser:
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
        except:
            print("Error url =", url)
        return self.__page

    def use_b_soup(self):
        b_soup = BeautifulSoup(self.open_page(), features="html.parser")
        return b_soup
    
class PIKParsing:
    """
    Собирает данные с сайта https://www.pik.ru/search очищает их, сохряняет
    """
    def __init__(self, url: str):
        self.__url = url
        self.__page = PagePerser(self.__url)
        self.__b_soup = self.__page.use_b_soup()
        self.__items_list = self.__b_soup.findAll("a", class_ = "styles__FlatCardRow-izq3tk-0 bncElg")
        
    def get_title(self):
        if not self.__items_list == []: 
            for item in self.__items_list:
                title_data = item.findAll("div", class_ = "styles__RoomsArea-m4iiyq-1 mKsPL")
                title = title_data[0].text
                print(title)

    
    