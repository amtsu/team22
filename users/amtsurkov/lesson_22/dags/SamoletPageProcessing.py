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


class SamoletServiceProcessing:
    """
        https://samolet.ru/api_redesign/flats/?ordering=-order_manual,filter_price_package,pk&free=1
        https://samolet.ru/api_redesign/flats/?ordering=-order_manual,filter_price_package,pk&free=1&offset=12&limit=12
    
        https://samolet.ru/api_redesign/flats/200343/
        
        {
          "count": 15190,
          "next": "https://samolet.ru/api_redesign/flats/?free=1&limit=12&offset=24&ordering=-order_manual%2Cfilter_price_package%2Cpk",
          "previous": "https://samolet.ru/api_redesign/flats/?free=1&limit=12&ordering=-order_manual%2Cfilter_price_package%2Cpk",
          "is_flat": true,
          "results": [
            {
              "id": 250365,
              "article": "ПРЛ8/К13.2-03-02-10-010",
              "project_id": 1,
              "project_ref_id": "dfad20e9-8c4b-e711-80c5-005056b8d207",
              "ref_id": "e6757db6-cea7-ed11-b825-005056b8a72c",
              "project": "Пригород Лесное",
              "building": "13.2",
              "building_id": 1981,
              "section": 3,
              "floor_number": 2,
              "total_floors": 17,
              "number": 10,
              "ppm": 151057,
              "living_area": 12.7,
              "in_favorite": false,
              "note": null,
              "hidden": false,
              "seen": false,
              "url": "https://samolet.ru/project/prigorod-lesnoe/flats/250365/",
              "api_url": "https://samolet.ru/api_redesign/flats/250365/",
              "status": 1,
              "area": 25.91,
              "rooms": 0,
              "price": 3913887,
              "old_price": null,
              "mortgage_payment": 17254,
              "mortgage": {

              },
              "is_apartment": false,
              "penthouse": false,
              "settling_date_formatted": "30 ноя. 2025",
              "has_discount": false,
              "discount": 0,
              "level_up": false,
              "is_resale": false,
              "renovation": true,
              "plan": "https://media.samolet.ru/flat/plan/e6757db6-cea7-ed11-b825-005056b8a72c.svg",
              "plan_png": "https://media.samolet.ru/flat/plan/e6757db6-cea7-ed11-b825-005056b8a72c_feed.png",
              "plan_xxl": null,
              "auction": null,
              "lot_url": null,
              "plan_with_furniture": null,
              "floor_plan": "https://media.samolet.ru/floor/13.2-3-2.svg",
              "floor_plan_width": 808.639,
              "floor_plan_height": 2000.94,
              "hover": "<path id=\"re10\" class=\"st0\" d=\"M354.9,1687.4v124.6H52.8v-228.7h278.6v104L354.9,1687.4L354.9,1687.4z\"/>",
              "window_view_image_spec": null,
              "layout": "С-25-Л-Д(3.10)",
              "azimuth": 0,
              "has_smartflat": false,
              "has_kitchen": true,
              "has_closet": false,
              "has_certificate": false,
              "has_furniture_set": true,
              "rename_flat_to_plan": false,
              "rename_plan_to_apart": false,
              "project_rename_flat_to_plan": false,
              "kitchen_price": 325815,
              "price_with_kitchen": 4303602,
              "old_price_with_kitchen_markup": 4229927,
              "old_price_with_kitchen": 4239702,
              "price_with_kitchen_markup": 4229927,
              "clean_price": null,
              "price_with_conditioner": 4303602,
              "filter_price": 4303602,
              "filter_price_package": 4303602,
              "booking_available": true,
              "has_individual_decoration": false,
              "installment_available": false,
              "flashsale": null,
              "acquiring_amount": 10000,
              "project_tags": {
                "Стороны света": [
                  {
                    "id": 2,
                    "slug": "yugovostok",
                    "name": "Юго-Восток",
                    "url": null,
                    "category_name": "Стороны света"
                  }
                ],
                "Общие": [
                  {
                    "id": 20,
                    "slug": "moscow_obl",
                    "name": "Московская область",
                    "url": null,
                    "category_name": "Общие"
                  }
                ],
                "Округа": [
                  {
                    "id": 13,
                    "slug": "uvao",
                    "name": "ЮВАО",
                    "url": "https://samolet.ru/novostroyki/uvao/",
                    "category_name": "Округа"
                  },
                  {
                    "id": 17,
                    "slug": "mo",
                    "name": "МО",
                    "url": "https://samolet.ru/novostroyki/mo/",
                    "category_name": "Округа"
                  }
                ],
                "Метро": [
                  {
                    "id": 41,
                    "slug": "domodedovskaya",
                    "name": "Домодедовская",
                    "url": "https://samolet.ru/novostroyki/domodedovskaya/",
                    "category_name": "Метро"
                  }
                ],
                "Район": [
                  {
                    "id": 33,
                    "slug": "leninskijokrug",
                    "name": "Ленинский округ",
                    "url": "https://samolet.ru/novostroyki/leninskijokrug/",
                    "category_name": "Район"
                  }
                ]
              },
              "projecttrait_set": [
                {
                  "id": 33,
                  "name": "Расположение",
                  "text": "Рядом лес и пруд",
                  "icon": "https://media.samolet.ru/project/traits/raspoloj_nUDsBy1.svg",
                  "order": 1,
                  "for_business_class": false
                },
                {
                  "id": 34,
                  "name": "Инфраструктура",
                  "text": "Открыты детские сады и школа. Яблоневый сад и SportHub",
                  "icon": "https://media.samolet.ru/project/traits/Namekindergarten_Size64_0PN6lEP.svg",
                  "order": 2,
                  "for_business_class": false
                },
                {
                  "id": 35,
                  "name": "Транспорт",
                  "text": "15 минут до метро «Домодедовская»",
                  "icon": "https://media.samolet.ru/project/traits/car_as383fX.svg",
                  "order": 3,
                  "for_business_class": false
                },
                {
                  "id": 165,
                  "name": "Улучшенная отделка",
                  "text": "Повышение класса отделки",
                  "icon": "https://media.samolet.ru/project/traits/Vector_Stroke_evjOGRb_GTMXjLn.svg",
                  "order": 4,
                  "for_business_class": false
                }
              ],
              "metro_set": [
                {
                  "name": "Домодедовская",
                  "color": "#4BAF4F",
                  "car_time": 15,
                  "walk_time": null,
                  "public_transport_time": null,
                  "cian_id": 39
                }
              ],
              "deposit": 645540,
              "project_settings": {
                "deposit": 15.0,
                "rate": 3.9,
                "term": 30.0,
                "deposit_max": 12.0
              },
              "closed_sale_available": false,
              "closed_sale": null,
              "high_ceiling": false,
              "has_decor_set": true,
              "key_distribution_date": null,
              "realty_type": "flat",
              "old_filter_price_package": 4303602,
              "is_flat_xxl": false
            },
          ]
        }
        
        
      "price": 6457129,
      "price_with_kitchen": 6782944,
      "price_with_kitchen_markup": 6636327,
      "clean_price": 6636327,
      "price_with_conditioner": 6846844,
+      "filter_price": 6636327,
      "filter_price_package": 6636327,
  
  
         
     
        
        title = project + building + str(floor_number) + str(area) # + address + location
        quantity = 1
        price = old_price_with_kitchen
        price_sale = filter_price
        datetime_create="1970-01-01T00:00:00.00Z",
        brand = "samolet.ru"
        brand_url = "samolet.ru"
        url = url
        img_url = plan
        --description = 
        #230211
        apartment 
        apartment_area = area
        --apartment_completion_quarter = completion_quarter
        --apartment_completion_year = completion_year
        --apartment_project = project
        apartment_floor = floor_number
        apartment_floors_total = total_floors
        --apartment_ceilingheight = ceilingheight
        apartment_room = rooms
        apartment_ppm = ppm
        apartment_address = project
        --apartment_location_lat = location.split(',')[0]
        --apartment_location_lon = location.split(',')[1]
        
        
    
    
    """

    # def load_url_by_default(self):
    #    self.__urls = [
    #    "https://samolet.ru/api_redesign/flats/?ordering=-order_manual,filter_price_package,pk&free=1"
    #    "https://samolet.ru/api_redesign/flats/?ordering=-order_manual,filter_price_package,pk&free=1&offset=12&limit=12"
    #
    #    "https://samolet.ru/api_redesign/flats/200343/"
    #    ]

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
                    next_url = jsons.get("next", "")

    def process(self):
        self.__urls = [
            "https://samolet.ru/api_redesign/flats/?ordering=-order_manual,filter_price_package,pk&free=1"
        ]

        self.__list_dict = []
        for jsons, source_url in self.__generate_jsons():
            for e in jsons["results"]:
               
                el = {}
                el[
                    "title"
                ] = f"{e['project']} {e['building']} {str(e['floor_number'])} {str(e['area'])}"
                el["quantity"] = 1
                el["price"] = e["old_price_with_kitchen"]
                el["price_sale"] = e["filter_price"]
                el["datetime_create"] = "1970-01-01T00:00:00.00Z"
                el["brand"] = "samolet.ru"
                el["brand_url"] = "samolet.ru"
                el["category"] = "Новостройки"
                el["url"] = e["url"]
                el["image_url"] = e["plan"]
                el["source_url"] = source_url
                el["apartment_area"] = e["area"]
                el["apartment_floor"] = int(e["floor_number"])
                if e.get("total_floors"):
                    el["apartment_floors_total"] = int(e["total_floors"])
                else:
                    print("not have floors_total in =", source_url)
                    el["apartment_floors_total"] = None
                el["apartment_room"] = int(e["rooms"])
                el["apartment_ppm"] = int(e["ppm"])
                el["apartment_address"] = e["project"]
                #print(e["floor"])
                
                self.__list_dict.append(el)
            print(source_url)

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
                    #category=e["category"],
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
                    apartment_address=e["apartment_address"],
                    #apartment_location=e["apartment_location"],
                    #apartment_location_lat=e["apartment_location_lat"],
                    #apartment_location_lon=e["apartment_location_lon"],
                    
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
