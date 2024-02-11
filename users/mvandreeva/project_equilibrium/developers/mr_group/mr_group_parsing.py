#!/usr/local/bin/python
# coding: utf-8
"""
Парсер для сайта 'наш.дом.рф' - 
"""
import urllib
import urllib.request
from pprint import pprint
from geopy.geocoders import Nominatim #Подключаем библиотеку
from typing import Optional
from bs4 import BeautifulSoup

import openapi_client 
# from pprint import pprint
from openapi_client.apis.tags import history_api 
from openapi_client.model.history import History 
from openapi_client.model.paginated_history_list import PaginatedHistoryList 
from openapi_client.model.patched_history import PatchedHistory  

from page_parsing import PageParser

# def none_to_zero(function):
#     """
#     Декоратор для перевода значений None в '0' или ''
#     """
#     def wrapper(*args, **kwargs):
#         data_dict = function(*args, **kwargs)
#         for key in data_dict:
#             if data_dict[key] is None:
#                 if key in [
#                     "bulding",
#                     "rooms",
#                     "floor",
#                     "area",
#                     "price",
#                     "price_sale",
#                     "apartment_ceilingheight",
#                     "apartment_ppm",
#                     "apartment_floors_total",
#                 ]:
#                     data_dict[key] = 0
#                 else:
#                     data_dict[key] = ""
#                 # print(key, "is None")
#         return data_dict
#     return wrapper



class MRGroupParser:
    """
    Получает данные с сайта "https://www.mr-group.ru/flats/"
    """
    def __init__(self, url: str):
        self.__url = url
        self.__page = PageParser(self.__url)
        self.__b_soup = self.__page.use_b_soup()
        self.__projects_list = self.__b_soup.findAll(
            "li", class_ = "search-list-item js-search-list-item dataLayerFlatCard"
        )
        if not self.__projects_list:
            print("Error in getting projects_list", self.__url)
        self.__dict_list = []
        
    # @none_to_zero
    # def _fill_dict(self, item: object, item_dict: dict) -> dict:
    #     """
    #     Метод наполняет данными словарь
    #     """
    #     item_dict["quantity"] = 1
#         item_dict["rooms"] = self._get_rooms(item)
#         
#         item_dict["price"] = self._get_price(item)
#         item_dict["url"] = self._get_item_url(item)
#         item_dict["category"] = self.CATEGORY
#         item_dict["price_sale"] = item_dict["price"]
#         item_dict["plan"] = self._get_plan(item)
#         one_item_url = item_dict["url"]
#         item_dict["apartment_ceilingheight"] = self._get_ceilingheight(one_item_url)
#         if item_dict["project"] == "Космо 4/22":
#             item_dict[
#                 "apartment_floors_total"
#             ] = (
#                 self.FLOORS_TOTAL_K
#             )  # нужно дополнять условия, если появятся данные в других ЖК!!!!!!!
#         else:
#             item_dict["apartment_floors_total"] = None
#         if item_dict["price"] and item_dict["area"]:
#             apartment_ppm = item_dict["price"] / item_dict["area"]
#             item_dict["apartment_ppm"] = int(round(apartment_ppm, 0))
#         else:
#             item_dict["apartment_ppm"] = None
#         if (
#             item_dict["project"] == "Космо 4/22"
#         ):  # Нужно добавлять условия для других проектов по мере их запуска
#             if item_dict["bulding"] == 8:
#                 item_dict["apartment_location"] = self.LOCATION_K_8
#             elif item_dict["bulding"] == 9:
#                 item_dict["apartment_location"] = self.LOCATION_K_8
#             item_dict["apartment_location_lat"] = item_dict["apartment_location"].split(
#                 ","
#             )[0][:9]
#             item_dict["apartment_location_lon"] = item_dict["apartment_location"].split(
#                 ","
#             )[1][:9]
#         else:
#             item_dict["apartment_location_lat"] = None
#             item_dict["apartment_location_lon"] = None
#         return item_dict

#     def _get_address(self, project: object) -> Optional[str]:
#         """
#         Получает адрес ЖК
#         """
#         address_data = project.findAll("span", class_ = "styles__Ellipsis-sc-1fw79ul-0 jYMONF styles__Value-sc-1ajig0k-5 styles__Label-sc-1ajig0k-6 styles__AddressLabel-sc-1ajig0k-7 lodXEI ewpwAU kLIuVv")
#         if address_data:
#             address_bad = address_data[0].text
#             address = address_bad.strip()
#         else:
#             print("Error in getting address")
#             address = None
#         return address
    
    def _get_area(self, item: object) -> Optional[float]:
        """
        Получает площадь квартиры
        """
        flat_data = item.findAll("span", class_="_with-sup js-booking-area")
        if flat_data:
            data_full = flat_data[0].text
            cut_stop = data_full.find("м")
            area_bad = data_full[:cut_stop]
            area = float(area_bad)
        else:
            print("Error in getting area")
            area = None
        return area

    def _get_brand(self, project: object) -> Optional[str]:
        """
        Получает наименование застройщика
        """
        footer_data = self.__b_soup.findAll("div", class_="footer-copyright")
        if footer_data:
            # for data in footer_data:
            brand_bad = footer_data[0].text
            cut_begin = brand_bad.find(" ")
            cut_stop = brand_bad.find(" 2023")
            brand_bad = brand_bad[cut_begin:cut_stop]
            brand = brand_bad.strip()
        else:
            print("Error in getting brand")
            brand = None
        return brand


    def _get_bulding(self, project: object) -> Optional[int]: # Обозначается словами, а не цифрами
        """
        Получает данные корпуса
        """
        flat_data = project.find("div", class_ = "title-group-container")
        building_data = data.findAll("span")
        if building_data:
            building_name = building_data[0].text
            building = building_name.strip()
        else:
            print("Error in getting building")
            building = None
        return building

#     def _get_ceilingheight(self, one_item_url: str) -> Optional[float]:
#         """
#         Получает высоту потолков (только онлайн)
#         """
#         page = PagePerser(one_item_url)
#         b_soup = page.use_b_soup()
#         full_data = b_soup.findAll("div", class_="realty-flat__options2")
#         if full_data:
#             for data in full_data:
#                 c_data = data.findAll("div")
#                 for data in c_data:
#                     # pprint(data)
#                     d_text = data.text
#                     f_text = d_text.find("Высота потолка, м")
#                     # print(f_text)
#                     if not f_text == -1:
#                         c_div = data.findAll("div")
#                         # pprint(c_div)
#                         ceil_bad = c_div[0].text
#                         # pprint(ceil_bad)
#                         ceil_bad = ceil_bad.replace(",", ".")
#                         ceil_bad = ceil_bad.replace("до ", "")
#                         # pprint(ceil_bad)
#                         ceilingheight = float(ceil_bad)
#                         # pprint(ceilingheight)
#                     # else:
#                     #     continue
#             return ceilingheight
#         else:
#             print("Error in getting ceilingheight")
#             ceilingheight = None
#             return ceilingheight

    def _get_completion_data(self, project: object) -> Optional[int]: 
        completion_data = project.findAll("span", class_ = "_release")
        if completion_data:
            completion_text = completion_data[0].text
            q_cut_stop = completion_text.find(" кв")
            completion_quarter_bad = completion_text[:q_cut_stop]
            completion_quarter_bad = completion_quarter_bad.strip()
            completion_quarter = int(completion_quarter_bad)
            y_cut_start = completion_text.find("20") # наверно можно как-то универсальнее подойти
            y_cut_stop = completion_text.rfind(" г.")
            completion_year_bad = completion_text[y_cut_start:y_cut_stop]
            completion_year_bad = completion_year_bad.strip()
            completion_year = int(completion_year_bad)
            completion_data = [completion_quarter, completion_year]
        else:
            print("Error in getting completion_data")
            completion_data = None
        return completion_data

#     def _get_description(self, project: object) -> Optional[str]:
#         """
#         Получает описания проекта
#         """
#         project_data = project.findAll("div", class_="index__projects__title")
#         for data in project_data:
#             project_bad = data.findAll("div")
#             # pprint(project_data)
#             if project_bad:
#                 # print("=============================")
#                 description_bad = project_bad[1].text
#                 description = description_bad.replace("\xa0", "")
#                 # print(project)
#             else:
#                 description = None
#                 print("Error in getting description")
#         return description

    def get_dict_list(self) -> list:
        """
        Формирует список словарей с данными по квартирам
        """
        for project in self.__projects_list:
            item_dict = {}
            item_dict["apartment_area"] = self._get_area(project)
#             item_dict["title"] = self._get_title(project) # перепутала с проджект для наш.дом
            item_dict["project"] = self._get_project(project)
            item_dict["brand"] = self._get_brand(project)
            item_dict["bulding"] = self._get_bulding(project)
# #             item_dict["description"] = self._get_description(project)
#             item_dict["apartment_address"] = self._get_address(project)
#             item_dict["apartment_floors_total"] = self._get_floors_total(project)
            apartment_completion_data = self._get_completion_data(project)
            item_dict[
                "apartment_completion_quarter"
            ] = apartment_completion_data[0]
            item_dict[
                "apartment_completion_year"
            ] = apartment_completion_data[1]
            item_dict["floor"] = self._get_floor(project)
#             item_dict["apartment_status"] = self._get_status(project)
#             item_dict["brand_url"] = self.BRAND_URL
#             # if project == 'Космо 4/22':
#             #     item_dict["apartment_floors_total"] = self.FLOORS_TOTAL_K
#             project_url = self._get_project_url(project)
#             page = PagePerser(project_url)
#             b_soup = page.use_b_soup()
#             items_list = b_soup.findAll("a", class_="grid-item grid-item2")
#             if not items_list:
#                 print("Error in getting items_list", project_url)
#             for (
#                 item
#             ) in (
#                 items_list
#             ):  
                # item_dict = self._fill_dict(item, item_dict)

# !!!!!!!!!!Изменила отступ, ближе влево!!!!!!!!!!
            item_dict[
                "source_url"
            ] = self.__url  
            self.__dict_list.append(item_dict)
#         # pprint(self.__dict_list) # проблема распечатки (кодировки)
        return self.__dict_list

#     def _get_floors_total(self, project: object) -> Optional[int]:
#         """
#         Получает количество этажей
#         """
#         floors_data = project.findAll("span", class_="styles__Ellipsis-sc-1fw79ul-0 jYMONF styles__Value-sc-1ajig0k-5 lodXEI")
#         if floors_data:
#             floors_total = floors_data[0].text
#             cut_stop = floors_total.find("э")
#             floors_bad = floors_total[:cut_stop]
#             floors_bad = floors_bad.strip()
#             floors = int(floors_bad)
#         else:
#             print("Error in getting floor")
#             floors = None
#         return floors

    def _get_floor(self, project: object) -> Optional[int]:
        """
        Получает этаж
        """
        flat_data = project.findAll("div", class_="item-info-second-row")
        floor_data = flat_data.findAll("span")
        if floor_data:
            floor_bad = floor_data[0].text
            cut_stop = floor_bad.find("э")
            floor_bad = floor_data[:cut_stop]
            floor_bad = floor_bad.strip()
            floor = int(floor_bad)
        else:
            print("Error in getting floor")
            floor = None
        return floor

#     def _get_item_url(self, item: object) -> Optional[str]:
#         """
#         Получает URL для конкретой квартиры
#         """
#         link = item["href"]
#         item_url = "https://hals-development.ru" + link
#         return item_url
    
#     def _get_location(self, adress: str) -> list: # не каждый адрес распознает - нужно определенное написание
#         """
#         Получает координаты объекта по адресу
#         """
#         geolocator = Nominatim(user_agent="Tester") #Указываем название приложения (так нужно, да) # списала из интернета
#         location = geolocator.geocode(adress) #Создаем переменную, которая состоит из нужного нам адреса
#         # print(location) #Выводим результат: адрес в полном виде
#         # print(location.latitude, location.longitude) #И теперь выводим GPS-координаты нужного нам адреса
#         location_data = [location.latitude, location.longitude]
#         return location_data
        
#     def _get_plan(self, item: object) -> Optional[str]:
#         """
#         Получает ссылку на план конкретой квартиры
#         """
#         plan_data = item.findAll("span", class_="grid-item__image__plan")
#         if plan_data:
#             plan_bad = plan_data[0]["style"]
#             cut_begin = plan_bad.find("(")
#             plan_bad = plan_bad[cut_begin:]
#             plan_bad = plan_bad.replace("(", "")
#             plan = plan_bad.replace(")", "")
#         else:
#             print("Error in getting plan")
#             plan = None
#         return plan

#     def _get_price(self, item: object) -> Optional[int]:
#         """
#         Получает цену квартиры
#         """
#         price_data = item.findAll("div", class_="default-price")
#         if price_data:
#             price_bad = price_data[0].text
#             # print(price_bad)
#             price_bad = price_bad.replace(" ", "")
#             price_bad = price_bad.replace("₽", "")
#             price = int(price_bad)
#         else:
#             print("Error in getting price")
#             price = None
#         return price

    def _get_project(self, project: object) -> Optional[str]:
        """
        Получает название проекта
        """
        project_data = project.findAll("h4")
        if project_data:
            project_bad = project_data[0].text
            project = project_bad.strip()
        else:
            print("Error in getting project")
            project = None
        return project

#     def _get_project_url(self, project: object) -> Optional[str]:
#         """
#         Получает URL проекта
#         """
#         project_data = project.findAll("a", class_="index__projects__img")
#         if project_data:
#             project_ref = project_data[0]["href"]
#             project_url = "https://hals-development.ru" + project_ref
#             # pprint(project_url)
#         else:
#             print("Error in getting project_url")
#             project_url = None
#         return project_url



#     def _get_rooms(self, item: object) -> Optional[int]:
#         """
#         Получает количество комнат
#         """
#         flat_data = item.findAll("div", class_="grid-item2__info2")
#         # print(flat_data)
#         if flat_data:
#             data_full = flat_data[0].text
#             # print(data_full)
#             # print("++++++++++++++++++++++++++++++++++")
#             rooms_bad = data_full[0]
#             # print(area_bad)
#             # print("++++++++++++++++++++++++++++++++++")
#             # area_bad = area_bad.replace('"','')
#             # area_bad = area_bad.replace('/','')
#             # area_bad = area_bad.replace(' ','')
#             # area_bad = area_bad.replace(',','.')
#             # print(area_bad)
#             rooms = int(rooms_bad)
#         else:
#             print("Error in getting rooms")
#             rooms = None
#         return rooms

#     def _get_status(self, project: object) -> Optional[str]:
#         """
#         Получает статус застройки
#         """
#         status_data = project.findAll("label", class_="styles__HouseStatusWrapper-sc-2y8yk1-0 ktZUtE")
#         if status_data:
#             status_bad = status_data[0].text
#             status = status_bad.strip()
#         else:
#             print("Error in getting status")
#             status = None
#         return status

#     def _get_title(self, project: object) -> Optional[str]:
#         """
#         Метод получает наименование квартиры со страницы со списком квартир
#         """
#         title_data = project.findAll("span", class_="styles__Ellipsis-sc-1fw79ul-0 jYMONF styles__Name-sc-1ajig0k-4 gRAIRo")
#         if title_data:
#             title_bad = title_data[0].text
#             title = title_bad.strip()
#         else:
#             print("Error in getting title")
#             title = None
#         return title

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
#                     description=e["description"],
#                     # params="params_example",
#                     # seller="seller_example",
#                     # seller_url="seller_url_example",
#                     source_url=e["source_url"],
#                     apartment_area=e["apartment_area"],
#                     apartment_completion_quarter=e["apartment_completion_quarter"],
#                     apartment_completion_year=e["apartment_completion_year"],
#                     apartment_floor=e["floor"],
#                     apartment_floors_total=e["apartment_floors_total"],
#                     apartment_ceilingheight=e["apartment_ceilingheight"],
#                     apartment_room=e["rooms"],
#                     apartment_ppm=e["apartment_ppm"],
#                     apartment_address=e["full_address"],
#                     # apartment_location=e["apartment_location"],
#                     apartment_location_lat=e["apartment_location_lat"],
#                     apartment_location_lon=e["apartment_location_lon"],
#                 )  # History |  (optional)

#                 try:
#                     api_response = api_instance.history_create(body=history) # написать в лог, что не смог отправить объект
#                     # pprint(api_response)
#                 except openapi_client.ApiException as e:
#                     print("Exception when calling HistoryApi->history_create: %s\n" % e) #!!!!
#             print("Count load object =", len(self.__dict_list))
            
class MRGroupParserFFile(MRGroupParser):
    """
    Собирает данные страницы, скачанной с сайта https://www.mr-group.ru/flats/ в файл 'sources/mrgroup' очищает их, сохряняет
    """
    def __init__(self, page_text):
        self.__url = None
        self.__b_soup = BeautifulSoup(page_text, features="html.parser")
        self.__projects_list = self.__b_soup.findAll(
            "li", class_ = "search-list-item js-search-list-item dataLayerFlatCard"
        )
        self.__dict_list = []
        
    def _get_brand(self, project: object) -> Optional[str]:
        """
        Получает наименование застройщика
        """
        footer_data = self.__b_soup.findAll("div", class_="footer-copyright")
        if footer_data:
            # for data in footer_data:
            brand_bad = footer_data[0].text
            cut_begin = brand_bad.find(" ")
            cut_stop = brand_bad.find(" 2023")
            brand_bad = brand_bad[cut_begin:cut_stop]
            brand = brand_bad.strip()
        else:
            print("Error in getting brand")
            brand = None
        return brand
        
    def get_dict_list(self) -> list:
        """
        Формирует список словарей с данными по квартирам
        """
        for project in self.__projects_list:
            item_dict = {}
            item_dict = {}
            item_dict["apartment_area"] = self._get_area(project)
#             item_dict["title"] = self._get_title(project) # перепутала с проджект для наш.дом
            item_dict["project"] = self._get_project(project)
            item_dict["brand"] = self._get_brand(project)
            item_dict["bulding"] = self._get_bulding(project)
            apartment_completion_data = self._get_completion_data(project)
            item_dict[
                "apartment_completion_quarter"
            ] = apartment_completion_data[0]
            item_dict[
                "apartment_completion_year"
            ] = apartment_completion_data[1]
            item_dict["floor"] = self._get_floor(project)
#             item_dict["description"] = self._get_description(project)
#             item_dict["full_address"] = self._get_address(project)
#             item_dict["brand"] = self._get_brand(project)
#             item_dict["brand_url"] = self.BRAND_URL
#             print(item_dict["project"])
#             if item_dict["project"] == self.PROJECTS_NAMES[0]:
#                 b_soup = BeautifulSoup(pages_dict["hals_kosmo"], features="html.parser")
#             elif item_dict["project"] == self.PROJECTS_NAMES[1]:
#                 b_soup = BeautifulSoup(pages_dict["hals_teatral"], features="html.parser")
#             elif item_dict["project"] == self.PROJECTS_NAMES[2]:
#                 b_soup = BeautifulSoup(pages_dict["hals_zamoskvorech"], features="html.parser") 
#             elif item_dict["project"] == self.PROJECTS_NAMES[3]:
#                 b_soup = BeautifulSoup(pages_dict["hals_engels"], features="html.parser")
#             elif item_dict["project"] == self.PROJECTS_NAMES[4]:
#                 b_soup = BeautifulSoup(pages_dict["hals_shossejnaya"], features="html.parser")
#             else:
#                 print("Undefined project", item_dict["project"])
#                 b_soup = None
#             items_list = b_soup.findAll("a", class_="grid-item grid-item2")
#             for (
#                 item
#             ) in (
#                 items_list
#             ):  
#                 item_dict = self._fill_dict(item, item_dict)
            item_dict[
                "source_url"
            ] = self.__url 
            self.__dict_list.append(item_dict)
        return self.__dict_list
    
#     def _get_ceilingheight(self, one_item_url: str) -> Optional[float]:
#         """
#         Получает высоту потолков (только онлайн)
#         """
#         pass

    