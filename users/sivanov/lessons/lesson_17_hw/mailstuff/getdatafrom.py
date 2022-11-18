#!/usr/local/bin/python
# coding: utf-8
import urllib
from bs4 import BeautifulSoup
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
        page = urllib.urlopen(self.__url)
        page.getcode()
        if page.getcode() == 200:
            text = page.read()
            soup = BeautifulSoup(text,features="html.parser")
            value = soup.findAll(self.__itemtype, class_=self.__item)
        else:
            value = ["go duck youself"]
        return value
    pass
##########################################################################################################
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
            output = inputlist.pop()
            output = output.text
        return output
    pass
##########################################################################################################
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