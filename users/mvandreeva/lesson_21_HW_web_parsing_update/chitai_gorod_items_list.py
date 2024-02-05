#!/usr/local/bin/python
# coding: utf-8

from web_parsing import OnePageParsing
from chitai_gorod_one_item import ChitaiGorodGetAuthorURL


class ChitaiGorodItemsList:
    """ Класс обработки страницы со списком элементов """
    
    def __init__(self, url: str): 
        self.__url = url
        self.__b_soup = OnePageParsing(url).read_page()
        
    def get_items_data(self) ->list :
        """ Получает данные по позициям, формирует список словарей """
        dict_list = []
        items_list = self.__b_soup.findAll("article", class_ = "product-card product-card product")
        for item in items_list:
            title_data = item.findAll("div", class_ = "product-title__head")
            title_bad = title_data[0].text
            title_bad = title_bad.replace("\n    ", "")
            title = title_bad.replace("\n  ", "")
            
            
            url_data = item.findAll("a", class_ = "product-card__picture product-card__row")
            url = url_data[0]["href"]
            
            price_data = item.findAll("div", class_ = "product-price__value")
            price_bad = price_data[0].text
            price_bad = price_bad.replace("\n    ", "")
            price_bad = price_bad.replace(" ₽\n  ", "")
            price = int(price_bad)
            
            author_data = item.findAll("div", class_ = "product-title__author")
            author_bad = author_data[0].text
            author_bad = author_bad.replace("\n    ", "")
            author = author_bad.replace("\n  ", "")
            
            item_url = "https://new.chitai-gorod.ru" + url
            
            #author_url = ChitaiGorodGetAuthorURL(item_url).get_text() # не работает, почему?
            #author_url_page = OnePageParsing(item_url).read_page()
            #author_url_data = author_url_page.findAll("a", class_ = "product-detail-title__author")
            #author_url = author_url_data[0]["href"]
            
            #img_data = item.findAll("picture", class_ = "product-picture")
            #img_data = item.findAll("img", class_ = "product-picture__img _loaded lazyloaded")
            #img_url = img_data[0]["src"]
            
            
            
            
            dict_list.append({
                    "url": url,
                    "title": title,
                    "price": price,
                    #"price_sale": price_sale, # не стала добавлять, т.к. по классу "product-price__value" выдает актуальную цену
                    "url": item_url,
                    "author": author,
                    #"author_url": author_url,
                    #"image_url": img_url,
                    "source_url": self.__url,
                })
        
        return dict_list