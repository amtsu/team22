#!/usr/local/bin/python
# coding: utf-8
"""
модуль, реализующий обработку веб-страниц. Загрузка, анализ, выделение интересующей информации
"""
import urllib.request
from bs4 import BeautifulSoup
import bs4
from abc import ABCMeta, abstractmethod
import json
import os 
import pytest
from usefulstuff import LocalLog
#from usefulstuff import ColoredStr
#from usefulstuff import HandmadeTestDecorator
llog = LocalLog(False)
class WebPage:
    """
    класс вебстраница
    работаем как с файлом: передаем путь, или не передаем
    метод "open" идет по адресу и открывает страницу
    метод "is_open" сообщает о успехе или неудачи загрузки
    метод text возвращает полученный методом open результат
    """
    def __init__(self,url=''):
        self.__url = url
        self.__is_opened = False
        self.__last_HTTP_error = 0
        self.__last_URL_error = 0
        self.__socket_timeout = 0
        self.__text = ''
        return None
    #--------------------------------------------
    @property
    def last_http_error_code(self):
        return self.__last_HTTP_error
    #--------------------------------------------
    @property
    def last_url_error_code(self):
        return self.__last_URL_error
    
    #--------------------------------------------
    def __str__(self):
        return ('url: %s, opened: %s, error codes: HTTP: %d, URL: %d, socket: %d' % 
                (self.__url, 
                 str(self.__is_opened),
                 self.__last_HTTP_error,
                 self.__last_URL_error,
                 self.__socket_timeout) )
    #--------------------------------------------
    def open(self):
        self.__is_opened = False
        self.__last_HTTP_error = 0
        self.__last_URL_error = 0
        self.__socket_timeout = 0 
        try:
            page = urllib.request.urlopen(self.__url)
        except urllib.error.HTTPError as e:
            self.__last_HTTP_error = e.code
            self.__text = ''
            self.__is_opened = False
            pass
        except urllib.error.URLError as e:
            self.__last_URL_error = e.reason
            self.__text = ''
            self.__is_opened = False
            pass
        except socket.timeout:
            self.__socket_timeout = 1
            self.__text = ''
            self.__is_opened = False
        else:
            #self.__last_HTTP_error =  # TODO: разобраться что с этим делать
            self.__last_URL_error = page.status 
            self.__text = page.read()
            self.__is_opened = True
        return  self.__text   
    #--------------------------------------------
    @property
    def text(self):
        return self.__text   
    #--------------------------------------------
    def is_open(self):
        return self.__is_opened
    #--------------------------------------------
    pass
#==================================================================================================================================
class UltraStripper:
    '''
    удалить заданные символы из списка символов,формируемого при создании 
    '''
    def __init__(self, trash_to_remove):
        self.__trash_to_remove = trash_to_remove
        return
    def __str__(self):
        return (',').join(self.__trash_to_remove)
    def __repr__(self):
        return self.__str__()
    def __call__(self, input_data):
        return self._do_damage_(input_data)
    def _do_damage_(self, input_data):
        result = input_data
        for item in self.__trash_to_remove:
            result = result.replace(item, "")
        return result.strip()
    pass
#==================================================================================================================================
#return element_1['href'] - это как вытащить значение
# возможн нужно сделать геттекст и гетвалюе, ну или написать два класса обработчика, это на подумать.
#==================================================================================================================================
class SimpleGetter:
    __metaclass__ = ABCMeta
    @abstractmethod
    def get(self, tag: bs4.element.Tag):
        pass
    pass
#==================================================================================================================================
class TagValue(SimpleGetter):
    """
    забрать значение параметра тега (то есть то что внутри и имеет соответствующее имя)
    если имя параметра не задано, для данного тега возвращается значение самого тега
    (то есть то что между открывающимся и закрывающимся тегом)
    """
    #---------------------------------------------------  
    def __init__(self, param_name:str = ""):
        if(len(param_name) == 0):
            self.__get_value = True
        else:
            self.__get_value = False
        self.__param_name = param_name
    #---------------------------------------------------    
    def get(self, tag: bs4.element.Tag):
        result = ''
        if(self.__get_value):
            result = tag.text
        else:    
            if(tag.has_key(self.__param_name)):
                result = tag[self.__param_name]        
        return result
    pass
#==================================================================================================================================
#class TagValue(SimpleGetter):
#    """
#    забрать значение тега, то есть то что между открывающимся и закрывающимся тегом
#    """
#    def __init__(self):
#        pass
#    def get(self, tag: bs4.element.Tag):
#        return tag.text
#    pass
#==================================================================================================================================
class PageElement:
    #initiate
    #--------------------------------------------------------------------------------
    def __init__(self, item_alias: str, element_data:dict) -> str:
        self.__item_alias = item_alias
        self.__item_type = element_data['tagname']
        self.__item_name = element_data['id']  
        self.__item_num = element_data['index'] 
        self.__stripper = UltraStripper(element_data['stripper_setting'].split(","))
        self.__getter = TagValue(element_data['what'])
        
    #--------------------------------------------------------------------------------
    @property
    def item_alias(self):
        return self.__item_alias
    #--------------------------------------------------------------------------------
    def __call__(self, soup):
        dirty_value = self._get_item_values_(soup)
        #llog(dirty_value)
        clean_value = self.__stripper(dirty_value) 
        #llog(clean_value)
        return clean_value
    #--------------------------------------------------------------------------------
    def __str__(self):
        return str("Ищем "+self.__item_alias +" <"+self.__item_type+" class='"+ self.__item_name+"'>. под номером "+str(self.__item_num))
    #--------------------------------------------------------------------------------
    def __repr__(self):
        return self.__str__()
    #--------------------------------------------------------------------------------
    def _get_item_values_(self, soup) -> str:
        value = ''
        llog('_getitemvalues_, <%s class=%s>' %(self.__item_type, self.__item_name))
        all_data = soup.findAll(self.__item_type, class_=self.__item_name)
        llog('-----------------')
        llog(all_data)
        llog('-----------------')
        if(self.__item_num < len(all_data)):
            correct_item = all_data[self.__item_num]
            value = self.__getter.get(correct_item)
        return value
    #--------------------------------------------------------------------------------
    pass
#==================================================================================================================================
class ProductInfo:
    """
    Класс, ответственный за получение корректных данных с одной веб странички
    должен предоставлять интерфейс к заполнению полей, которые потом нужно будет выдрать.
    должен возвращать словарь с именованными данными.
    """
    #------------------------------------------------------------------------------------
    def __init__(self, elements:dict):
        """
        инициализируется урлом, с которого нужно забирать данные.
        """
        self.__url = elements['url']
        self.__page = WebPage(self.__url) #сразу докинем читалку страниц
        self.__soup = None
        self.__data_loaded = False
        self.__elements = []
        self.setup(elements['data'])
    #------------------------------------------------------------------------------------
    def __str__(self):
        return ('\n').join((str(element) for element in self.__elements))
    #------------------------------------------------------------------------------------
    def setup(self, elements:dict):
        """
        метод, принимающий и ининциализирующий параметры, которые неободимо выдрать из загруженного супа
        elements должен иметь структуру "класс элемента": ("тип элемента",номер_элемента, стриппер), например 
        {'a_price_element':('div',0,a_price_element_stripper)}
        
        ИЗЛИШНЕ ПОКА ЭТОТ РАЗБОР ДРАМАТИЗИРОВАТЬ НЕ БУДУ, ПО ХОДУ ДЕЛА ПРИДЕТСЯ ДОРАБОТАТЬ
        """
        self.__elements = []
        for key in elements.keys():
            self.__elements.append(PageElement(key,elements[key]))
        
    #------------------------------------------------------------------------------------
    def load(self):
        """
        Долгий метод, будет загружать страницу и отдавать её в суп.
        на выходе либо заполнит суп данными, либо не заполнит
        """
        self.__page.open()
        if(self.__page.is_open()):
            self.__data_loaded = True
            self.__soup = BeautifulSoup(self.__page.text,features="html.parser") 
        else:
            self.__data_loaded = False
            print(str(self.__page))
    #------------------------------------------------------------------------------------ 
    def get(self):
        result = {}
        if(self.__data_loaded):
            for element in self.__elements:
                result[element.item_alias] = element(self.__soup)
        else:
            pass #TODO хз, может и просто надо удалить
        result['url'] = self.__url
        return result 
                                   
    #------------------------------------------------------------------------------------                               
    pass
#==================================================================================================================================
def CreateProductInfo(filename:str)->ProductInfo:
    """
    функция создания экземпляров класса ProductInfo, основываясь на json-файлах
    """
    with open(filename,"r") as fin:
        data = json.loads(fin.read())
    return ProductInfo(data)
#==================================================================================================================================
def main():
    """
    наверное, пригодится
    """  
    return None
#==================================================================================================================================
if __name__ == '__main__':
    #llog = LocalLog(True)
    main()
    