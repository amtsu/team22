#!/usr/local/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib
import urllib.request

import openapi_client
from pprint import pprint
from openapi_client.apis.tags import history_api
from openapi_client.model.history import History
from openapi_client.model.paginated_history_list import PaginatedHistoryList
from openapi_client.model.patched_history import PatchedHistory

from typing import Any, Dict, Optional

from page_parsing import PagePerser

"""
Парсер для сайта застройщика 'ГАЛС'
"""
# def none_to_zero(function):
#     def wrapper(*args, **kwargs):
#         d = function(*args, **kwargs)
#         for key in d:
#             if d[key] == None:
#                 if key in ["bulding", "rooms", "floor", "area", "price", "price_sale"]:
#                     d[key] = 0
#                 else:
#                     d[key] = ""
#         return d
#     return wrapper
        
class HALSParser:
    """
    Собирает данные с сайта https://hals-development.ru/realty/residential по всем запущенным проектам очищает их, сохряняет
    """
    def __init__(self, url: str):
        self.__url = url
        self.__page = PagePerser(self.__url)
        self.__b_soup = self.__page.use_b_soup()
        try:
            self.__project_list = self.__b_soup.findAll("div", class_ = "index__projects__item")
            # print(self.__project_list)
        except:
            print("Error in getting projects_list", self.__url)
        # try:
        #     self.__items_list = self.__b_soup.findAll("a", class_="grid-item grid-item2")
        # except:
        #     print("Error in getting items_list", self.__url)
        # self.__dict_list = []  # type: list[dict]
        
    BRAND_URL = "https://hals-development.ru"
    CATEGORY = "Новостройки"
#     CEILINGHEIGHT = 3  # здесь написано в тексте https://cg-tricolor.ru/catalog
    # CITY = "Москва"
    COMPLETION_QUARTER_KOSMO = 4  # на дом.pa
    COMPLETION_YEAR_KOSMO = 2024  # на дом.pa
#     DEVELOPER = "Capital Group"
#     FLOORS_TOTAL_B1 = 58  # нашла на циане
#     FLOORS_TOTAL_B2 = 10
#     FLOORS_TOTAL_B3 = 58
#     FLOORS_TOTAL_B4 = 38

#     @none_to_zero
    def _fill_dict(self, item: object, item_dict: dict) -> dict:
        """
        Метод наполняет данными словарь
        """
        item_dict["quantity"] = 1
        item_dict["bulding"] = self._get_bulding(item)
        item_dict["title"] = self._get_title(item)
        item_dict["rooms"] = self._get_rooms(item)
        item_dict["floor"] = self._get_floor(item)
        item_dict["area"] = self._get_square(item)
        item_dict["price"] = self._get_price(item)
        item_dict["url"] = self._get_item_url(item)
        item_dict["category"] = self.CATEGORY
        item_dict["price_sale"] = item_dict["price"]
        item_dict["plan"] = self._get_plan(item)
        item_dict[
            "apartment_completion_quarter"
        ] = self.COMPLETION_QUARTER_KOSMO  # на дом.pa
        item_dict["apartment_completion_year"] = self.COMPLETION_YEAR_KOSMO  # на дом.pa
        item_dict[
            "apartment_ceilingheight"
        ] = self._get_ceilingheight(item_dict["url"])  

#         if item_dict["bulding"] == 1:
#             item_dict["apartment_floors_total"] = self.FLOORS_TOTAL_B1
#         elif item_dict["bulding"] == 2:
#             item_dict["apartment_floors_total"] = self.FLOORS_TOTAL_B2
#         elif item_dict["bulding"] == 3:
#             item_dict["apartment_floors_total"] = self.FLOORS_TOTAL_B3
#         elif item_dict["bulding"] == 4:
#             item_dict["apartment_floors_total"] = self.FLOORS_TOTAL_B4

        if item_dict["price"] and item_dict["area"]:
            apartment_ppm = item_dict["price"] / item_dict["area"]
            item_dict["apartment_ppm"] = int(round(apartment_ppm, 0))
        else:
            item_dict["apartment_ppm"] = 0
        # item_dict["datetime_create"] = "1970-01-01T00:00:00.00Z"
#         # item_dict["apartment_location"] = e["location"]
#         # item_dict["apartment_location_lat"] = e["location"].split(',')[0][:9]
#         # item_dict["apartment_location_lon"] = e["location"].split(',')[1][:9]
        return item_dict

    def _get_address(self, project: object) -> Optional[str]:
        """
        Получает адрес ЖК
        """
        address_data = project.findAll("div", class_ = "index__projects__dop-info--metro")
        if address_data:
            address_bad = address_data[0].text
            address_bad = address_bad.replace("&nbsp;", "")
            address = address_bad.strip()
        else:
            print("Error in getting address")  
            address = None
        return address
    

    def _get_brand(self) -> Optional[str]:
        """
        Получает наименование застройщика
        """
        footer_data = self.__b_soup.findAll("div", class_ = "footer2-copy")
        if footer_data:
            for data in footer_data:
                brand_data = data.find("div")
                brand_bad = brand_data.text
                cut_begin = brand_bad.find(",")
                cut_stop = brand_bad.find(".")
                brand_bad = brand_bad[cut_begin:cut_stop]
                brand_bad = brand_bad.replace(",", "")
                brand = brand_bad.strip()
        else:
            print("Error in getting brand")  
            brand = None
        return brand
            
                
    def _get_bulding(self, item: object) -> Optional[int]:
        """
        Получает номер корпуса
        """
        flat_data = item.findAll("div", class_ = "grid-item2__info")
        if flat_data:
            building_data = flat_data[0].text
            if not building_data.find("Река") == -1: # Проект Космо 4/22 # нужно прописывать условия для новых проектов
                building = 8
            elif not building_data.find("Сад") == -1: # Проект Космо 4/22
                building = 9
            elif not building_data.find("Секция") == -1: # Проект Театральный дом
                building = 1
            else:
                print("New project started. class HALSParser _get_building method needs review")
        else:
            print("Error in getting building")  
            building = None
        return building
    
    def _get_ceilingheight(self, item_dict_url: str) -> Optional[int]:
        page = PagePerser(item_dict_url)
        b_soup = page.use_b_soup()
        try:
            ceil_data = b_soup.findAll("div", class_="realty-flat__options2")
            for data in ceil_data:
                if not data.find("Высота потолка, м") == -1:
                    ceil_d = data.findAll("div")
                    ceil_bad = ceil_d.text
                    ceil_bad = ceil_bad.replace(",",".")
                    ceilingheight = float(ceil_bad)
        except:
            print("Error in getting ceilingheight")
            ceilingheight = None
    
    # def _get_completion_data(self, b_soup: object) -> Optional[int]: # думала спарсить с дом.рф через кнопку "Документы", но она есть только на космо
# решила пока отложить
    #     project_data = b_soup.findAll("a", class_ = "obj-panel__item")
    #     for data in project_data:
    #         is_doc = data.find("Документы")
    #         if not is_doc == -1:
    #             doc_url = data[0]["href"]
    #             doc_page = PagePerser(doc_url)
    #             b_soup = doc_page.use_b_soup()
    #             try:
    #                 compl_data = b_soup.findAll("div", class_="styles__Value-sc-13pfgqd-2 hVswsH")
    #                 for data in compl_data:
    #                     if data.find(" кв. "):
    #                         compl_text = data.text
    #                         cut_stop = compl_text.find(" кв.")
    #                         compl_q = compl_text[:cut_stop]
    #                         compl_y = compl_text[-4:]
    #             except:
    #                 print("Error in getting items_list", project_url)

    def _get_description(self, project: object)-> Optional[str]:
        """
        Получает описания проекта 
        """
        project_data = project.findAll("div", class_ = "index__projects__title")
        for data in project_data:
            project_bad = data.findAll("div")
        # pprint(project_data)
            if project_bad:
                # print("=============================")
                description_bad = project_bad[1].text
                description = description_bad.replace("\xa0","")
                # print(project)
            else:
                description = None
                print("Error in getting description")
        return description

    def get_dict_list(self) -> list:
        """
        Формирует список словарей с данными по квартирам
        """
        self.__dict_list = []
        brand_name = self._get_brand()
        for project in self.__project_list:
            item_dict = {}
            item_dict["project"] = self._get_project(project)
            item_dict["description"] = self._get_description(project)
            item_dict["full_address"] = self._get_address(project)
            item_dict["brand"] = brand_name
            item_dict["brand_url"] = self.BRAND_URL
            project_url = self._get_project_url(project)
            page = PagePerser(project_url)
            b_soup = page.use_b_soup()
            try:
                items_list = b_soup.findAll("a", class_="grid-item grid-item2")
            except:
                print("Error in getting items_list", project_url)
            for item in items_list: # парсит одну квартиру(наверно перезаписывает данные в словаре)
                item_dict = self._fill_dict(item, item_dict)
                item_dict[
                    "source_url"
                ] = self.__url  # какой указывать - на застройщика или на проект?
                self.__dict_list.append(item_dict)

#                 self.__dict_list.append(item_dict)
        # return self.__dict_list
            # print(item_dict)
            # return item_dict
        
        return self.__dict_list

    def _get_floor(self, item: object) -> Optional[int]:
        """
        Получает этаж 
        """
        flat_data = item.findAll("div", class_ = "grid-item2__info")
        if flat_data:
            floor_data = flat_data[0].text
            cut_begin = floor_data.rfind("/")
            cut_stop = floor_data.find("э",cut_begin)
            floor_bad = floor_data[cut_begin:cut_stop]
            # cut_begin = floor_bad.find("/")
            floor_bad = floor_bad.replace("/","")
            floor_bad = floor_bad.strip()
            floor = int(floor_bad)
        else:
            print("Error in getting floor")
            floor = None
        return floor

    def _get_item_url(self, item: object) -> Optional[str]: 
        """
        Получает URL для конкретой квартиры 
        """
        flat_data = item.findAll("a", class_ = "grid-item grid-item2")
        print(flat_data)
        if flat_data:
            link = flat_data[0]["href"]
            item_url = "https://hals-development.ru" + link
        else:
            print("Error in getting item_url")
            item_url = None
        return item_url

    def _get_plan(self, item: object) -> Optional[str]:
        """
        Получает ссылку на план конкретой квартиры 
        """
        plan_data = item.findAll("span", class_ = "grid-item__image__plan")
        if plan_data:
            plan_bad = plan_data[0]["style"]
            cut_begin = plan_bad.find("(")
            plan_bad = plan_bad[cut_begin:]
            plan_bad = plan_bad.replace("(","")
            plan = plan_bad.replace(")","")
        else:
            print("Error in getting plan")
            plan = None
        return plan

    def _get_price(self, item: object) -> Optional[int]:
        """
        Получает цену квартиры 
        """
        price_data = item.findAll("div", class_ = "default-price")
        if price_data:
            price_bad = price_data[0].text
            # print(price_bad)
            price_bad = price_bad.replace(" ", "")
            price_bad = price_bad.replace("₽", "")
            price = int(price_bad)
        else:
            print("Error in getting price")
            price = None
        return price
    
    def _get_project(self, project: object)-> Optional[str]:
        """
        Получает название проекта 
        """
        project_data = project.findAll("div", class_ = "index__projects__title")
        for data in project_data:
            project_bad = data.findAll("div")
        # pprint(project_data)
            if project_bad:
                # print("=============================")
                project = project_bad[0].text
                # print(project)
            else:
                print("Error in getting project")
                project = None
        return project
    
    def _get_project_url(self, project: object)-> Optional[str]:
        """
        Получает URL проекта 
        """
        project_data = project.findAll("a", class_ = "index__projects__img")
        if project_data:
            project_ref = project_data[0]["href"]
            project_url = "https://hals-development.ru" + project_ref
            # pprint(project_url)
        else:
            print("Error in getting project_url")
            project_url = None    
        return project_url

    def _get_rooms(self, item: object) -> Optional[int]:
        """
        Получает количество комнат 
        """
        flat_data = item.findAll("div", class_ = "grid-item2__info2")
        # print(flat_data)
        if flat_data:
            data_full = flat_data[0].text
            # print(data_full)
            # print("++++++++++++++++++++++++++++++++++")
            rooms_bad = data_full[0]
            # print(square_bad)
            # print("++++++++++++++++++++++++++++++++++")
            # square_bad = square_bad.replace('"','')
            # square_bad = square_bad.replace('/','')
            # square_bad = square_bad.replace(' ','')
            # square_bad = square_bad.replace(',','.')
            # print(square_bad)
            rooms = int(rooms_bad)
        else:
            print("Error in getting rooms")
            rooms = None
        return rooms

    def _get_square(self, item: object) -> Optional[int]:
        """
        Получает площадь квартиры 
        """
        flat_data = item.findAll("div", class_ = "grid-item2__info2")
        # print(flat_data)
        if flat_data:
            data_full = flat_data[0].text
            # print(data_full)
            # print("++++++++++++++++++++++++++++++++++")
            cut_begin = data_full.find("/")
            cut_stop = data_full.find("м",cut_begin)
            square_bad = data_full[cut_begin:cut_stop]
            # print(square_bad)
            # print("++++++++++++++++++++++++++++++++++")
            square_bad = square_bad.replace('"','')
            square_bad = square_bad.replace('/','')
            square_bad = square_bad.replace(' ','')
            square_bad = square_bad.replace(',','.')
            # print(square_bad)
            square = float(square_bad)
        else:
            print("Error in getting square")
            square = None
        return square

    def _get_title(self, item: object) -> Optional[str]:
        """
        Метод получает наименование квартиры со страницы со списком квартир
        """
        title_data = item.findAll("div", class_ = "grid-item2__info")
        # print(title_data)
        if title_data:
            title_bad = title_data[0].text
            title_bad = title_bad.replace("\n","")
            title_bad = title_bad.replace(" /",",")
            title = title_bad.replace('"','')
            # print(title)
        else:
            print("Error in getting title")
            title = None
        return title

#     def send_to_api(self):
#         """
#         Формирует API для отправки в БД
#         """
#         configuration = openapi_client.Configuration(host="http://absrent.ru:8000")

#         with openapi_client.ApiClient(configuration) as api_client:
#             api_instance = history_api.HistoryApi(api_client)
#             for e in self.__dict_list:
#                 # print(e)
#                 history = History(
#                     pk=1,
#                     title=e["title"],
#                     quantity=1,
#                     price=str(e["price"]),
#                     price_sale=str(e["price_sale"]),
#                     datetime_create="1970-01-01T00:00:00.00Z",
#                     # score="-807",
#                     # count_comments=1,
#                     # count_likes=1,
#                     # count_stars_all=1,
#                     # count_stars_1=1,
#                     # count_stars_2=1,
#                     # count_stars_3=1,
#                     # count_stars_4=1,
#                     # count_stars_5=1,
#                     # count_how_much_buy=1,
#                     # count_questions=1,
#                     # count_photo=1,
#                     category=e["category"],
#                     # category_url="category_url_example",
#                     brand=e["brand"],
#                     brand_url=e["brand_url"],
#                     # day_to_delivery=1,
#                     # sku="sku_example",
#                     url=e["url"],
#                     # canonical_url="canonical_url_example",
#                     img_url=e["plan"],
#                     # description=e["description"],
#                     # params="params_example",
#                     # seller="seller_example",
#                     # seller_url="seller_url_example",
#                     source_url=e["source_url"],
#                     apartment_area=e["area"],
#                     apartment_completion_quarter=e["apartment_completion_quarter"],
#                     apartment_completion_year=e["apartment_completion_year"],
#                     apartment_floor=e["floor"],
#                     apartment_floors_total=e["apartment_floors_total"],
#                     apartment_ceilingheight=e["apartment_ceilingheight"],
#                     apartment_room=e["rooms"],
#                     apartment_ppm=e["apartment_ppm"],
#                     apartment_address = e["full_address"],
#                     # apartment_location=e["apartment_location"],
#                     # apartment_location_lat=e["apartment_location_lat"],
#                     # apartment_location_lon=e["apartment_location_lon"],
#                 )  # History |  (optional)

#                 try:
#                     api_response = api_instance.history_create(body=history)
#                     # pprint(api_response)
#                 except openapi_client.ApiException as e:
#                     print("Exception when calling HistoryApi->history_create: %s\n" % e)
#             print("Count load object =", len(self.__dict_list))


# class TricolorParserFFile(TricolorParser):
#     """
#     Собирает данные страницы, скачанной с сайта https://cg-tricolor.ru/catalog/flats в файл 'sources/tricolor' очищает их, сохряняет
#     """

#     def __init__(self, page_text):
#         self.__url = None
#         self.__b_soup = BeautifulSoup(page_text, features="html.parser")
#         self.__items_list = self.__b_soup.findAll("tr", class_="results__tr")
#         self.__dict_list = []

#     # @replace_none_to_zero_str
#     def _get_address(self) -> Optional[str]:
#         """
#         Получает адрес ЖК
#         """
#         try:
#             # print(self.__b_soup)
#             address_data = self.__b_soup.findAll("div", class_="site-nav site-nav--tel")
#             # print(address_data)
#             address_bad = address_data[0].text
#             address_bad = address_bad.replace("\n", "")
#             address_bad = address_bad.replace(
#                 "                            +7 (495) 771 77 52                        ",
#                 "",
#             )
#             address = address_bad.strip()
#             # pprint(address_bad)
#         except:
#             print("Error in getting address")  # , self.__url)
#             address = None
#         return address

#     def get_dict_list(self) -> list:
#         """
#         Формирует список словарей с данными по квартирам
#         """
#         if self.__items_list:
#             for item in self.__items_list:
#                 item_dict = self._fill_dict(item)
#                 item_dict[
#                     "source_url"
#                 ] = self.__url  # Вывела отдельно, чтоб не было ошибки при наследовании
#                 self.__dict_list.append(item_dict)
#             return self.__dict_list
#         else:
#             print("Error in getting Items List")

#     # @replace_none_to_zero_str
#     def _get_project(self):
#         """
#         Получает название проекта 
#         """
#         try:
#             project_data = self.__b_soup.findAll("div", class_="site-aside__container")
#             # pprint(project_data)
#             project_bad = project_data[0].text
#             project = project_bad[-9:-1]
#             # pprint(project)
#         except:
#             print("Error in getting project name")  # , self.__url)
#             project = None
#         return project
