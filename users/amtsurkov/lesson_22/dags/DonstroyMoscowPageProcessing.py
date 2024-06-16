import re
import urllib.request
import urllib
from bs4 import BeautifulSoup
import json

import time
import openapi_client  # type: ignore
from pprint import pprint  # type: ignore

from openapi_client.apis.tags import history_api  # type: ignore
from openapi_client.model.history import History  # type: ignore
from openapi_client.model.paginated_history_list import PaginatedHistoryList  # type: ignore
from openapi_client.model.patched_history import PatchedHistory  # type: ignore


class Element:
    """
    Попытка сделать интерфей, для последующего построения на его основе классов обработки различных элементов на странице, таких как название, цена, ...
    """

    def get(self):
        """
        Получить значение элемента
        """
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self) -> str:
        """
        Достать строку содержашую значение элемента
        """
        assert False
        return ""

    def __init__(self, soup):
        """
        инициализация обекта
        """
        self.__soup = soup

    def __is_page_ok(self):
        """
        проверить что на данной странице(в данном блоке) есть неободимый элемент
        """
        return True

    def __normalization(self, price_bad: str) -> str:
        """
        Очисть элемент от лишнего

        В случае с ценой это может быть: какие то выделения основной части, разделитили, символы валюты
        """
        return price_bad

    def __type_convert(self, text):
        """
        Преобразовать элемент к требуемому типу
        """
        return text

    def _w(self):
        """
        Этот метод был введен чтобы показать как работает наследование
        """
        return "w"

    def __z(self):
        """
        Этот метод был введен чтобы показать как работает наследование
        """
        return "z"


class PriceElement(Element):
    def get(self) -> int:
        """
        Получить значение элемента
        """
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self) -> str:
        """
        Достать строку содержашую значение элемента
        """
        list_price_data = self.__soup.findAll("div", class_="prices_for_popup")
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all("div", class_="price")
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        """
        инициализация обекта
        """
        self.__soup = soup

    def __is_page_ok(self) -> bool:
        """
        проверить что на данной странице(в данном блоке) есть неободимый элемент
        """
        list_price_data = self.__soup.findAll("div", class_="prices_for_popup")
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all("div", class_="price")
        assert len(list_reports_data) == 2
        if len(list_reports_data) != 2:
            return False
        return True

    def __normalization(self, price_bad: str) -> str:
        """
        Очисть элемент от лишнего

        В случае с ценой это может быть: какие то выделения основной части, разделитили, символы валюты
        """
        price_bad = price_bad.replace("\u2009", "")  # ' '
        price_bad = price_bad.replace("\u20bd", "")  # '₽'
        price_bad = price_bad.replace(" ", "")  # ' '
        return price_bad
        # price_good = int(price_bad)
        # return price_good

    def __type_convert(self, text: str) -> int:
        """
        Преобразовать элемент к требуемому типу
        """
        assert text.isnumeric()
        return int(text)

    def __z(self):
        return "z"


class PriceSaleElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self):
        list_price_data = self.__soup.findAll("div", class_="prices_for_popup")
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all(
            "div", class_="price price_disc"
        )
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_price_data = self.__soup.findAll("div", class_="prices_for_popup")
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all(
            "div", class_="price price_disc"
        )
        assert len(list_reports_data) == 1
        if len(list_reports_data) != 1:
            return False
        return True

    def __normalization(self, price_bad):
        price_bad = price_bad.replace("\u2009", "")  # ' '
        price_bad = price_bad.replace("\u20bd", "")  # '₽'
        price_bad = price_bad.replace(" ", "")  # ' '
        return price_bad
        price_good = int(price_bad)
        return price_good

    def __type_convert(self, text):
        assert text.isnumeric()
        return int(text)

    def __z(self):
        return "z"


class TitleElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self):
        list_reports_data = self.__soup.findAll("h2")
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_reports_data = self.__soup.findAll("h2")
        # print(list_reports_data)
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
        list_reports_data = self.__soup.findAll("div", class_="bread")
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_reports_data = self.__soup.findAll("div", class_="bread")
        # print(list_reports_data)
        assert len(list_reports_data) == 1
        if len(list_reports_data) != 1:
            return False
        return True

    def __normalization(self, price_bad):
        return price_bad.replace("\n", "")

    def __type_convert(self, text):
        return text


class BrandUrlElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self):
        list_price_data = self.__soup.findAll("div", class_="bread")
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all("a")
        element_1 = list_reports_data[-1]
        return element_1["href"]

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_price_data = self.__soup.findAll("div", class_="bread")
        assert len(list_price_data) == 1
        list_reports_data = list_price_data[0].find_all("a")
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
        list_price_data = self.__soup.findAll("script")
        script = list_price_data[10]
        # "big": "\/images\/catalog\/lbj7000_xt3_130_lv_storm_blue_rgb300dpi_2539265.jpg"
        return re.search(r'big": "(.+)"', script.text).group(1)

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        # list_price_data = self.__soup.findAll('script')
        # script = list_price_data[10]
        ##"big": "\/images\/catalog\/lbj7000_xt3_130_lv_storm_blue_rgb300dpi_2539265.jpg"
        # image_url = re.search(r'big": "(.+)"', script.text).group(1)

        # assert len(list_price_data) == 49
        # if len(list_price_data) != 49:
        #    return False
        return True

    def __normalization(self, price_bad):
        return price_bad.replace("\\", "")

    def __type_convert(self, text):
        return text


class OnePageProcessor:
    """
    """

    def __init__(self, text_page, url):
        self.__soup = BeautifulSoup(text_page, features="html.parser")
        self.__url = url

    def list_dict(self):
        """
        Формиует список состоящий из одного словаря с занчениями найденными на странице товара
        """
        return [
            {
                "title": TitleElement(self.__soup).get(),
                "price": PriceElement(self.__soup).get(),
                "price_sale": PriceSaleElement(self.__soup).get(),
                "brand": BrandElement(self.__soup).get(),
                "brand_url": BrandUrlElement(self.__soup).get(),
                "image_url": ImageUrlElement(self.__soup).get(),
                "url": self.__url,
                "source_url": self.__url,
            }
        ]


class ListPageProcessor:
    """
    """

    def __init__(self, text_page, url):
        self.__soup = BeautifulSoup(text_page, features="html.parser")
        self.__url = url

    def list_dict(self):
        """
        Формирует список слловарей, где каждый словарь представляет товар найденный на странице.
        Поиск элемента, его очистка, и преобразование также происходят на в данном методе.
        """
        l = []
        list_data = self.__soup.findAll("div", class_="d-flat-list")
        #print('---1111----')
        #print(list_data)
        #print('len =', len(list_data))
        for i in list_data:

            #print('---222---')
            #print(i)
            d = i.find_all("a", class_="d-flat-list__link")
            if not len(d):
                continue 
            url = d[0]["href"]
            title = ''#d[0].text
            
#
#                                       <div class="d-flat-list">
#                        <div class="d-flat-list__item _item1">
#                            <img src="/hydra/svg/apartment/10/b19-s2-f3_6-p11.svg">
#                        </div>
#                        <div class="d-flat-list__item _item2">
#                            <div class="d-flat-list__label">Комнат</div>Студия                         </div>
#                        <div class="d-flat-list__item _item3">
#                            <div class="d-flat-list__object">Символ                                <small>Независимость</small>
#                            </div>
#                        </div>
#                        <div class="d-flat-list__item _item4">
#                            <div class="d-flat-list__label">Корпус</div>19, 2 секц
#                        </div>
#                        <div class="d-flat-list__item _item5">
#                            <div class="d-flat-list__label">Этаж</div>3 из 24                        </div>
#                        <div class="d-flat-list__item _item6">
#                            <div class="d-flat-list__label">Номер</div>283                        </div>
#                        <div class="d-flat-list__item _item7">
#                            <div class="d-flat-list__label">Площадь, м&sup2;</div>28.3                        </div>
#                        <div class="d-flat-list__item _item8">
#                            <div class="d-flat-list__price">
#                                10 125 740 ₽                            </div>
#                        </div>
#                        <div class="d-flat-list__item _item9">
#                            <div class="d-flat-list__actions">
#                                                                                            </div>
#                        </div>
#                        <div class="d-flat-list__item _item10">
#                            <button class="d-button _flatIcon _favorite" data-favorite-icon="10-19-2-260119283">
#                                <svg>
#                                    <use xlink:href="/assets/blueant/assets/sprite.svg#sprite-heart"></use>
#                                </svg>
#                                <div class="d-button__tooltip">Добавить в избранное</div>
#                            </button>
#                        </div>
#                        <a class="d-flat-list__link" href="/objects/simvol/plans/quarter6/korpus19/section2/floor3/flat260119283/" target="_blank"></a>
#                    </div>




#                    <div class="d-flat-list _mobile">
#                        <div class="d-flat-list__top">
#                            <div class="d-flat-list__img">
#                                <img src="/hydra/svg/apartment/10/b19-s2-f3_6-p11.svg">
#                            </div>
#                            <div class="d-flat-list__price">
#                                10 125 740 ₽                            </div>
#                            <div class="d-flat-list__object">
#                                Символ                                <small>Независимость</small>
#                            </div>
#                        </div>
#                        <div class="d-flat-list__bottom">
#                            <div class="d-flat-list__items">
#                                <div class="d-flat-list__item">Ст</div>
#                                <div class="d-flat-list__item">28.3 м2</div>
#                                <div class="d-flat-list__item">3 эт.</div>
#                            </div>
#                            <div class="d-flat-list__actions">
#                                <img src="assets/img/d/icon_fire.svg">
#                                <img src="assets/img/d/icon_brush.svg">
#                            </div>
#                            <button class="d-button _flatIcon _favorite" data-favorite-icon="10-19-2-260119283">
#                                <svg>
#                                    <use xlink:href="/assets/blueant/assets/sprite.svg#sprite-heart"></use>
#                                </svg>
#                                <div class="d-button__tooltip">Добавить в избранное</div>
#                            </button>
#                        </div>
#                        <a class="d-flat-list__link" href="/objects/simvol/plans/quarter6/korpus19/section2/floor3/flat260119283/" target="_blank"></a>
#                    </div>


#
#                    <div class="d-flat-list">
#                        <div class="d-flat-list__item _item1">
#                            <img src="/hydra/svg/apartment/28/b63-s1-f10_18-p5.svg">
#                        </div>
#                        <div class="d-flat-list__item _item2">
#                            <div class="d-flat-list__label">Комнат</div>Студия                         </div>
#                        <div class="d-flat-list__item _item3">
#                            <div class="d-flat-list__object">Остров                                <small>Остров.6</small>
#                            </div>
#                        </div>
#                        <div class="d-flat-list__item _item4">
#                            <div class="d-flat-list__label">Корпус</div>3, 1 секц
#                        </div>
#                        <div class="d-flat-list__item _item5">
#                            <div class="d-flat-list__label">Этаж</div>16 из 21                        </div>
#                        <div class="d-flat-list__item _item6">
#                            <div class="d-flat-list__label">Номер</div>100                        </div>
#                        <div class="d-flat-list__item _item7">
#                            <div class="d-flat-list__label">Площадь, м&sup2;</div>29                        </div>
#                        <div class="d-flat-list__item _item8">
#                            <div class="d-flat-list__price">
#                                19 244 400 ₽                            </div>
#                        </div>



#                   <div class="d-flat-list">
#                        <div class="d-flat-list__item _item1">
#                            <img src="/hydra/svg/apartment/10/b29-s1-f2-p1.svg">
#                        </div>
#                        <div class="d-flat-list__item _item2">
#                            <div class="d-flat-list__label">Комнат</div>2                        </div>
#                        <div class="d-flat-list__item _item3">
#                            <div class="d-flat-list__object">Символ                                <small>Вдохновение</small>
#                            </div>
#                        </div>
#                        <div class="d-flat-list__item _item4">
#                            <div class="d-flat-list__label">Корпус</div>29, 1 секц
#                        </div>
#                        <div class="d-flat-list__item _item5">
#                            <div class="d-flat-list__label">Этаж</div>2 из 26                        </div>
#                        <div class="d-flat-list__item _item6">
#                            <div class="d-flat-list__label">Номер</div>1                        </div>
#                        <div class="d-flat-list__item _item7">
#                            <div class="d-flat-list__label">Площадь, м&sup2;</div>58.6                        </div>
#                        <div class="d-flat-list__item _item8">
#                            <div class="d-flat-list__price">
#                                24 149 060 ₽                            </div>
#                        </div>
#                        <div class="d-flat-list__item _item9">
#                            <div class="d-flat-list__actions">
#                                                                                            </div>
#                        </div>
#                        <div class="d-flat-list__item _item10">
#                            <button class="d-button _flatIcon _favorite" data-favorite-icon="10-29-1-260129001">
#                                <svg>
#                                    <use xlink:href="/assets/blueant/assets/sprite.svg#sprite-heart"></use>
#                                </svg>
#                                <div class="d-button__tooltip">Добавить в избранное</div>
#                            </button>
#                        </div>
#                        <a class="d-flat-list__link" href="/objects/simvol/plans/quarter5/korpus29/section1/floor2/flat260129001/" target="_blank"></a>
#                    </div>


            d = i.find_all("div", class_="d-flat-list__item _item3")
            if not len(d):
                continue 
            #project = d[0].text
            #kvartal = d[0].find_all("small")[0].text
            kvartal = d[0].small.extract().text
            kvartal = kvartal.replace('\n', '')

            project = d[0].text
            project = project.replace('\n', '')
            project = project.rstrip()
            #print(project)
            #print('===')
            ##kvartal = d[0].text.rstrip()
            #print(kvartal)

            d = i.find_all("div", class_="d-flat-list__item _item4")
            if not len(d):
                continue 
            korpus = d[0].div.extract().text
            section = d[0].text
            section = section.replace('\n', '')
            section = section.rstrip()

            
            d = i.find_all("div", class_="d-flat-list__item _item6")
            if not len(d):
                continue 
            nomer_title = d[0].div.extract().text
            nomer_room = d[0].text
            nomer_room = nomer_room.replace('\n', '')
            nomer_room = nomer_room.rstrip()

            

            #print(i)
            #print(i.text)
            d = i.find_all("div", class_="d-flat-list__item _item5")
            if not len(d):
                continue 
            d[0].div.extract()
            floor = d[0].text
            #print(floor)
            floor, floors = floor.split(' из ')
            ##print(floor[5:])
            #print(floor)
            #print(floors)
            #floor, floors = int(floor[5:]), int(floors)
            floor, floors = int(floor), int(floors)

            d = i.find_all("div", class_="d-flat-list__item _item1")
            if not len(d):
                continue 
            f = d[0].find_all("img")
            image_plan = f[0]["src"]


            d = i.find_all("div", class_="d-flat-list__item _item7")
            if not len(d):
                continue 
            #d[0] = d[0].div.extract()
            dd = d[0].div.extract()
            #d[0] = d[0].div

            area = d[0].text
            area = area.replace('\n', '')
            area = area.replace(' ', '')


            d = i.find_all("div", class_="d-flat-list__item _item2")
            if not len(d):
                continue 
            #print(d)
            hh = d[0].div.extract()
            #print('----')
            #print(hh)
            room = d[0].text
            room = room.rstrip()
            #print(room) 
            if 'Студия' in room:
                room = 0
            elif 'Пентхаус' in room:
                room = 0
            elif room:
                #print('---')
                #print(room)
                #print('-!!!!--')
                #print('-!!!!--')
                room = int(room)
###                room = int(room)
                #print('--')
            else:
                room = 0

            address = ''


            #print('----3333---')


            #d-flat-list__price
            d = i.find_all("div", class_="d-flat-list__price")
            #10 116 430 ₽
            #print(d[0]) 
            #print(d[0].text) 
            if len(d[0].text) < 1:    
                # same product have not price
                #print('product have not price =', title)
                #TODO need fix API
                price_sale = 0
                price = 0
            else:

                d1 = i.find_all("div", class_="d-flat-list__priceOld")
                if d1:
                    hh1 = d[0].div.extract()
                    price = d[0].text
                else:

                    price = d[0].text


                #print(price)
                price = price.replace("&thinsp;", "")
                price = price.replace("&thinsp;", "")
                price = price.replace(" &#8381", "")
                price = price.replace(" &#8381", "")
                price = price.replace("\n", "")
                price = price.replace("₽", "")
                price = price.replace("&nbsp;", "")
                price = price.replace(" ", "")

                try:
                    price = int(price)
                except:
                    price = 0


            d = i.find_all("div", class_="d-flat-list__priceOld")
            price_sale = price
            #print(d)
            #print(d[0])
            if d:
                price_sale_s = d[0].text
                #price_sale = int(d[0].text[:-2])
                price_sale = price_sale_s
                price_sale = price_sale.replace("\n", "")
                price_sale = price_sale.replace("₽", "")
                price_sale = price_sale.replace("&nbsp;", "")
                price_sale = price_sale.replace(" ", "")

                price_sale = int(price_sale)

            else:
                d = i.find_all("span", class_="discount")
                if d:
                    price_sale_s = d[0].text
                    if len(price_sale_s) > 6:
                        try:
                            price_sale = int(price_sale_s[:-6] + price_sale_s[-5:-2])
                        except:
                            price_sale = int(price_sale_s[:-7] + price_sale_s[-6:-3])
                    else:
                        price_sale = int(d[0].text[:-2])

            #print('----3333---')

            source_url = self.__url
            ee = {
                    #"title": title,
                    "source_url": source_url,


                    #"url": url,
                    "url": "https://donstroy.moscow" + url,
                    "price": price,
                    "price_sale": price_sale,
                    "quantity": 1,
                    "datetime_create": "1970-01-01T00:00:00.00Z",
                    "brand": "donstroy.moscow",
                    "brand_url": "donstroy.moscow",
                    "category": "Новостройки",
                    "image_url": image_plan,
                    "source_url": source_url,
                    "apartment_area": area,
                    "apartment_floor": int(floor),


                    "title": f"{project} | {kvartal} | {korpus} | {section} | {floor} | {area} | {address} | {nomer_room}",

                    "apartment_room": int(room),
                    "apartment_address": address,

                    #"description": '',#f"{project} {kvartal} {korpus} {section} {floor} {area} {address}",

                    "description": f"{project} {kvartal} {korpus} {section} {floor} {area} {address}",
                }


            if floors:
                ee["apartment_floors_total"] = int(floors)
            else:
                print("not have floors_total in =", source_url)
                ee["apartment_floors_total"] = None


            l.append(ee)

            #print('----3333---')
            #print(ee)

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


class DonstroyMoscowServiceProcessing:
    """
    """

    def __init__(self):
        self.__list_dict = []

    def load_url_by_default(self):
        """
        Инициализирует списки urls для послеющего их получения с веб ресрса и их обработки
        """

        self.__urls = []
        #self.__urls = [
        #        "https://donstroy.moscow/full-search/?price%5B%5D=8.8&price%5B%5D=725.2&area%5B%5D=25&area%5B%5D=392&floor_number%5B%5D=1&floor_number%5B%5D=51&floor_first_last=false&discount=false&furnish=false&apartments=false&sort=price-asc&view_type=flats&view=list&page=",
        #]

        url = "https://donstroy.moscow/full-search/?price%5B%5D=8.8&price%5B%5D=725.2&area%5B%5D=25&area%5B%5D=392&floor_number%5B%5D=1&floor_number%5B%5D=51&floor_first_last=false&discount=false&furnish=false&apartments=false&sort=price-asc&view_type=flats&view=list&page="

        self.__url_list = [
            "https://donstroy.moscow/full-search/?price%5B%5D=8.8&price%5B%5D=725.2&area%5B%5D=25&area%5B%5D=392&floor_number%5B%5D=1&floor_number%5B%5D=51&floor_first_last=false&discount=false&furnish=false&apartments=false&sort=price-asc&view_type=flats&view=list&page="
        ]

        #discount=true
    
        #for i in range(130):
        #for i in range(1):
        #    self.__url_list.append(url+str(i))

    def process(self):
        """
        Формирует финальный список ссылок на документы для обработки и преобразовыает их в нужный формат.
        """
        self.__list_dict = []
        for url in self.__urls:
            for object_params in OnePage(url).list_dict():
                self.__list_dict.append(object_params)

        for url in self.__url_list:
            #for i in range(1, 200):
            #for i in range(1, 130):
            for i in range(1, 140):
            #for i in range(1, 3):
            #for i in range(1, 2):
            #for i in range(1, 22):
                r_url = url + str(i)
                print(r_url)
                #with urllib.request.urlopen(r_url) as response:
                #    self.__page = response.read()
                #    self.__list_page_processor = ListPageProcessor(self.__page, r_url)
                #    for object_params in self.__list_page_processor.list_dict():
                #        self.__list_dict.append(object_params)

                #response = urllib.request.urlopen(r_url)

                req = urllib.request.Request(r_url)
                req.add_header('user-agent', 'curl/8.4.0')
                response = urllib.request.urlopen(req)
                self.__page = response.read()
                #print(self.__page)
                self.__list_page_processor = ListPageProcessor(self.__page, r_url)
                for object_params in self.__list_page_processor.list_dict():
                     self.__list_dict.append(object_params)


    def send_in_api(self):
        """
        Отправляет полученные данные в олговремнное хранилище
        """
        configuration = openapi_client.Configuration(host="http://absrent.ru:8000")

        with openapi_client.ApiClient(configuration) as api_client:
            i = 0
            api_instance = history_api.HistoryApi(api_client)
            for e in self.__list_dict:
                #print(e)
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
                    # worker="worker_example",
                    # task="task_example",

                    category=e["category"],
                    # category_url="category_url_example",
                    brand=e["brand"],
                    brand_url=e["brand_url"],
                    # day_to_delivery=1,
                    # sku="sku_example",
                    url=e["url"],
                    # canonical_url="canonical_url_example",
                    img_url=e["image_url"],
                    description=e["description"],
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
                    #apartment_ppm=e["apartment_ppm"],
                    apartment_address=e["apartment_address"],
                    #apartment_location=e["apartment_location"],
                    #apartment_location_lat=e["apartment_location_lat"],
                    #apartment_location_lon=e["apartment_location_lon"],
 


                )  # History |  (optional)

                try:
                    api_response = api_instance.history_create(body=history)
                    i += 1
                    #pprint(api_response)
                except openapi_client.ApiException as e:
                    print("Exception when calling HistoryApi->history_create: %s\n" % e)
                if i % 100 == False:
                    print('i=', i)
            print("Count load object =", len(self.__list_dict))
