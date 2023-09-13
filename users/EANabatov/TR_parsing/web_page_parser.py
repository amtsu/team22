"""
модуль парсинга сайта книжного магазина
https://www.moscowbooks.ru/
(онлайн)
"""
import logging

from bs4 import BeautifulSoup
import urllib.request
from parsing_helper import ultimate_finder

# todo добавить логирование и признак активности
# todo добавить остальные возможные параметры с страницы
# todo тесты
# todo нормальные докстринги


class BookStoreParser:
    """класс парсинга сайта книжного магазина"""

    def __init__(self, start_parsing_index, end_parsing_index):
        self.__books = []
        self.__parsing(start_parsing_index, end_parsing_index)
        logging.basicConfig(
            level=logging.INFO,
            filename="eanabatov_web_parser.log",
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s",
        )

    def __parsing(self, start_parsing_index, end_parsing_index):
        for identificator in range(start_parsing_index, end_parsing_index + 1):
            __summary = {}
            __link = "https://www.moscowbooks.ru/book/" + str(identificator) + "/"
            __mini_counter = 0
            try:
                self.page = urllib.request.urlopen(__link)
                self.text = self.page.read()
                self.soup = BeautifulSoup(self.text, features="html.parser")
                if self.page.getcode() == 200:
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

                    __summary["the_year_of_publishing"] = ultimate_finder(
                        __link, "Год издания:"
                    )
                    __summary["publisher"] = ultimate_finder(__link, "Издательство:")
                    __summary["product_code"] = ultimate_finder(__link, "Код товара:")
                    __summary["vendor_code"] = ultimate_finder(__link, "Артикул:")
                    __summary["isbn"] = ultimate_finder(__link, "ISBN:")
                    __summary["pegi"] = ultimate_finder(__link, "Возраст:")
                    __summary["link"] = self.__link()
                else:
                    logging.error(self.page.getcode())
            except:
                logging.error(
                    "Страшно, очень страшно! Мы не знаем что это такое, если бы мы знали что это такое, "
                    "но мы не знаем что это такое!"
                )

            if __summary != {}:
                self.__books.append(__summary)
            logging.info("OK", __mini_counter)
        print(self.__books)
        return self.__books

    def __book_name(self):
        """название книги"""
        return (
            self.soup.find("span", class_="link-gray-light")
            .text.replace(" ", " ")
            .strip()
        )

    def __author_name(self):
        """имя автора (отсутствует если это журнал)"""
        return self.soup.find("a", class_="author-name").text.replace(" ", "").strip()

    def __shop_price(self):
        """цена в магазине (отсутствует если товара нет в наличии)"""
        return self.soup.find("span", class_="rubs").text.replace(" ", "").strip()

    def __internet_price(self):
        """цена на сайте (отсутствует если товара нет в наличии)"""
        return (
            self.soup.find("span", class_="silver rubs rubfont")
            .text.replace(" ", "")
            .strip()
        )

    def __link(self):
        """находит ссылку на страницу с книгой"""
        return self.soup.find("link").get("href")  # ссылка на книгу

    def __in_stock(self):
        """определяет в наличии ли книга в магазине на данный момент"""
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


a2 = BookStoreParser(1156290, 1156292)
# a2.return_books()
