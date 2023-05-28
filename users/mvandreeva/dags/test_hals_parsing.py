"""
Тесты модуля hals_parsing
"""

import pytest
# from bs4 import BeautifulSoup
from hals_parsing import HALSParser #, HALSParserFFile
# from page_parsing import PagePerser

def test_hals_parsing_get_title():
    """
    Тест загрузки данных в словарь
    """
    flats_data = HALSParser("https://hals-development.ru/realty/residential")
    flats_dict_list = flats_data.get_dict_list()
    assert flats_dict_list
    