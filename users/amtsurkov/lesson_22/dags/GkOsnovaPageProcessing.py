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


class GkOsnovaServiceProcessing:
    """
{
  "data": [
    {
      "id": 22516,
      "uuid": "C98E7455-1210-46C2-9073-5520A4ADD432",
      "status": "available",
      "number": "100",
      "meter_cost": 457400,
      "cost": 11846660,
      "number_on_floor": 4,
      "layout": {
        "code": "k1-a100",
        "type": "apartment",
        "room_count": "S",
        "area": 25.9,
        "living_area": 0,
        "plan_image": {
          "image_thumb": "https://api.gkosnova.tech/public/storage/media/2023/9/450/dVqoq3QPDo5kg0BrM48kpRFCC9iUz6xoLr99wM99.png"
      },
      "building": "1",
      "section": "1",
      "floor": {
        "compass_direction": 40,
        "number": 10,
        "plan_image": {
          "image_thumb": "https://api.gkosnova.tech/public/storage/media/2023/9/450/axla3sDz6kzjVucb0quSn4OVPWRWP4WolODlXLCe.jpg"
      },
      "properties": {
        "mortgage_percent": 0,
        "new_cost": 0,
        "with_promotion": false,
        "tour": "",
        "description": "",
        "view_from_window": null,
        "plan_type": "",
        "with_decoration": false
      },
      "project_id": 14,
    },
    
        title = str(project_id) + building + section + number_on_floor + str(floor[number]) + str(layout[area]) + ' ' + building + '-' + section + ' ' + layout[room_count]
        quantity = 1
        price = cost
        price_sale = cost 
        datetime_create="1970-01-01T00:00:00.00Z",
        brand = "gk-osnova.ru"
        brand_url = "gk-osnova.ru"
        url = url
        img_url =layout[plan_image][image_thumb] 
        #description = to_str(specialmortgageoffer_set)
        #230211
        apartment 
        apartment_area = layout[area]
        #apartment_completion_quarter = completion_quarter
        #apartment_completion_year = completion_year
        --apartment_project = project
        apartment_floor = number_on_floor
        apartment_floors_total = floor[number]
        #apartment_ceilingheight = ceilingheight
        apartment_room = layout[room_count]
        apartment_ppm = meter_cost
        #apartment_address = address
        #apartment_location_lat = location.split(',')[0]
        #apartment_location_lon = location.split(',')[1]
    """



    def __generate_jsons(self):
        #i = 0
        for url_base in self.__urls:
            next_url = url_base
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
#            "https://api.gkosnova.tech/public/api/v1/building-objects/14/properties?detail=0",
        ]
        for i in range(3):
            self.__urls.append("https://api.gkosnova.tech/public/api/v1/building-objects/" + str(i) + "/properties?detail=0")


        self.__list_dict = []
        for jsons, source_url in self.__generate_jsons():
            for e in jsons["results"]:
                el = {}
                #el[
                #    "title"
                #] = f"{e['project']} {e['building']} {str(e['floor'])} {str(e['area'])} {e['address']} {e['location']}"
                #el["quantity"] = 1
 
                el["title"] = f'{e["project_id"])} {e["building"]} {e["section"]} {e["number_on_floor"]} {e["floor"]["number"]} {e["layout"]["area"]} {e["layout"]["room_count"]}'
                el["quantity"] = 1
                el["price"] = e["cost"]
                el["price_sale"] = e["cost"]
                el["datetime_create"] = "1970-01-01T00:00:00.00Z",
                el["brand"] = "gk-osnova.ru"
                el["brand_url"] = "gk-osnova.ru"
                #el["url"] = e["url"]
                el["url"] = source_url
                el["img_url"] = e["layout"]["plan_image"]["image_thumb"] 
                el["apartment_area"] = e["layout"]["area"]
                el["apartment_floor"] = e["number_on_floor"]
                el["apartment_floors_total"] = e["floor"]["number"]
                el["apartment_room"] = e["layout"]["room_count"]
                el["apartment_ppm"] = e["meter_cost"]

                el["category"] = "Новостройки"
                el["source_url"] = source_url
                
                #el["apartment_area"] = e["area"]
                #el["apartment_floor"] = int(e["floor"])
                ##if e.get("floors_total"):
                #    el["apartment_floors_total"] = int(e["floors_total"])
                #else:
                #    print("not have floors_total in =", source_url)
                #    el["apartment_floors_total"] = None
                

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
                    #description=e["description"],
                    # params="params_example",
                    # seller="seller_example",
                    # seller_url="seller_url_example",
                    source_url=e["source_url"],
                    apartment_area=e["apartment_area"],
                    #apartment_completion_quarter=e["apartment_completion_quarter"],
                    #apartment_completion_year=e["apartment_completion_year"],
                    apartment_floor=e["apartment_floor"],
                    apartment_floors_total=e["apartment_floors_total"],
                    #apartment_ceilingheight=e["apartment_ceilingheight"],
                    apartment_room=e["apartment_room"],
                    apartment_ppm=e["apartment_ppm"],
                    #apartment_address=e["apartment_address"],
                    #apartment_location=e["apartment_location"],
                    #apartment_location_lat=e["apartment_location_lat"],
                    #apartment_location_lon=e["apartment_location_lon"],
                    
                    # urls_other_products_on_the_page="urls_other_products_on_the_page_example",
                    # worker="worker_example",
                    # task="task_example",
                )  # History |  (optional)

                try:
#                    api_response = api_instance.history_create(body=history)
                    # pprint(api_response)
                except openapi_client.ApiException as e:
                    print("Exception when calling HistoryApi->history_create: %s\n" % e)
            print("Count load object =", len(self.__list_dict))
 
