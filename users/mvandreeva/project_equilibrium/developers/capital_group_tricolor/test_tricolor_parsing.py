import pytest
from bs4 import BeautifulSoup
from tricolor_parsing import TricolorParser, TricolorParserFFile
from page_parsing import PagePerser


def test_page_parser_open():
    page_data = PagePerser("https://cg-tricolor.ru/catalog/flats")
    page_text = page_data.open_page()
    assert not page_text == ""
    
def test_page_parser_open_file():
    page_data = PagePerser("https://cg-tricolor.ru/catalog/flats")
    page_text = page_data.open_page()
    with open("sources/tricolor", "rb") as page:
        saved_page = page.read()
    assert not page_text == saved_page
    
def test_page_parser_use_b_soup():
    page_data = PagePerser("https://cg-tricolor.ru/catalog/flats")
    page_b_soup = page_data.use_b_soup()
    with open("sources/tricolor", "rb") as page:
        saved_page = page.read()
    saved_b_soup = BeautifulSoup(saved_page, features="html.parser")
    assert not page_b_soup == saved_b_soup
    
@pytest.fixture()
def read_from_flie_tricolor():
    text = ''
    with open('sources/tricolor','rb') as response:
        text = response.read() 
    return text

def test_tricolor_parsing_get_title_ffile(read_from_flie_tricolor):
    flats_data = TricolorParserFFile(read_from_flie_tricolor)
    flats_dict_list = flats_data.get_dict_list()
    assert not flats_dict_list == []
    
def test_tricolor_parsing_get_title():
    flats_data = TricolorParser("https://cg-tricolor.ru/catalog/flats")
    flats_dict_list = flats_data.get_dict_list()
    assert not flats_dict_list == []