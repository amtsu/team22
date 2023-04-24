"""
модуль, содержащий описание одной записи в телефонной книге
"""
from usefulstuff import ColoredStr


class PhoneBookRecord:
    """
    класс, описывающий одну запись в телефонной книге
    """

    def __init__(self, name: str, phone_number: str, city: str) -> None:
        """
        Конструктор класса
        :param name:
        :param phone_number:
        :param city:
        """
        self.__name = name
        self.__phone_number = phone_number
        self.__city = city

    @property
    def name(self):
        return self.__name

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def city(self):
        return self.__city

    def __str__(self):
        """
        возвращает строковое представление данных этого класса
        :return:
        """
        green_str = ColoredStr("green, bold")
        blue_str = ColoredStr("blue")
        yellow_str = ColoredStr("yellow, bold")
        return f"name: {green_str(self.__name)}, phone number: {blue_str(self.__phone_number)}, city: {yellow_str(self.__city)}"
    def getcsv(self):
        """
        возвращает строку с csv-представлением данных класса
        :return:
        """
        return f"{self.__name}, {self.__phone_number}, {self.city},"
