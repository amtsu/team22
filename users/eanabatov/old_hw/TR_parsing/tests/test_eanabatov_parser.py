"""

"""
from urllib.request import urlopen

import pytest
from bs4 import BeautifulSoup

from team22.users.EANabatov.TR_parsing.local_page_parser import parsing
from team22.users.EANabatov.TR_parsing.web_page_parser import BookStoreParser
from team22.users.EANabatov.TR_parsing.parsing_helper import ultimate_finder


class TestWebParser:
    """Класс тестирования веб парсера"""

    def test_normal_work_web_parser(self):
        "Проверка нормальной работы парсера"
        test_object = BookStoreParser()
        normal_case = [
            {
                "in_stock": "в наличии",
                "book_name": "Фундаментальный подход к программной архитектуре: паттерны, свойства, проверенные методы",
                "author_name": "Ричардс М.",
                "shop_price": "3340",
                "internet_price": "2977",
                "the_year_of_publishing": "2023",
                "publisher": "Питер",
                "publish_place": "СПб",
                "text_language": "русский",
                "cover_type": "Мягкая обложка",
                "paper_type": None,
                "Illustrations": None,
                "Illustrators": None,
                "weight": "690 гр.",
                "Circulation": None,
                "product_code": "1156290",
                "vendor_code": "К29878",
                "isbn": "978-5-4461-1842-7",
                "pegi": "16+",
                "on_sale_from": "21.06.2023",
                "link_for_parsing": "https://www.moscowbooks.ru/book/1156290/",
            },
        ]
        assert test_object.start_parsing(1156290, 1156290) == normal_case


class TestLocalParser:
    def test_local_parser(self):
        """Проверка нормальной работы парсера"""
        normal_case = [
            {
                "in_stock": "в наличии",
                "book_name": "Фундаментальный подход к программной архитектуре: паттерны, свойства, проверенные методы",
                "author_name": "Ричардс М.",
                "shop_price": "3340",
                "internet_price": "2977",
                "the_year_of_publishing": "2023",
                "publisher": "Питер",
                "publish_place": "СПб",
                "text_language": "русский",
                "cover_type": "Мягкая обложка",
                "paper_type": None,
                "Illustrations": None,
                "Illustrators": None,
                "weight": "690 гр.",
                "Circulation": None,
                "product_code": "1156290",
                "vendor_code": "К29878",
                "isbn": "978-5-4461-1842-7",
                "pegi": "16+",
                "on_sale_from": "21.06.2023",
            }
        ]
        test_parsing = [parsing()]
        assert test_parsing == normal_case


class TestParsingHelper:
    def test_normal_work_parsing_helper(self):
        "Проверка нормальной работы функции парсера"
        soup = BeautifulSoup(
            urlopen("https://www.moscowbooks.ru/book/1156291/").read(),
            features="html.parser",
        )
        expected = "Питер"
        assert ultimate_finder("Издательство:", soup) == expected
