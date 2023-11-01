"""

"""
from urllib.error import URLError

import pytest

from local_page_parser import parsing
from web_page_parser import BookStoreParser
from parsing_helper import ultimate_finder


class TestWebParser:
    """"""

    # def test__parser(self):
    #     """"""
    #     test_object = BookStoreParser()
    #     with pytest.raises(URLError):
    #         test_object.start_parsing(1156290, 1156290)

    def test_first_condition(self):
        test_object = BookStoreParser()
        with pytest.raises(KeyError):
            test_object.start_parsing(1156666, 1155555)

    def test_local_parser(self):
        """"""
        test_object = BookStoreParser()
        kek = []
        kek.append(parsing())
        assert kek == test_object.start_parsing(1156290, 1156290)

    # def test_function(self):
    #     """"""
    #     link = "https://www.moscowbooks.ru/book/1156292/"
    #     assert isinstance(ultimate_finder(link, "Издательство:"), str)
