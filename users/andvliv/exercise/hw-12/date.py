#Создайте класс Date, который представляет дату. У него должны быть атрибуты для хранения дня, месяца и года. Добавьте методы для сравнения двух дат и вычисления разницы между ними.
from datetime import datetime
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.date = datetime(year, month, day)

    def compare(self, other_date):
        return (self.date - other_date.date).days
