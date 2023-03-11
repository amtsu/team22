#!/usr/local/bin/python
# coding: utf-8
"""
Тесты для модуля getddatafrom
"""
import os
from getdatafrom import WebPage
from getdatafrom import UltraStripper
from getdatafrom import PageElement
#тесты
def test_webpage_str_1():
    """
    Тест создания экземпляра webpage и работоспособности его метода __str__
    """
    assert str(WebPage('test')) == 'url: test, opened: False, error codes: HTTP: 0, URL: 0'
#--------------------------------------------------------------------------------------------------
def test_webpage_str_2():
    """
    Тест создания экземпляра webpage и работоспособности его метода __str__
    """
    assert str(WebPage('test')) != 'url: test, opened: True, error codes: HTTP: 0, URL: 0'
#--------------------------------------------------------------------------------------------------
def test_webpage_last_url_error_1():
    """
    Тест создания экземпляра webpage и свойства last_URL_error_code
    """
    assert WebPage('test').last_url_error_code == 0
#--------------------------------------------------------------------------------------------------
def test_webpage_last_http_error_1():
    """
    Тест создания экземпляра webpage и свойства last_URL_error_code
    """
    assert WebPage('test').last_http_error_code == 0
#--------------------------------------------------------------------------------------------------
def test_webpage_last_error_slow():
    """
    ТЕСТ МЕДЛЕННЫЙ, ходит в интернет
    Тест создания экземпляра webpage, его методов open(), is_open() и свойства last_URL_error_code
    """
    a_page = WebPage('http://moscompass.ru')
    a_page.open()
    assert a_page.is_open()
    assert a_page.last_url_error_code == 200
#--------------------------------------------------------------------------------------------------
def test_webpage_last_error_slow_2():
    """
    ТЕСТ МЕДЛЕННЫЙ, ходит в интернет
    Тест создания экземпляра webpage, его методов open(), is_open() и свойства last_HTTP_error_code
    """
    a_page = WebPage('http://moscompass.ru/notexists.html')
    a_page.open()
    assert not a_page.is_open()
    assert a_page.last_http_error_code == 404
#--------------------------------------------------------------------------------------------------
def test_webpage_open_1():
    """
    ТЕСТ СОЗДАЕТ ФАЙЛ В ТЕКУЩЕМ КАТАЛОГЕ И ПОТОМ УДАЛЯЕТ ЕГО
    Тест создания экземпляра webpage, его методов open(), is_open()
    """
    test_html =  '<html><head><meta charset="utf-8"></head><body>'
    test_html += '<div class=\"test\">some text</div>'
    test_html += '<div class=\"price\">1 345р.</div></body></html>'
    filename = os.getcwd() + '/test.html'
    assert not os.path.exists(filename)
    with open(filename,'w',encoding='utf-8') as output_file:
        output_file.write(test_html)
    a_page = WebPage('file://' + filename)
    text = a_page.open().decode('utf-8')
    os.remove(filename)
    assert a_page.is_open()
    assert text == test_html# + 'fail'
#--------------------------------------------------------------------------------------------------
def test_ultra_stripper_1():
    """
    тест работы стриппера - очистка строки от нежелательных символов
    """
    inputdata = '6 500 ₽    '
    superstripper = UltraStripper([' ','\u20bd','\xa0'])
    assert superstripper(inputdata) == '6500'
#--------------------------------------------------------------------------------------------------
def test_ultra_stripper_2():
    """
    тест работы стриппера - метода __str__
    """
    superstripper = UltraStripper([' ','\u20bd','\xa0'])
    assert str(superstripper) == ' ,\u20bd,\xa0'
#--------------------------------------------------------------------------------------------------
def test_ultra_stripper_3():
    """
    тест работы стриппера - очистка строки от нежелательных символов
    """
    inputdata = 'h1e2l3l4o5 6w7o8r9l0d'
    superstripper = UltraStripper(list('hello world'))
    assert superstripper(inputdata) == '1234567890'
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
    