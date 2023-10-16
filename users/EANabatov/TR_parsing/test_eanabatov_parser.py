"""

"""
import pytest

from local_page_parser import parsing
from web_page_parser import BookStoreParser
from parsing_helper import ultimate_finder


class TestParser:
    """"""

    def test_web_paser(self):
        """"""
        test_object = BookStoreParser()
        assert isinstance(test_object.__parsing(11562900, 11562900), list)

    def test_first_condition(self):
        test_object = BookStoreParser()
        with pytest.raises(KeyError):
            test_object.__parsing(1156666, 1155555)

    def test_local_parser(self):
        """"""
        assert isinstance(parsing(), dict)

    def test_function(self):
        """"""
        link = "https://www.moscowbooks.ru/book/1156292/"
        assert isinstance(ultimate_finder(link, "Издательство:"), str)
