#!/usr/local/bin/python
# coding: utf-8
"""
    модуль с полезными функциями/классами, которые когда-то были написаны
    на момент написания коммента было три класса:
    LocalLog - управление отладочной печатью. можно быстро включить-отключить
    ColoredStr - печать в консоль цветного текста на цветном фоне
    HandmadeTestDecorator - декоратор для тестов пайтеста, чтобы можно было их вызывать как
функции внутри модуля последовательно (наверное, больше не нужен)
"""
import random

# ---------------------------------------------------------------------------------
class LocalLog:
    """
    LocalLog выводит сообщения в консоль. Или не выводит, смотря как его инициализировать
    """

    def __init__(self, show_messages=True):
        self.__show_messages = show_messages

    def __call__(self, a_message):
        if self.__show_messages:
            print(a_message)

    def __str__(self):
        return f"Showing log messages: {self.__show_messages}"


# ---------------------------------------------------------------------------------
class ColoredStr:
    """
    Выводит текст в соответствующем модном формате, потом отменяет его
    коды можно посмотреть в https://habr.com/ru/sandbox/158854/
    """

    def __init__(self, format_string):
        self.__format_string = str("")
        colours_and_style = {
            # __text colours
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "violet": "\033[35m",
            "navy": "\033[36m",
            "white": "\033[37m",
            # background_colours
            "back_black": "\033[40m",
            "back_red": "\033[41m",
            "back_green": "\033[42m",
            "back_yellow": "\033[43m",
            "back_blue": "\033[44m",
            "back_violet": "\033[45m",
            "back_navy": "\033[46m",
            "back_white": "\033[47m",
            # styles
            "default": "\033[0m",
            "bold": "\033[1m",
            "light": "\033[2m",
            "italic": "\033[3m",
            "underlined": "\033[4m",
            "blinked": "\033[5m",
            "insane": "\033[6m",
            "inversed": "\033[7m",
        }
        lcase_format_string = format_string.lower()
        lcase_format_list = lcase_format_string.split(",")
        for specifier in lcase_format_list:
            if specifier.strip() in colours_and_style:  # keys() is not necessary
                # for iteration
                self.__format_string += colours_and_style[specifier.strip()]
        self.__format_string += "{}\033[0m"

    def __call__(self, text):
        return (self.__format_string).format(text)

    def __str__(self):
        return self.__format_string.format("test")


# ---------------------------------------------------------------------------------
class HandmadeTestDecorator:
    """
    декоратор для тестов с assert, чтобы и пайтест работал, и ручные поделки
    """

    def __init__(self, failed, passed):
        self.__failed = failed
        self.__passed = passed

    def __call__(self, decorated_function):
        def wrapper(*args, **kvargs):
            try:
                decorated_function(*args, **kvargs)
            except:  # pylint: disable=bare-except # не только AssertionError а вообще любые исключения
                result = self.__failed
                # raise #дальше ошибку пускать не будем, дадим остальным тестам тоже поработать
            else:
                result = self.__passed
            result += " : " + str(decorated_function.__name__)
            return result

        return wrapper

    def __str__(self):
        return "HandmadeTestDecorator"


# ---------------------------------------------------------------------------------
def generate_random_list(count, fixed=False):
    """
        # функция возвращает список псевдослучайными чисел из
    # диапазона от 1 до count; длина списка равна count
    # параметр fixed позволяет создавать одинаковый
    # список от запуска к запуску ( при fixed =True)
    # или разные от запуска к запуску (fixed = False
    """
    list_rezult = []
    if fixed:
        random.seed(15432)
    else:
        random.seed()
    list_rezult = list(random.randint(0, count) for i in range(0, count))
    return list_rezult
