
import pprint
import undetected_chromedriver as uc
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def get_general_categories_from_lenta() -> list[dict[str, str]]:
    """Получает список категорий из товаров из каталога Ленты"""
    BASE_URL = "https://www.lenta.com"
    LENTA_CATALOG = "https://www.lenta.com/catalog/"
    CATEGORIES_CARDS = "group-card"

    # формируем настройки для хрома
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')  # отключает открытие браузера
    options.add_argument('--window-size=1280x1696')
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    # создаем экземпляр класса браузера с заданными настройками
    chrome = uc.Chrome(options=options)

    try:
        # пробуем получить страницу каталога
        chrome.get(f"{LENTA_CATALOG}")
        # даем время на загрузку страницы
        time.sleep(1)
        # получаем html страницы
        html = chrome.page_source
        # варим суп
        lenta_soup = BeautifulSoup(html, "lxml")
    except AttributeError as e:
        print(f"Неудалось получить общий каталог, ошибка - {e}")

    # находим все основные категории товаров с страницы
    general_categories = lenta_soup.find_all("a", class_=CATEGORIES_CARDS, href=True)

    # в список будем складывать словарь с данными
    general_categories_list = []

    # проходим по списку основного каталога
    for category in general_categories:
    # извлекаем из него: название категонии, ссылку на категорию
        categories = {
            "category_name": category["ga-event-label"],
            "link": BASE_URL + category["href"],
            }
    # добавляем полученный словарь в список 
        general_categories_list.append(categories)
    return general_categories_list


def goods_from_first_page_category(general_categories_list: list[dict[str, str]]) -> list[dict[str, str]]:
    """Получает список товаров по категории (только с первой страницы)"""
    PRODUCT_CARDS = "lui-sku-product-card-text lui-sku-product-card-text--view-primary"
    FIRST_PRICE = "lui-priceText lui-priceText--view_regular"
    SECOND_PRICE = "lui-priceText lui-priceText--view_secondary"

    # формируем настройки для хрома
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')  # отключает открытие браузера
    options.add_argument('--window-size=1280x1696')
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    # создаем экземпляр класса браузера с заданными настройками
    chrome = uc.Chrome(options=options)

    # в список будем складывать словарь с данными
    categories_list = []

    # проходим по списку с словарем основного каталога
    for category in general_categories_list:
        try:
            # по ссылке поулачаем html каталога товара
            chrome.get(f"{category['link']}")
            # даем время на загрузку страницы
            time.sleep(1)
            # получаем html страницы
            html = chrome.page_source
            # варим суп
            lenta_category_soup = BeautifulSoup(html, "lxml", from_encoding="UTF-8")
        except AttributeError as e:
            print(f"Неудалось получить каталог {category['category_name']}, ошибка - {e}")

        # в подготовленной странице каталога находим:
            # все названия товаров
            # цены товаров по карте
            # цены товаров без карты
        try:
            goods_names = lenta_category_soup.find_all("div", class_= PRODUCT_CARDS)
        except:
            goods_names = ""
        try:
            first_prices = lenta_category_soup.find_all("div", FIRST_PRICE)
        except:
            first_prices = ""
        try:
            second_prices = lenta_category_soup.find_all("div", SECOND_PRICE)
        except:
            second_prices = ""

        # единцм циклом проходим по всем полученным спискам 
        # и добавляем найденную информацию в словарь
        for (goods_name, first_price, second_price) in zip(goods_names, first_prices, second_prices):
            goods_info = {
                "goods_name": goods_name.get_text(),
                "first_price": first_price.get_text(separator=" ", strip=True),
                "second_price": second_price.get_text(separator=" ", strip=True),
            }
            # добавляем полученный словарь в список
            categories_list.append(goods_info)

        # заносим подготовленный список в изначальный словарь категорий
        category.update({"info": categories_list})
    return general_categories_list


def main():
    """менеджерит функции"""
    general_categories = get_general_categories_from_lenta()
    goods_from_first_page_each_category = goods_from_first_page_category(general_categories)

    # подсмотрено у Алехандро
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(goods_from_first_page_each_category)


if __name__ == "__main__":
    main()

