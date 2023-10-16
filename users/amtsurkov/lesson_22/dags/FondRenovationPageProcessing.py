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


class FondRenovationServiceProcessing:
    """
        https://fr.mos.ru/pokupka-nedvizhimosti-dlya-vseh/ajax.php?type[]=R&__status[]=FINISHED&__status[]=PROCESSING&price_min=0&price_max=35000000&floor_min=-1&floor_max=54&open_sale=1&pagesize=100000
        
{
  "objects": {
    "items": [
      {
        "id": "34215",
        "name": "Дежнева пр-д., влд. 30, к. 3",
        "code": "dezhneva-pr-d-vld-30-k-3",
        "district": 2559,
        "coords": [
          "55.8727",
          "37.6333"
        ],
        "status_code": "PROCESSING",
        "finishing_code": "FULL",
        "img": "/upload/resize_cache/iblock/0b1/1000_500_1/2pkwvi9gyeo67c20w3s8igextsd5x17k.jpg",
        "metro": [
          "53381",
          "53544"
        ],
        "floors": "21",
        "flats": "96",
        "vvod": "2024 г.",
        "county": 2455
      },
  ],
  "housings": {
    "items": [
      {
        "id": "60497",
        "name": "кв. 2_Дежнева пр-д., влд. 30, к. 3",
        "object": "Дежнева пр-д., влд. 30, к. 3",
        "object_id": "34215",
        "object_code": "dezhneva-pr-d-vld-30-k-3",
        "number": "2",
        "rooms": "1",
        "floor": "2",
        "area": "44.26",
        "price": "9334434",
        "price_m": "210900",
        "plan_s": "/upload/resize_cache/iblock/860/600_600_1/k18cxj6gvy0y95z9g1h71q19vjpx5wyt.png",
        "plan": "/upload/iblock/860/k18cxj6gvy0y95z9g1h71q19vjpx5wyt.png",
        "type": "R",
        "term_of_application": "13.04.2023",
        "open_sale": 1,
        "y2_sell": 0,
        "for_sell": 0,
        "auction": "https://investmoscow.ru/tenders/tender/18957055",
        "floor_plan": {
          "full": "/upload/iblock/19c/tn0mj11frauehqe0duwf8f0eimgajcyp.png",
          "small": "/upload/resize_cache/iblock/19c/600_600_1/tn0mj11frauehqe0duwf8f0eimgajcyp.png"
        }
      },
    """

    def __generate_jsons(self):
        for url_base in self.__urls:
            next_url = url_base
            while next_url:
                url = next_url
                next_url = ""
                # print(url)
                with urllib.request.urlopen(url) as response:
                    self.__page = response.read()
                    jsons = json.loads(self.__page)
                    yield (jsons, url)
                    # next_url = jsons.get("next", "")

    def process(self):
        self.__urls = [
            "https://fr.mos.ru/pokupka-nedvizhimosti-dlya-vseh/ajax.php?type[]=R&__status[]=FINISHED&__status[]=PROCESSING&price_min=0&price_max=35000000&floor_min=-1&floor_max=54&open_sale=1&pagesize=100000",
        ]

        self.__list_dict = []
        for jsons, source_url in self.__generate_jsons():
            objects_to_params = {}
            for h in jsons["objects"]["items"]:
                objects_to_params[h['code']] = h
                
            for e in jsons["housings"]["items"]:
                el = {}
                el["title"] = f"{e['name']} {e['object_code']} {str(e['floor'])} {str(e['area'])} {e['object']}"
                
                el["quantity"] = 1
                el["price"] = e["price"]
                el["price_sale"] = e["price"]
                el["datetime_create"] = "1970-01-01T00:00:00.00Z"
                el["brand"] = "fr.mos.ru"
                el["brand_url"] = "fr.mos.ru"
                el["category"] = "Реновация"
                #el["url"] = e["auction"]
                el["url"] = e.get("auction", '')
                #print(e.get("auction", 'aaaaaa'))
                el["image_url"] = "https://fr.mos.ru" + e["plan"]
                #el["description"] = json.dumps(e["object"])[0:100]
                #el["description"] = e["object"]
                el["description"] = f"object: {e['object']}, district: {objects_to_params[e['object_code']]['district']}, county: {objects_to_params[e['object_code']]['county']}, flats: {objects_to_params[e['object_code']]['flats']}"
                if(objects_to_params[e["object_code"]].get("developer")):
                    el["description"] += f", developer: {objects_to_params[e['object_code']]['developer']}"
                el["description"] = el["description"][0:200]
                
                el["source_url"] = source_url                
                el["apartment_area"] = e["area"]
                
                #if e.get("completion_quarter"):
                #    el["apartment_completion_quarter"] = int(e["completion_quarter"])
                #else:
                #    print("not have completion_quarter in =", source_url)
                #    el["apartment_completion_quarter"] = None
                el["apartment_completion_quarter"] = None
                #el["apartment_completion_year"] = int(e["completion_year"])
                if(objects_to_params[e["object_code"]].get("vvod")):
                    el["apartment_completion_year"] = int(objects_to_params[e["object_code"]]["vvod"][0:4])
                else:
                    el["apartment_completion_year"] = None
                el["apartment_floor"] = int(e["floor"])
                #el["apartment_floors_total"] = int(e["floors_total"])
                if '-' in objects_to_params[e["object_code"]]["floors"]:
                    el["apartment_floors_total"] = objects_to_params[e["object_code"]]["floors"].split('-')[-1]
                else:    
                    el["apartment_floors_total"] = int(objects_to_params[e["object_code"]]["floors"])
                #el["apartment_ceilingheight"] = e["ceilingheight"]
                el["apartment_ceilingheight"] = None
                el["apartment_room"] = int(e["rooms"])
                el["apartment_ppm"] = int(e["price_m"])
                el["apartment_address"] = e["object"]
                #el["apartment_location"] = e["location"]
                el["apartment_location"] = f"district: {objects_to_params[e['object_code']]['district']}, county: {objects_to_params[e['object_code']]['county']}, flats: {objects_to_params[e['object_code']]['flats']}"
                if(objects_to_params[e["object_code"]].get("developer")):
                    el["apartment_location"] += f", developer: {objects_to_params[e['object_code']]['developer']}"
                #el["apartment_location_lat"] = e["location"].split(',')[0][:9]
                el["apartment_location_lat"] = objects_to_params[e["object_code"]]["coords"][0]
                #el["apartment_location_lon"] = e["location"].split(',')[1][:9]                
                el["apartment_location_lon"] = objects_to_params[e["object_code"]]["coords"][1]
                self.__list_dict.append(el)

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
