#!/usr/local/bin/python
# coding: utf-8
"""
Парсер для сайта застройщика 'CapitalGroup', проект 'Триколор'
"""
import urllib
import urllib.request
from urllib.parse import quote, urlsplit, urlunsplit

from bs4 import BeautifulSoup

class PageParser:
    """
    Производит открытие страницы, её первичную обработку
    """

    def __init__(self, url: str):
        self.__url = url
        self.__page = ""
        self.b_soup = None

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
    
    def open_page_encode(self):
        """
        Открывает страницу, требующую изменение кодировки (пример - домен на кириллице)
        """
        parts = list(urlsplit(self.__url))
        parts[0] = quote(parts[0], safe=':/?&')
        parts[1] = parts[1].encode('idna').decode('ascii')
        parts[2] = quote(parts[2], safe=':/?&')
        parts[3] = quote(parts[3], safe=':/?&')
        parts[4] = quote(parts[4], safe=':/?&')
        url = urlunsplit(parts)
        try:
            with urllib.request.urlopen(url) as page:
                self.__page = page.read() 
            # page_text = str(self.__page) # отд. скрипт или здесь разово сохранить в файл
            # with open("sources/nash_dom" , "w") as w_file:
            #     w_file.writelines(page_text)
            self.b_soup = BeautifulSoup(self.__page, features="html.parser")
        except (urllib.request.HTTPError, urllib.request.URLError):
            print("Error url =", self.__url)
        return self.b_soup

    def use_b_soup(self):
        """
        Создает объект класса BeautifulSoup
        """
        self.b_soup = BeautifulSoup(self.open_page(), features="html.parser")
        return self.b_soup