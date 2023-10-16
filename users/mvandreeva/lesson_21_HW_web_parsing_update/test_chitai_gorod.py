#!/usr/local/bin/python
# coding: utf-8

import pytest
from chitai_gorod_one_item import ChitaiGorodGetPrice, ChitaiGorodGetTitle, ChitaiGorodGetAuthor, ChitaiGorodGetAuthorURL
from chitai_gorod_items_list import ChitaiGorodItemsList, ChitaiGorodURLConfiguration
from web_parsing import PageParsing
from bs4 import BeautifulSoup


# test_get_text_price из chitai_gorod - ChitaiGorodGetPrice
#def test_get_text_price_chitai_gorod():
#    __page = PageParsing('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391')
#    page_text = __page.read_page()
#    get_text_price = ChitaiGorodGetPrice(page_text).get_text()
#    #print("__text=",get_text_price)
#    assert get_text_price == """\n      1\xa0100 ₽\n    """

@pytest.fixture()
def page_parsing_2640391():
    page = PageParsing('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391')
    page_text = page_parsing_2640391.get_page()
    page_url = page_parsing_2640391.get_url()
    return page_text, page_url

# test_clean_data для price из chitai_gorod - ChitaiGorodGetPrice
def test_clean_data_price_chitai_gorod():
#    __page = PageParsing('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391')
#    page_text = page_parsing_2640391.get_page()
#    page_url = page_parsing_2640391.get_url()
    page_parsing = page_parsing_2640391()
    chitai_gorod = ChitaiGorodGetPrice(page_parsing[0], page_parsing[1])
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
#    __page = PageParsing('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391')
    page_text = page_parsing_2640391.get_page()
    page_url = page_parsing_2640391.get_url()
    chitai_gorod = ChitaiGorodGetAuthor(page_text, page_url)
    author = chitai_gorod.clean_data() 
    assert author == "Роберт С. Мартин"
    #print(type(author), author)
    

# test_get_text для author_url из chitai_gorod_one_item - ChitaiGorodGetAuthorURL
#def test_get_text_author_url_chitai_gorod():
#    get_text_author_url = ChitaiGorodGetAuthorURL('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391').get_text()
#    print("__text=",get_text_author_url)
#    assert get_text_author_url == "/author/martin-robert-s-586375"


# test_get_items_data из chitai_gorod_items_list + author_url
def test_get_items_chitai_gorod():
    chitai_gorod_list = ChitaiGorodItemsList("https://www.chitai-gorod.ru/catalog/kanctovars/elektrotovary-3442")
    items_data = chitai_gorod_list.get_items_data()
    #print (items_data) # выдает последнюю позицию текущей страницы, а не первую
    data_for_test = {'url': 'https://new.chitai-gorod.ru/product/vospalenie-pridatkov-adneksit-sovremennyy-vzglyad-na-lechenie-i-profilaktiku-2069025', 'title': 'Воспаление придатков - аднексит. Современный взгляд на лечение и профилактику', 'price': 31, 'price_sale': 31, 'author': 'Виктория Россошанская', 'author_url': '/author/rossoshanskaya-viktoriya-7518434', 'source_url': 'https://new.chitai-gorod.ru/catalog/books/nauka-i-tehnika-9170?sort=price&order=asc'}
    assert data_for_test in items_data

# test ChitaiGorodURLConfiguration как работает инициализация через файл
def test_ChitaiGorodURLConfiguration_init_file():
    urls = ChitaiGorodURLConfiguration()
    data = urls.get_urls_list("url_data_for_test.txt")
    data_for_test = {'url': 'https://new.chitai-gorod.ru/product/nashi-deti-azbuka-semi-s-avtografom-2904994', 'title': 'Наши дети. Азбука семьи (с автографом)', 'price': 500, 'price_sale': 500, 'author': 'Диана Машкова', 'author_url': '/author/mashkova-diana-390923', 'source_url': 'https://new.chitai-gorod.ru/catalog/books/knigi-s-avtografom-18265?sort=price&order=asc&page=1'}
    assert data_for_test in data
    
    
