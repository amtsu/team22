"""Модуль парсинга сайта книжного магазина
https://www.moscowbooks.ru/
(онлайн)
"""
import logging
from typing import List
import sys
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

from team22.users.EANabatov.TR_parsing.logs.logs_config import start_logs
from team22.users.EANabatov.TR_parsing.parsing_helper import ultimate_finder


class BookStoreParser:
    """Класс парсинга сайта книжного магазина"""

    def __init__(self):
        """Конструктор класса парсинга"""
        self.__status: bool = False
        self.__books: List[dict] = []
        self.__current_parsing_code: int = 0
        self.__counter: int = 0
        start_logs()

    def __parsing(self, link: str) -> dict:
        """Парсит html страницу через запросы"""
        self.__secure()
        summary: dict = {}
        link_for_parsing: str = link
        soup = self.__make_get_request(link_for_parsing)
        if (ultimate_finder("Издательство:", soup) is None) and (
            ultimate_finder("Тираж:", soup) is None
        ):
            logging.info(
                "%s не книга (%s)", self.__current_parsing_code, link_for_parsing
            )
        else:
            try:
                summary["in_stock"] = self.__in_stock(soup)
            except Exception:
                summary["in_stock"] = ""
            try:
                summary["book_name"] = self.__book_name(soup)
            except Exception:
                summary["book_name"] = ""
            try:
                summary["author_name"] = self.__author_name(soup)
            except Exception:
                summary["author_name"] = ""
            try:
                summary["shop_price"] = self.__shop_price(soup)
            except Exception:
                summary["shop_price"] = ""
            try:
                summary["internet_price"] = self.__internet_price(soup)
            except Exception:
                summary["internet_price"] = ""
            try:
                summary["the_year_of_publishing"] = ultimate_finder(
                    "Год издания:", soup
                )
            except Exception:
                summary["the_year_of_publishing"] = ""
            summary["publisher"] = ultimate_finder("Издательство:", soup)
            summary["publish_place"] = ultimate_finder("Место издания:", soup)
            summary["text_language"] = ultimate_finder("Язык текста:", soup)
            summary["cover_type"] = ultimate_finder("Тип обложки:", soup)
            summary["paper_type"] = ultimate_finder("Бумага:", soup)
            summary["Illustrations"] = ultimate_finder("Иллюстрации:", soup)
            summary["Illustrators"] = ultimate_finder("Иллюстраторы:", soup)
            summary["weight"] = ultimate_finder("Вес:", soup)
            summary["Circulation"] = ultimate_finder("Тираж:", soup)
            summary["product_code"] = ultimate_finder("Код товара:", soup)
            summary["vendor_code"] = ultimate_finder("Артикул:", soup)
            summary["isbn"] = ultimate_finder("ISBN:", soup)
            summary["pegi"] = ultimate_finder("Возраст:", soup)
            summary["on_sale_from"] = ultimate_finder("В продаже с:", soup)
            summary["link_for_parsing"] = link_for_parsing
            self.__counter += 1
            logging.info(
                "Process %s: OK (counter: %s)",
                self.__current_parsing_code,
                self.__counter,
            )
        return summary

    def __make_get_request(self, link: str):
        try:
            page = urlopen(link)
            text: bytes = page.read()
            soup: object = BeautifulSoup(text, features="html.parser")
            if page.getcode() != 200:
                logging.error(f"Код: {page.getcode()} ({link})")
                raise URLError(
                    reason="Проблема с сервером или соединением",
                    filename="web_page_parser.py",
                )
            return soup
        except Exception:
            logging.error(
                f"process {self.__current_parsing_code}. Страшно, очень страшно! Мы не знаем что это такое, если бы мы "
                f"знали что это такое,"
                "но мы не знаем что это такое!"
                "P.S. Проблема с URL"
            )
            raise URLError(
                reason="Проблема с URL",
                filename="web_page_parser.py",
            )

    def __book_name(self, soup: object) -> str:
        """Название книги"""
        self.__secure()
        return soup.find("span", class_="link-gray-light").text.replace(" ", "").strip()

    def __author_name(self, soup: object) -> str:
        """Имя автора"""
        self.__secure()
        return soup.find("a", class_="author-name").text.replace(" ", "").strip()

    def __shop_price(self, soup: object) -> str:
        """Цена в магазине (отсутствует если товара нет в наличии)"""
        self.__secure()
        return soup.find("span", class_="rubs").text.replace(" ", "").strip()

    def __internet_price(self, soup: object) -> str:
        """Цена на сайте (отсутствует если товара нет в наличии)"""
        self.__secure()
        return (
            soup.find("span", class_="silver rubs rubfont")
            .text.replace(" ", "")
            .strip()
        )

    def __in_stock(self, soup: object) -> str:
        """Определяет в наличии ли книга в магазине на данный момент"""
        self.__secure()
        try:
            stock = (
                soup.find("span", class_="book__shop-instock")
                .text.replace(" ", " ")
                .strip()
            )
        except:
            stock = (
                soup.find("span", class_="instock1")
                .text.replace(" ", " ")
                .strip()
                .lower()
            )
        return stock

    def __is_done(self):
        """Деактивация статуса парсера"""
        self.__status = False

    def __in_progress(self):
        """Активация статуса парсера"""
        self.__status = True

    def __secure(self):
        """Проверка на сбой статуса парсера"""
        if not self.__status:
            sys.exit(126)

    def start_parsing(
        self, start_parsing_code: int, end_parsing_code: int
    ) -> List[dict]:
        """class management method"""
        if end_parsing_code < start_parsing_code:
            start_parsing_code, end_parsing_code = end_parsing_code, start_parsing_code
        self.__in_progress()
        self.__current_parsing_code = int(start_parsing_code)
        while self.__current_parsing_code <= int(end_parsing_code):
            result = self.__parsing(
                "https://www.moscowbooks.ru/book/"
                + f"{self.__current_parsing_code}"
                + "/"
            )
            if result != {}:
                self.__books.append(result)
            self.__current_parsing_code += 1
        self.__is_done()
        return self.__books
