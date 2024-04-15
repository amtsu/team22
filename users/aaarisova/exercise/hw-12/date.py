'''9.Создайте класс Date, который представляет дату. У него должны быть атрибуты для хранения дня, месяца и года. Добавьте методы для сравнения двух дат и вычисления разницы между ними.'''

from datetime import datetime


class Date:

    def __init__(self, year, month, day):
        self.day = day
        self.month = month
        self.year = year
        self.date = datetime(year, month, day)
        

    def __sub__(self, other): 
        '''метод позволяет определить поведение объекта при выполнении вычитания с другим объектом
        "subtraction" - вычитание'''
        return (self.date - other.date).days


    def __lt__(self, other):  #использ для определения поведения при сравнении объектов с помощью оператора <
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
        return False


