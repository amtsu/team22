"""Модуль парсинга сайта книжного магазина
https://www.moscowbooks.ru/
(онлайн)
"""
import logging
from urllib.error import URLError, HTTPError

from bs4 import BeautifulSoup
import urllib.request

from typing import List

from parsing_helper import ultimate_finder


def main():
    """Псевдо фронтэнд для работы с парсером"""
    start_parsing_code = input("Введите начальный код товара для парсинга: ")
    end_parsing_code = input("Введите конечный код товара для парсинга: ")
    object_one = BookStoreParser()
    object_one.start_parsing(start_parsing_code, end_parsing_code)


class BookStoreParser:
    """Класс парсинга сайта книжного магазина"""

    def __init__(self):
        """Конструктор класса парсинга"""
        logging.basicConfig(
            level=logging.INFO,
            filename="eanabatov_web_parser.log",
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s",
        )
        self.__status = False
        self.__books = []
        self.current_parsing_code = None
        self.__page = None
        self.__text = None
        self.__soup = None
        self.counter = 0

    def __parsing(self, link: str) -> dict:
        """Парсит html страницу через запросы"""
        # counter: int = 0
        summary = {}
        link_for_parsing = link
        try:
            self.__page = urllib.request.urlopen(link_for_parsing)
            self.__text = self.__page.read()
            self.__soup = BeautifulSoup(self.__text, features="html.parser")
        except:
            logging.error(
                f"process {self.current_parsing_code}. Страшно, очень страшно! Мы не знаем что это такое, если бы мы "
                f"знали что это такое,"
                "но мы не знаем что это такое!"
            )
            raise URLError
        if self.__page.getcode() != 200:
            logging.error(f"Код: {self.__page.getcode()}")
            raise HTTPError(f"Error code: {self.__page.getcode()}")
        if (ultimate_finder(link_for_parsing, "Издательство:") is None) and (
            ultimate_finder(link_for_parsing, "Тираж:") is None
        ):
            logging.info(f"{self.current_parsing_code} не книга ({self.__link()})")
        else:
            try:
                summary["in_stock"] = self.__in_stock()
            except:
                summary["in_stock"] = None
            try:
                summary["book_name"] = self.__book_name()
            except:
                summary["book_name"] = None
            try:
                summary["author_name"] = self.__author_name()
            except:
                summary["author_name"] = None
            try:
                summary["shop_price"] = self.__shop_price()
            except:
                summary["shop_price"] = None
            try:
                summary["internet_price"] = self.__internet_price()
            except:
                summary["internet_price"] = None
            try:
                summary["the_year_of_publishing"] = ultimate_finder(
                    link_for_parsing, "Год издания:"
                )
            except:
                summary["the_year_of_publishing"] = None
            summary["publisher"] = ultimate_finder(link_for_parsing, "Издательство:")
            summary["publish_place"] = ultimate_finder(
                link_for_parsing, "Место издания:"
            )
            summary["text_language"] = ultimate_finder(link_for_parsing, "Язык текста:")
            summary["cover_type"] = ultimate_finder(link_for_parsing, "Тип обложки:")
            summary["paper_type"] = ultimate_finder(link_for_parsing, "Бумага:")
            summary["Illustrations"] = ultimate_finder(link_for_parsing, "Иллюстрации:")
            summary["Illustrators"] = ultimate_finder(link_for_parsing, "Иллюстраторы:")
            summary["weight"] = ultimate_finder(link_for_parsing, "Вес:")
            summary["Circulation"] = ultimate_finder(link_for_parsing, "Тираж:")
            summary["product_code"] = ultimate_finder(link_for_parsing, "Код товара:")
            summary["vendor_code"] = ultimate_finder(link_for_parsing, "Артикул:")
            summary["isbn"] = ultimate_finder(link_for_parsing, "ISBN:")
            summary["pegi"] = ultimate_finder(link_for_parsing, "Возраст:")
            summary["on_sale_from"] = ultimate_finder(link_for_parsing, "В продаже с:")
            summary["link_for_parsing"] = self.__link()
            self.counter += 1
            logging.info(
                f"Process {self.current_parsing_code}: OK (counter: {self.counter})"
            )
        return summary

    def __book_name(self) -> str:
        """Название книги"""
        return (
            self.__soup.find("span", class_="link-gray-light")
            .text.replace(" ", "")
            .strip()
        )

    def __author_name(self) -> str:
        """Имя автора"""
        return self.__soup.find("a", class_="author-name").text.replace(" ", "").strip()

    def __shop_price(self) -> str:
        """Цена в магазине (отсутствует если товара нет в наличии)"""
        return self.__soup.find("span", class_="rubs").text.replace(" ", "").strip()

    def __internet_price(self) -> str:
        """Цена на сайте (отсутствует если товара нет в наличии)"""
        return (
            self.__soup.find("span", class_="silver rubs rubfont")
            .text.replace(" ", "")
            .strip()
        )

    def __link(self) -> str:
        """Находит ссылку на страницу с книгой"""
        return self.__soup.find("link").get("href")

    def __in_stock(self) -> str:
        """Определяет в наличии ли книга в магазине на данный момент"""
        stock = None
        try:
            stock = (
                self.__soup.find("span", class_="book__shop-instock")
                .text.replace(" ", " ")
                .strip()
            )
        except:
            stock = (
                self.__soup.find("span", class_="instock1")
                .text.replace(" ", " ")
                .strip()
                .lower()
            )
        return stock

    def __is_done(self):
        self.__status = False

    def __return_data_from_parsing(self) -> List[dict] or None:
        result = None
        if self.__books:
            result = self.__books
        return result

    def start_parsing(self, start_parsing_code: int, end_parsing_code: int) -> List[dict]:
        """class management method"""
        if end_parsing_code < start_parsing_code:
            raise KeyError("End point smaller then starting point")
        self.__status = True
        self.current_parsing_code = int(start_parsing_code)
        result = None
        while self.current_parsing_code <= int(end_parsing_code):
            result = self.__parsing(
                "https://www.moscowbooks.ru/book/"
                + f"{self.current_parsing_code}"
                + "/"
            )
            if result != {}:
                self.__books.append(result)
            self.current_parsing_code += 1
        self.__is_done()
        return self.__return_data_from_parsing()


if __name__ == "__main__":
    main()
