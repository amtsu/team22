#!/usr/local/bin/python
# coding: utf-8

from typing import Any, Dict, Optional
from bs4 import BeautifulSoup

import openapi_client
from pprint import pprint
from openapi_client.apis.tags import history_api
from openapi_client.model.history import History

# from openapi_client.model.paginated_history_list import PaginatedHistoryList
# from openapi_client.model.patched_history import PatchedHistory

#from page_parsing import PagePerser
from users.mvandreeva.d221217_2227.page_parsing import PagePerser

"""
Парсер для сайта застройщика 'CapitalGroup', проект 'Триколор'
"""
# def replace_none_to_zero_int(function):
#     def wrapper():
#         if function() == None:
#             # if function() is Optional[int]:
#             return 0
        
# def replace_none_to_zero_str(function):
#     def wrapper():
#         if function() == None:
#             # if function -> Optional[str]:
#             return ""

def none_to_zero(function):
    def wrapper(*args, **kwargs):
        d = function(*args, **kwargs)
        for key in d:
            if d[key] == None:
                if key in ["bulding", "rooms", "floor", "area", "price", "price_sale"]:
                    d[key] = 0
                else:
                    d[key] = ""
        return d
    return wrapper
        
class TricolorParser:
    """
    Собирает данные с сайта https://cg-tricolor.ru/catalog/flats очищает их, сохряняет
    """
    def __init__(self, url: str):
        self.__url = url
        self.__page = PagePerser(self.__url)
        self.__b_soup = self.__page.use_b_soup()
        try:
            self.__items_list = self.__b_soup.findAll("tr", class_="results__tr")
        except:
            print("Error in getting items_list", self.__url)
        self.__dict_list = []  # type: list[dict]
        # self.__dict: Dict[str, Any] = {}
        
    CATEGORY = "Новостройки"
    CEILINGHEIGHT = 3  # здесь написано в тексте https://cg-tricolor.ru/catalog
    COMPLETION_QUARTER = 4  # нашла на циане
    COMPLETION_YEAR = 2015  # нашла на циане
    DEVELOPER = "Capital Group"
    FLOORS_TOTAL_B1 = 58  # нашла на циане
    FLOORS_TOTAL_B2 = 10
    FLOORS_TOTAL_B3 = 58
    FLOORS_TOTAL_B4 = 38

    @none_to_zero
    def _fill_dict(self, item: object) -> dict:
        """
        Метод наполняет данными словарь
        """
        item_dict = (
            {}
        )  # приходится копировать словарь и все наполнение в аналогичный метод class TricolorParserFFile(TricolorParser)
        # item_dict["quantity"] = 1
        item_dict["bulding"] = self._get_bulding(item)
        bulding_str = str(item_dict["bulding"])
        item_dict["title"] = self._get_title(item) + bulding_str
        if item_dict["title"]:
            rooms = item_dict["title"][0]
            item_dict["rooms"] = int(rooms)
        else:
            item_dict["rooms"] = None
        item_dict["floor"] = self._get_floor(item)
        item_dict["area"] = self._get_square(item)
        item_dict["price"] = self._get_price(item)
        item_dict["url"] = self._get_item_url(item)
        item_dict["project"] = self._get_project()
        item_dict["full_address"] = self._get_address()
        # item_dict["address"] = "Проспект Мира, 188Б"
        # item_dict["city"] = "Москва"
        item_dict["brand"] = self.DEVELOPER
        item_dict["brand_url"] = "https://capitalgroup.ru/"
        item_dict["category"] = self.CATEGORY
        item_dict["price_sale"] = item_dict["price"]
        # item_dict["datetime_create"] = "1970-01-01T00:00:00.00Z"
        item_dict["plan"] = self._get_plan(item)
        # item_dict["description"] = json.dumps(e["specialmortgageoffer_set"])
        item_dict[
            "apartment_completion_quarter"
        ] = self.COMPLETION_QUARTER  # нашла на циане
        item_dict["apartment_completion_year"] = self.COMPLETION_YEAR  # нашла на циане
        item_dict[
            "apartment_ceilingheight"
        ] = self.CEILINGHEIGHT  # здесь написано в тексте https://cg-tricolor.ru/catalog

        if item_dict["bulding"] == 1:
            item_dict["apartment_floors_total"] = self.FLOORS_TOTAL_B1
        elif item_dict["bulding"] == 2:
            item_dict["apartment_floors_total"] = self.FLOORS_TOTAL_B2
        elif item_dict["bulding"] == 3:
            item_dict["apartment_floors_total"] = self.FLOORS_TOTAL_B3
        elif item_dict["bulding"] == 4:
            item_dict["apartment_floors_total"] = self.FLOORS_TOTAL_B4

        if item_dict["price"] and item_dict["area"]:
            apartment_ppm = item_dict["price"] / item_dict["area"]
            item_dict["apartment_ppm"] = int(round(apartment_ppm, 0))
        else:
            item_dict["apartment_ppm"] = 0
        # item_dict["apartment_location"] = e["location"]
        # item_dict["apartment_location_lat"] = e["location"].split(',')[0][:9]
        # item_dict["apartment_location_lon"] = e["location"].split(',')[1][:9]
        return item_dict

    # @replace_none_to_zero_str
    def _get_address(self) -> Optional[str]:
        """
        Получает адрес ЖК
        """
        try:
            # print(self.__b_soup)
            address_data = self.__b_soup.findAll("div", class_="site-nav site-nav--tel")
            # print(address_data)
            address_bad = address_data[0].text
            address_bad = address_bad.replace("\n", "")
            address_bad = address_bad.replace(
                "                            +7 (495) 771 77 52                        ",
                "",
            )
            address = address_bad.strip()
            # pprint(address_bad)
        except:
            print("Error in getting address")  # , self.__url)
            address = None
        return address

    # @replace_none_to_zero_int
    def _get_bulding(self, item: object) -> Optional[int]:
        """
        Получает номер корпуса
        """
        flat_data = item.findAll("td")
        if flat_data:
            building_str = flat_data[0].text
            building = int(building_str)
        else:
            building = None
        return building

    def get_dict_list(self) -> list:
        """
        Формирует список словарей с данными по квартирам
        """
        # if not self.__items_list == []: # нужна ли проверка?

        for item in self.__items_list:
            item_dict = self._fill_dict(item)
            item_dict[
                "source_url"
            ] = self.__url  # Вывела отдельно, чтоб не было ошибки при наследовании
            self.__dict_list.append(item_dict)
        return self.__dict_list

    # @replace_none_to_zero_int
    def _get_floor(self, item: object) -> Optional[int]:
        """
        Получает этаж 
        """
        flat_data = item.findAll("td")
        if flat_data:
            floor_str = flat_data[1].text
            floor = int(floor_str)
        else:
            floor = None
        return floor

    # @replace_none_to_zero_str
    def _get_item_url(self, item: object) -> Optional[str]: 
        """
        Получает URL для конкретой квартиры 
        """
        flat_data = item.findAll("a", class_="results__link")
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

    # @replace_none_to_zero_str
    def _get_plan(self, item: object) -> Optional[str]:
        """
        Получает ссылку на план конкретой квартиры 
        """
        plan_data = item.findAll("img")
        if plan_data:
            plan = plan_data[0]["src"]
        else:
            plan = None
        return plan

    def _get_price(self, item: object) -> Optional[int]:
        """
        Получает цену квартиры 
        """
        flat_data = item.findAll("td")
        if flat_data:
            price_data = flat_data[3].text
            # print(price_data)
            price_bad = price_data.replace("\n","")
            price_bad = price_bad.replace(" ", "")
            price_bad = price_bad.replace("руб.", "")
            price_bad = price_bad[:8]
            price = int(price_bad)
        else:
            price = None
        return price
    
    # @replace_none_to_zero_str
    def _get_project(self)-> Optional[str]:
        """
        Получает название проекта 
        """
        try:
            project_data = self.__b_soup.findAll("div", class_="site-aside__container")
            # pprint(project_data)
            project_bad = project_data[0].text
            project = project_bad[-9:-1]
            # pprint(project)
        except:
            print("Error in getting project name")  # , self.__url)
            project = None
        return project

    # def _det_rooms_data(self, item: object) -> int: # добавлю в _get_title(), т.к. есть только в title

    # @replace_none_to_zero_int
    def _get_square(self, item: object) -> Optional[int]:
        """
        Получает площадь квартиры 
        """
        flat_data = item.findAll("td")
        if flat_data:
            square_str = flat_data[2].text
            square = int(square_str)
        else:
            square = None
        return square

    # @replace_none_to_zero_str
    def _get_title_flat_page(self, item: object) -> Optional[str]: # не используется
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

    # @replace_none_to_zero_str
    def _get_title(self, item: object) -> Optional[str]:
        """
        Метод получает наименование квартиры из всплывающего окна страницы со списком квартир
        """
        title_data = item.findAll("div")
        # print(title_data)
        if title_data:
            title = title_data[2].text
            # print(title)
        else:
            title = None
        return title

    def send_to_api(self):
        """
        Формирует API для отправки в БД
        """
        configuration = openapi_client.Configuration(host="http://absrent.ru:8000")

        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = history_api.HistoryApi(api_client)
            for e in self.__dict_list:
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
                    img_url=e["plan"],
                    # description=e["description"],
                    # params="params_example",
                    # seller="seller_example",
                    # seller_url="seller_url_example",
                    source_url=e["source_url"],
                    apartment_area=e["area"],
                    apartment_completion_quarter=e["apartment_completion_quarter"],
                    apartment_completion_year=e["apartment_completion_year"],
                    apartment_floor=e["floor"],
                    apartment_floors_total=e["apartment_floors_total"],
                    apartment_ceilingheight=e["apartment_ceilingheight"],
                    apartment_room=e["rooms"],
                    apartment_ppm=e["apartment_ppm"],
                    # apartment_address = e["city"] + ", " + e["address"],
                    apartment_address=e["full_address"],
                    # apartment_location=e["apartment_location"],
                    # apartment_location_lat=e["apartment_location_lat"],
                    # apartment_location_lon=e["apartment_location_lon"],
                )  # History |  (optional)

                try:
                    api_response = api_instance.history_create(body=history)
                    # pprint(api_response)
                except openapi_client.ApiException as e:
                    print("Exception when calling HistoryApi->history_create: %s\n" % e)
            print("Count load object =", len(self.__dict_list))


class TricolorParserFFile(TricolorParser):
    """
    Собирает данные страницы, скачанной с сайта https://cg-tricolor.ru/catalog/flats в файл 'sources/tricolor' очищает их, сохряняет
    """

    def __init__(self, page_text):
        self.__url = None
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")
        self.__items_list = self.__b_soup.findAll("tr", class_="results__tr")
        self.__dict_list = []

    # @replace_none_to_zero_str
    def _get_address(self) -> Optional[str]:
        """
        Получает адрес ЖК
        """
        try:
            # print(self.__b_soup)
            address_data = self.__b_soup.findAll("div", class_="site-nav site-nav--tel")
            # print(address_data)
            address_bad = address_data[0].text
            address_bad = address_bad.replace("\n", "")
            address_bad = address_bad.replace(
                "                            +7 (495) 771 77 52                        ",
                "",
            )
            address = address_bad.strip()
            # pprint(address_bad)
        except:
            print("Error in getting address")  # , self.__url)
            address = None
        return address

    def get_dict_list(self) -> list:
        """
        Формирует список словарей с данными по квартирам
        """
        if self.__items_list:
            for item in self.__items_list:
                item_dict = self._fill_dict(item)
                item_dict[
                    "source_url"
                ] = self.__url  # Вывела отдельно, чтоб не было ошибки при наследовании
                self.__dict_list.append(item_dict)
            return self.__dict_list
        else:
            print("Error in getting Items List")

    # @replace_none_to_zero_str
    def _get_project(self):
        """
        Получает название проекта 
        """
        try:
            project_data = self.__b_soup.findAll("div", class_="site-aside__container")
            # pprint(project_data)
            project_bad = project_data[0].text
            project = project_bad[-9:-1]
            # pprint(project)
        except:
            print("Error in getting project name")  # , self.__url)
            project = None
        return project
