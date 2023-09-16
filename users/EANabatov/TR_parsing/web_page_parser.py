"""
Модуль парсинга сайта книжного магазина
https://www.moscowbooks.ru/
(онлайн)
"""
import logging
import re
from bs4 import BeautifulSoup
import urllib.request
from parsing_helper import ultimate_finder


# todo тесты


class BookStoreParser:
    """Класс парсинга сайта книжного магазина"""
    def __init__(self, start_parsing_index, end_parsing_index):
        """Конструктор класса парсинга"""
        logging.basicConfig(
            level=logging.INFO,
            filename="eanabatov_web_parser.log",
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s",
        )
        self.start_parsing_index = start_parsing_index
        self.end_parsing_index = end_parsing_index
        self.__books = []
        self.__parsing(self.start_parsing_index, self.end_parsing_index)

    def __parsing(self, start_parsing_index=int, end_parsing_index=int):
        """Парсит html страницу через запросы"""
        if end_parsing_index < start_parsing_index:
            raise KeyError("End point smaller starting point")
        __counter = 1
        for identificator in range(start_parsing_index, end_parsing_index + 1):
            __summary = {}
            __link = "https://www.moscowbooks.ru/book/" + str(identificator) + "/"
            try:
                self.page = urllib.request.urlopen(__link)
                self.text = self.page.read()
                self.soup = BeautifulSoup(self.text, features="html.parser")
                if self.page.getcode() == 200:
                    if self.soup.find(
                        href=re.compile("books"), class_="link-gray-light"
                    ) and not self.soup.find(
                        href=re.compile("magazines"), class_="link-gray-light"
                    ):
                        try:
                            __summary["in_stock"] = self.__in_stock()
                        except:
                            __summary["in_stock"] = None
                        try:
                            __summary["book_name"] = self.__book_name()
                        except:
                            __summary["book_name"] = None
                        try:
                            __summary["author_name"] = self.__author_name()
                        except:
                            __summary["author_name"] = None
                        try:
                            __summary["shop_price"] = self.__shop_price()
                        except:
                            __summary["shop_price"] = None
                        try:
                            __summary["internet_price"] = self.__internet_price()
                        except:
                            __summary["internet_price"] = None
                        try:
                            __summary["the_year_of_publishing"] = ultimate_finder(
                                __link, "Год издания:"
                            )
                        except:
                            __summary["the_year_of_publishing"] = None
                        __summary["publisher"] = ultimate_finder(
                            __link, "Издательство:"
                        )
                        __summary["publish_place"] = ultimate_finder(
                            __link, "Место издания:"
                        )
                        __summary["text_language"] = ultimate_finder(
                            __link, "Язык текста:"
                        )
                        __summary["cover_type"] = ultimate_finder(
                            __link, "Тип обложки:"
                        )
                        __summary["paper_type"] = ultimate_finder(__link, "Бумага:")
                        __summary["Illustrations"] = ultimate_finder(
                            __link, "Иллюстрации:"
                        )
                        __summary["Illustrators"] = ultimate_finder(
                            __link, "Иллюстраторы:"
                        )
                        __summary["weight"] = ultimate_finder(__link, "Вес:")
                        __summary["Circulation"] = ultimate_finder(__link, "Тираж:")
                        __summary["product_code"] = ultimate_finder(
                            __link, "Код товара:"
                        )
                        __summary["vendor_code"] = ultimate_finder(__link, "Артикул:")
                        __summary["isbn"] = ultimate_finder(__link, "ISBN:")
                        __summary["pegi"] = ultimate_finder(__link, "Возраст:")
                        __summary["on_sale_from"] = ultimate_finder(
                            __link, "В продаже с:"
                        )
                        __summary["link"] = self.__link()
                        logging.info(
                            f"Process {identificator}: OK (counter: {__counter})"
                        )
                        __counter += 1
                    else:
                        logging.info(f"{identificator} не книга ({self.__link()})")
                else:
                    logging.error(f"{self.page.getcode()}")
            except:
                logging.error(
                    f"process {identificator}. Страшно, очень страшно! Мы не знаем что это такое, если бы мы "
                    f"знали что это такое,"
                    "но мы не знаем что это такое!"
                )
            if __summary != {}:
                self.__books.append(__summary)
        print(self.__books)

    def __book_name(self):
        """Название книги"""
        return (
            self.soup.find("span", class_="link-gray-light")
            .text.replace(" ", " ")
            .strip()
        )

    def __author_name(self):
        """Имя автора"""
        return self.soup.find("a", class_="author-name").text.replace(" ", "").strip()

    def __shop_price(self):
        """Цена в магазине (отсутствует если товара нет в наличии)"""
        return self.soup.find("span", class_="rubs").text.replace(" ", "").strip()

    def __internet_price(self):
        """Цена на сайте (отсутствует если товара нет в наличии)"""
        return (
            self.soup.find("span", class_="silver rubs rubfont")
            .text.replace(" ", "")
            .strip()
        )

    def __link(self):
        """Находит ссылку на страницу с книгой"""
        return self.soup.find("link").get("href")  # ссылка на книгу

    def __in_stock(self):
        """Определяет в наличии ли книга в магазине на данный момент"""
        __stock = None
        try:
            __stock = (
                self.soup.find("span", class_="book__shop-instock")
                .text.replace(" ", " ")
                .strip()
            )
        except:
            __stock = (
                self.soup.find("span", class_="instock1")
                .text.replace(" ", " ")
                .strip()
                .lower()
            )
        return __stock


a2 = BookStoreParser(1156000, 1157000)

