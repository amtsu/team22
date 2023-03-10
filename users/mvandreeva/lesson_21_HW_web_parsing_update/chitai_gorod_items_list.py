#!/usr/local/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
from web_parsing import PageParsing
from chitai_gorod_one_item import ChitaiGorodGetAuthorURL
import json


class ChitaiGorodItemsList:
    """ Класс обработки страницы со списком элементов """
    
    def __init__(self, url: str): 
        self.__url = url
        page = PageParsing(self.__url)
        page_text = page.get_page()
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")
        
    def get_items_data(self) ->list :
        """ Получает данные по позициям, формирует список словарей """
        dict_list = []
        items_list = self.__b_soup.findAll("article", class_ = "product-card product-card product")
        #print(items_list)
        for item in items_list:
            title_data = item.findAll("div", class_ = "product-title__head")
            if not title_data:
                title = None
            else:
                title_bad = title_data[0].text
                title_bad = title_bad.replace("\n    ", "")
                title = title_bad.replace("\n  ", "")
            
            
            url_data = item.findAll("a", class_ = "product-card__picture product-card__row")
            if not url_data:
                url = None
            else:
                url = url_data[0]["href"]
            
            price_data = item.findAll("div", class_ = "product-price__value")
            if not price_data:
                price = None
            else:
                price_bad = price_data[0].text
                price_bad = price_bad.replace("\n    ", "")
                price_bad = price_bad.replace(" ₽\n  ", "")
                price = int(price_bad)
            
            author_data = item.findAll("div", class_ = "product-title__author")
            if not author_data:
                author = None
            else:
                author_bad = author_data[0].text
                author_bad = author_bad.replace("\n    ", "")
                author = author_bad.replace("\n  ", "")
            
            item_url = "https://new.chitai-gorod.ru" + url
            #print(item_url)
            
            #author_url = ChitaiGorodGetAuthorURL(item_url).get_text() # не работает, почему?
            author_url_page = PageParsing(item_url)
            try:
                author_url_page_text = author_url_page.get_page() 
                #print(author_url_page)
                author_url_soup = BeautifulSoup(author_url_page_text, features="html.parser")
                author_url_data = author_url_soup.findAll("a", class_ = "product-detail-title__author")
                if not author_url_data:
                    #print(f"Not find author in {item_url}")
                    author_url = None
                    continue
                else:
                    author_url = author_url_data[0]["href"]
            except:
                print("Error in getting author_url, page is unavailable")
                continue
            
            #img_data = item.findAll("picture", class_ = "product-picture")
            #img_data = item.findAll("img", class_ = "product-picture__img _loaded lazyloaded")
            #img_url = img_data[0]["src"]
            
            
            
            
            dict_list.append({
                    "url": url,
                    "title": title,
                    "price": price,
                    "price_sale": price, # по классу "product-price__value" выдает актуальную цену, независимо от скидки
                    "url": item_url,
                    "author": author,
                    "author_url": author_url,
                    #"image_url": img_url,
                    "source_url": self.__url,
                })
        
        return dict_list
    
class ChitaiGorodURLConfiguration:
    """
    Обрабатывает данные по url сайта chitai-gorod и выдает ссылки на url-адреса для последующей обработки, отправки в api 
    """
     
    def __load_default_urls(self):
        "Подгружает базовый список URL-ов"
        self.__urls_list = {
        "https://www.chitai-gorod.ru/catalog/souvenirs/pozdravitelnaya-atributika-10635":2,
#        }    
#        """
        "https://www.chitai-gorod.ru/catalog/books/hudozhestvennaya-literatura-9657": 2021,
        "https://www.chitai-gorod.ru/catalog/books/knigi-dlya-detey-9072": 1246,
        "https://www.chitai-gorod.ru/catalog/books/obrazovanie-9405": 1222,
        "https://www.chitai-gorod.ru/catalog/books/nauka-i-tehnika-9170": 1006,
        "https://www.chitai-gorod.ru/catalog/books/obshchestvo-9304": 639,
        "https://www.chitai-gorod.ru/catalog/books/delovaya-literatura-8979": 278,
        "https://www.chitai-gorod.ru/catalog/books/krasota-zdorove-sport-9116": 204,
        "https://www.chitai-gorod.ru/catalog/books/uvlecheniya-9564": 377,
        "https://www.chitai-gorod.ru/catalog/books/psihologiya-9530": 311,
        "https://www.chitai-gorod.ru/catalog/books/ezoterika-9705": 247,
        "https://www.chitai-gorod.ru/catalog/books/filosofiya-i-religiya-9645": 306,
        "https://www.chitai-gorod.ru/catalog/books/iskusstvo-9035": 303,
        "https://www.chitai-gorod.ru/catalog/books/podarochnye-izdaniya-9469": 85,
        "https://www.chitai-gorod.ru/catalog/books/knigi-na-inostrannyh-yazykah-9154": 318,
        "https://www.chitai-gorod.ru/catalog/books/knigi-s-avtografom-18265":13,
            
        "https://www.chitai-gorod.ru/catalog/kanctovars/bumazhnye-izdeliya-2856":377,
        "https://www.chitai-gorod.ru/catalog/kanctovars/galantereya-3438":60,
        "https://www.chitai-gorod.ru/catalog/kanctovars/prochie-kanctovary-3439": 4,
        "https://www.chitai-gorod.ru/catalog/kanctovars/upakovka-3440": 72,
        "https://www.chitai-gorod.ru/catalog/kanctovars/tovary-dlya-hudozhnikov-3441":158,
        "https://www.chitai-gorod.ru/catalog/kanctovars/elektrotovary-3442":1,
        "https://www.chitai-gorod.ru/catalog/kanctovars/penaly-10711":1,
        "https://www.chitai-gorod.ru/catalog/kanctovars/ofisnye-prinadlezhnosti-2921":78,
        "https://www.chitai-gorod.ru/catalog/kanctovars/pismennye-prinadlezhnosti-2963":92,
        "https://www.chitai-gorod.ru/catalog/kanctovars/chertezhnye-prinadlezhnosti-3005":24,
        "https://www.chitai-gorod.ru/catalog/kanctovars/shkolnye-tovary-3018":113,
        "https://www.chitai-gorod.ru/catalog/toys/igry-10731":211,
        "https://www.chitai-gorod.ru/catalog/toys/igrushki-10732":39,
        "https://www.chitai-gorod.ru/catalog/hobbies/nabory-dlya-detskogo-tvorchestva-18198":130,
        "https://www.chitai-gorod.ru/catalog/hobbies/nabory-dlya-vzroslogo-tvorchestva-18232":65,
        "https://www.chitai-gorod.ru/catalog/hobbies/zagotovki-18217":16,
        "https://www.chitai-gorod.ru/catalog/hobbies/instrumenty-i-prisposobleniya-18218":13,
        "https://www.chitai-gorod.ru/catalog/hobbies/rashodnye-materialy-18219":48,
        "https://www.chitai-gorod.ru/catalog/hobbies/him-sostavy-kraski-geli-laki-klei-i-pr-18236":13,
        "https://www.chitai-gorod.ru/catalog/hobbies/dekorirovanie-18242":43,
        "https://www.chitai-gorod.ru/catalog/hobbies/bizhuteriya-18206":5,
        "https://www.chitai-gorod.ru/catalog/souvenirs/suveniry-k-prazdniku-10234":21,
        "https://www.chitai-gorod.ru/catalog/souvenirs/dom-byt-dekor-10289":32,
        "https://www.chitai-gorod.ru/catalog/souvenirs/igry-i-igrushki-10348":44,
        "https://www.chitai-gorod.ru/catalog/souvenirs/lichnye-veshchi-10385":121,
        "https://www.chitai-gorod.ru/catalog/souvenirs/melochi-suvenirnye-10439":32,
        "https://www.chitai-gorod.ru/catalog/souvenirs/predskazaniya-pozhelaniya-astrologiya-ezoterika-10512":1,
        "https://www.chitai-gorod.ru/catalog/souvenirs/suvenirnye-kancelyarskie-i-ofisnye-prinadlezhnosti-10527":24,
        "https://www.chitai-gorod.ru/catalog/souvenirs/pozdravitelnaya-atributika-10635":2,
        "https://www.chitai-gorod.ru/catalog/souvenirs/otkrytki-i-postery-10691":4,
        "https://www.chitai-gorod.ru/catalog/kalendari":95,
        "https://www.chitai-gorod.ru/catalog/rasprodazha":23,
        }
#        """
        return self.__urls_list
    
    def get_urls_list(self, *args):
        """
        Формирует список URLs и скачивает данные с соответствующих страниц
        """  
        if not args:
            urls_dict = self.__load_default_urls()
            for url, pages in urls_dict.items():
                url = url + "?sort=price&order=asc"
                for i in range(1, pages):
                    url_p = url + "&page=" + str(i) 
                    print(url_p)
                    try:
                        page_parsing = ChitaiGorodItemsList(url_p)                
                        dict_list = page_parsing.get_items_data()
                        self.__list_dict.append(dict_list)
                    except:
                        continue
         
        if args:
            for arg in args:
                if isinstance(arg, dict):
                    for url in arg:
                        url = url + "?sort=price&order=asc" 
                        for i in range(1, arg[url]):
                            url_p = url + "&page=" + str(i) 
                            print(url_p)
                            #page = PageParsing(url_p):
                            #page_text = page.get_page()
                            #page_url = page.get_url()
                            page_parsing = ChitaiGorodItemsList(url_p)
                            dict_list = page_parsing.get_items_data()
                            self.__list_dict.append(dict_list)
                if isinstance(arg, list):
                    for url in arg:
                        url = url + "?sort=price&order=asc" 
                        for i in range(1, 2022):
                            url_p = url + "&page=" + str(i)
                            print(url_p)
                            try:
                                page_parsing = ChitaiGorodItemsList(url_p)
                                dict_list = page_parsing.get_items_data()
                                self.__list_dict.append(dict_list)
                            except:
                                break
                if isinstance(arg, str): # не работает, перебирает посимвольно
                    if not arg == "": 
                        with open(arg, "r") as urls_data:
                            self.__url_list = urls_data.read()
                            self.__url_list = json.loads(self.__url_list)
                            #print(type(self.__url_list))
                            #print(self.__url_list)
                            #if isinstance(self.__url_list, list):
                            for url in self.__url_list:
                                url = url + "?sort=price&order=asc"
                                for i in range(1, 2022):
                                    url_p = url + "&page=" + str(i)
                                    print(url_p)
                                    try:
                                        page_parsing = ChitaiGorodItemsList(url_p)
                                        dict_list = page_parsing.get_items_data()
                                        self.__list_dict.append(dict_list)
                                    except:
                                        break
                        #else:
                        #    self.__url_list = [self.__url_list]
                        #    for url in self.__url_list:
                        #        url = url + "?sort=price&order=asc"
                        #        for i in range(1, 2022):
                        #            url_p = url + "&page=" + str(i)
                        #            page_parsing = ChitaiGorodItemsList(url_p)
                        #            dict_list = page_parsing.get_items_data()
                        #            self.__list_dict.append(dict_list)
                else:
                    print("Incorrect input data")
        print(self.__list_dict)
        return self.__list_dict
    
    def __init__(self):
        self.__urls_list = []
        self.__list_dict = []
    
    
    def __str__(self):
        return str(self.__url_list)
    
    