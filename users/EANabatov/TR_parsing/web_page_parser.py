"""
Модуль парсинга сайта книжного магазина
https://www.moscowbooks.ru/
(онлайн)
"""
import logging
import re

from bs4 import BeautifulSoup
import urllib.request

from typing import List

from parsing_helper import ultimate_finder


def main():
    start_parsing_code = input("Введите начальный код товара для парсинга: ")
    end_parsing_code = input("Введите конечный код товара для парсинга: ")
    if end_parsing_code < start_parsing_code:
        raise KeyError("End point smaller then starting point")
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
        self.current_parsing_code = None
        self.__status = False
        self.__books = []

    def __parsing(self, link=str) -> dict:
        """Парсит html страницу через запросы"""
        counter = 1
        summary = {}
        try:
            self.page = urllib.request.urlopen(link)
            self.text = self.page.read()
            self.soup = BeautifulSoup(self.text, features="html.parser")
            if self.page.getcode() == 200:
                if self.soup.find(
                    href=re.compile("__books"), class_="link-gray-light"
                ) and not self.soup.find(
                    href=re.compile("magazines"), class_="link-gray-light"
                ):
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
                            link, "Год издания:"
                        )
                    except:
                        summary["the_year_of_publishing"] = None
                    summary["publisher"] = ultimate_finder(link, "Издательство:")
                    summary["publish_place"] = ultimate_finder(link, "Место издания:")
                    summary["text_language"] = ultimate_finder(link, "Язык текста:")
                    summary["cover_type"] = ultimate_finder(link, "Тип обложки:")
                    summary["paper_type"] = ultimate_finder(link, "Бумага:")
                    summary["Illustrations"] = ultimate_finder(link, "Иллюстрации:")
                    summary["Illustrators"] = ultimate_finder(link, "Иллюстраторы:")
                    summary["weight"] = ultimate_finder(link, "Вес:")
                    summary["Circulation"] = ultimate_finder(link, "Тираж:")
                    summary["product_code"] = ultimate_finder(link, "Код товара:")
                    summary["vendor_code"] = ultimate_finder(self.link, "Артикул:")
                    summary["isbn"] = ultimate_finder(link, "ISBN:")
                    summary["pegi"] = ultimate_finder(link, "Возраст:")
                    summary["on_sale_from"] = ultimate_finder(link, "В продаже с:")
                    summary["link"] = self.link()
                    logging.info(
                        f"Process {self.current_parsing_code}: OK (counter: {counter})"
                    )
                    counter += 1
                else:
                    logging.info(
                        f"{self.current_parsing_code} не книга ({self.link()})"
                    )
            else:
                logging.error(f"{self.page.getcode()}")
        except:
            logging.error(
                f"process {self.current_parsing_code}. Страшно, очень страшно! Мы не знаем что это такое, если бы мы "
                f"знали что это такое,"
                "но мы не знаем что это такое!"
            )
        return summary

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
        stock = None
        try:
            stock = (
                self.soup.find("span", class_="book__shop-instock")
                .text.replace(" ", " ")
                .strip()
            )
        except:
            stock = (
                self.soup.find("span", class_="instock1")
                .text.replace(" ", " ")
                .strip()
                .lower()
            )
        return stock

    def __is_done(self) -> List[dict]:
        self.__status = False
        print(self.__books)

    def start_parsing(self, start_parsing_code, end_parsing_code) -> None:
        self.__status = True
        self.current_parsing_code = int(start_parsing_code)
        result = None
        while self.current_parsing_code <= int(end_parsing_code):
            result = self.__parsing(
                "https://www.moscowbooks.ru/book/"
                + str(self.current_parsing_code)
                + "/"
            )
            if result != {}:
                self.__books.append(result)
            self.current_parsing_code += 1
        self.__is_done()


if __name__ == "__main__":
    main()
