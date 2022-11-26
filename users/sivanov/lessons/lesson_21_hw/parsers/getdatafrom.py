#!/usr/local/bin/python
# coding: utf-8
import urllib.request
from bs4 import BeautifulSoup
import pytest
from usefulstuff import LocalLog
from usefulstuff import ColoredStr
from usefulstuff import HandmadeTestDecorator
class webpage:
    """
    класс вебстраница
    работаем как с файлом: передаем путь, или не передаем
    метод "open" идет по адресу и открывает страницу
    метод "is_open" сообщает о успехе или неудачи загрузки
    метод text возвращает полученный методом open результат
    """
    def __init__(self,url=""):
        self.__url = url
        self.__is_opened = False
        self.__last_error = 0
        return None
    #--------------------------------------------
    def __str__(self):
        return 'url: ' + self.__url + ', opened: '+ str(self.__is_opened) + ', error code: '+ str(self.__last_error)
    #--------------------------------------------
    def open(self):
        page = urllib.request.urlopen(self.__url)
        self.__last_error = page.getcode()
        if((self.__last_error == 200) or (self.__last_error == None)):
            # все ок
            self.__text = page.read()
            self.__is_opened = True
        else:
            self.__text = 'page not opened, error: ' + str(self.__last_error)
            self.__is_opened = False
        return  self.__text   
    #--------------------------------------------
    def text(self):
        return self.__text   
    #--------------------------------------------
    def is_open(self):
        return self.__is_opened
    #--------------------------------------------
    pass
    

#--------------------------------------------------------------------------------------------------------
#тесты
def test_webpage_str_1():
    assert str(webpage('test')) == 'url: test, opened: False, error code: 0'
    return None
def test_webpage_str_2():
    assert str(webpage('test')) != 'url: test, opened: True, error code: 0'
    return None
def test_webpage_open_1():
    test_html = '<html><head><meta charset="utf-8"></head><body><div class=\"test\">some text</div><div class=\"price\">1 345р.</div></body></html>'
    with open('test.html','w') as f:
        f.write(test_html)
    
    #КОСТЫЛИНА КАПЕЦ ПРОСТО
    test_page = webpage('file:///home/jupyter-isergy/github/team22/users/sivanov/lessons/lesson_21_hw/parsers/test.html')
    
    text = test_page.open().decode('utf-8')
    assert text == test_html# + 'fail'
    return None
    
    
#==================================================================================================================================
class get_data_from:
    #initiate
    def __init__(self,url,item, itemtype="div"):
        self.__url = url
        self.__item = item
        self.__itemtype = itemtype
        return
    def __call__(self):
        return self._getitemvalue_()
    def __str__(self):
        return str("Адрес объекта: "+self.__url+" ; ищем <"+self.__itemtype+" class='"+ self.__item+"'>")
    def _getitemvalue_(self):
        value = [""]
        page = urllib.request.urlopen(self.__url)
        page.getcode()
        if page.getcode() == 200:
            text = page.read()
            soup = BeautifulSoup(text,features="html.parser")
            value = soup.findAll(self.__itemtype, class_=self.__item)
        else:
            value = ["go duck youself"]
        return value
    pass
#==================================================================================================================================
class preprocess_data:
    '''
    обработать то, что выдает get_data_from
    '''
    def __init__(self, position):
        self.__position = position
        return
    def __str__(self):
        return ""
    def __repr__(self):
        return self.__str()
    def __call__(self,inputlist):
        return self._do_preprocess_(inputlist)
    def _do_preprocess_(self, inputlist):
        output = ""
        position = self.__position
        if(position < 0):
            output = (',').join(inputlist)
        if(position < len(inputlist)):
            output = inputlist[position].text
        else:
            output = inputlist[-1]
            output = output.text
        return output
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
# тесты модуля
def _tests():
    rbstr = ColoredStr("red, bold")
    gbstr = ColoredStr("green, bold")
    failed = rbstr("!!!FAILED!!! : ")
    passed = gbstr("PASSED : ")
    htc = HandmadeTestDecorator(failed, passed)
    print("begin testing")
    print(htc(test_webpage_str_1)())
    print(htc(test_webpage_str_2)())
    print(htc(test_webpage_open_1)())   
    print("testing end")
    return None
#==================================================================================================================================
def main():
    return _tests()
#==================================================================================================================================
if __name__ == '__main__':
    #llog = LocalLog(True)
    main()
pass    