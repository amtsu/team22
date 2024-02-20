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


class PikServiceProcessing:
    """
        https://flat.pik-service.ru/api/v1/filter/block?type=1,2&location=2,3&flatLimit=50&blockLimit=1000&geoBox=55.20936697505167,56.264571542902-36.93957410937494,38.104124890624945
        https://www.pik.ru/search/kutuzovskiy?bulk=9861
        https://flat.pik-service.ru/api/v1/filter/flat-by-block/1196?type=1,2&location=2,3&bulk=9861&flatPage=2&flatLimit=8&onlyFlats=1
        https://flat.pik-service.ru/api/v1/filter/flat?flatPage=0



{
  "success": true,
  "data": {
    "time": {
      "filter": 0.04,
      "stats": 0.001,
      "statsEmpty": 0
    },
    "cache": {
      "filter": false,
      "stats": true,
      "statsEmpty": true
    },
    "stats": {
      "count": 23274,
      "countBlocks": 89,
      "currentPage": 500,
      "lastPage": 1164,
      "priceMin": 2601739,
      "priceMax": 57249610,
      "floorMin": 1,
      "floorMax": 50,
      "areaMin": 191,
      "areaMax": 1332,
      "areaKitchenMin": 0,
      "areaKitchenMax": 344,
      "types": [
      ],
      "blocks": [
      ]
    },
    "items": [
      {
        "id": 722054,
        "area": 84.03,
        "floor": 8,
        "metro": {
          "id": null,
          "name": null,
          "color": null
        },
        "price": 18251316,
        "rooms": 2,
        "status": "free",
        "typeId": 2,
        "planUrl": "https://0.db-estate.cdn.pik-service.ru/attachment/7678000000000/7678e9f6-3d71-eb11-84d4-02bf0a4d8e27/c_2klr_10_7-3_t_a_lr1-2_95_lr3-2_96_90_2_bd0280637f168d0e406d2530c0357dd8.svg",
        "bulkName": "Lot 31 Block 53",
        "maxFloor": 25,
        "blockName": "ONE SIERRA",
        "blockSlug": "",
        "finishType": 1,
        "meterPrice": 217200,
        "settlementDate": "2024-04-16",
        "currentBenefitId": null
      },
    
    ######


      {
        "id": 320,
        "name": "Holland park",
        "path": "/hp",
        "image": {
          "mobile": "https://0.db-estate.cdn.pik-service.ru/block/2023/04/19/686x428.rev00_Fy9vvJoZRHGyt4ra.jpg",
          "desktop": "https://0.db-estate.cdn.pik-service.ru/block/2023/04/19/2432x508.rev00_CQLuqoMGTFPZAVTk.jpg"
        },
        "metro": "Спартак",
        "sticker": null,
        "latitude": 55.815722,
        "mapImage": "https://0.db-estate.cdn.pik-service.ru/attachment_pikru/0/1c7b76f2-2b50-11e8-ac2a-001ec9d8c6a2/320_hlp_5971dc163da153c3e45bcb79a6be6541.jpg",
        "priceMin": 9912320,
        "isPremium": false,
        "longitude": 37.425869,
        "timeOnFoot": 5,
        "surveillance": {
        },
        "metroStations": [
          {
            "id": 195,
            "line": "Таганско-Краснопресненская линия",
            "name": "Спартак",
            "lineColor": "#B61D8E"
          }
        ],
        "timeOnTransport": 0
      },
        



        title = name + metro r(area) # + address + location
        quantity = 1
        price = old_price_with_kitchen
        price_sale = filter_price
        datetime_create="1970-01-01T00:00:00.00Z",
        brand = "pik.ru"
        brand_url = "pik.ru"
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

    def __generate_jsons(self):
        for url_base in self.__urls:
            i = 0
            next_url = url_base
            while next_url:
                i += 1
                url = next_url + str(i)
                next_url = ""
                print(url)
                #sessionid=kjw99ls6bcb4onofwazpcufjmwwa308x
                a_request = urllib.request.Request(url)
                #a_request.add_header("Cookie", "sessionid=kjw99ls6bcb4onofwazpcufjmwwa308x")
                #qrator_jsr=1701810731.684.adBf0Vn0XMh8G9sf-f67qh8uqbbmbh3a42siunqadovrbv0vp-00
                #a_request.add_header("Cookie", "qrator_jsr=1701810731.684.adBf0Vn0XMh8G9sf-f67qh8uqbbmbh3a42siunqadovrbv0vp-00; Max-Age=300; Path=/;")
                with urllib.request.urlopen(a_request) as response:
                #with urllib.request.urlopen(url) as response:
                    self.__page = response.read()
                    jsons = json.loads(self.__page)
                    yield (jsons, url)
                    print(jsons['data']['stats']['count']) 
                    print(jsons['data']['stats']) 
                    #print(jsons['data']['statsEmpty']) 
                    print(jsons['data']['cache']) 
                    print(jsons['data']['time']) 
                    print(jsons['data']) 
                    next_url = url_base if len(jsons['data']['items']) > 0 and i < 4 and i < int((jsons['data']['stats']['count'] / 20) + 1) else None 

    def process(self):
        self.__urls = [
            "https://flat.pik-service.ru/api/v1/filter/flat?type=1,2&flatPage=",
        ]

        self.__list_dict = []
        for jsons, source_url in self.__generate_jsons():
            for e in jsons["data"]["items"]:
               
                el = {}
                el[
                    "title"
                ] = f"{e['blockName']} {e['bulkName']} {str(e['floor'])} {str(e['area'])}"
                el["quantity"] = 1
                el["price"] = e["price"]
                el["price_sale"] = e["price"]
                el["datetime_create"] = "1970-01-01T00:00:00.00Z"
                el["brand"] = "pik.ru"
                el["brand_url"] = "pik.ru"
                el["category"] = "Новостройки"
                el["url"] = "https://www.pik.ru/flat/" + str(e["id"])
                el["image_url"] = e["planUrl"]
                el["source_url"] = source_url
                el["apartment_area"] = e["area"]
                el["apartment_floor"] = int(e["floor"])
                if e.get("maxFloor"):
                    el["apartment_floors_total"] = int(e["maxFloor"])
                else:
                    print("not have floors_total in =", source_url)
                    el["apartment_floors_total"] = None
                el["apartment_room"] = int(e["rooms"])
                el["apartment_ppm"] = int(e["meterPrice"])
                el["apartment_address"] = e["blockName"]
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
