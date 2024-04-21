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
        
#Создадим объект данного класса
date1 = Date(1998, 5, 15)
date2 = Date(2000, 4, 16)

print(date1.compare(date2))