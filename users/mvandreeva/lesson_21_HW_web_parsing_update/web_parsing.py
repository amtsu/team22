#!/usr/local/bin/python
# coding: utf-8

""" модуль открытия и общей обработки web-страницы """
import urllib
import urllib.request
from bs4 import BeautifulSoup

class OnePageParsing:
    """ Описывает общие методы обработки одной страницы """
    def get_source(self) -> str :
        """ Возвращает переданный URL """
        return self.__url

    def make_list_of_dicts(self, **kwargs): # наверно лучше без универсального составителя списка словарей
        """ метод формирует список словарей"""
        """
            **kwargs например: price = ChitaiGorodGetPrice(self.__url).clean_data()
            [
                {
                    "price": ChitaiGorodGetPrice(self.__url).clean_data(),
                    "author": ChitaiGorodGetAuthor(self.__url).clean_data(),
                    ...
                }
            ]
        """
        dict_list = []
        dict_of_values = {}
        for key, value in kwargs.items():
            dict_of_values[key] = value
        dict_list.append(dict_of_values)
        return dict_list        

    #Что будет, если я запихну в __init__  сразу открытие страницы  и "приготовление супа"? чем это чревато? 
    def __init__(self, url: str):
        self.__url = url
        try:
            with urllib.request.urlopen(self.__url) as page:
                page_text = page.read()
                if not page_text == []:
                    #print (self.__page_text)
                    self.__b_soup = BeautifulSoup(page_text, features="html.parser")
                else:
                    assert False
        except:
            print("Error url =", url)
        
#    def __open_page(self):
#        """ метод открывает web-страницу """
#        with urllib.request.urlopen(self.__url) as page:
#            print("Page code: ", page.getcode())
#            page_text = page.read()
#            return page_text
        
#    def __prepare_soup(self):
#        if not self.__open_page == []:
#            #print "Soup was prepared"
#            b_soup = BeautifulSoup(self.__open_page)
#            return b_soup
#        assert False

    def read_page(self): # можно ли сюда вставить декоратор @property?
        """ метод обрабатывает web-страницу """
        #print("Page code: ", self.__page.getcode()) # переделать в метод проверки загрузки страницы
        return self.__b_soup
        
    def __repr__(self):
        return self.__url
    
    def __str__(self):
        return self.__url