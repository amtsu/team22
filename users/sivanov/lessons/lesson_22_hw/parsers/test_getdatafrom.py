#!/usr/local/bin/python
# coding: utf-8
"""
Тесты для модуля getddatafrom
"""
import os
from bs4 import (  # pylint: disable=E0401 #не проверять на корректность импорта
    BeautifulSoup,
)
from getdatafrom import (  # pylint: disable=E0401 #не проверять на корректность импорта
    WebPage,
)
from getdatafrom import (  # pylint: disable=E0401 #не проверять на корректность импорта
    UltraStripper,
)
from getdatafrom import (  # pylint: disable=E0401 #не проверять на корректность импорта
    TagValue,
)
from getdatafrom import (  # pylint: disable=E0401 #не проверять на корректность импорта
    PageElement,
)

# тесты
def test_webpage_str_1():
    """
    Тест создания экземпляра webpage и работоспособности его метода __str__
    """
    assert (
        str(WebPage("test"))
        == "url: test, opened: False, error codes: HTTP: 0, URL: 0, socket: 0"
    )


# --------------------------------------------------------------------------------------------------
def test_webpage_str_2():
    """
    Тест создания экземпляра webpage и работоспособности его метода __str__
    """
    assert (
        str(WebPage("test"))
        != "url: test, opened: True, error codes: HTTP: 0, URL: 0, socket: 0"
    )


# --------------------------------------------------------------------------------------------------
def test_webpage_last_url_error_1():
    """
    Тест создания экземпляра webpage и свойства last_URL_error_code
    """
    assert WebPage("test").last_url_error_code == 0


# --------------------------------------------------------------------------------------------------
def test_webpage_last_http_error_1():
    """
    Тест создания экземпляра webpage и свойства last_URL_error_code
    """
    assert WebPage("test").last_http_error_code == 0


# --------------------------------------------------------------------------------------------------
def test_webpage_last_error_slow():
    """
    ТЕСТ МЕДЛЕННЫЙ, ходит в интернет
    Тест создания экземпляра webpage, его методов open(), is_open() и свойства last_URL_error_code
    """
    a_page = WebPage("http://moscompass.ru")
    a_page.open()
    assert a_page.is_open()
    assert a_page.last_url_error_code == 200


# --------------------------------------------------------------------------------------------------
def test_webpage_last_error_slow_2():
    """
    ТЕСТ МЕДЛЕННЫЙ, ходит в интернет
    Тест создания экземпляра webpage, его методов open(), is_open() и свойства last_HTTP_error_code
    """
    a_page = WebPage("http://moscompass.ru/notexists.html")
    a_page.open()
    assert not a_page.is_open()
    assert a_page.last_http_error_code == 404


# --------------------------------------------------------------------------------------------------
def test_webpage_open_1():
    """
    ТЕСТ СОЗДАЕТ ФАЙЛ В ТЕКУЩЕМ КАТАЛОГЕ И ПОТОМ УДАЛЯЕТ ЕГО
    Тест создания экземпляра webpage, его методов open(), is_open()
    """
    test_html = '<html><head><meta charset="utf-8"></head><body>'
    test_html += '<div class="test">some text</div>'
    test_html += '<div class="price">1 345р.</div></body></html>'
    filename = os.getcwd() + "/test.html"
    assert not os.path.exists(filename)
    with open(filename, "w", encoding="utf-8") as output_file:
        output_file.write(test_html)
    a_page = WebPage("file://" + filename)
    text = a_page.open().decode("utf-8")
    os.remove(filename)
    assert a_page.is_open()
    assert text == test_html  # + 'fail'


# --------------------------------------------------------------------------------------------------
def test_ultra_stripper_1():
    """
    тест работы стриппера - очистка строки от нежелательных символов
    """
    inputdata = "6 500 ₽    "
    superstripper = UltraStripper([" ", "\u20bd", "\xa0"])
    assert superstripper(inputdata) == "6500"


# --------------------------------------------------------------------------------------------------
def test_ultra_stripper_2():
    """
    тест работы стриппера - метода __str__
    """
    superstripper = UltraStripper([" ", "\u20bd", "\xa0"])
    assert str(superstripper) == " ,\u20bd,\xa0"


# --------------------------------------------------------------------------------------------------
def test_ultra_stripper_3():
    """
    тест работы стриппера - очистка строки от нежелательных символов
    """
    inputdata = "h1e2l3l4o5 6w7o8r9l0d"
    superstripper = UltraStripper(list("hello world"))
    assert superstripper(inputdata) == "1234567890"


# --------------------------------------------------------------------------------------------------
def test_tag_value_1():
    """
    тест класса TagValue
    тестирование получения корректного значения тэга
    """
    expected_tag_value = "The Dormouse's story caption"
    expected_parameter_value = "Testing"
    html_doc = (
        f"<html><head><title>The Dormouse's story</title></head>"
        f"<body>"
        f'<p class="Caption" purpose="{expected_parameter_value}"><b>'
        f"{expected_tag_value}</b></p>"
        f"</body></html>"
    )
    soup = BeautifulSoup(html_doc, features="html.parser")
    tag_value = TagValue()
    assert tag_value.get(soup.p.b) == expected_tag_value


# --------------------------------------------------------------------------------------------------
def test_tag_value_2():
    """
    тест класса TagValue
    тестирование получения некорректного значения тэга - так я планировал, но не вышло
    получаем по-прежнему корректное значение
    """
    expected_tag_value = "The Dormouse's story caption"
    expected_parameter_value = "Testing"
    html_doc = (
        f"<html><head><title>The Dormouse's story</title></head>"
        f"<body>"
        f'<p class="Caption" purpose="{expected_parameter_value}"><b>'
        f"{expected_tag_value}</b></p>"
        f"</body></html>"
    )
    soup = BeautifulSoup(html_doc, features="html.parser")
    tag_value = TagValue()
    # прикол на приколе
    # значения soup.p.text и soup.p.b.text ОДИНАКОВЫЕ
    # скорее всего это фича и нужно больше узнать про bs4
    assert tag_value.get(soup.p) == expected_tag_value


# --------------------------------------------------------------------------------------------------
def test_tag_value_3():
    """
    тест класса TagValue
    тестирование получения корректного значения параметра тэга
    """
    expected_tag_value = "The Dormouse's story caption"
    expected_parameter_value = "Testing"
    html_doc = (
        f"<html><head><title>The Dormouse's story</title></head>"
        f"<body>"
        f'<p class="Caption" purpose="{expected_parameter_value}"><b>'
        f"{expected_tag_value}</b></p>"
        f"</body></html>"
    )
    soup = BeautifulSoup(html_doc, features="html.parser")
    tag_value = TagValue("purpose")
    assert tag_value.get(soup.p) == expected_parameter_value


# --------------------------------------------------------------------------------------------------
def test_tag_value_4():
    """
    тест класса TagValue
    тестирование получения некорректного значения параметра тэга
    """
    expected_tag_value = "The Dormouse's story caption"
    expected_parameter_value = "Testing"
    html_doc = (
        f"<html><head><title>The Dormouse's story</title></head>"
        f"<body>"
        f'<p class="Caption" purpose="{expected_parameter_value}"><b>'
        f"{expected_tag_value}</b></p>"
        f"</body></html>"
    )
    soup = BeautifulSoup(html_doc, features="html.parser")
    tag_value = TagValue("purpose")
    assert not tag_value.get(soup.p.b) == expected_parameter_value


# --------------------------------------------------------------------------------------------------
def test_page_element_1():
    """
    тест класса PageElement
    тест получения нормального значения тэга
    """
    item_alias = "Цена"
    item_data = {
        "id": "Caption",
        "tagname": "p",
        "index": 0,
        "what": "",
        "stripper_setting": "₽",
    }
    expected_tag_value = "The Dormouse's story caption"
    expected_parameter_value = "Testing"
    html_doc = (
        f"<html><head><title>The Dormouse's story</title></head>"
        f"<body>"
        f'<p class="Caption" purpose="{expected_parameter_value}"><b>'
        f"{expected_tag_value}</b></p>"
        f"</body></html>"
    )
    page_element = PageElement(item_alias, item_data)
    soup = BeautifulSoup(html_doc, features="html.parser")
    assert page_element(soup) == expected_tag_value


# --------------------------------------------------------------------------------------------------
def test_page_element_2():
    """
    тест класса PageElement
    тест получения нормального значения параметра тэга
    """
    item_alias = "Цена"
    item_data = {
        "id": "Caption",
        "tagname": "p",
        "index": 0,
        "what": "purpose",
        "stripper_setting": "₽",
    }
    expected_tag_value = "The Dormouse's story caption"
    expected_parameter_value = "Testing"
    html_doc = (
        f"<html><head><title>The Dormouse's story</title></head>"
        f"<body>"
        f'<p class="Caption" purpose="{expected_parameter_value}"><b>'
        f"{expected_tag_value}</b></p>"
        f"</body></html>"
    )
    page_element = PageElement(item_alias, item_data)
    soup = BeautifulSoup(html_doc, features="html.parser")
    assert page_element(soup) == expected_parameter_value


# --------------------------------------------------------------------------------------------------
def test_page_element_3():
    """
    тест класса PageElement
    тест получения неправильного значения параметра тэга
    """
    item_alias = "Цена"
    item_data = {
        "id": "Caption",
        "tagname": "p",
        "index": 0,
        "what": "purpose",
        "stripper_setting": "₽, ,T",
    }
    expected_tag_value = "The Dormouse's story caption"
    expected_parameter_value = "Testing"
    html_doc = (
        f"<html><head><title>The Dormouse's story</title></head>"
        f"<body>"
        f'<p class="Caption" purpose="{expected_parameter_value}"><b>'
        f"{expected_tag_value}</b></p>"
        f"</body></html>"
    )
    page_element = PageElement(item_alias, item_data)
    soup = BeautifulSoup(html_doc, features="html.parser")
    assert not page_element(soup) == expected_parameter_value


# --------------------------------------------------------------------------------------------------
def test_page_element_4():
    """
    тест класса PageElement
    тест item_alias
    """
    item_alias = "Цена"
    item_data = {
    }
    page_element = PageElement(item_alias, item_data)
    assert page_element.item_alias == item_alias


# --------------------------------------------------------------------------------------------------
