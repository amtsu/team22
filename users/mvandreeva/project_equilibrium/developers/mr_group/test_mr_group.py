"""
Тесты модуля hals_parsing
"""

import pytest
# from bs4 import BeautifulSoup

from mr_group_parsing import MRGroupParser, MRGroupParserFFile
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
def read_ffile_mrg():
    text = ""
    with open("sources/mrgroup", "rb") as response:
        text = response.read()
    return text
    
@pytest.fixture()
def get_params():
    with open("params.txt", "rb") as params:
        params_list = list(params)
    return params_list

@pytest.fixture()
def download_dict_mr_group():
    url = "https://www.mr-group.ru/flats/"
    flats_data = MRGroupParser(url)
    flats_dict_list = flats_data.get_dict_list()
    # print("fixture")
    return flats_dict_list

def test_page_parser_open():
    url = "https://www.mr-group.ru/flats/"
    page_data = PageParser(url)
    page_text = page_data.use_b_soup()
    # print(page_text)
    assert page_text


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

def test_nd_parsing_get_data(download_dict_mr_group):
    """
    Тест загрузки данных в словарь
    """
    flats_dict_list = download_dict_mr_group
    assert flats_dict_list
    

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
# def test_nash_dom_parsing_nd_title(download_dict_nash_dom):
#     flats_dict_list = download_dict_nash_dom
#     for item in flats_dict_list:
#         assert item["title"] 
        
def test_mrgroup_parsing_nodata(download_dict_mr_group, get_params):
    flats_dict_list = download_dict_mr_group
    for item in flats_dict_list:
        data_list = get_params
        for data in data_list:
            assert data in item.keys() 
            
def test_mrgroup_parsing_nodata_ff(read_ffile_mrg, get_params):
    flats_data = MRGroupParserFFile(read_ffile_mrg)
    flats_dict_list = flats_data.get_dict_list()
    print(flats_dict_list)
    for item in flats_dict_list:
        data_list = get_params
        for data in data_list:
            assert data in item.keys() 
        
# !!!!!!!!!!!!!!!!!!


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