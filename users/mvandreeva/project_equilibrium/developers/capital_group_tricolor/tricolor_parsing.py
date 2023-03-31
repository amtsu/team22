#!/usr/local/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib
import urllib.request

from page_parsing import PagePerser

"""
Парсер для сайта застройщика 'CapitalGroup', проект 'Триколор'
"""
    
class TricolorParser:
    """
    Собирает данные с сайта https://cg-tricolor.ru/catalog/flats очищает их, сохряняет
    """
    def _get_bulding(self, item: object) -> int:
        flat_data = item.findAll("td")
        if flat_data:
            building_str = flat_data[0].text
            building = int(building_str)
        else:
            building = None
        return building
    
    def get_dict_list(self) -> list:
        for item in self.__items_list:
            item_dict = {}
            item_dict["title"] = self._get_title(item)
            if  item_dict["title"]:
                rooms = item_dict["title"][0]
                item_dict["rooms"] = int(rooms)
            else:
                item_dict["rooms"] = None
            item_dict["bulding"] = self._get_bulding(item)
            item_dict["floor"] = self._get_floor(item)
            item_dict["square"] = self._get_square(item)
            item_dict["price"] = self._get_price(item)
            item_dict["url"] = self._get_item_url(item)
            self.__dict_list.append(item_dict)
        return self.__dict_list    
            
    def _get_floor(self, item: object) -> int:
        flat_data = item.findAll("td")
        if flat_data:
            floor_str = flat_data[1].text
            floor = int(floor_str)
        else:
            floor = None
        return floor
    
    def _get_item_url(self, item: object) -> str:
        flat_data = item.findAll("a", class_ = "results__link")
        if flat_data:
            link = flat_data[0]["href"]
            item_url = "https://cg-tricolor.ru" + link
        else:
            item_url = None
        return item_url
    
    # def _get_one_item(self, item: object): # рашила пока обойтись без него
    #     item_url = self._get_item_url(item)
    #     page = PagePerser(item_url)
    #     b_soup = page.use_b_soup()
    #     return 
    
    def _get_price(self, item: object) -> int:
        flat_data = item.findAll("td", {"sorttable_customkey" : "37775845"})
        if flat_data:
            price_data = flat_data[0].text
            price_bad =  price_data.replace("\n                        ","")
            price_bad =  price_bad.replace("\n\n\n\n\n3 – комнатная квартира 139,00м2 3 этаж №7 в корпусе \n\n\n", "")
            price_bad =  price_bad.replace("руб.", "")
            price_bad =  price_bad.replace(" ","")
            price = int(price_bad)
        else:
            price = None
        return price
    
    # def _det_rooms_data(self, item: object) -> int: # добавлю в _get_title(), т.к. есть только в title 
        
            
    def _get_square(self, item: object) -> int:
        flat_data = item.findAll("td")
        if flat_data:
            square_str = flat_data[2].text
            square = int(square_str)
        else:
            square = None
        return square
            
    def _get_title(self, item: object) -> str:
        """
        Метод получает наименование квартиры, переходя на сайт с отдельной квартирой
        """
        # if not self.__items_list == []: # прописать эти два условия там, где данные будут собираться в словарь/ список словарей
        #     for item in self.__items_list:
        item_url = self._get_item_url(item)
        page = PagePerser(item_url)
        b_soup = page.use_b_soup()
        title_data = b_soup.findAll("h1")
        if title_data:
            title = title_data[0].text
        else:
            title = None
        return title
            
    def __init__(self, url: str):
        self.__url = url
        self.__page = PagePerser(self.__url)
        self.__b_soup = self.__page.use_b_soup()
        try:
            self.__items_list = self.__b_soup.findAll("tr", class_ = "results__tr")
        except:
            print("Error in getting items_list", self.__url)
        self.__dict_list = []
        self.__dict = {}
    
                        
class TricolorParserFFile(TricolorParser):
    """
    Собирает данные страницы, скачанной с сайта https://cg-tricolor.ru/catalog/flats в файл 'sources/tricolor' очищает их, сохряняет
    """
    def __init__(self, page_text):
        self.__url = None
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")
        self.__items_list = self.__b_soup.findAll("tr", class_ = "results__tr")
        self.__dict_list = []
            
    def get_dict_list(self) -> list:
        if self.__items_list:
            for item in self.__items_list:
                item_dict = {}
                item_dict["title"] = self._get_title(item)
                if  item_dict["title"]:
                    rooms = item_dict["title"][0]
                    item_dict["rooms"] = int(rooms)
                else:
                    item_dict["rooms"] = None
                item_dict["bulding"] = self._get_bulding(item)
                item_dict["floor"] = self._get_floor(item)
                item_dict["square"] = self._get_square(item)
                item_dict["price"] = self._get_price(item)
                self.__dict_list.append(item_dict)
            return self.__dict_list  
        else:
            print("Error in getting Items List")