#!/usr/local/bin/python
# coding: utf-8

""" модуль открытия и общей обработки web-страницы """
import urllib
import urllib.request
from bs4 import BeautifulSoup

class PageParsing:
    """ Описывает общие методы обработки одной страницы """
    def get_url(self) -> str : # посмотреть, нужен ли этот метод
        """ Возвращает переданный URL """
        return self.__url

    def list_dict(self, **kwargs): 
        """ метод формирует список словарей"""
        """
            **kwargs например: price = ChitaiGorodGetPrice(self.__page, self.__url).clean_data()
            [
                {
                    "price": ChitaiGorodGetPrice(self.__page, self.__url).clean_data(),
                    "price_sale": ChitaiGorodGetPrice(self.__page, self.__url).clean_data(),                    
                    "author": ChitaiGorodGetAuthor(self.__page, self.__url).clean_data(),
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

    def __init__(self, url: str):
        self.__url = url
        try:
            with urllib.request.urlopen(self.__url) as page:
                self.__page = page.read() # остановилась здесь
                #if not self.__page == []:
                    #print (self.__page)
                #    self.__b_soup = BeautifulSoup(self.__page, features="html.parser")
                #else:
                #    assert False
        except:
            print("Error url =", url)
        
    def get_page(self): 
        """ метод возвращает текст веб-страницы """
        #print("Page code: ", self.__page.getcode()) # переделать в метод проверки загрузки страницы
        return self.__page
        
    def __repr__(self):
        return self.__url
    
    def __str__(self):
        return self.__url