import os
# import traceback
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver

# Импортируем классы для Chrome. Если у вас другой браузер - измените импорт.
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Если у вас установлен другой браузер - импортируйте нужный драйвер.
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import IEDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.opera import OperaDriverManager

# DJANGO_URL = 'http://158.160.172.156/'
# TEST_URL = 'https://ozon.ru/t/rRw3MDq'
# TEST_URL = 'https://twentysix.ru/blog/stuff/143819.html'
# TEST_URL = 'https://admarginem.ru/product/teoriya-kino-kratkij-putevoditel/'
# TEST_URL = 'https://www.ozon.ru/product/
# zen-and-the-art-of-motorcycle-maintenance-dzen-i-iskusstvo-obsluzhivaniya-mototsiklov-kniga-na-1639529508/'
TEST_URL = "https://kuper.ru/products/26157296-smetana-30-250-g"
# USERNAME = 'somany'
# PASSWORD = 'somany123'
PAUSE_DURATION_SECONDS = 1


def parse_price_admarginem(url):
    # Проверка и установка (или обновление) драйвера
    # для Chrome через DriverManager.
    service = Service(executable_path=ChromeDriverManager().install())
    # Запуск веб-драйвера для Chrome.
    driver = webdriver.Chrome(service=service)

    # Открытие страницы по заданному адресу.
    driver.get(url)
    # Развёртывание окна на полный экран.
    driver.maximize_window()
    # Здесь и далее паузы, чтобы рассмотреть происходящее.
    sleep(PAUSE_DURATION_SECONDS)

    os.makedirs("test_stuff", exist_ok=True)

    driver.save_screenshot("test_stuff/screenshot.png")

    sleep(PAUSE_DURATION_SECONDS)

    html = driver.page_source

    with open("test_stuff/output.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("HTML сохранен в файл output.html")

    try:
        soup = BeautifulSoup(html, "html.parser")

        # ad_margimem_parser
        # ad_margimem_parser
        pr = soup.find(class_="woocommerce-Price-amount amount")
        # json_script = soup.find('script', type='application/ld+json')
        price_text = pr.get_text(strip=True)
        # Удалить символ валюты и пробелы, если нужно
        price_value = price_text.split()[0]  # Получить первое слово
        return price_value
    except Exception as e:
        print("Не удалось найти")
        print(f"Ошибка: {e}")
        # traceback.print_exc()

    # print(pr)

    # # Поиск первого поста на странице по классу.
    # first_post = driver.find_element(By.CLASS_NAME, 'card-text')
    # # Вывод текста найденного элемента в терминал.
    # print(first_post.text)
    # Закрытие веб-драйвера.
    driver.quit()

    return "не удалось найти"


if __name__ == "__main__":
    parse_price_admarginem(TEST_URL)
