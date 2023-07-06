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
    print(flats_dict_list)
    assert not flats_dict_list == []
    
def test_nash_dom_parsing_ff_nd_price(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["price"] != 0
    
def test_nash_dom_parsing_ff_nd_price_sale(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["price_sale"] != 0
        
def test_nash_dom_parsing_ff_nd_title(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["title"] != ""
    
def test_nash_dom_parsing_ff_nd_category(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["category"] != ""
    
def test_nash_dom_parsing_ff_nd_brand(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["brand"] != ""
    
def test_nash_dom_parsing_ff_nd_brand_url(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["brand_url"] != ""
        
def test_nash_dom_parsing_ff_nd_url(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["url"] != ""
    
def test_nash_dom_parsing_ff_nd_img_url(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["plan"] != ""
        
def test_nash_dom_parsing_ff_nd_description(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["description"] != ""
    
def test_nash_dom_parsing_ff_nd_source_url(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["source_url"] != ""
        
def test_nash_dom_parsing_ff_nd_apartment_area(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["area"] != ""
    
def test_nash_dom_parsing_ff_nd_apartment_completion_quarter(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["apartment_completion_quarter"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_completion_year(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["apartment_completion_year"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_floor(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["floor"] != 0
        
def test_nash_dom_parsing_ff_nd_apartment_floors_total(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["apartment_floors_total"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_ceilingheight(read_ffile_h_main, read_ff_h_projects): # в API строка?
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["apartment_ceilingheight"] != 0 or item["apartment_ceilingheight"] != ""
        
def test_nash_dom_parsing_ff_nd_apartment_room(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["rooms"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_ppm(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["apartment_ppm"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_address(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["full_address"] != ""
        
def test_nash_dom_parsing_ff_nd_apartment_location_lat(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["apartment_location_lat"] != ""
    
def test_nash_dom_parsing_ff_nd_apartment_location_lon(read_ffile_h_main, read_ff_h_projects):
    flats_data = HALSParserFFile(read_ffile_h_main)
    flats_dict_list = flats_data.get_dict_list(read_ff_h_projects)
    for item in flats_dict_list:
        assert item["apartment_location_lon"] != ""