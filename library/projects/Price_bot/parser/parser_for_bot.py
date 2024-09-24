from bs4 import BeautifulSoup
import time
import requests
import random


class Parser:
    # этот класс создан с целью открыть страницу, вытащить название и цены интересующего продукта
    def __init__(self, url):
        self.url = url

    # метод отвечает за парсинг самой страницы и собирает весь ее текс
    def open_html(self):
        html = requests.get(self.url)
        return html.text

    # метод собирает название продукта
    def name_parser(self, html):
        soup = BeautifulSoup(html, "html.parser")

        name_element = soup.find_all(
            "h1", class_="Product__title js-datalayer-catalog-list-name"
        )
        name_element = name_element[0].text.strip(
            '<h1 class="Product__title js-datalayer-catalog-list-name">   '
        )
        return name_element

    # метод собирает текущую цену на товар
    def main_price_parser(self, html):
        soup = BeautifulSoup(html, "html.parser")

        price_element = soup.find_all(
            "span", class_="js-datalayer-catalog-list-price hidden"
        )

        price_element = price_element[0].text.strip(
            '<h class="Product__title js-datalayer-catalog-list-name">   '
        )
        return price_element


def main_parser_engin():
    # запускает парсинг выбранных юрл и выдает словарь, где ключ - имя товара, а значение - его цена

    # ниже идет присвоение url переменным с понятным названием, для упрощения редактирования списка urls
    # coffee_1 = 'https://vkusvill.ru/goods/kofe-zharenyy-molotyy-v-drip-paketakh-braziliya-72854.html'
    # coffee_2 = 'https://vkusvill.ru/goods/kofe-100-arabika-v-filtr-paketakh-6-sht-kafe-36350.html'
    # coffee_3 = 'https://vkusvill.ru/goods/drip-kofe-molotyy-miks-verle-peru-efiopiya-kolumbiya-42356.html'
    coffee_bigest = (
        "https://vkusvill.ru/goods/drip-kofe-yellow-submarine-48-sht-95071.html"
    )
    coffee_biger = (
        "https://vkusvill.ru/goods/drip-kofe-yellow-submarine-24-sht-78591.html"
    )
    mini_cakes = "https://vkusvill.ru/goods/korzinochki-mini-malina-klubnika-s-maslyanym-kremom-4-sht-88403.html"
    pancake_cake = "https://vkusvill.ru/goods/tort-blinnyy-shokoladnyy-29906.html"
    carrot_cake = (
        "https://vkusvill.ru/goods/tort-morkovnyy-s-pekanom-postnyy-24734.html"
    )

    urls = [coffee_biger, coffee_bigest, mini_cakes, pancake_cake, carrot_cake]

    # ниже идут переменные для цикла
    price: str = ""
    name: str = ""
    result: dict = {}

    # этот цикл работает со списком url созданным выше каждый url проходит через парсер в конце цикла есть переменная
    # delay, которая играет роль задержки перед запуском новой итераци, дабы сайт не воспринял нашу программу как бота
    for url in urls:
        parser = Parser(url)

        try:
            html = parser.open_html()
            price = parser.main_price_parser(html)
            name = parser.name_parser(html)
            result.update({name: price})
            print("Данные сохранены")
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            print(result)

        delay = random.uniform(3, 10)
        time.sleep(delay)

    return result
