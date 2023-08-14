import pytest
from cap_towers_parsing import PagePerser, CapTowersParser, CapTowersParserFFile

def test_page_parser_open():
    page_data = PagePerser("https://capitaltowers.ru/catalog/flats/")
    page_text = page_data.open_page()
    assert not page_text == ""
    
def test_page_parser_open_file():
    page_data = PagePerser("https://capitaltowers.ru/catalog/flats/")
    page_text = page_data.open_page()
    with open("sources/capitaltowers", "rb") as page:
        saved_page = page.read()
    assert not page_text == saved_page
    
@pytest.fixture()
def read_from_flie_capitaltowers():
    text = ''
    with open('sources/capitaltowers','rb') as response:
        text = response.read() 
    return text

def test_captower_parsing_get_tower_name_ffile(read_from_flie_capitaltowers):
    flats = CapTowersParserFFile(read_from_flie_capitaltowers)
    flats_tower = flats.get_tower_name()
    
def test_captower_parsing_get_tower_name():
    flats = CapTowersParser("https://capitaltowers.ru/catalog/flats/")
    flats_tower = flats.get_tower_name()