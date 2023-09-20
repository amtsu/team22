"""
Модуль парсинга сайта книжного магазина
https://www.moscowbooks.ru/
(локальная страница)
"""
from bs4 import BeautifulSoup
import urllib.request
from parsing_helper import ultimate_finder


def parsing() -> dict:
    """Основная функция парсинга локальной страницы"""
    summary = {}
    link = "file:./book_parsing.html"
    page = urllib.request.urlopen(link)
    text = page.read()
    soup = BeautifulSoup(text, features="html.parser")
    try:
        summary["in_stock"] = in_stock(soup)
    except:
        summary["in_stock"] = None
    try:
        summary["book_name"] = book_name(soup)
    except:
        summary["book_name"] = None
    try:
        summary["author_name"] = author_name(soup)
    except:
        summary["author_name"] = None
    try:
        summary["shop_price"] = shop_price(soup)
    except:
        summary["shop_price"] = None
    try:
        summary["internet_price"] = internet_price(soup)
    except:
        summary["internet_price"] = None
    try:
        summary["the_year_of_publishing"] = ultimate_finder(link, "Год издания:")
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
    summary["vendor_code"] = ultimate_finder(link, "Артикул:")
    summary["isbn"] = ultimate_finder(link, "ISBN:")
    summary["pegi"] = ultimate_finder(link, "Возраст:")
    summary["on_sale_from"] = ultimate_finder(link, "В продаже с:")
    return summary


def book_name(soup) -> str:
    """Поиск названия книги"""
    return soup.find("span", class_="link-gray-light").text.replace(" ", " ").strip()


def author_name(soup) -> str:
    """Поиск имени автора"""
    return soup.find("a", class_="author-name").text.replace(" ", "").strip()


def shop_price(soup) -> str:
    """Поиск цены в магазине"""
    return soup.find("span", class_="rubs").text.replace(" ", "").strip()


def internet_price(soup) -> str:
    """Поиск цены в интернет магазине"""
    return soup.find("span", class_="silver rubs rubfont").text.replace(" ", "").strip()


def in_stock(soup) -> str:
    """
    Определяет в наличии ли книга в магазине на данный момент.
    От наличия товара зависит поиск других функций.
    """
    stock = None
    try:
        stock = (
            soup.find("span", class_="book__shop-instock")
            .text.replace(" ", " ")
            .strip()
        )
    except:
        stock = (
            soup.find("span", class_="instock1").text.replace(" ", " ").strip().lower()
        )
    return stock
