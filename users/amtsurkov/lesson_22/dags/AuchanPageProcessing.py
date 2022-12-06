#import urllib3 as urllib
#import urllib as urllib
import re
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

class Element():
    pass

class PriceElement(Element):
    pass

class PriceSaleElement(Element):
    pass

class TitleElement(Element):
    pass

class BrandElement(Element):
    pass

class BrandUrlElement(Element):
    pass

class ImageUrlElement(Element):
    pass
        
class OnePageProcessor():
    pass

class OnePage():
    pass

class ListPage():
    pass

class ServiceProcessing():
    pass

class AuchanServiceProcessing(ServiceProcessing):
    """ 
    "items": [
{
      "id": 15574399,
      "code": "nozhnicy-kust-dobrynya-57sm",
      "categoryCodes": [
        {
          "id": 1974,
          "name": "Сад и огород",
          "code": "tovary-dlya-dachi"
        },
        {
        }
      ],
      "title": "Ножницы кустарниковые Добрыня М",
      "vendorCode": "4610000695609",
      "price": {
        "value": 993.99,
        "currency": "RUB",
        "per": "item"
      },
      "stock": {
        "qty": 5,
        "storeId": 40
      },
      "catalogImageId": 27090238,
      "catalogImageUrl": "https://www.auchan.ru/files/original/27090238",
      "media": [
        27090238
      ],
      "description": {
        "content": "Предназначены для срезания веток, вырезки кустарника и поросли растений. Особенности: специальная геометрия ножниц (режущая часть отклонена от линии ручек в направлении резания), режущий нож имеет специальные углы заточки, противорежущий нож имеет зубчатую поверхность, что помогает удерживать срезаемые ветки большого диаметра от выскальзывания от оси ножниц (уменьшается усилие резания). Кроме того режущий нож ножниц изготовлен из специальной стали с термообработкой, на ножницах имеются пластиковые амортизаторы, ручки ножниц изготовлены из профильной металлической окрашенной трубы с двухцветными, эргономичными и надежными ручками - держателями. Все это делает кустарниковые ножницы одними из лучших по режущим свойствам. Максимальный диаметр резания - 22 мм. Длина - 0,57 м."
      },
      "characteristics": [
        {
          "id": 1,
          "title": "Масса нетто, кг",
          "value": "0.86"
        },
        {
        }
      ],
      "brand": {
        "name": "-",
        "code": "-1"
      },
    },
    
    
    
    {
      "id": 16136277,
      "code": "lyzh-kompl-s-palkami-180-nn75",
      "categoryCodes": [
        {
          "id": 1628,
          "name": "Спорт и отдых",
          "code": "sport-i-otdyh"
        },
        {
          "id": 2128,
          "name": "Лыжи, сноуборды",
          "code": "lyzhi_snoubordy"
        },
        {
          "id": 2878,
          "name": "Горные лыжи",
          "code": "gornye_lyzhi"
        }
      ],
      "title": "Лыжный комплект STC NN75 с палками, 180 см",
      "vendorCode": "4690623030391",
      "price": {
        "value": 3090.99,
        "currency": "RUB",
        "per": "item"
      },
      "stock": {
        "qty": 4,
        "storeId": 40
      },
      "basketStep": 1,
      "saleActive": true,
      "active": true,
      "isAdult": false,
      "isHidden": false,
      "oldPrice": null,
      "discount": null,
      "catalogImageId": 27327211,
      "catalogImageUrl": "https://www.auchan.ru/files/original/27327211",
      "media": [
        27327211
      ],
      "mediaUrls": [
        "https://www.auchan.ru/files/original/27327211"
      ],
      "description": {
        "content": "Лыжный комплект STC NN75 180 см предназначен для любителей лыжных прогулок и туризма. Лыжи: Конструкция: внешняя оболочка из ABS пластика, облегченный клин из переклееной древесины, шлифованная синтетическая поверхность. Палки: 100% стекловолокно, ручки с темляком. Крепления: 75 мм. Товар представлен в ассортименте без возможности выбора!"
      },
      "characteristics": [
        {
          "id": 1,
          "title": "Масса нетто, кг",
          "value": "1.98"
        },
      ],
      "brand": {
        "name": "STC",
        "code": "stc"
      },
      "gimaId": "995508",
    },
    
   
    title = title 
    quantity = stock['qty']
    price = oldPrice
    price_sale =  price['value']
    datetime_create="1970-01-01T00:00:00.00Z",
    brand = brand['name']
    brand_url = 
    category = categoryCodes for name
    url = "https://www.auchan.ru/product/" + code
    img_url = catalogImageUrl
    description = description['content']
    """
    def load_url_by_default(self):
        self.__urls = [
            #"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=1",
            #"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=",            
        #]
        
        
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=1",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=2",
#        ]
#        ss =[
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=3",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=4",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=5",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=6",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=7",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=8",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=9",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=14",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=15",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=16",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=17",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=18",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=19",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=21",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=22",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=23",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=24",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=25",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=26",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=27",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=28",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=29",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=31",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=32",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=33",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=34",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=35",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=36",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=37",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=38",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=39",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=41",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=42",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=43",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=44",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=46",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=48",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=51",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=52",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=53",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=54",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=55",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=56",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=57",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=59",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=61",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=62",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=63",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=64",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=65",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=66",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=67",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=69",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=73",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=75",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=101",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=102",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=201",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=301",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=312",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=318",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=350",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=701",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=703",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=704",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=705",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=707",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=709",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=711",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=712",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=713",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=714",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=715",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=716",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=717",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=718",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=719",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=721",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=724",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=725",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=726",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=727",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=729",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=731",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=732",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=733",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=734",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=736",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=739",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=741",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=743",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=744",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=745",
"https://www.auchan.ru/v1/catalog/products?page=1&perPage=40000&merchantId=746",
        ]
        
    def depricated__generate_jsons(self):
        for url_base in self.__urls:
            next_url = url_base
            page = 1
            while next_url:
                url = next_url + str(page)
                page += 1
                if page > 1001:
                    break
                print(url)
                jsons = '[{}]'
                
                try:
                    with urllib.request.urlopen(url) as response:
                        self.__page = response.read()
                        jsons = json.loads(self.__page)
                    yield jsons
                except urllib.error.HTTPError:
                    print('Error url = ', url)
                    
    def __generate_jsons(self):
        for url in self.__urls:
            print(url)
            try:
                with urllib.request.urlopen(url) as response:
                    self.__page = response.read()
                    jsons = json.loads(self.__page)
                yield jsons
            except urllib.error.HTTPError:
                print('Error url = ', url)
        
    def process(self):
        self.__list_dict = []
        for jsons in self.__generate_jsons():
            for e in jsons['items']:
                el = {}
                #el['title'] = f"{e['project']} {e['building']} {str(e['floor'])} {str(e['area'])} {e['address']} {e['location']}"
                el['title'] = e['title']
                el['quantity'] = e['stock']['qty']
                el['price'] = e['oldPrice']
                el['price_sale'] = e['price']['value']
                el['datetime_create'] = "1970-01-01T00:00:00.00Z"
                el['brand'] = e['brand']['name']
                #el['brand_url'] =
                el['category'] = ' > '.join(i['name'] for i in e['categoryCodes'])
                el['url'] = "https://www.auchan.ru/product/" + e['code']
                el['image_url'] = e['catalogImageUrl']
                el['description'] = e['description']['content']

                self.__list_dict.append(el)

    def __create_file_name_with_current_datetime(self):
        return 'auchane_fresh.json'

    def save_in_file_with_current_datetime(self):
        json_string = json.dumps(self.__list_dict)
        file_name = self.__create_file_name_with_current_datetime()
        with open(file_name, 'w') as outfile:
            json.dump(json_string, outfile)

    def send_in_api(self):
        configuration = openapi_client.Configuration(
            host = "http://absrent.ru:8000"
        )

        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = history_api.HistoryApi(api_client)
            for e in self.__list_dict:
                #print(e)
                history = History(
                    pk=1,
                    title=e['title'],
                    quantity=e['quantity'],
                    price=str(e['price']['value'] if e['price'] else 0),
                    price_sale=str(e['price_sale']),
                    datetime_create="1970-01-01T00:00:00.00Z",
                    #score="-807",
                    #count_comments=1,
                    #count_likes=1,
                    #count_stars_all=1,
                    #count_stars_1=1,
                    #count_stars_2=1,
                    #count_stars_3=1,
                    #count_stars_4=1,
                    #count_stars_5=1,
                    #count_how_much_buy=1,
                    #count_questions=1,
                    #count_photo=1,
                    category=e["category"],
                    #category_url="category_url_example",
                    brand=e["brand"],
                    #brand_url=e["brand_url"],
                    #day_to_delivery=1,
                    #sku="sku_example",
                    url=e["url"],
                    #canonical_url="canonical_url_example",
                    img_url=e["image_url"],
                    description=e["description"],
                    #params="params_example",
                    #seller="seller_example",
                    #seller_url="seller_url_example",
                    #source_url="source_url_example",
                    #urls_other_products_on_the_page="urls_other_products_on_the_page_example",
                    #worker="worker_example",
                    #task="task_example",
                ) # History |  (optional)

                try:
                    api_response = api_instance.history_create(body=history)
                    #pprint(api_response)
                except openapi_client.ApiException as e:
                    print("Exception when calling HistoryApi->history_create: %s\n" % e)
            print('Count load object =', len(self.__list_dict))

