import re
import urllib.request
import urllib
from bs4 import BeautifulSoup
import json


from multiprocessing import freeze_support
freeze_support()

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.webdriver import WebDriver

import time
import openapi_client  # type: ignore
from pprint import pprint  # type: ignore

from openapi_client.apis.tags import history_api  # type: ignore
from openapi_client.model.history import History  # type: ignore
from openapi_client.model.paginated_history_list import PaginatedHistoryList  # type: ignore
from openapi_client.model.patched_history import PatchedHistory  # type: ignore
   

class ListPageProcessor:
    def __init__(self, text_page, url):
        self.__soup = BeautifulSoup(text_page, features="html.parser")
        self.__url = url

    def list_dict(self):
        """
        Формирует список слловарей, где каждый словарь представляет товар найденный на странице.
        Поиск элемента, его очистка, и преобразование также происходят на в данном методе.
        """
        l = []
        list_data = self.__soup.findAll("div", class_="product-card__middle-wrap")
        for i in list_data:
#            print(i.text)
#            print(i)
#            print(str(i))
            #d = i.find_all("ins", class_="price__lower-price")
            ##url = d[0]["href"]
            #price = d[0].text
            
            #d = i.find_all("del", class_="price__lower-price")
            #old_price = d[0].text
            
            #<ins class="price__lower-price">                    1&nbsp;089&nbsp;₽                </ins>
            #d = i.find_all("span")
            #for t in d :
            #    print(t)
                
            #print('----')    
            d = i.find_all("span", class_="product-card__name")
            title = ''
            for t in d :
                title = t.text
                title = title.replace(" / ", "")
#                print(title)
                # / 
                   
            #print('----')  
            
            #d = i.find_all("span", class_="product-card__name")
            #title = d[0].text
            
            d = i.find_all("del")
            #price = d[0].text
            price = 0
            for t in d :
                price = t.text
                #print(price)
                #print(price.split())
                #print(len(price.split()))
                price = price.replace("&nbsp;", "")
                #print(price)
                price = price.replace("₽", "")
                #print(price)
                price = price.replace(" ", "")
                price = ''.join(price.split())
#                print(price)
            
            d = i.find_all("ins", class_="price__lower-price")
            #price_sale = d[0].text
            price_sale = 0
            for t in d :
                price_sale = t.text
                price_sale = price_sale.replace("&nbsp;", "")
                price_sale = price_sale.replace("₽", "")
                price_sale = price_sale.replace(" ", "")
                price_sale = ''.join(price_sale.split())
#                print(price_sale)

            l.append(
                {
                    #"url": url,
                    "title": title,
                    "price": price,# if price else "",
                    "price_sale": price_sale if price_sale else (price),
                    "url": self.__url,
                    "brand": "b",
                    "brand_url": "bu",
                    "image_url": "iu",
                    "source_url": self.__url,
                }
            )
        return l


class OnePage:
    """
    Класс необходим для позода в вею сервис за получением конкртеной старницы и проследюущим ее процессиногом.

    Дальнейшее расширение:
    - учитывать время иземения доуемента используя запрос head, чтобы лишний раз не скачивать документы.
    - в качестве параметра инциализации принимать обект(класс) для процессинга чтобы можно было динамически менять исполнителее(DI)
    -
    """

    def __init__(self, url: str):
        self.__url = url
        with urllib.request.urlopen(self.__url) as response:
            self.__page = response.read()
            self.__one_page_processor = OnePageProcessor(self.__page, self.__url)

    def list_dict(self) -> list:
        """
        Возращает список, содержащий словарь с данными взями с страницы.
        """
        return self.__one_page_processor.list_dict()


class WildberriesServiceProcessing:
    def __init__(self):
        self.__list_dict = []
        self.__urls = []
        self.__url_list = []

    def load_url_by_default(self):
        """
        Инициализирует списки urls для послеющего их получения с веб ресрса и их обработки
        """
        #https://catalog.wb.ru/catalog/appliances1/catalog?appType=1&cat=9808&curr=rub&dest=-1257786&page=1&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,22,1,31,66,110,48,71,114&sort=priceup&spp=0&uclusters=0&xsubject=2473;5686
        # по 10 страниц
        self.__url_list = [
            "https://www.wildberries.ru/catalog/elektronika/tehnika-dlya-doma/uvlazhniteli-i-vozduhootchistiteli?sort=priceup&xsubject=2473%3B5686&page=",
            
            "https://www.wildberries.ru/catalog/igrushki/konstruktory-lego?sort=priceup&page=",
            
            "https://www.wildberries.ru/catalog/igrushki/konstruktory?sort=priceup&priceU=150000%3B15920000&page=",
            
            "https://www.wildberries.ru/catalog/igrushki/nastolnye-igry?sort=priceup&xsubject=120&page=",
            "https://www.wildberries.ru/catalog/igrushki/nastolnye-igry?sort=priceup&priceU=50000%3B35879200&page=",
            "https://www.wildberries.ru/catalog/igrushki/nastolnye-igry?sort=priceup&priceU=100000%3B35879200&page=",
            "https://www.wildberries.ru/catalog/igrushki/nastolnye-igry?sort=priceup&priceU=200000%3B35879200&page=",
            "https://www.wildberries.ru/catalog/igrushki/nastolnye-igry?sort=priceup&priceU=400000%3B35879200&page=",
            "https://www.wildberries.ru/catalog/igrushki/nastolnye-igry?sort=priceup&priceU=500000%3B35879200&page=",
            
            "https://www.wildberries.ru/catalog/igrushki/nastolnye-igry?sort=priceup&priceU=700000%3B35879200&page=",
            "https://www.wildberries.ru/catalog/igrushki/nastolnye-igry?sort=priceup&priceU=700000%3B35879200&page=",
        ]

    def process(self):
        """
        Формирует финальный список ссылок на документы для обработки и преобразовыает их в нужный формат.
        """
        
        # формируем настройки для хрома
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--headless')  # отключает открытие браузера
        options.add_argument('--window-size=1280x1696')
        options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        
        chrome = uc.Chrome(options=options)
        #chrome = uc.Chrome()
        
    
        #self.__list_dict = []
        #for url in self.__urls:
        #    for object_params in OnePage(url).list_dict():
        #        self.__list_dict.append(object_params)

        for url in self.__url_list:
            #for i in range(1, 10):
            for i in range(1, 10):
                r_url = url + str(i)
                # r_url = url
#                print(r_url)
                

                try:
                    # пробуем получить страницу каталога
                    chrome.get(r_url)
                    # даем время на загрузку страницы
                    time.sleep(3)
                    # получаем html страницы
                    page = chrome.page_source
                    # варим суп
                    #lenta_soup = BeautifulSoup(page, "lxml")
                    
                    self.__list_page_processor = ListPageProcessor(page, r_url)
                    for object_params in self.__list_page_processor.list_dict():
                        self.__list_dict.append(object_params)
                        
                except AttributeError as e:
                    print(f"Неудалось получить общий каталог, ошибка - {e}")
        
                
                #with urllib.request.urlopen(r_url) as response:
                #    self.__page = response.read()
                #    self.__list_page_processor = ListPageProcessor(self.__page, r_url)
                #    for object_params in self.__list_page_processor.list_dict():
                #        self.__list_dict.append(object_params)

    def send_in_api(self):
        """
        Отправляет полученные данные в олговремнное хранилище
        """
        configuration = openapi_client.Configuration(host="http://absrent.ru:8000")

        with openapi_client.ApiClient(configuration) as api_client:
            i = 0
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
                    # category="category_example",
                    # category_url="category_url_example",
                    brand=e["brand"],
                    brand_url=e["brand_url"],
                    # day_to_delivery=1,
                    # sku="sku_example",
                    url=e["url"],
                    # canonical_url="canonical_url_example",
                    img_url=e["image_url"],
                    # description="description_example",
                    # params="params_example",
                    # seller="seller_example",
                    # seller_url="seller_url_example",
                    source_url=e["source_url"],
                    # urls_other_products_on_the_page="urls_other_products_on_the_page_example",
                    # worker="worker_example",
                    # task="task_example",
                )  # History |  (optional)

                try:
                    api_response = api_instance.history_create(body=history)
                    i += 1
                    # pprint(api_response)
                except openapi_client.ApiException as e:
                    print("Exception when calling HistoryApi->history_create: %s\n" % e)
                if i % 100 == False:
                    print('i=', i)
            print("Count load object =", len(self.__list_dict))
