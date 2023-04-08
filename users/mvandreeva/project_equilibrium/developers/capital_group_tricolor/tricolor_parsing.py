#!/usr/local/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib
import urllib.request

from page_parsing import PagePerser

"""
Парсер для сайта застройщика 'CapitalGroup', проект 'Триколор'
"""
    
class TricolorParser:
    """
    Собирает данные с сайта https://cg-tricolor.ru/catalog/flats очищает их, сохряняет
    """
    def _get_bulding(self, item: object) -> int:
        flat_data = item.findAll("td")
        if flat_data:
            building_str = flat_data[0].text
            building = int(building_str)
        else:
            building = None
        return building
    
    def get_dict_list(self) -> list:
        # if not self.__items_list == []: # нужна ли проверка?
        
        for item in self.__items_list:
            item_dict = {}
            item_dict["quantity"] = 1
            item_dict["bulding"] = self._get_bulding(item)
            item_dict["title"] = self._get_title_2(item) + str(item_dict["bulding"])
            if  item_dict["title"]:
                rooms = item_dict["title"][0]
                item_dict["rooms"] = int(rooms)
            else:
                item_dict["rooms"] = None
            item_dict["floor"] = self._get_floor(item)
            item_dict["area"] = self._get_square(item)
            item_dict["price"] = self._get_price(item)
            item_dict["url"] = self._get_item_url(item)
            item_dict["project"] = "Триколор"
            item_dict["address"] = "Проспект Мира, 188Б"
            item_dict["city"] = "Москва"
            item_dict["brand"] = "Capital Group"
            item_dict["brand_url"] = "https://capitalgroup.ru/"
            item_dict["category"] = "Новостройки"
            item_dict["source_url"] = self.__url
            item_dict["price_sale"] = item_dict["price"]
            # item_dict["datetime_create"] = "1970-01-01T00:00:00.00Z"
            item_dict["plan"] = self._get_plan(item)
            # item_dict["description"] = json.dumps(e["specialmortgageoffer_set"])
            item_dict["apartment_completion_quarter"] = 4   # нашла на циане
            item_dict["apartment_completion_year"] = 2015   # нашла на циане
            item_dict["apartment_ceilingheight"] = 3 # здесь написано в тексте https://cg-tricolor.ru/catalog
            
            if item_dict["bulding"] == 1:
                item_dict["apartment_floors_total"] = 58 # нашла на циане
            elif item_dict["bulding"] == 2:
                item_dict["apartment_floors_total"] = 10
            elif item_dict["bulding"] == 3:
                item_dict["apartment_floors_total"] = 58
            elif item_dict["bulding"] == 4:
                item_dict["apartment_floors_total"] = 38
                
            if item_dict["price"] and item_dict["area"]:
                item_dict["apartment_ppm"] = item_dict["price"]/item_dict["area"]
            # item_dict["apartment_location"] = e["location"]
            # item_dict["apartment_location_lat"] = e["location"].split(',')[0][:9]
            # item_dict["apartment_location_lon"] = e["location"].split(',')[1][:9]
            
            self.__dict_list.append(item_dict)
        return self.__dict_list    
            
    def _get_floor(self, item: object) -> int:
        flat_data = item.findAll("td")
        if flat_data:
            floor_str = flat_data[1].text
            floor = int(floor_str)
        else:
            floor = None
        return floor
    
    def _get_item_url(self, item: object) -> str:
        flat_data = item.findAll("a", class_ = "results__link")
        if flat_data:
            link = flat_data[0]["href"]
            item_url = "https://cg-tricolor.ru" + link
        else:
            item_url = None
        return item_url
    
    # def _get_one_item(self, item: object): # рашила пока обойтись без него
    #     item_url = self._get_item_url(item)
    #     page = PagePerser(item_url)
    #     b_soup = page.use_b_soup()
    #     return 
    
    def _get_plan(self, item: object) -> str:
        plan_data = item.findAll("img")
        if plan_data:
            plan = plan_data[0]["src"]
        else:
            plan = None
        return plan
    
    def _get_price(self, item: object) -> int:
        flat_data = item.findAll("td", {"sorttable_customkey" : "37775845"})
        if flat_data:
            price_data = flat_data[0].text
            price_bad =  price_data.replace("\n                        ","")
            price_bad =  price_bad.replace("\n\n\n\n\n3 – комнатная квартира 139,00м2 3 этаж №7 в корпусе \n\n\n", "")
            price_bad =  price_bad.replace("руб.", "")
            price_bad =  price_bad.replace(" ","")
            price = int(price_bad)
        else:
            price = None
        return price
    
    # def _det_rooms_data(self, item: object) -> int: # добавлю в _get_title(), т.к. есть только в title 
        
            
    def _get_square(self, item: object) -> int:
        flat_data = item.findAll("td")
        if flat_data:
            square_str = flat_data[2].text
            square = int(square_str)
        else:
            square = None
        return square
            
    def _get_title(self, item: object) -> str:
        """
        Метод получает наименование квартиры, переходя на сайт с отдельной квартирой
        """
        item_url = self._get_item_url(item)
        page = PagePerser(item_url)
        b_soup = page.use_b_soup()
        title_data = b_soup.findAll("h1")
        if title_data:
            title = title_data[0].text
        else:
            title = None
        return title
    
    def _get_title_2(self, item: object) -> str:
        """
        Метод получает наименование квартиры из всплывающего окна страницы со списком квартир
        """
        # link_data = item.findAll("a", class_ = "results__link")
        # print(link_data)
        
        title_data = item.findAll("div")
        # print(title_data)
        
        if title_data:
            title = title_data[2].text
            # print(title)
        else:
            title = None
        return title
            
    def __init__(self, url: str):
        self.__url = url
        self.__page = PagePerser(self.__url)
        self.__b_soup = self.__page.use_b_soup()
        try:
            self.__items_list = self.__b_soup.findAll("tr", class_ = "results__tr")
        except:
            print("Error in getting items_list", self.__url)
        self.__dict_list = []
        self.__dict = {}
    
#     def send_in_api(self):
#         configuration = openapi_client.Configuration(host="http://absrent.ru:8000")

#         with openapi_client.ApiClient(configuration) as api_client:
#             api_instance = history_api.HistoryApi(api_client)
#             for e in self.__list_dict:
#                 # print(e)
#                 history = History(
#                     pk=1,
#                     title=e["title"],
#                     quantity=1,
#                     price=str(e["price"]),
#                     price_sale=str(e["price_sale"]),
#                     datetime_create="1970-01-01T00:00:00.00Z",
#                     # score="-807",
#                     # count_comments=1,
#                     # count_likes=1,
#                     # count_stars_all=1,
#                     # count_stars_1=1,
#                     # count_stars_2=1,
#                     # count_stars_3=1,
#                     # count_stars_4=1,
#                     # count_stars_5=1,
#                     # count_how_much_buy=1,
#                     # count_questions=1,
#                     # count_photo=1,
#                     category=e["category"],
#                     # category_url="category_url_example",
#                     brand=e["brand"],
#                     brand_url=e["brand_url"],
#                     # day_to_delivery=1,
#                     # sku="sku_example",
#                     url=e["url"],
#                     # canonical_url="canonical_url_example",
#                     img_url=e["image_url"],
#                     description=e["description"],
#                     # params="params_example",
#                     # seller="seller_example",
#                     # seller_url="seller_url_example",
#                     source_url=e["source_url"],
#                     apartment_area=e["apartment_area"],
#                     apartment_completion_quarter=e["apartment_completion_quarter"],
#                     apartment_completion_year=e["apartment_completion_year"],
#                     apartment_floor=e["apartment_floor"],
#                     apartment_floors_total=e["apartment_floors_total"],
#                     apartment_ceilingheight=e["apartment_ceilingheight"],
#                     apartment_room=e["apartment_room"],
#                     apartment_ppm=e["apartment_ppm"],
#                     apartment_address=e["apartment_address"],
#                     apartment_location=e["apartment_location"],
#                     apartment_location_lat=e["apartment_location_lat"],
#                     apartment_location_lon=e["apartment_location_lon"],
                    
#                     # urls_other_products_on_the_page="urls_other_products_on_the_page_example",
#                     # worker="worker_example",
#                     # task="task_example",
#                 )  # History |  (optional)

#                 try:
#                     api_response = api_instance.history_create(body=history)
#                     # pprint(api_response)
#                 except openapi_client.ApiException as e:
#                     print("Exception when calling HistoryApi->history_create: %s\n" % e)
#             print("Count load object =", len(self.__list_dict))
                        
class TricolorParserFFile(TricolorParser):
    """
    Собирает данные страницы, скачанной с сайта https://cg-tricolor.ru/catalog/flats в файл 'sources/tricolor' очищает их, сохряняет
    """
    def __init__(self, page_text):
        self.__url = None
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")
        self.__items_list = self.__b_soup.findAll("tr", class_ = "results__tr")
        self.__dict_list = []
            
    def get_dict_list(self) -> list:
        if self.__items_list:
            for item in self.__items_list:
                item_dict = {}
                item_dict["title"] = self._get_title(item)
                if  item_dict["title"]:
                    rooms = item_dict["title"][0]
                    item_dict["rooms"] = int(rooms)
                else:
                    item_dict["rooms"] = None
                item_dict["bulding"] = self._get_bulding(item)
                item_dict["floor"] = self._get_floor(item)
                item_dict["square"] = self._get_square(item)
                item_dict["price"] = self._get_price(item)
                item_dict["url"] = self._get_item_url(item)
                item_dict["project"] = "Триколор"
                # item_dict["plan"] = 
                item_dict["address"] = "Проспект Мира, 188Б"
                item_dict["city"] = "Москва"
                item_dict["brand"] = "Capital Group"
                item_dict["brand_url"] = "https://capitalgroup.ru/"
                item_dict["category"] = "Новостройки"
                item_dict["source_url"] = "https://cg-tricolor.ru/catalog/flats"
                # item_dict["price_sale"] = e["price"]
                # item_dict["datetime_create"] = "1970-01-01T00:00:00.00Z"
                # item_dict["image_url"] = e["plan"]
                # item_dict["description"] = json.dumps(e["specialmortgageoffer_set"])
                # item_dict["apartment_completion_quarter"]
                # item_dict["apartment_completion_year"] = int(e["completion_year"])
                # item_dict["apartment_floors_total"] = int(e["floors_total"])
                # item_dict["apartment_ceilingheight"] = e["ceilingheight"]
                # item_dict["apartment_ppm"] = int(e["ppm"])
                # item_dict["apartment_location"] = e["location"]
                # item_dict["apartment_location_lat"] = e["location"].split(',')[0][:9]
                # item_dict["apartment_location_lon"] = e["location"].split(',')[1][:9]
                
                self.__dict_list.append(item_dict)
            return self.__dict_list  
        else:
            print("Error in getting Items List")