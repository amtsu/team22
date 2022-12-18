#!/usr/local/bin/python
# coding: utf-8
"""
модуль, реализующий обработку веб-страниц. Загрузка, анализ,
выделение интересующей информации
"""
import urllib.request
import json
import socket
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import List
from typing import Any
import bs4
from bs4 import BeautifulSoup

# import os
# import pytest
# не проверять на корректность импорта
from usefulstuff import LocalLog  # pylint: disable=E0401

# from usefulstuff import ColoredStr
# from usefulstuff import HandmadeTestDecorator
llog = LocalLog(False)

# =====================================================================================
class WebPage:
    """
    класс вебстраница
    работаем как с файлом: передаем путь, или не передаем
    метод "open" идет по адресу и открывает страницу
    метод "is_open" сообщает о успехе или неудачи загрузки
    метод text возвращает полученный методом open результат
    """

    def __init__(self, url: str = ""):
        self.__url = url
        self.__is_opened = False
        self.__last_http_error = 0
        self.__last_url_error = 0
        self.__socket_timeout = 0
        self.__text = ""

    # -------------------------------------------------------------------------------
    @property
    def last_http_error_code(self):
        """
        Свойство, сообщающее возникшую при открытии страницы ошибку протокола http
        """
        return self.__last_http_error

    # -------------------------------------------------------------------------------
    @property
    def last_url_error_code(self):
        """
        Свойство, сообщающее возникшую при открытии страницы ошибку url
        """
        return self.__last_url_error

    # -------------------------------------------------------------------------------
    def __str__(self):
        """
        Конвертер экземпляра класса WebPage  в строку (такой себе, конечно)
        """
        return (
            f"url: {self.__url}, opened: {self.__is_opened}, "
            f"error codes: HTTP: {self.__last_http_error}, "
            f"URL: {self.__last_url_error}, socket: {self.__socket_timeout}"
        )

    # -------------------------------------------------------------------------------
    def open(self):
        """
        метод, совершающий попытку открыть веб-страницу,и если все в порядке,
        возвращающий её текст.
        если не всё в порядке, заполняется информация о произошедшей ошибке
        """
        self.__is_opened = False
        self.__last_http_error = 0
        self.__last_url_error = 0
        self.__socket_timeout = 0
        try:
            with urllib.request.urlopen(self.__url) as page:
                # self.__last_http_error =  # TODO: разобраться что с этим делать
                self.__last_url_error = page.status
                self.__text = page.read()
                self.__is_opened = True

        except urllib.error.HTTPError as http_error:
            self.__last_http_error = http_error.code
            self.__text = ""
            self.__is_opened = False
        except urllib.error.URLError as url_error:
            self.__last_url_error = url_error.reason
            self.__text = ""
            self.__is_opened = False
        except socket.timeout:
            self.__socket_timeout = 1
            self.__text = ""
            self.__is_opened = False
        else:
            pass
        return self.__text

    # -------------------------------------------------------------------------------
    @property
    def text(self):
        """
        свойство, возвращающее текст страницы
        """
        return self.__text

    # -------------------------------------------------------------------------------
    def is_open(self):
        """
        функция, влзвращающая признак того, что страница открылась без проблем
        и можно получить её текст
        """
        return self.__is_opened

    # -------------------------------------------------------------------------------


# ===================================================================================
class UltraStripper:
    """
    удалить заданные символы из списка символов,формируемого при создании
    """

    def __init__(self, trash_to_remove: List[Any]) -> None:
        """
        типа конструктор.
        класс инициализируется списком, содержащим в себе всё что нужно будет
        потом удалять
        """
        self.__trash_to_remove = trash_to_remove

    def __str__(self):
        """
        конвертер UltraStripper в строку, ну, вроде того
        """
        return (",").join(self.__trash_to_remove)

    def __repr__(self):
        """
        повторяет __str__, зачем-то был нужен когда отлаживался
        """
        return self.__str__()

    def __call__(self, input_data: str) -> str:
        """
        превращает объект класса UltraStripper в callable
        """
        return self.__do_damage(input_data)

    def __do_damage(self, input_data: str) -> str:
        """
        скрытый метод, делающий всю работу по очистке входной строки от нежелательной
        информации, в соответствии с данными, которыми класс был инициализирован
        """
        result = input_data
        for item in self.__trash_to_remove:
            result = result.replace(item, "")
        return result.strip()


# ===================================================================================
# return element_1['href'] - это как вытащить значение
# возможн нужно сделать геттекст и гетвалюе, ну или написать два класса обработчика,
# это на подумать.
# ===================================================================================
@dataclass  # декоратор, автоматически добавляет init repr и прочее
class SimpleGetter:
    """
    абстрактный класс, задающий интерфейс для возможных потомков, создаваемых
    для получения конкрутных значений тегов

    раньше потомков было 2, сейчас один, можно обойтись и без этого интерфейса

    или перепишу-ка я его под NVI

    про датаклассы:
    https://docs.python.org/3/library/dataclasses.html
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def _get_tag_value_or_tag_parameter_value(self, tag: bs4.element.Tag) -> str:
        """
        абстрактный метод, получающий значение класса.
        "типа private", насколько это тут возможно
        """

    def get(self, tag: bs4.element.Tag) -> str:
        """
        а это уже интерфейс
        "типа паблик", хотя тут все методы павлики
        возвращает результат работы того, чего в потомках напрограммировано в методе
        _get_tag_value_or_tag_parameter_value. Надеюсь, это будет строка.
        """
        return self._get_tag_value_or_tag_parameter_value(tag)


# ===================================================================================
@dataclass
class TagValue(SimpleGetter):
    """
    единственный наследник симпл геттера
    забрать значение параметра тега (то есть то что внутри и имеет соответствующее
    имя)
    если имя параметра не задано, для данного тега возвращается значение самого
    тега (то есть то что между открывающимся и закрывающимся тегом)
    """

    # -------------------------------------------------------------------------------
    def __init__(self, param_name: str = "") -> None:
        """
        инициализация.
        На вход хочет получить имя параметра тэга, значение которого нужно вернуть,
        или пустую строку, если нужно вернуть значение тэга
        """
        if len(param_name) == 0:
            self.__get_value = True
        else:
            self.__get_value = False
        self.__param_name = param_name

    # -------------------------------------------------------------------------------
    def _get_tag_value_or_tag_parameter_value(self, tag: bs4.element.Tag) -> str:
        """
        Переопределение родительского абстрактного метода
        Потомок возвращает значение тэга или параметра тэга из переданного ему
        параметра tag
        листья тополя падают с ясеня - в процессе тестирования вылезло предупреждение
        что has_key больше не стоит использоватьб, вместо него теперь has_attr
        """
        result = ""
        if self.__get_value:
            result = tag.text
        else:
            if tag.has_attr(self.__param_name):
                result = str(tag[self.__param_name])
        return result


# ===================================================================================
# class TagValue(SimpleGetter):
#    """
#    забрать значение тега, то есть то что между открывающимся и закрывающимся тегом
#    оказлся ненужным
#    """
#    def __init__(self):
#        pass
#    def get(self, tag: bs4.element.Tag):
#        return tag.text
#    pass
# ===================================================================================
class PageElement:
    """
    класс, обрабатывающий один элемент из загруженной страницы
    callable
    должен возвращать значение элемента страницы в соответствии с настройками
    """

    # initiate
    # -------------------------------------------------------------------------------
    def __init__(self, item_alias: str, element_data: dict) -> None:
        """
        в качестве настроек принимает название, данное этому элементу, например
        "Название товара"
        и словарик примерно такого вида:
        {
                        "id": "price_cell_title__cbJWZ", - название класа тэга
                        "tagname": "h1",  - тип тэга
                        "index": 0, - номер в списке значений, возвращаемых супом
                        "what": "", - имя параметра тэга, значение которого надо забрать,
                          или пустая строка, если нужно взять значение самого
                          тэга
                        "stripper_setting": "" - то, от чего нужно избавиться в результирующей
                                    строке (настройки для UltraStripper)
                },

        """
        self.__item_alias = item_alias
        self.__item_type = ""
        self.__item_name = ""
        self.__item_num = 0
        self.__stripper = UltraStripper([""])
        self.__getter = TagValue("")
        if set(["tagname", "id", "index", "stripper_setting", "what"]).issubset(
            set(element_data.keys())
        ):
            self.__item_type = element_data["tagname"]
            self.__item_name = element_data["id"]
            self.__item_num = int(
                element_data["index"]
            )  # TODO добавить проверку корректности
            print(type(element_data["index"]))
            self.__stripper = UltraStripper(element_data["stripper_setting"].split(","))
            self.__getter = TagValue(element_data["what"])

    # -------------------------------------------------------------------------------
    @property
    def item_alias(self):
        """
        Свойство, возвращающее человекочитаемое название, назначенное данному значению
        """
        return self.__item_alias

    # -------------------------------------------------------------------------------
    def __call__(self, soup: bs4.BeautifulSoup):
        """
        делает объекты класса PageElement - callable
        работает в два этапа - добывает значение элемента,
        и очищает его стриппером
        """
        dirty_value = self.__get_item_value(soup)
        # llog(dirty_value)
        clean_value = self.__stripper(dirty_value)
        # llog(clean_value)
        return clean_value

    # -------------------------------------------------------------------------------
    def __str__(self):
        """
        печать информации о себе (что ищем на странице)
        """
        return (
            f"Ищем {self.__item_alias} <{self.__item_type} class='"
            f"{self.__item_name}'>. под номером {self.__item_num}"
        )

    # -------------------------------------------------------------------------------
    def __repr__(self):
        """
        повторяет __str__, зачем-то был нужен
        """
        return self.__str__()

    # -------------------------------------------------------------------------------
    def __get_item_value(self, soup: bs4.BeautifulSoup) -> str:
        """
        метод, работающий с супом и выбирающий из него нужное значение. Если все в порядке,
        возвращает значение элемента в соответствтии с настройками.
        Если не в порядке - пустую строку, или упадет, как повезёт
        """
        value = ""
        llog(f"_getitemvalue_, <{self.__item_type} class={self.__item_name}>")
        all_data = soup.findAll(self.__item_type, class_=self.__item_name)
        llog("-----------------")
        llog(all_data)
        llog("-----------------")
        if self.__item_num < len(all_data):
            correct_item = all_data[self.__item_num]
            value = self.__getter.get(correct_item)
        return value

    # -------------------------------------------------------------------------------


# ===================================================================================
class ProductInfo:
    """
    Класс, ответственный за получение корректных данных с одной веб странички
    должен предоставлять интерфейс к заполнению полей, которые потом нужно будет
    выдрать.
    должен возвращать словарь с именованными данными.
    """

    # -------------------------------------------------------------------------------
    def __init__(self, elements: dict):
        """
        инициализируется урлом, с которого нужно забирать данные.
        """
        self.__url = elements["url"]
        self.__page = WebPage(self.__url)  # сразу докинем читалку страниц
        self.__soup = BeautifulSoup("")  # TODO нужно обсудить как тут быть
        # self.__soup = None  # TODO: обсудить как тут быть
        """
        если оставить self.__soup = None, ругается mypy
        если совсем убрать - ругается pylint
        self.__soup = BeautifulSoup("") - прокатит, но мне вообще не
        нравится просто так делать обЪект, которыйц 146% не нужен
        """
        self.__data_loaded = False
        self.__elements: list[PageElement] = []
        self.setup(elements["data"])

    # -------------------------------------------------------------------------------
    def __str__(self):
        """
        используется при выводе на печать информации о классе.
        печатает НАСТРОЙКИ а не результат работы
        """
        return ("\n").join((str(element) for element in self.__elements))

    # -------------------------------------------------------------------------------
    def setup(self, elements: dict):
        """
        метод, принимающий и ининциализирующий параметры, которые неободимо выдрать
        из загруженного супа elements должен иметь структуру "класс элемента":
        ("тип элемента",номер_элемента, стриппер), например
        {'a_price_element':('div',0,a_price_element_stripper)}

        ИЗЛИШНЕ ПОКА ЭТОТ РАЗБОР ДРАМАТИЗИРОВАТЬ НЕ БУДУ, ПО ХОДУ ДЕЛА ПРИДЕТСЯ
        ДОРАБОТАТЬ
        """
        self.__elements = []
        for key in elements.keys():
            self.__elements.append(PageElement(key, elements[key]))

    # -------------------------------------------------------------------------------
    def load(self):
        """
        Долгий метод, будет загружать страницу и отдавать её в суп.
        на выходе либо заполнит суп данными, либо не заполнит
        """
        self.__page.open()
        if self.__page.is_open():
            self.__data_loaded = True
            self.__soup = BeautifulSoup(self.__page.text, features="html.parser")
        else:
            self.__data_loaded = False
            print(str(self.__page))

    # -------------------------------------------------------------------------------
    def is_loaded(self):
        """
        метод, возвращающий информацию, удалось ли загрузить в суп требуемую страничку
        """
        return self.__data_loaded

    # -------------------------------------------------------------------------------
    def get(self) -> dict:
        """
        метод, в соответствии с настройками, возвращающий словарик с необходимой
        информацией, полученной со странички
        """
        result = {}
        if self.__data_loaded:
            for element in self.__elements:
                result[element.item_alias] = element(self.__soup)
            result["url"] = self.__url
        else:
            pass  # TODO хз, может и просто надо удалить
        return result

    # -------------------------------------------------------------------------------


# ===================================================================================
def create_product_info(filename: str) -> ProductInfo:
    """
    функция создания экземпляров класса ProductInfo, основываясь на json-файле
    с настройками, типа такого:
    {
        "url": "https://delivery.metro-cc.ru/metro/
        vino-matsu-el-picaro-toro-do-krasnoe-suhoe-14-5-0-75-l-ispaniya-0459ac3",
        "data": {
                "Цена": {
    "id": "price_cell_priceRow__WPJQk price_root__niT7G
    price_default__sNIab price_default__sNIab",
                        "tagname": "div",
                        "index": 0,
                        "what": "",
                        "stripper_setting": " ,₽, ,<span>,</span>"
                },
                "Название товара": {
                        "id": "price_cell_title__cbJWZ",
                        "tagname": "h1",
                        "index": 0,
                        "what": "",
                        "stripper_setting": ""
                },
                "Бренд": {
                        "id": "product-link",
                        "tagname": "a",
                        "index": 0,
                        "what": "",
                        "stripper_setting": "<span itemprop=\"name\">,</span>"
                },
                "Код товара": {
                        "id": "",
                        "tagname": "",
                        "index": 0,
                        "what": "",
                        "stripper_setting": ""
                }
        }
    }
    """
    with open(filename, "r", encoding="utf-8") as fin:
        data = json.loads(fin.read())
    return ProductInfo(data)


# ===================================================================================
def main():
    """
    наверное, пригодится
    """
    return None


# ===================================================================================
if __name__ == "__main__":
    # llog = LocalLog(True)
    main()
