#Создайте класс Date, который представляет дату. У него должны быть атрибуты для хранения дня, месяца и года. Добавьте методы для сравнения двух дат и вычисления разницы между ними.

from datetime import datetime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.date = datetime (year, month, day)

    def compare_days (self, other):
        result = ''
        if self.date > other.date:
            result = 'больше'
        elif self.date < other.date:
            result = 'меньше'
        elif self.date == other.date:
            result = 'равны' 
        return result

    def difference_dates (self, other):
        return (self.date - other.date).days