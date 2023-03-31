#!/usr/local/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib
import urllib.request

"""
Парсер для сайта застройщика 'CapitalGroup', проект 'Триколор'
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
            print("Error url =", self.__url)
        return self.__page

    def use_b_soup(self):
        b_soup = BeautifulSoup(self.open_page(), features="html.parser")
        return b_soup