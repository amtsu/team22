#!/usr/local/bin/python
# coding: utf-8

import pytest
from chitai_gorod_one_item import ChitaiGorodGetPrice, ChitaiGorodGetTitle, ChitaiGorodGetAuthor, ChitaiGorodGetAuthorURL
from chitai_gorod_items_list import ChitaiGorodItemsList
from web_parsing import PageParsing
from bs4 import BeautifulSoup


# test_get_text_price из chitai_gorod - ChitaiGorodGetPrice
#def test_get_text_price_chitai_gorod():
#    page = PageParsing('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391')
#    page_text = page.read_page()
#    get_text_price = ChitaiGorodGetPrice(page_text).get_text()
#    #print("text=",get_text_price)
#    assert get_text_price == """\n      1\xa0100 ₽\n    """

# test_clean_data для price из chitai_gorod - ChitaiGorodGetPrice
def test_clean_data_price_chitai_gorod():
    page = PageParsing('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391')
    page_text = page.get_page()
    page_url = page.get_url()
    chitai_gorod = ChitaiGorodGetPrice(page_text, page_url)
    price = chitai_gorod.clean_data()
    assert isinstance(price, int)
   
    #print(type(price), price)

    
# test_get_text для author из chitai_gorod_one_item - ChitaiGorodGetAuthor
#def test_get_text_author_chitai_gorod():
#    
#    get_text_author = ChitaiGorodGetAuthor('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391').get_text()
#    assert get_text_author == """\n          Роберт С. Мартин\n        """

        
# test_clean_data для author из chitai_gorod_one_item - ChitaiGorodGetAuthor
def test_clean_data_author_chitai_gorod():
    page = PageParsing('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391')
    page_text = page.get_page()
    page_url = page.get_url()
    chitai_gorod = ChitaiGorodGetAuthor(page_text, page_url)
    author = chitai_gorod.clean_data() 
    assert author == "Роберт С. Мартин"
    #print(type(author), author)
    

# test_get_text для author_url из chitai_gorod_one_item - ChitaiGorodGetAuthorURL
#def test_get_text_author_url_chitai_gorod():
#    get_text_author_url = ChitaiGorodGetAuthorURL('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391').get_text()
#    print("text=",get_text_author_url)
#    assert get_text_author_url == "/author/martin-robert-s-586375"


# test_get_items_data из chitai_gorod_items_list
def test_get_items_chitai_gorod():
    chitai_gorod_list = ChitaiGorodItemsList("https://new.chitai-gorod.ru/catalog/books/nauka-i-tehnika-9170?sort=price&order=asc")
    items_data = chitai_gorod_list.get_items_data()
    #print (items_data) # выдает последнюю позицию текущей страницы, а не первую
    data_for_test = {'url': 'https://new.chitai-gorod.ru/product/vospalenie-pridatkov-adneksit-sovremennyy-vzglyad-na-lechenie-i-profilaktiku-2069025', 'title': 'Воспаление придатков - аднексит. Современный взгляд на лечение и профилактику', 'price': 31, 'price_sale': 31, 'author': 'Виктория Россошанская', 'author_url': '/author/rossoshanskaya-viktoriya-7518434', 'source_url': 'https://new.chitai-gorod.ru/catalog/books/nauka-i-tehnika-9170?sort=price&order=asc'}
    assert data_for_test in items_data
