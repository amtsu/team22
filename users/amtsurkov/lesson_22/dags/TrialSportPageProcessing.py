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
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)
    
    def __get_text(self):
        assert Flase

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        return True
    
    def __normalization(self, price_bad):
        return price_bad
    
    def __type_convert(self, text):
        return text
    
    def _w(self):
        return 'w'
        
    def __z(self):
        return 'z'

class PriceElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)
    
    def __get_text(self):
        list_price_data = self.__soup.findAll('div', class_='prices_for_popup')
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all('div', class_='price')
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_price_data = self.__soup.findAll('div', class_='prices_for_popup')
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all('div', class_='price')
        assert len(list_reports_data) == 2
        if len(list_reports_data) != 2:
            return False
        return True
    
    def __normalization(self, price_bad):
        price_bad = price_bad.replace(u'\u2009', '') # ' '
        price_bad = price_bad.replace(u'\u20bd', '') # '₽'
        price_bad = price_bad.replace(u' ', '') # ' '
        return price_bad
        price_good = int(price_bad)
        return price_good
    
    def __type_convert(self, text):
        assert text.isnumeric()
        return int(text)
    
    def __z(self):
        return 'z'

class PriceSaleElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)
    
    def __get_text(self):
        list_price_data = self.__soup.findAll('div', class_='prices_for_popup')
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all('div', class_='price price_disc')
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_price_data = self.__soup.findAll('div', class_='prices_for_popup')
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all('div', class_='price price_disc')
        assert len(list_reports_data) == 1
        if len(list_reports_data) != 1:
            return False
        return True

    def __normalization(self, price_bad):
        price_bad = price_bad.replace(u'\u2009', '') # ' '
        price_bad = price_bad.replace(u'\u20bd', '') # '₽'
        price_bad = price_bad.replace(u' ', '') # ' '
        return price_bad
        price_good = int(price_bad)
        return price_good

    def __type_convert(self, text):
        assert text.isnumeric()
        return int(text)

    def __z(self):
        return 'z'


class TitleElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self):
        list_reports_data = self.__soup.findAll('h2')
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_reports_data = self.__soup.findAll('h2')
        #print(list_reports_data)
        assert len(list_reports_data) == 5
        if len(list_reports_data) != 5:
            return False
        return True
    
    def __normalization(self, price_bad):
        return price_bad
    
    def __type_convert(self, text):
        return text


class BrandElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self):
        list_reports_data = self.__soup.findAll('div', class_="bread")
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_reports_data = self.__soup.findAll('div', class_="bread")
        #print(list_reports_data)
        assert len(list_reports_data) == 1
        if len(list_reports_data) != 1:
            return False
        return True
    
    def __normalization(self, price_bad):
        return price_bad.replace('\n', '')
    
    def __type_convert(self, text):
        return text


class BrandUrlElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self):
        list_price_data = self.__soup.findAll('div', class_='bread')
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all('a')
        element_1 = list_reports_data[-1]
        return element_1['href']

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_price_data = self.__soup.findAll('div', class_='bread')
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all('a')
        assert len(list_reports_data) == 6
        if len(list_reports_data) != 6:
            return False
        return True
    
    def __normalization(self, price_bad):
        return price_bad
    
    def __type_convert(self, text):
        return text
 

class ImageUrlElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self):
        list_price_data = self.__soup.findAll('script')
        script = list_price_data[10]
        #"big": "\/images\/catalog\/lbj7000_xt3_130_lv_storm_blue_rgb300dpi_2539265.jpg"
        return re.search(r'big": "(.+)"', script.text).group(1)

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        #list_price_data = self.__soup.findAll('script')
        #script = list_price_data[10]
        ##"big": "\/images\/catalog\/lbj7000_xt3_130_lv_storm_blue_rgb300dpi_2539265.jpg"
        #image_url = re.search(r'big": "(.+)"', script.text).group(1)

        #assert len(list_price_data) == 49
        #if len(list_price_data) != 49:
        #    return False
        return True
    
    def __normalization(self, price_bad):
        return price_bad.replace('\\', '')
    
    def __type_convert(self, text):
        return text
        

class OnePageProcessor():
    """
        Not good use BeautifulSoup object, and then use them in coheshe object
    """
    def __init__(self, text_page):
        self.__soup = BeautifulSoup(text_page, features="html.parser")

    def list_dict(self):
        return [
            {
                "title": TitleElement(self.__soup).get(),
                "price": PriceElement(self.__soup).get(),
                "price_sale": PriceSaleElement(self.__soup).get(),
                "brand": BrandElement(self.__soup).get(),
                "brand_url": BrandUrlElement(self.__soup).get(),
                "image_url": ImageUrlElement(self.__soup).get(),
            }
        ]


# модуль trial-sport.ru
class OnePage():
#    def get_price(self):
#        e = PriceElement(self.__soup)
#        #print(e._w())
#        #print(e.__z())
#        return e.get()
#
    def __init__(self, url):
        self.__url = url
        #print(help(urllib.request))
        with urllib.request.urlopen(self.__url) as response:
        #with urllib.urlopen(self.__url) as response:
            self.__page = response.read()
            self.__one_page_processor = OnePageProcessor(self.__page)
            
#    def get_title(self):
#        e = TitleElement(self.__soup)
#        return e.get()

    def list_dict(self):
        return self.__one_page_processor.list_dict()
    

class ListPage():
    pass


class ServiceProcessing():
    pass

class TrialSportServiceProcessing(ServiceProcessing):
    """
    when we have many ServiceProcessing, we nead create one Modeul with configuration 
    """
    def load_url_by_default(self):
        self.__urls = [
            "https://trial-sport.ru/goods/51530/1179889.html",
            "https://trial-sport.ru/goods/51527/2175792.html",
            "https://trial-sport.ru/goods/51527/2175355.html",
            "https://trial-sport.ru/goods/51527/2174687.html",
            "https://trial-sport.ru/goods/51527/2174362.html",
            "https://trial-sport.ru/goods/51527/1525157.html",
            "https://trial-sport.ru/goods/51527/1525371.html",
            "https://trial-sport.ru/goods/51527/2174317.html",
        ]

    def process(self):
        self.__list_dict = []
        for url in self.__urls:
            for object_params in OnePage(url).list_dict():
                self.__list_dict.append(object_params)
        #create file with name current datetime
        # whene trabsfer to airflow we need change save file, becouse runner may start in any server

    def __create_file_name_with_current_datetime(self):
        return 'trialsport_fresh.json'

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
                    #category="category_example",
                    #category_url="category_url_example",
                    brand=e["brand"],
                    brand_url=e["brand_url"],
                    #day_to_delivery=1,
                    #sku="sku_example",
                    #url="url_example",
                    #canonical_url="canonical_url_example",
                    img_url=e["image_url"],
                    #description="description_example",
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


