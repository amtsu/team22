import pytest
from pik_parser import PagePerser, PIKParsing

def test_page_parser_open():
    page_data = PagePerser("https://www.pik.ru/search")
    page_text = page_data.open_page()
    assert not page_text == ""
    
def test_page_parser_open_file():
    page_data = PagePerser("https://www.pik.ru/search")
    page_text = page_data.open_page()
    with open("sources/pik", "rb") as page:
        saved_page = page.read()
    assert not page_text == saved_page
    
def test_pik_parsing_get_title():
    flats = PIKParsing("https://www.pik.ru/search")
    flats_title = flats.get_title()
        