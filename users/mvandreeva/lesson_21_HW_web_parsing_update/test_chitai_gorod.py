#!/usr/local/bin/python
# coding: utf-8

import pytest
from chitai_gorod_one_item import ChitaiGorodGetPrice, ChitaiGorodGetTitle, ChitaiGorodGetAuthor, ChitaiGorodGetAuthorURL
from chitai_gorod_items_list import ChitaiGorodItemsList


# test_get_text_price из chitai_gorod - ChitaiGorodGetPrice
#def test_get_text_price_chitai_gorod():
#    page_text = OnePageParsing('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391').read_page()
#    get_text_price = ChitaiGorodGetPrice(page_text).get_text()
#    #print("text=",get_text_price)
#    if get_text_price == """\n      1\xa0100 ₽\n    """:
#        print ("passed")
#    else:
#        assert False

# test_clean_data для price из chitai_gorod - ChitaiGorodGetPrice
def test_clean_data_price_chitai_gorod():
    page_text = OnePageParsing('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391').read_page()
    price = ChitaiGorodGetPrice(page_text).clean_data()
    if price == 1100:
        print ("passed")
    else:
        assert False    
    #print(type(price), price)

    
# test_get_text для author из chitai_gorod_one_item - ChitaiGorodGetAuthor
#def test_get_text_author_chitai_gorod():
#    get_text_author = ChitaiGorodGetAuthor('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391').get_text()
#    if get_text_author == """\n          Роберт С. Мартин\n        """:
#        print ("passed")
#    else:
#        assert False
        
# test_clean_data для author из chitai_gorod_one_item - ChitaiGorodGetAuthor
def test_clean_data_author_chitai_gorod():
    author = ChitaiGorodGetAuthor('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391').clean_data()
    if author == "Роберт С. Мартин":
        print ("passed")
    else:
        assert False    
    #print(type(author), author)
    

# test_get_text для author_url из chitai_gorod_one_item - ChitaiGorodGetAuthorURL
#def test_get_text_author_url_chitai_gorod():
#    get_text_author_url = ChitaiGorodGetAuthorURL('https://new.chitai-gorod.ru/product/chistaya-arhitektura-iskusstvo-razrabotki-programmnogo-obespecheniya-2640391').get_text()
#    print("text=",get_text_author_url)
#    if get_text_author_url == "/author/martin-robert-s-586375":
#        print ("passed")
#    else:
#        assert False


# test_get_items_data из chitai_gorod_items_list
def test_get_items_data_chitai_gorod_2(): # не сработает, пока не разберусь с author_url
    items_data = ChitaiGorodItemsList("https://new.chitai-gorod.ru/catalog/books/nauka-i-tehnika-9170?sort=price&order=asc").get_items_data()
    #print (items_data) # выдает последнюю позицию текущей страницы, а не первую
    data_for_test = {'url': 'https://new.chitai-gorod.ru/product/zadachi-seminara-2003-2004-2828128', 'title': 'Задачи семинара. 2003 - 2004', 'price': 35, 'author': 'Владимир Арнольд', 'source_url': 'https://new.chitai-gorod.ru/catalog/books/nauka-i-tehnika-9170?sort=price&order=asc'}
    if data_for_test in items_data:
        print ("passed")
    else:
        assert False
        
