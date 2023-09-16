#!/usr/local/bin/python
# coding: utf-8

import pytest
#from chitai_gorod_one_item import ChitaiGorodGetPrice, ChitaiGorodGetTitle, ChitaiGorodGetAuthor, ChitaiGorodGetAuthorURL
from chitai_gorod_items_list import ChitaiGorodItemsList, ChitaiGorodURLConfiguration, ChitaiGorodItemsFromFile
from web_parsing import PageParsing
from bs4 import BeautifulSoup


# test_get_items_data из chitai_gorod_items_list + author_url
def test_get_items_chitai_gorod():
    chitai_gorod_list = ChitaiGorodItemsList("https://www.chitai-gorod.ru/catalog/kanctovars/elektrotovary-3442")
    items_data = chitai_gorod_list.get_items_data()
    #print (items_data) # выдает последнюю позицию текущей страницы, а не первую
    data_for_test = {'url': 'https://new.chitai-gorod.ru/product/vospalenie-pridatkov-adneksit-sovremennyy-vzglyad-na-lechenie-i-profilaktiku-2069025', 'title': 'Воспаление придатков - аднексит. Современный взгляд на лечение и профилактику', 'price': 31, 'price_sale': 31, 'author': 'Виктория Россошанская', 'author_url': '/author/rossoshanskaya-viktoriya-7518434', 'source_url': 'https://new.chitai-gorod.ru/catalog/books/nauka-i-tehnika-9170?sort=price&order=asc'}
    assert data_for_test in items_data
    
@pytest.fixture()
def read_from_flie_responce_goods_3442():
    text = ''
    with open('sources/elektrotovary-3442','rb') as response:
        text = response.read() 
    return text
    
def test_get_items_chitai_gorod_from_file(read_from_flie_responce_goods_3442): # допилить тест, чтоб не зависел от цены
    chitai_gorod_list = ChitaiGorodItemsFromFile(read_from_flie_responce_goods_3442)
    items_data = chitai_gorod_list.get_items_data()
    #print (items_data) # выдает последнюю позицию текущей страницы, а не первую
    data_for_test = {'title': 'Батарейки "Duracell Basic", AA, 2 штуки\n  ', 'url': '/product/batareyki-duracell-basic-aa-2-shtuki-234618', 'price': 255, 'author': 'Батарейки', 'author_url': 'No data'}    
    assert data_for_test in items_data


# test ChitaiGorodURLConfiguration как работает инициализация через файл
def test_ChitaiGorodURLConfiguration_init_file():
    urls = ChitaiGorodURLConfiguration()
    data = urls.get_urls_list("url_data_for_test.txt")
    data_for_test = {'url': 'https://new.chitai-gorod.ru/product/nashi-deti-azbuka-semi-s-avtografom-2904994', 'title': 'Наши дети. Азбука семьи (с автографом)', 'price': 500, 'price_sale': 500, 'author': 'Диана Машкова', 'author_url': '/author/mashkova-diana-390923', 'source_url': 'https://new.chitai-gorod.ru/catalog/books/knigi-s-avtografom-18265?sort=price&order=asc&page=1'}
    assert data_for_test in data
    
    
