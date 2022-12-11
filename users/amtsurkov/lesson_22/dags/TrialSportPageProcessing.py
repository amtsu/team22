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
    Класс формиует, на основе текста html, страницы список словарей содержаший объеты найденные на данной странице.
    Используется для страниц на которых есть только одни основной обект  (пример https://trial-sport.ru/goods/51530/1179889.html)
        Not good use BeautifulSoup object, and then use them in coheshe object
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
    Класс формиует, на основе текста html страницы, список словарей содержаший объеты найденные на данной странице.
    Используется для страниц на которых есть список оьбектов (пример https://trial-sport.ru/gds.php?s=51528)

    Не использует ранее созданные классы конкртеных элеменотов, а формирует все в одном месте.
    Можно сравнить какой подзод проще к прочтению и пониманию.
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
        list_data = self.__soup.findAll("div", class_="object ga")
        for i in list_data:
            d = i.find_all("a", class_="title")
            url = d[0]["href"]
            title = d[0].text

            d = i.find_all("span", class_="price")
            price = d[0].text
            price = price.replace("&thinsp;", "")
            price = price.replace("&thinsp;", "")
            price = price.replace(" &#8381", "")
            price = price.replace(" &#8381", "")
            price = price.replace("\n", "")
            if len(price) > 6:
                try:
                    price = int(price[:-6] + price[-5:-2])
                except:
                    price = int(price[:-7] + price[-6:-3])
            else:
                price = int(price[:-2])

            d = i.find_all("span", class_="discount discountsale")
            price_sale = price
            if d:
                price_sale_s = d[0].text
                if len(price_sale_s) > 6:
                    try:
                        price_sale = int(price_sale_s[:-6] + price_sale_s[-5:-2])
                    except:
                        price_sale = int(price_sale_s[:-7] + price_sale_s[-6:-3])
                else:
                    price_sale = int(d[0].text[:-2])
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

            l.append(
                {
                    "url": url,
                    "title": title,
                    "price": price,
                    "price_sale": price_sale,
                    "url": "https://trial-sport.ru" + url,
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


class TrialSportServiceProcessing:
    """
    Основной класс по работе с поставщиком данных TrialSport.
    Нужен для получения данных от поставщик, их отрансормации, и последующей отправки в долговрменное хранилище.

    when we have many ServiceProcessing, we nead create one Modeul with configuration
    """

    def __init__(self):
        self.__list_dict = []

    def load_url_by_default(self):
        """
        Инициализирует списки urls для послеющего их получения с веб ресрса и их обработки
        """
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

        self.__url_list = [
            #'https://trial-sport.ru/gds.php?s=761611&sort=price&gpp=100&pg=9'
            # ]
            # dd = [
            # "https://trial-sport.ru/gds.php?s=51530&sort=price&gpp=100&pg=2",
            # "https://trial-sport.ru/gds.php?s=51530&sort=price&gpp=100",
            # https://trial-sport.ru/gds.php?s=51528&discount=1&sort=price&gpp=100&pg=51
            "https://trial-sport.ru/gds.php?s=51530",
            "https://trial-sport.ru/gds.php?s=51533",
            "https://trial-sport.ru/gds.php?s=51527",
            "https://trial-sport.ru/gds.php?s=51526",
            "https://trial-sport.ru/gds.php?s=51528",
            "https://trial-sport.ru/gds.php?s=761611",
            "https://trial-sport.ru/gds.php?s=51516",
            "https://trial-sport.ru/gds.php?s=1256729",
            "https://trial-sport.ru/gds.php?s=51525",
            "https://trial-sport.ru/gds.php?s=1546522",
            "https://trial-sport.ru/gds.php?s=1340407",
            "https://trial-sport.ru/gds.php?s=51534",
        ]

    def process(self):
        """
        Формирует финальный список ссылок на документы для обработки и преобразовыает их в нужный формат.
        """
        self.__list_dict = []
        for url in self.__urls:
            for object_params in OnePage(url).list_dict():
                self.__list_dict.append(object_params)

        for url in self.__url_list:
            for i in range(1, 68):
                # for i in range(1, 2):
                r_url = url + "&sort=price&gpp=100" + "&pg=" + str(i)
                # r_url = url
                print(r_url)
                with urllib.request.urlopen(r_url) as response:
                    self.__page = response.read()
                    self.__list_page_processor = ListPageProcessor(self.__page, r_url)
                    for object_params in self.__list_page_processor.list_dict():
                        self.__list_dict.append(object_params)

    def __create_file_name_with_current_datetime(self):
        """
        Формирует имя файла для сохранния полученных данных
        """
        return "trialsport_fresh.json"

    def save_in_file_with_current_datetime(self):
        """
        Сохраняет полученные данные в локальный фаил
        """
        json_string = json.dumps(self.__list_dict)
        file_name = self.__create_file_name_with_current_datetime()
        with open(file_name, "w") as outfile:
            json.dump(json_string, outfile)

    def send_in_api(self):
        """
        Отправляет полученные данные в олговремнное хранилище
        """
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
                    # pprint(api_response)
                except openapi_client.ApiException as e:
                    print("Exception when calling HistoryApi->history_create: %s\n" % e)
            print("Count load object =", len(self.__list_dict))
