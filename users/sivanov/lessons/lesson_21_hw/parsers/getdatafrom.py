#!/usr/local/bin/python
# coding: utf-8
"""
модуль, реализующий обработку веб-страниц. Загрузка, анализ, выделение интересующей информации
"""
import urllib.request
from bs4 import BeautifulSoup
import pytest
from usefulstuff import LocalLog
#from usefulstuff import ColoredStr
#from usefulstuff import HandmadeTestDecorator
llog = LocalLog(False)
class webpage:
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
        self.__text = ''
        return None
    #--------------------------------------------
    @property
    def last_HTTP_error_code(self):
        return self.__last_HTTP_error
    #--------------------------------------------
    @property
    def last_URL_error_code(self):
        return self.__last_URL_error
    
    #--------------------------------------------
    def __str__(self):
        return ('url: %s, opened: %s, , error codes: HTTP: %d, URL: %d' % 
                (self.__url, 
                 str(self.__is_opened),
                 self.__last_HTTP_error,
                 self.__last_URL_error) )
    #--------------------------------------------
    def open(self):
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
class ultra_strip:
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
        return result
    pass
#==================================================================================================================================
class page_element:
    #initiate
    #--------------------------------------------------------------------------------
    def __init__(self, item_alias: str, item_name:str, item_type:str, item_num:int, stripper:ultra_strip) -> str:
        self.__item_alias = item_alias
        self.__item_type = item_type
        self.__item_name = item_name  
        self.__item_num = item_num 
        self.__stripper = stripper
    #--------------------------------------------------------------------------------
    @property
    def item_alias(self):
        return self.__item_alias
    #--------------------------------------------------------------------------------
    def __call__(self, soup):
        dirty_value = self._getitemvalues_(soup)
        llog(dirty_value)
        clean_value = self.__stripper(dirty_value[self.__item_num].text) 
        llog(clean_value)
        return clean_value
    #--------------------------------------------------------------------------------
    def __str__(self):
        return str("Ищем "+self.__item_alias +" <"+self.__item_type+" class='"+ self.__item_name+"'>. под номером "+str(self.__item_num))
    #--------------------------------------------------------------------------------
    def __repr__(self):
        return self.__str__()
    #--------------------------------------------------------------------------------
    def _getitemvalues_(self, soup) -> str:
        value = ['']
        llog('_getitemvalues_, <%s class=%s>' %(self.__item_type, self.__item_name))
        value = soup.findAll(self.__item_type, class_=self.__item_name)
        return value
    #--------------------------------------------------------------------------------
    pass
#==================================================================================================================================
class product_info:
    """
    Класс, ответственный за получение корректных данных с одной веб странички
    должен предоставлять интерфейс к заполнению полей, которые потом нужно будет выдрать.
    должен возвращать словарь с именованными данными.
    """
    #------------------------------------------------------------------------------------
    def __init__(self, url:str, elements:dict):
        """
        инициализируется урлом, с которого нужно забирать данные.
        """
        self.__url = url
        self.__page = webpage(self.__url) #сразу докинем читалку страниц
        self.__soup = None
        self.__data_loaded = False
        self.__elements = []
        self.setup(elements)
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
            self.__elements.append(page_element(key,elements[key][0],elements[key][1],elements[key][2],elements[key][3]))
        
    #------------------------------------------------------------------------------------
    def load_page(self):
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
    #------------------------------------------------------------------------------------ 
    def get_all(self):
        result = {}
        if(self.__data_loaded):
            for element in self.__elements:
                result[element.item_alias] = element(self.__soup)
        else:
            pass #TODO хз, может и просто надо удалить
        return result 
                                   
    #------------------------------------------------------------------------------------                               
    pass

#==================================================================================================================================
def main():
    #llog = LocalLog(True)
    superstripper = ultra_strip([u" ",u"\u20bd",u"\xa0"])
    nostrip = ultra_strip([])
    smara1_data_2_get = {"Цена":("catalog-detail__price","div", 0, superstripper),
                  "Название товара":("catalog-detail__name","h1", 0, nostrip)
                  }
    smara1 = product_info("https://sport-marafon.ru/catalog/gamaki/gamak-eno-doublenest-print-tie-dye-red/",smara1_data_2_get)
    smara1.load_page()
    data = smara1.get_all()
    print(data)
                                                                                                       
    
    return None
#==================================================================================================================================
if __name__ == '__main__':
    #llog = LocalLog(True)
    main()
pass    