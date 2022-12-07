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

class Ka5ServiceProcessing(ServiceProcessing):
    """ 
    {
  "next": "http://5ka.ru/api/v2/special_offers/?offset=10012&page=2",
  "previous": null,
  "results": [
    {
      "id": 248,
      "name": "Дск СВИТИ 1кг",
      "mech": null,
      "img_link": "https://media.5ka.ru/media/products/2629.jpg",
      "plu": 2629,
      "promo": {
        "id": 1248865771,
        "date_begin": "2022-12-06",
        "date_end": "2022-12-12",
        "type": "",
        "description": "",
        "kind": "Z001",
        "expired_at": 5
      },
      "current_prices": {
        "price_reg__min": 149.99,
        "price_promo__min": 139.99
      },
      "store_name": null
    },
    
   
    title = name
    quantity = 1
    price = current_prices[price_reg__min]
    price_sale = current_prices[price_promo__min]
    url = 'https://5ka.ru/api/v2/special_offers/' + id + '/'
    img_url = img_link
    """
    def load_url_by_default(self):
        self.__urls = [
            "https://5ka.ru/api/v2/special_offers/",
        ]
        
    def __generate_jsons(self):
        for url_base in self.__urls:
            next_url = url_base
            while next_url:
                url = next_url
                next_url = ''
                print(url)
                with urllib.request.urlopen(url) as response:
                    self.__page = response.read()
                    jsons = json.loads(self.__page)
                    yield (jsons, url)
                    next_url = jsons.get('next', '')
        
    def process(self):
        self.__list_dict = []
        for jsons, source_url in self.__generate_jsons():
            print(jsons)
            for e in jsons['results']:
                el = {}
                el['title'] = e['name']
                el['quantity'] = 1
                el['price'] = e['current_prices']['price_reg__min']
                el['price_sale'] = e['current_prices']['price_promo__min']
                el['datetime_create'] = "1970-01-01T00:00:00.00Z"
                el['url'] = 'https://5ka.ru/api/v2/special_offers/' + str(e['id']) + '/'
                el['image_url'] = e['img_link']
                el['source_url'] = source_url

                self.__list_dict.append(el)

    def __create_file_name_with_current_datetime(self):
        return 'ka5_fresh.json'

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
                    quantity=1,
                    price=str(e['price']),
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
#                    category=e["category"],
                    #category_url="category_url_example",
#                    brand=e["brand"],
#                    brand_url=e["brand_url"],
                    #day_to_delivery=1,
                    #sku="sku_example",
                    url=e["url"],
                    #canonical_url="canonical_url_example",
                    img_url=e["image_url"],
#                    description=e["description"],
                    #params="params_example",
                    #seller="seller_example",
                    #seller_url="seller_url_example",
                    source_url=e["source_url"],
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

