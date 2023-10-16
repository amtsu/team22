#!/usr/local/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
from web_parsing import PageParsing
#from chitai_gorod_one_item import ChitaiGorodGetAuthorURL
import json

# лезет на сайт
# 
class ChitaiGorodItemsList:
    """ Класс обработки страницы со списком элементов """
    
    def __init__(self, url: str): 
        self.__url = url
        page = PageParsing(self.__url)
        page_text = page.get_page()
        #print(page_text)
        self._b_soup = BeautifulSoup(page_text, features="html.parser")

        
    def get_items_data(self) ->list :
        """ Получает данные по позициям, формирует список словарей """
        dict_list = []
        
        # print("____________________________")
        # print(self._b_soup)
        items_list = self._b_soup.findAll("article", class_ = "product-card product-card product")
        if not items_list == []: # ввела проверку, чтоб парсер не пытался скачать пустые траницы (чтоб жестко не привязываться к числу страниц раздела) 
            for item in items_list:
                item_dict = {}
                title_data = item.findAll("div", class_ = "product-title__head")
                #print(title_data)
                if not title_data or title_data == []:
                    item_dict["title"] = "No data"
                else:
                    title_bad = title_data[0].__text
                    title_bad = title_bad.replace("\n    ", "")
                    title = title_bad.replace("\n  ", "")
                    title = title_bad.replace("\xa0", " ")
                    item_dict["title"] = title
                    # print("_______________")
                    # print(title)
                    # print(type(title))
                    # print(item_dict["title"])
                    # print(item_dict)


                url_data = item.findAll("a", class_ = "product-card__picture product-card__row")
                #print(url_data)
                if not url_data or url_data == []:
                    item_dict["url"] = "No data"
                else:
                    url = url_data[0]["href"]
                    item_dict["url"] = url

                price_data = item.findAll("div", class_ = "product-price__value")
                if not price_data or price_data == []:
                   # price = "No data"
                    item_dict["price"] = "No data"
                else:
                    price_bad = price_data[0].__text
                    price_bad = price_bad.replace("\n    ", "")
                    price_bad = price_bad.replace(" ₽\n  ", "")
                    price_bad = price_bad.replace("\xa0", "") 
                    price = int(price_bad)
                    item_dict["price"] = price

                author_data = item.findAll("div", class_ = "product-title__author")
                #print(author_data)
                if not author_data or author_data == []:
                    #author = "No data"
                    item_dict["author"] = "No data" 
                else:
                    author_bad = author_data[0].__text
                    author_bad = author_bad.replace("\n    ", "")
                    author = author_bad.replace("\n  ", "")
                    item_dict["author"] = author
                # print("authorauthorauthorauthorauthorauthorauthorauthor")
                # print(author)
                # print(item_dict["author"])
                # print(item_dict)

                if not url == "No data":
                    item_url = "https://new.chitai-gorod.ru" + url
                    #print(item_url)

                    author_url_page = PageParsing(item_url)
                    try:
                        author_url_page_text = author_url_page.get_page() 
                    except:
                        print("Error in getting author_url, web-__page is not available")
                        # continue
                    #print(author_url_page)
                    if author_url_page_text: # ?? будет ли видна здесь переменная author_url_page_text из блока try / except? 
                        # - вроде работает, но иногда возникает ошибка, решается повторным выполнением кода и в следующий раз все срабатывает без ошибок....
                        author_url_soup = BeautifulSoup(author_url_page_text, features="html.parser")
                        author_url_data = author_url_soup.findAll("a", class_ = "product-detail-title__author")
                        if not author_url_data:
                        # if author_url_data == []:
                            #print(f"Not find author in {item_url}")
                            item_dict["author_url"] = "No data"
                            # continue
                        else:
                            author_url = author_url_data[0]["href"]
                            item_dict["author_url"] = author_url
                    else:    
                        item_dict["author_url"] = "No data"
                    
                else:
                    item_dict["author_url"] = "No data"
                # print(item_dict["author_url"])
                # print(item_dict)

                #img_data = item.findAll("picture", class_ = "product-picture")
                #img_data = item.findAll("img", class_ = "product-picture__img _loaded lazyloaded")
                #img_url = img_data[0]["src"]
                # print("::::::::")
                # print(item_dict)         
                dict_list.append(item_dict) # ??что лучше, создавать словарь по каждой позиции и сохранять в список словарей или вариант ниже?
                # dict_list.append({ 
                #         "url": url,
                #         "title": title,
                #         "price": price,
                #         "price_sale": price, # по классу "product-price__value" выдает актуальную цену, независимо от скидки
                #         "url": item_url,
                #         "author": author,
                #         "author_url": author_url,
                #         #"image_url": img_url,
                #         "source_url": self.__url,
                #     })
        else: 
            return dict_list
        # print(dict_list)
        return dict_list
    
class ChitaiGorodItemsFromFile(ChitaiGorodItemsList):
    """ Класс обработки страницы со списком элементов """
    
    def __init__(self, page_text): 
        #print(page_text)
        self.__url = None
        self._b_soup = BeautifulSoup(page_text, features="html.parser")
    
class ChitaiGorodURLConfiguration:
    """
    Обрабатывает данные по url сайта chitai-gorod и выдает ссылки на url-адреса для последующей обработки, отправки в api 
    """
     
    def __load_default_urls(self):
        "Подгружает базовый список URL-ов"
        self.__urls_list = {
        # "https://www.chitai-gorod.ru/catalog/souvenirs/pozdravitelnaya-atributika-10635":2,
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
    
    #def get_urls_list(self, *args): # сделать несколько функций
        """
        Лучше не закреплять жестко количество страниц - оно может меняться. попробовать if 
        """
    def get_urls(self):
        """
        Формирует список URLs из аттрибута класса self.__urls_list и скачивает данные с соответствующих страниц
        """  
        urls_dict = self.__load_default_urls()
        for url, pages in urls_dict.items():
            url = url + "?sort=price&order=asc"
            #for i in range(1, pages):
            for i in range(1, 2):
                url_p = url + "&__page=" + str(i)
                #print(url_p)
                try: 
                    page_parsing = ChitaiGorodItemsList(url_p)                
                    dict_list = page_parsing.get_items_data()
                    self.__list_dict.append(dict_list)
                except:
                    continue
        #print(self.__list_dict)
        return self.__list_dict
    
    def get_urls_dict(self, urls_dict):
        """
        Формирует список URLs из переданного в метод словаря (url: кол-во страниц) и скачивает данные с соответствующих страниц
        """
        for url in urls_dict:
            url = url + "?sort=price&order=asc" 
            for i in range(1, urls_dict[url]):
                url_p = url + "&__page=" + str(i)
                #print(url_p)
                try: 
                    page_parsing = ChitaiGorodItemsList(url_p)                
                    dict_list = page_parsing.get_items_data()
                    self.__list_dict.append(dict_list)
                except:
                    continue
        #print(self.__list_dict)
        return self.__list_dict

    def get_urls_from_file(self, file_name: str): # возможно, вернусь к спискам позже, когда придумаю как быть с количеством страниц
        """
        Загружает данные (словарь url:кол-во_страниц) из файла.
        Формирует список URLs и скачивает данные с соответствующих страниц.
        """
        with open(file_name, "r") as urls_data:
            self.__url_list = urls_data.read()
            self.__url_list = json.loads(self.__url_list)
            #print(type(self.__url_list))
            #print(self.__url_list)
            if isinstance(self.__url_list, dict):
                for url in self.__url_list:
                    url = url + "?sort=price&order=asc"
                    for i in range(1, self.__url_list[url]):
                        url_p = url + "&__page=" + str(i)
                        print(url_p)
                        try:
                            page_parsing = ChitaiGorodItemsList(url_p)
                            dict_list = page_parsing.get_items_data()
                            self.__list_dict.append(dict_list)
                        except:
                            continue
            else:
                print(f"Incorrect data type in file {file_name}. Should be dict type: url:pages. type(url) = str, type(__page) = int.")
        print(self.__list_dict)
        return self.__list_dict
    
    # def get_urls_list(self, urls_list): # возможно, вернусь к спискам позже, когда придумаю как быть с количеством страниц
    #     for url in urls_list:
    #         url = url + "?sort=price&order=asc" 
    #         #for i in range(1, 2022):
    #         for i in range(1, 2):
    #             url_p = url + "&__page=" + str(i)
    #             #print(url_p)
    #             try: # не стоит использовать try для остановки перебора страниц
    #                 page_parsing = ChitaiGorodItemsList(url_p)
    #                 dict_list = page_parsing.get_items_data()
    #                 self.__list_dict.append(dict_list)
    #             except:
    #                 break
                    
    # def get_urls_from_file(self, file_name): # возможно, вернусь к спискам позже, когда придумаю как быть с количеством страниц
    #             if isinstance(arg, str): 
    #                 if not arg == "": 
    #                     with open(arg, "r") as urls_data:
    #                         self.__url_list = urls_data.read()
    #                         self.__url_list = json.loads(self.__url_list)
    #                         #print(type(self.__url_list))
    #                         #print(self.__url_list)
    #                         #if isinstance(self.__url_list, list):
    #                         for url in self.__url_list:
    #                             url = url + "?sort=price&order=asc"
    #                             for i in range(1, 2022):
    #                                 url_p = url + "&__page=" + str(i)
    #                                 print(url_p)
    #                                 try:
    #                                     page_parsing = ChitaiGorodItemsList(url_p)
    #                                     dict_list = page_parsing.get_items_data()
    #                                     self.__list_dict.append(dict_list)
    #                                 except:
    #                                     break
    #             else:
    #                 print("Incorrect input data")
    #     print(self.__list_dict)
    #     return self.__list_dict
    
    
    
    def __create_file_name(self):
        """
        Формирует имя файла для сохранния полученных данных
        """
        return "chitai_gorod.json"

    def save_to_file(self):
        """
        Сохраняет полученные данные в локальный фаил
        """
        json_string = json.dumps(self.__list_dict)
        file_name = self.__create_file_name()
        with open(file_name, "w") as outfile:
            outfile.write(json_string) # у Артёма по-другому, почему?
    
    def __init__(self):
        self.__urls_list = []
        self.__list_dict = []
    
    
    def __str__(self):
        return str(self.__url_list)
    
    