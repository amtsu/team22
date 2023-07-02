"""
Тесты модуля hals_parsing
"""

import pytest
# from bs4 import BeautifulSoup

from nash_dom_parsing import NashDomParser, NashDomParserFFile
# from page_parsing import PagePerser

def test_nd_parsing_get_title():
    """
    Тест загрузки данных в словарь
    """
    flats_data = NashDomParser("https://hals-development.ru/realty/residential")
    flats_dict_list = flats_data.get_dict_list()
    assert flats_dict_list
    
    
#     одна фикстура для страницы с проектами, вторая - для списка из текстов страницы каждого проекта

@pytest.fixture()
def read_ffile_nd():
    text = ""
    with open("sources/nash_dom", "rb") as response:
        text = response.read()
    return text

# @pytest.fixture()
# def read_ff_nd_projects():
#     projects_pages = {}
#     with open("sources/hals_kosmo", "rb") as response:
#         projects_pages["hals_kosmo"] = response.read()
#     with open("sources/hals_teatral", "rb") as response:
#         projects_pages["hals_teatral"] = response.read()
#     with open("sources/hals_engels", "rb") as response:
#         projects_pages["hals_engels"] = response.read()
#     with open("sources/hals_shossejnaya", "rb") as response:
#         projects_pages["hals_shossejnaya"] = response.read()
#     with open("sources/hals_zamoskvorech", "rb") as response:
#         projects_pages["hals_zamoskvorech"] = response.read()
#     return projects_pages


# def test_hals_parsing_ffile(read_ffile_nd_main, read_ff_nd_projects):
#     flats_data = NashDomParserFFile(read_ffile_nd_main)
#     flats_dict_list = flats_data.get_dict_list(read_ff_nd_projects)
#     pprint(flats_dict_list)
#     assert not flats_dict_list == []

def test_hals_parsing_ffile(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    pprint(flats_dict_list)
    assert not flats_dict_list == []
    
