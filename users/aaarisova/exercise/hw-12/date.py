'''9.Создайте класс Date, который представляет дату. У него должны быть атрибуты для хранения дня, месяца и года. Добавьте методы для сравнения двух дат и вычисления разницы между ними.'''

from datetime import datetime


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):  #преобраз в стр
        return f"{self.day}.{self.month}.{self.year}"


    def __eq__(self, other): #для определения поведения при сравнении объектов с помощью оператора ==.
        return self.day == other.day and self.month == other.month and self.year == other.year


    def __lt__(self, other):  #использ для определения поведения при сравнении объектов с помощью оператора <
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
        return False


    def __sub__(self, other): #приблизительно (30дней и 365)
        '''метод позволяет определить поведение объекта при выполнении вычитания с другим объектом
        "subtraction" - вычитание'''
        days_self = self.day + self.month * 30 + self.year * 365
        days_other = other.day + other.month * 30 + other.year * 365
        return abs(days_self - days_other) #для получения абсолютного значения числа или выражения


