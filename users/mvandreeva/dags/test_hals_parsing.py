import pytest
from bs4 import BeautifulSoup
from hals_parsing import HALSParser, HALSParserFFile
from page_parsing import PagePerser

@pytest.fixture()
def read_from_flie_hals():
    text = ""
    with open("sources/hals", "rb") as response:
        text = response.read()
    return text

def test_hals_parsing_get_title_ffile(read_from_flie_hals):
    flats_data = HALSParserFFile(read_from_flie_hals)
    flats_dict_list = flats_data.get_dict_list()
    assert not flats_dict_list == []


def test_tricolor_parsing_get_title():
    flats_data = HALSParser("https://hals-development.ru/realty/residential")
    flats_dict_list = flats_data.get_dict_list()
    assert not flats_dict_list == []