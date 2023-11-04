"""
Модуль парсинга сайта книжного магазина
https://www.moscowbooks.ru/
(локальная страница)
"""
from bs4 import BeautifulSoup
import urllib.request
from team22.users.EANabatov.TR_parsing.parsing_helper import ultimate_finder


def parsing() -> dict:
    """Основная функция парсинга локальной страницы"""
    summary: dict = {}
    link: str = "file:/home/evgeniy/Tsurkov_repository/team22/users/EANabatov/TR_parsing/html_page/book_parsing.html"
    page: classmethod = urllib.request.urlopen(link)
    text: bytes = page.read()
    soup: object = BeautifulSoup(text, features="html.parser")
    try:
        summary["in_stock"] = in_stock(soup)
    except Exception:
        summary["in_stock"] = None
    try:
        summary["book_name"] = book_name(soup)
    except Exception:
        summary["book_name"] = None
    try:
        summary["author_name"] = author_name(soup)
    except Exception:
        summary["author_name"] = None
    try:
        summary["shop_price"] = shop_price(soup)
    except Exception:
        summary["shop_price"] = None
    try:
        summary["internet_price"] = internet_price(soup)
    except Exception:
        summary["internet_price"] = None
    try:
        summary["the_year_of_publishing"] = ultimate_finder("Год издания:", soup)
    except Exception:
        summary["the_year_of_publishing"] = None
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
    return summary


def book_name(soup: object) -> str:
    """Поиск названия книги"""
    return soup.find("span", class_="link-gray-light").text.replace(" ", " ").strip()


def author_name(soup: object) -> str:
    """Поиск имени автора"""
    return soup.find("a", class_="author-name").text.replace(" ", "").strip()


def shop_price(soup: object) -> str:
    """Поиск цены в магазине"""
    return soup.find("span", class_="rubs").text.replace(" ", "").strip()


def internet_price(soup: object) -> str:
    """Поиск цены в интернет магазине"""
    return soup.find("span", class_="silver rubs rubfont").text.replace(" ", "").strip()


def in_stock(soup: object) -> str:
    """
    Определяет в наличии ли книга в магазине на данный момент.
    """
    soup = soup
    stock = None
    try:
        stock = (
            soup.find("span", class_="book__shop-instock")
            .text.replace(" ", " ")
            .strip()
        )
    except Exception:
        stock = (
            soup.find("span", class_="instock1").text.replace(" ", " ").strip().lower()
        )
    return stock


parsing()
