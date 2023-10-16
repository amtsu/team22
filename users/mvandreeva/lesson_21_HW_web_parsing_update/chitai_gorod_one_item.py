#!/usr/local/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
from web_parsing import PageParsing

class ChitaiGorodGetElement:
    
    """
    Класс получает данные со страницы товара, "очищает" эти данные для последующей обработки
    """
    
    def clean_data(self): 
        """ метод очистки данных"""
        if not self.__to_int:    
            if not len(self.__remove) == 1:
                bad_data = self.__get_text()[0].replace(self.__remove[0], "")
                self.__remove.pop(0)
            else:
                good_data = self.__get_text()[0].replace(self.__remove[0], "")

        else:
            if not len(self.__remove) == 1:
                bad_data = self.__get_text()[0].replace(self.__remove[0], "")
                self.__remove.pop(0)
            else:
                bad_data = self.__get_text()[0].replace(self.__remove[0], "")
                good_data = int(bad_data)
        return good_data
    
    def __get_text(self) -> list: # подумать над методом поиска тега и класса
        """
        Метод получения текстового значения искомого элемента (не очищенного)
        """
        data_list = self.__b_soup.findAll(self.__tag, class_ = self.__class_name)
        if data_list == []:
            assert False
        else:
            data = []
            for index, element in enumerate(data_list):
                data.append(element.__text)
                print((index + 1), element.__text)
        return data
    
    def __init__(self, b_soup, remove: list, to_int, tag: str, class_name: str):
        self.__b_soup = b_soup
        self.__remove = remove
        self.__to_int = to_int
        self.__tag = tag
        self.__class_name = class_name
        
        
        
class ChitaiGorodGetPrice(ChitaiGorodGetElement):
    #нужен ли класс PriceSaleElement, если основной класс итак загружает актуальную цену ввиду специфики сайта?
    """
    Получает цену со страницы товара сайта chitai-gorod
    """
    
    def clean_data(self) -> int:
        """ очистка данных - получение итоговой цены """
        bad_data = self.__get_text()
        bad_data = bad_data.replace("\n      ", "")
        bad_data = bad_data.replace("\xa0", "")
        bad_data = bad_data.replace(" ₽\n    ", "")
        good_data = int(bad_data)
        return good_data
    
    def __get_text(self): 
        data_list = self.__b_soup.findAll('span', class_='product-detail-offer-header__price-currency')
        #print (len(data_list))
        assert len(data_list) == 1
        element = data_list[0]
        #print(element)
        #data = [] # это и 4 строки ниже оставила чтоб смотреть символы для удаления
        #for index, element in enumerate(data_list):
        #    data.append(element.__text)
            #print((index + 1), element.__text)
        #print(prices)
        return element.text
    
    def __init__(self, page_text: str, url: str):
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")
        
class ChitaiGorodGetTitle(ChitaiGorodGetElement): # не работает: 
    # При загрузке страницы вручную заголовок находится в теге h1, а при загрузке через BS данного тега нет.
    """
    Получает наименование со страницы товара сайта chitai-gorod
    """
    
    def clean_data(self) -> str:
        """ очистка данных - получение итогового наименования """
        bad_data = self.__get_text()
        bad_data = bad_data.replace("\n      ", "")
        bad_data = bad_data.replace("\xa0", "")
        good_data = bad_data.replace(" ₽\n    ", "")
        
        return good_data
    
    def __get_text(self):
        #print(self.__b_soup)
        data_list = self.__b_soup.findAll("div", class_ = "product-title__head") #Не находит!
        #print (data_list)
        #print (len(data_list))
        assert len(data_list) == 1
        element = data_list[0]
        #print(element)
        #data = [] # это и 4 строки ниже оставила чтоб смотреть символы для удаления
        #for index, element in enumerate(data_list):
        #    data.append(element.__text)
            #print((index + 1), element.__text)
        #print(prices)
        return element.text
    
    def __init__(self, page_text: str, url: str):
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")
        

class ChitaiGorodGetAuthor(ChitaiGorodGetElement):
    
    """
    Получает автора со страницы товара сайта chitai-gorod
    """
    
    def clean_data(self) -> str:
        """ очистка данных - получение итоговой цены """
        bad_data = self.__get_text()
        bad_data = bad_data.replace("\n          ", "")
        good_data = bad_data.replace("\n        ", "")
        
        return good_data
    
    def __get_text(self):
        data_list = self.__b_soup.findAll('a', class_='product-detail-title__author')
        #print (len(data_list))
        assert len(data_list) == 1
        element = data_list[0]
        #print(element)
        #data = [] # это и 4 строки ниже оставила чтоб смотреть символы для удаления
        #for index, element in enumerate(data_list):
        #    data.append(element.__text)
        #    print((index + 1), element.__text)
        #print(data)
        return element.text
    
    def __init__(self, page_text: str, url: str):
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")
        
        
class ChitaiGorodGetAuthorURL(ChitaiGorodGetElement):
    
    """
    Получает ссылку на автора со страницы товара сайта chitai-gorod
    """
    
    def clean_data(self):
        good_data = self.__get_text()
    
    def __get_text(self):
        data_list = self.__b_soup.findAll('a', class_='product-detail-title__author')
        #print (len(data_list))
        assert len(data_list) == 1
        element = data_list[0]["href"]
        #print(element)
        #data = [] # это и 4 строки ниже оставила чтоб смотреть символы для удаления
        #for index, element in enumerate(data_list):
        #    data.append(element.__text)
        #    print((index + 1), element.__text)
        #print(data)
        return element
    
    def __init__(self, page_text: str, url: str):
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")