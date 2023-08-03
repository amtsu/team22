#!/usr/local/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib
import urllib.request

"""
Парсер для сайта застройщика 'CapitalGroup', проект 'Capital Towers'
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
    
class CapTowersParser:
    """
    Собирает данные с сайта https://capitaltowers.ru/catalog/flats/ очищает их, сохряняет
    """
    def __init__(self, url: str):
        self.__url = url
        self.__page = PagePerser(self.__url)
        self.__b_soup = self.__page.use_b_soup()
        try:
            self.__items_list = self.__b_soup.findAll("a", class_ = "styles__FlatCardRow-izq3tk-0 bncElg")
        except:
            print("Error in getting items_list", self.__url)
        self.__dict_list = []
        self.__dict = {}
            
    def __get_tower_name(self):
        # if not self.__items_list == []: # прописать эти два условия там, где данные будут собираться в словарь/ список словарей
        #     for item in self.__items_list:
        tower_data = item.findAll("div", class_ = "calculator__flat-tower")
        for tower_name_data in tower_data:
            tower_name = tower_name_data.findAll("p")
            if tower_name:
                tower_name = tower_name[0].text)
            else:
                continue
                        
class CapTowersParserFFile(CapTowersParser):
    """
    Собирает данные страницы, скачанной с сайта https://capitaltowers.ru/catalog/flats/ в файл 'sources/capitaltowers' очищает их, сохряняет
    """
    def __init__(self, page_text):
        self.__url = None
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")
        self.__items_list = self.__b_soup.findAll("a", class_ = "styles__FlatCardRow-izq3tk-0 bncElg")
            