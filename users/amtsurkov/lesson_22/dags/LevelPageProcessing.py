# import re
import urllib.request
import urllib
from bs4 import BeautifulSoup
import json

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import history_api
from openapi_client.model.history import History
from openapi_client.model.paginated_history_list import PaginatedHistoryList
from openapi_client.model.patched_history import PatchedHistory


class LevelServiceProcessing:
    """
        "count": 1097,
        "next": "https://level.ru/api/flat/?limit=8&offset=108",
        "previous": "https://level.ru/api/flat/?limit=8&offset=92",
        "results": [
            {
    -            "pk": "32732-0",
    -            "id": 32732,
    -            "ref_id": "890cb4b4-9cd2-ec11-80f2-005056010f28",
    -            "area": 17.8,
    -            "building": "1",
    -            "project": "Селигерская",
    -            "floor": 3,
                "old_price": 8766862.0,
                "price": 6136803,
    -            "ppm": 344764,
                "plan": "https://storage.yandexcloud.net/level-media/core/flat/plane/1-1-28_TOPxi6m.svg",
                "url": "https://level.ru/selig/flat/1room/1-1-28/",
    -            "full_payment_price": 6136803,
    -            "address": "пр-д Ильменский, вл. 12",
    -            "location": "55.859441,37.545155",
    -            "mortgage_payment": 20481.6772347551,
                "specialmortgageoffer_set": [
                    {
                        "name": "Ставка по кредиту 1%, первоначальный взнос от 15%, срок кредитования до 30 лет, сумма кредита до 12 млн руб.",
                        "amount": "12000000.00",
                        "term": 360,
                        "deposit": 15.0,
                        "mortgage_percent": 1.0,
                        "mortgage_price": 7890175,
                    },
                    {
                    },
                ],
                #230211
                "area": 17.7, # площадь
                "completion_quarter": 2, # кваратл сдачи строительства
                "completion_year": 2026, # год сдачи строительства
                --"project": "Южнопортовая", # название проекта
                "floor": 3, # этаж
                "floors_total": 24, # этажей в здании
                "ceilingheight": "2.90", # высота потолков
                "room": 1, # количество комнат
                "ppm": 398598 # цена за квадртыный метр
            }
        ]

        title = project + building + str(floor) + str(area) + address + location
        quantity = 1
        price = old_price
        price_sale = price
        datetime_create="1970-01-01T00:00:00.00Z",
        brand = "level.ru"
        brand_url = "level.ru"
        url = url
        img_url = plan
        description = to_str(specialmortgageoffer_set)
        #230211
        apartment 
        apartment_area = area
        apartment_completion_quarter = completion_quarter
        apartment_completion_year = completion_year
        --apartment_project = project
        apartment_floor = floor
        apartment_floors_total = floors_total
        apartment_ceilingheight = ceilingheight
        apartment_room = room
        apartment_ppm = ppm
        apartment_address = address
        apartment_location_lat = location.split(',')[0]
        apartment_location_lon = location.split(',')[1]
    """

    # def load_url_by_default(self):
    #    self.__urls = [
    #        "https://level.ru/api/flat/",
    #        #"https://level.ru/api/flat/?limit=8&offset=1070",
    #    ]

    def __generate_jsons(self):
        #i = 0
        for url_base in self.__urls:
            next_url = url_base
            #i += 1
            #if i > 2:
            #    break
            while next_url:
                url = next_url
                next_url = ""
                # print(url)
                with urllib.request.urlopen(url) as response:
                    self.__page = response.read()
                    jsons = json.loads(self.__page)
                    yield (jsons, url)
                    next_url = jsons.get("next", "")

    def process(self):
        self.__urls = [
            "https://level.ru/api/flat/",
            # "https://level.ru/api/flat/?limit=8&offset=1070",
        ]

        self.__list_dict = []
        for jsons, source_url in self.__generate_jsons():
            for e in jsons["results"]:
                el = {}
                el[
                    "title"
                ] = f"{e['project']} {e['building']} {str(e['floor'])} {str(e['area'])} {e['address']} {e['location']}"
                el["quantity"] = 1
                el["price"] = e["old_price"]
                el["price_sale"] = e["price"]
                el["datetime_create"] = "1970-01-01T00:00:00.00Z"
                el["brand"] = "level.ru"
                el["brand_url"] = "level.ru"
                el["category"] = "Новостройки"
                el["url"] = e["url"]
                el["image_url"] = e["plan"]
                el["description"] = json.dumps(e["specialmortgageoffer_set"])[:1000]                
                el["source_url"] = source_url
                # el['description'] = json.dumps(e['specialmortgageoffer_set'])[0:100]
                # el['description'] = "json.dumps(e['specialmortgageoffer_set'])"[0:10]
                # el['description'] = "json.dumps"
                
                el["apartment_area"] = e["area"]
                if e.get("completion_quarter"):
                    el["apartment_completion_quarter"] = int(e["completion_quarter"])
                else:
                    print("not have completion_quarter in =", source_url)
                    el["apartment_completion_quarter"] = None
                if e.get("completion_year"):
                    el["apartment_completion_year"] = int(e["completion_year"])
                else:
                    print("not have completion_year in =", source_url)   
                    el["apartment_completion_year"] = None
                el["apartment_floor"] = int(e["floor"])
                if e.get("floors_total"):
                    el["apartment_floors_total"] = int(e["floors_total"])
                else:
                    print("not have floors_total in =", source_url)
                    el["apartment_floors_total"] = None
                el["apartment_ceilingheight"] = e["ceilingheight"]
                el["apartment_room"] = int(e["room"])
                el["apartment_ppm"] = int(e["ppm"])
                el["apartment_address"] = e["address"]
                el["apartment_location"] = e["location"]
                el["apartment_location_lat"] = e["location"].split(',')[0][:9]
                el["apartment_location_lon"] = e["location"].split(',')[1][:9]
                #print(el["apartment_location_lat"])
                #print(e["floor"])
                

                self.__list_dict.append(el)

    # def pp(self):
    #    return self.__list_dict

    # def __create_file_name_with_current_datetime(self):
    #    return 'lelev_fresh.json'

    # def save_in_file_with_current_datetime(self):
    #    json_string = json.dumps(self.__list_dict)
    #    file_name = self.__create_file_name_with_current_datetime()
    #    with open(file_name, 'w') as outfile:
    #        json.dump(json_string, outfile)

    def send_in_api(self):
        configuration = openapi_client.Configuration(host="http://absrent.ru:8000")

        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = history_api.HistoryApi(api_client)
            for e in self.__list_dict:
                # print(e)
                history = History(
                    pk=1,
                    title=e["title"],
                    quantity=1,
                    price=str(e["price"]),
                    price_sale=str(e["price_sale"]),
                    datetime_create="1970-01-01T00:00:00.00Z",
                    # score="-807",
                    # count_comments=1,
                    # count_likes=1,
                    # count_stars_all=1,
                    # count_stars_1=1,
                    # count_stars_2=1,
                    # count_stars_3=1,
                    # count_stars_4=1,
                    # count_stars_5=1,
                    # count_how_much_buy=1,
                    # count_questions=1,
                    # count_photo=1,
                    category=e["category"],
                    # category_url="category_url_example",
                    brand=e["brand"],
                    brand_url=e["brand_url"],
                    # day_to_delivery=1,
                    # sku="sku_example",
                    url=e["url"],
                    # canonical_url="canonical_url_example",
                    img_url=e["image_url"],
                    description=e["description"],
                    # params="params_example",
                    # seller="seller_example",
                    # seller_url="seller_url_example",
                    source_url=e["source_url"],
                    apartment_area=e["apartment_area"],
                    apartment_completion_quarter=e["apartment_completion_quarter"],
                    apartment_completion_year=e["apartment_completion_year"],
                    apartment_floor=e["apartment_floor"],
                    apartment_floors_total=e["apartment_floors_total"],
                    apartment_ceilingheight=e["apartment_ceilingheight"],
                    apartment_room=e["apartment_room"],
                    apartment_ppm=e["apartment_ppm"],
                    apartment_address=e["apartment_address"],
                    apartment_location=e["apartment_location"],
                    apartment_location_lat=e["apartment_location_lat"],
                    apartment_location_lon=e["apartment_location_lon"],
                    
                    # urls_other_products_on_the_page="urls_other_products_on_the_page_example",
                    # worker="worker_example",
                    # task="task_example",
                )  # History |  (optional)

                try:
                    api_response = api_instance.history_create(body=history)
                    # pprint(api_response)
                except openapi_client.ApiException as e:
                    print("Exception when calling HistoryApi->history_create: %s\n" % e)
            print("Count load object =", len(self.__list_dict))
