"""
Модуль парсинга сайта книжного магазина
https://www.moscowbooks.ru/
(локальная страница)
"""
from bs4 import BeautifulSoup
import urllib.request
from parsing_helper import ultimate_finder


class LocalPageParsing:
    """"""
    def __init__(self):
        """"""
        self.__link = "file:///home/evgeniy/Documents/html/book_parsing.html"
        self.__page = urllib.request.urlopen(self.__link)
        self.__text = self.__page.read()
        self.__soup = BeautifulSoup(self.__text, features="html.parser")
        self.__pars(self.__link, self.__page, self.__text, self.__soup)

    def __pars(self, link, page, text, soup):
        """"""
        __summary = {}
        __link = link
        __page = page
        __text = text
        __soup = soup
        try:
            __summary["in_stock"] = self.__in_stock(self.__soup)
        except:
            __summary["in_stock"] = None
        try:
            __summary["book_name"] = self.__book_name(self.__soup)
        except:
            __summary["book_name"] = None
        try:
            __summary["author_name"] = self.__author_name(self.__soup)
        except:
            __summary["author_name"] = None
        try:
            __summary["shop_price"] = self.__shop_price(self.__soup)
        except:
            __summary["shop_price"] = None
        try:
            __summary["internet_price"] = self.__internet_price(self.__soup)
        except:
            __summary["internet_price"] = None
        try:
            __summary["the_year_of_publishing"] = ultimate_finder(
                __link, "Год издания:"
            )
        except:
            __summary["the_year_of_publishing"] = None
        __summary["publisher"] = ultimate_finder(__link, "Издательство:")
        __summary["publish_place"] = ultimate_finder(__link, "Место издания:")
        __summary["text_language"] = ultimate_finder(__link, "Язык текста:")
        __summary["cover_type"] = ultimate_finder(__link, "Тип обложки:")
        __summary["paper_type"] = ultimate_finder(__link, "Бумага:")
        __summary["Illustrations"] = ultimate_finder(__link, "Иллюстрации:")
        __summary["Illustrators"] = ultimate_finder(__link, "Иллюстраторы:")
        __summary["weight"] = ultimate_finder(__link, "Вес:")
        __summary["Circulation"] = ultimate_finder(__link, "Тираж:")
        __summary["product_code"] = ultimate_finder(__link, "Код товара:")
        __summary["vendor_code"] = ultimate_finder(__link, "Артикул:")
        __summary["isbn"] = ultimate_finder(__link, "ISBN:")
        __summary["pegi"] = ultimate_finder(__link, "Возраст:")
        __summary["on_sale_from"] = ultimate_finder(__link, "В продаже с:")
        return __summary

    def __book_name(self, soup):
        """Название книги"""
        return (
            soup.find("span", class_="link-gray-light")
            .text.replace(" ", " ")
            .strip()
        )

    def __author_name(self, soup):
        """Имя автора"""
        return soup.find("a", class_="author-name").text.replace(" ", "").strip()

    def __shop_price(self, soup):
        """Цена в магазине (отсутствует если товара нет в наличии)"""
        return soup.find("span", class_="rubs").text.replace(" ", "").strip()

    def __internet_price(self, soup):
        """Цена на сайте (отсутствует если товара нет в наличии)"""
        return (
            soup.find("span", class_="silver rubs rubfont")
            .text.replace(" ", "")
            .strip()
        )

    def __in_stock(self, soup):
        """Определяет в наличии ли книга в магазине на данный момент"""
        __stock = None
        try:
            __stock = (
                soup.find("span", class_="book__shop-instock")
                .text.replace(" ", " ")
                .strip()
            )
        except:
            __stock = (
                soup.find("span", class_="instock1")
                .text.replace(" ", " ")
                .strip()
                .lower()
            )
        return __stock


a1 = LocalPageParsing()
