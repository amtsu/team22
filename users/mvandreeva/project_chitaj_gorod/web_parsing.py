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