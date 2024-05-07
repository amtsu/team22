#Создайте класс Date, который представляет дату.
#У него должны быть атрибуты для хранения дня, месяца и года.
#Добавьте методы для сравнения двух дат и вычисления разницы между ними.
import datetime
class Date():

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.date = datetime.datetime(year, month, day)

    def __sub__(self, other):
        return (self.date - other.date).days

    def dif (self, other):
        y = (self.date - other.date).days//365
        d = (self.date - other.date).days % 365
        return (y, d)
    def more_than(self, other):
        return (self.date > other.date)

date1 = Date(26,4,1990)
date2 = Date(7,5,2024)

print(date2-date1)

print(date2.dif(date1))