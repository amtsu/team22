#!/usr/local/bin/python
# coding: utf-8
"""
Тесты модуля hals_parsing
"""

import pytest
# from bs4 import BeautifulSoup

from nash_dom_parsing import NashDomParser, NashDomParserFFile
from page_parsing import PageParser

# конкретные данные полное соответствие всех элементов
# кол-во словарей

# dict_1 = {'apartment_address': 'Республика Северная Осетия-Алания, г.Владикавказ, '
#                        'ул.Калинина,62',
#   'apartment_completion_data': [4, 2006],
#   'apartment_completion_quarter': 4,
#   'apartment_completion_year': 2006,
#   'apartment_floors_total': 9,
#   'apartment_status': 'Проблемный',
#   'brand': 'ЖСК - 121',
#   'source_url': 'https://наш.дом.рф/сервисы/каталог-новостроек/список-объектов/список?page=0&limit=10',
#   'title': 'Жилой дом'}
# if dict_1 in flats_dict_list:
    

@pytest.fixture()
def download_dict_nash_dom():
    url = "https://наш.дом.рф/сервисы/каталог-новостроек/список-объектов/список?page=0&limit=10"
    flats_data = NashDomParser(url)
    flats_dict_list = flats_data.get_dict_list()
    print("fixture")
    return flats_dict_list

def test_page_parser_open():
    url = "https://наш.дом.рф/сервисы/каталог-новостроек/список-объектов/список?page=0&limit=10"
    page_data = PageParser(url)
    page_text = page_data.open_page_encode()
    assert not page_text == ""


# def test_page_parser_open_file():
#     page_data = PagePerser("https://cg-tricolor.ru/catalog/flats")
#     page_text = page_data.open_page()
#     with open("sources/tricolor", "rb") as page:
#         saved_page = page.read()
#     assert not page_text == saved_page


# def test_page_parser_use_b_soup():
#     page_data = PagePerser("https://cg-tricolor.ru/catalog/flats")
#     page_b_soup = page_data.use_b_soup()
#     with open("sources/tricolor", "rb") as page:
#         saved_page = page.read()
#     saved_b_soup = BeautifulSoup(saved_page, features="html.parser")
#     assert not page_b_soup == saved_b_soup

def test_nd_parsing_get_data(download_dict_nash_dom):
    """
    Тест загрузки данных в словарь
    """
    flats_dict_list = download_dict_nash_dom
    assert flats_dict_list
    

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
# def test_nash_dom_parsing_ff_nd_price(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["price"] != 0

    
# def test_nash_dom_parsing_ff_nd_price_sale(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["price_sale"] != 0
        
def test_nash_dom_parsing_nd_title(download_dict_nash_dom):
    flats_dict_list = download_dict_nash_dom
    for item in flats_dict_list:
        assert item["title"] 
        
def test_nash_dom_parsing_nd_data(download_dict_nash_dom):
    flats_dict_list = download_dict_nash_dom
    for item in flats_dict_list:
        data_list = [ "title","quantity","price","price_sale","category","brand","brand_url","url","img_url","description","source_url","apartment_area","apartment_completion_quarter","apartment_completion_year","apartment_floor","apartment_floors_total","apartment_ceilingheight","apartment_room","apartment_ppm","apartment_address","apartment_location_lat","apartment_location_lon"]
        for data in data_list:
            assert data in item.keys() 
        

    
# def test_nash_dom_parsing_ff_nd_category(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["category"] != ""
    
def test_nash_dom_parsing_nd_brand(download_dict_nash_dom):
    flats_dict_list = download_dict_nash_dom
    for item in flats_dict_list:
        assert item["brand"]
    
# def test_nash_dom_parsing_ff_nd_brand_url(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["brand_url"] != ""
        
# def test_nash_dom_parsing_ff_nd_url(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["url"] != ""
    
# def test_nash_dom_parsing_ff_nd_img_url(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["img_url"] != ""
        
# def test_nash_dom_parsing_ff_nd_description(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["description"] != ""
    
# def test_nash_dom_parsing_ff_nd_source_url(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["source_url"] != ""
        
# def test_nash_dom_parsing_ff_nd_apartment_area(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_area"] != ""
    
def test_nash_dom_parsing_nd_apartment_completion_quarter(download_dict_nash_dom):
    flats_dict_list = download_dict_nash_dom
    for item in flats_dict_list:
        assert item["apartment_completion_quarter"]
    
def test_nash_dom_parsing_nd_apartment_completion_year(download_dict_nash_dom):
    flats_dict_list = download_dict_nash_dom
    for item in flats_dict_list:
        assert item["apartment_completion_year"]
    
# def test_nash_dom_parsing_ff_nd_apartment_floor(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_floor"] != 0
        
def test_nash_dom_parsing_nd_apartment_floors_total(download_dict_nash_dom):
    flats_dict_list = download_dict_nash_dom
    for item in flats_dict_list:
        assert item["apartment_floors_total"]
    
# def test_nash_dom_parsing_ff_nd_apartment_ceilingheight(read_ffile_nd): # в API строка?
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_ceilingheight"] != 0 or item["apartment_ceilingheight"] != ""
        
# def test_nash_dom_parsing_ff_nd_apartment_room(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_room"] != 0
    
# def test_nash_dom_parsing_ff_nd_apartment_ppm(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_ppm"] != 0
    
def test_nash_dom_parsing_nd_apartment_address(download_dict_nash_dom):
    flats_dict_list = download_dict_nash_dom
    for item in flats_dict_list:
        assert item["apartment_address"]
        
# def test_nash_dom_parsing_ff_nd_apartment_location_lat(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_location_lat"] != ""
    
# def test_nash_dom_parsing_ff_nd_apartment_location_lon(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_location_lon"] != ""

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
#     одна фикстура для страницы с проектами, вторая - для списка из текстов страницы каждого проекта

# @pytest.fixture()
# def read_ffile_nd():
#     text = ""
#     with open("sources/nash_dom", "rb") as response:
#         text = response.read()
#     return text

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

# def test_nash_dom_parsing_ffile(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     pprint(flats_dict_list)
#     assert not flats_dict_list == []
    
# def test_nash_dom_parsing_ff_no_data(read_ffile_nd):
#     no_data = []
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for param in flats_dict_list:
#         if flats_dict_list[param] == 0 or flats_dict_list[param] == "":
#             no_data.append(param)
#     pprint(no_data)
#     assert no_data == []
    
# def test_nash_dom_parsing_ff_nd_price(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["price"] != 0
    
# def test_nash_dom_parsing_ff_nd_price_sale(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["price_sale"] != 0
        
# def test_nash_dom_parsing_ff_nd_title(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["title"] != ""
    
# def test_nash_dom_parsing_ff_nd_category(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["category"] != ""
    
# def test_nash_dom_parsing_ff_nd_brand(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["brand"] != ""
    
# def test_nash_dom_parsing_ff_nd_brand_url(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["brand_url"] != ""
        
# def test_nash_dom_parsing_ff_nd_url(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["url"] != ""
    
# def test_nash_dom_parsing_ff_nd_img_url(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["img_url"] != ""
        
# def test_nash_dom_parsing_ff_nd_description(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["description"] != ""
    
# def test_nash_dom_parsing_ff_nd_source_url(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["source_url"] != ""
        
# def test_nash_dom_parsing_ff_nd_apartment_area(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_area"] != ""
    
# def test_nash_dom_parsing_ff_nd_apartment_completion_quarter(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_completion_quarter"] != 0
    
# def test_nash_dom_parsing_ff_nd_apartment_completion_year(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_completion_year"] != 0
    
# def test_nash_dom_parsing_ff_nd_apartment_floor(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_floor"] != 0
        
# def test_nash_dom_parsing_ff_nd_apartment_floors_total(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_floors_total"] != 0
    
# def test_nash_dom_parsing_ff_nd_apartment_ceilingheight(read_ffile_nd): # в API строка?
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_ceilingheight"] != 0 or item["apartment_ceilingheight"] != ""
        
# def test_nash_dom_parsing_ff_nd_apartment_room(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_room"] != 0
    
# def test_nash_dom_parsing_ff_nd_apartment_ppm(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_ppm"] != 0
    
# def test_nash_dom_parsing_ff_nd_apartment_address(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_address"] != ""
        
# def test_nash_dom_parsing_ff_nd_apartment_location_lat(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_location_lat"] != ""
    
# def test_nash_dom_parsing_ff_nd_apartment_location_lon(read_ffile_nd):
#     flats_data = NashDomParserFFile(read_ffile_nd)
#     flats_dict_list = flats_data.get_dict_list()
#     for item in flats_dict_list:
#         assert item["apartment_location_lon"] != ""
    
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