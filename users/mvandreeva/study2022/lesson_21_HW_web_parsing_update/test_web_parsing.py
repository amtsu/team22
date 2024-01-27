#!/usr/local/bin/python
# coding: utf-8

import pytest
from web_parsing import PageParsing
import urllib
import urllib.request
from bs4 import BeautifulSoup

def test_page_parsing_read():
    page = PageParsing("https://quke.ru/shop/UID_70281___306_.html")
    quke_page_parsing = page.get_page()
    with urllib.request.urlopen("https://quke.ru/shop/UID_70281___306_.html") as page_2:
        text = page_2.read()
    print(quke_page_parsing)
    #print(type(quke_one_page_parsing))
    #print("********************")
    print(text)
    assert quke_page_parsing == text
    
def test_page_parsing_read_2():
    page = PageParsing("https://quke.ru/shop/UID_70281___306_.html")
    quke_one_page_parsing = page.get_page()
    with urllib.request.urlopen("https://quke.ru/shop/UID_70281___306_.html") as page:
        text = page.read()
        #soup = BeautifulSoup(text)
    #print(quke_one_page_parsing)
    #print(type(quke_one_page_parsing))
    #print("********************")
    #print(soup)
    assert quke_one_page_parsing == text
