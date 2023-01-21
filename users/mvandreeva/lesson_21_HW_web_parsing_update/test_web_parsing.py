#!/usr/local/bin/python
# coding: utf-8

import pytest
from web_parsing import OnePageParsing

def test_one_page_parsing_read():
    quke_one_page_parsing = OnePageParsing("https://quke.ru/shop/UID_70281___306_.html").read_page()
    with urllib.request.urlopen("https://quke.ru/shop/UID_70281___306_.html") as page:
        text = page.read()
        soup = BeautifulSoup(text)
    #print(quke_one_page_parsing)
    #print(type(quke_one_page_parsing))
    #print("********************")
    #print(soup)
    if quke_one_page_parsing == soup:
        return "test_open_page_prepare_soup is passed"
    else:
        assert False