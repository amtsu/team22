"""
Тесты модуля hals_parsing
"""

import pytest
# from bs4 import BeautifulSoup

from hals_parsing import HALSParser, HALSParserFFile
# from page_parsing import PageParser

def test_hals_parsing_get_title():
    """
    Тест загрузки данных в словарь
    """
    flats_data = HALSParser("https://hals-development.ru/realty/residential")
    flats_dict_list = flats_data.get_dict_list()
    assert flats_dict_list
    
    
#     одна фикстура для страницы с проектами, вторая - для списка из текстов страницы каждого проекта

@pytest.fixture()
def read_ffile_h_main():
    text = ""
    with open("sources/hals_projects", "rb") as response:
        text = response.read()
    return text

@pytest.fixture()
def read_ff_h_projects():
    projects_pages = {}
    with open("sources/hals_kosmo", "rb") as response:
        projects_pages["hals_kosmo"] = response.read()
    with open("sources/hals_teatral", "rb") as response:
        projects_pages["hals_teatral"] = response.read()
    with open("sources/hals_engels", "rb") as response:
        projects_pages["hals_engels"] = response.read()
    with open("sources/hals_shossejnaya", "rb") as response:
        projects_pages["hals_shossejnaya"] = response.read()
    with open("sources/hals_zamoskvorech", "rb") as response:
        projects_pages["hals_zamoskvorech"] = response.read()
    return projects_pages


def test_hals_parsing_ffile(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    pprint(flats_dict_list)
    assert not flats_dict_list == []