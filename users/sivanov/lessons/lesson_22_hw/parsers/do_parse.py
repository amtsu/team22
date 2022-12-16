"""
Модуль, демонстрирующий работу с парсером
Вытащил из main`a модуля getdatafrom, чтобы было понятно где что поменялось при коммитах
"""
import os
import openapi_client  # type: ignore
from openapi_client.apis.tags import history_api  # type: ignore
from openapi_client.model.history import History  # type: ignore

# не проверять на корректность импорта
from getdatafrom import create_product_info  # pylint: disable=E0401

# не проверять на корректность импорта
from usefulstuff import LocalLog  # pylint: disable=E0401

llog = LocalLog(False)


class Parser:
    """
    класс парсинга веб-страничек
    содержит два статических метода:
    do_parse ходит по страничкам и собирает нужную информацию
    sent_to_api отправляет собранные данные в базу через рест
    """

    # =====================================================================================
    @staticmethod
    def send_to_api(data: list):
        """
        работа с джанго базой днных
        у меня пока есть :
        {'Цена': '5290',
         'Название товара': 'Улей 12 рам 1 корпус + 2 магазина (сетчатое дно) комплект',
         'Бренд': '', 'Код товара':'5127',
         'url': 'https://i-uley.pro/catalog/uley_dadana/
                 uley-12-ram-1-korpus-2-magazina-setchatoe-dno-komplekt/'}
        """
        configuration = openapi_client.Configuration(host="http://absrent.ru:8000")

        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = history_api.HistoryApi(api_client)
            for element in data:
                # print(e)
                history = History(
                    pk=1,
                    title=element["Название товара"],
                    quantity=1,
                    price=str(element["Цена"]),
                    # price_sale=str(e['price_sale']),
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
                    brand=element["Бренд"],
                    # brand_url=e["brand_url"],
                    # day_to_delivery=1,
                    sku=element["Код товара"],
                    url=element["url"],
                    # canonical_url="canonical_url_example",
                    # img_url=e["image_url"],
                    # description="description_example",
                    # params="params_example",
                    # seller="seller_example",
                    # seller_url="seller_url_example",
                    # source_url=e["source_url"],
                    # urls_other_products_on_the_page="urls_other_products_on_the_page_example",
                    worker="sivanov_parser_22",
                    # task="task_example",
                )  # History |  (optional)

                try:
                    api_response = api_instance.history_create(body=history)
                    llog(api_response)
                except openapi_client.ApiException as e_api:
                    print(
                        f"Exception when calling HistoryApi->history_create: {e_api}\n"
                    )
            print(f"Count load object : {len(data)}")

    # =====================================================================================
    @staticmethod
    def do_parse():
        """
        пример загрузки информации со см
        """
        # ---------------------------------------------------------------------------
        # создаем пустой список для  парсеров
        pi_list = []
        result = []
        # создадим список для настроечных файлов,которые потом возьму из ./json
        json_dir = (
            os.path.dirname(os.path.abspath(__file__)) + "/json/"
        )  # os.getcwd()+'/json/'
        with os.scandir(json_dir) as files:
            filename_list = [
                file.name
                for file in files
                if file.is_file() and file.name.startswith("parse_")
            ]
        for filename in filename_list:
            pi_list.append(
                create_product_info(json_dir + filename)
            )  # os.getcwd()+'/json/'
        # ---------------------------------------------------------------------------
        # парсим и печатаем результат
        for product_info in pi_list:
            product_info.load()
            if product_info.is_loaded():
                result.append(product_info.get())
            # if(len(result)>0):
            #    with open(json_dir + 'result.pickle', 'wb') as fout:
            #        pickle.dump(result,fout)
        return result


# =========================================================================================
def main():
    """
    вызывается при выполнении данного модуля,
    выполняет парсинг страниц, заданных файлами типа "./json/parse_*.json"
    выполняет проверку функционирования методов класса Parser, пока нет полноценных тестов
    """
    result = Parser.do_parse()
    print(result)
    Parser.send_to_api(result)


# =========================================================================================
if __name__ == "__main__":
    main()
