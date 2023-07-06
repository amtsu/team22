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

def test_nash_dom_parsing_ffile(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    pprint(flats_dict_list)
    assert not flats_dict_list == []
    
def test_nash_dom_parsing_ff_no_data(read_ffile_nd):
    no_data = []
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for param in flats_dict_list:
        if flats_dict_list[param] == 0 or flats_dict_list[param] == "":
            no_data.append(param)
    pprint(no_data)
    assert no_data == []
    
def test_nash_dom_parsing_ff_nd_price(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["price"] != 0
    
def test_nash_dom_parsing_ff_nd_price_sale(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["price_sale"] != 0
        
def test_nash_dom_parsing_ff_nd_title(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["title"] != ""
    
def test_nash_dom_parsing_ff_nd_category(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["category"] != ""
    
def test_nash_dom_parsing_ff_nd_brand(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["brand"] != ""
    
def test_nash_dom_parsing_ff_nd_brand_url(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["brand_url"] != ""
        
def test_nash_dom_parsing_ff_nd_url(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["url"] != ""
    
def test_nash_dom_parsing_ff_nd_img_url(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["img_url"] != ""
        
def test_nash_dom_parsing_ff_nd_description(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["description"] != ""
    
def test_nash_dom_parsing_ff_nd_source_url(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["source_url"] != ""
        
def test_nash_dom_parsing_ff_nd_apartment_area(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_area"] != ""
    
def test_nash_dom_parsing_ff_nd_apartment_completion_quarter(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_completion_quarter"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_completion_year(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_completion_year"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_floor(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_floor"] != 0
        
def test_nash_dom_parsing_ff_nd_apartment_floors_total(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_floors_total"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_ceilingheight(read_ffile_nd): # в API строка?
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_ceilingheight"] != 0 or item["apartment_ceilingheight"] != ""
        
def test_nash_dom_parsing_ff_nd_apartment_room(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_room"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_ppm(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_ppm"] != 0
    
def test_nash_dom_parsing_ff_nd_apartment_address(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_address"] != ""
        
def test_nash_dom_parsing_ff_nd_apartment_location_lat(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_location_lat"] != ""
    
def test_nash_dom_parsing_ff_nd_apartment_location_lon(read_ffile_nd):
    flats_data = NashDomParserFFile(read_ffile_nd)
    flats_dict_list = flats_data.get_dict_list()
    for item in flats_dict_list:
        assert item["apartment_location_lon"] != ""
    
# @pytest.fixture()
# def get_params():
#     with open("params.txt", "rb") as params:
#         params_list = list(params)
#     return params_list

# # def construct_tests()
    
# def test_nash_dom_parsing_ff_nd(read_ffile_nd):
#     # no_data = []
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for param in flats_dict_list:
#     #     if flats_dict_list[param] == 0 or flats_dict_list[param] == "":
#     #         no_data.append(param)
#     # pprint(no_data)
#     assert no_data == []
    
    
    
"""
Декоратор дополняет функцию данными из списка (получаем из файла через фикстуру),
запускает эту функцию
собирает результат её выполнения
выдает assertion? если данных нет (0 или "")
продолжает проверку следующей функции, дополненной следующими данными по списку
"""