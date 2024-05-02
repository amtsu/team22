class Date():
    """
    Создайте класс Date, который представляет дату.
    У него должны быть атрибуты для хранения дня, месяца и года.
    Добавьте методы для сравнения двух дат и вычисления разницы между ними.
    """
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        """метод для определения равенства двух дат"""
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __gt__(self, other):
        """метод для определения, что self > other """
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    def __lt__(self, other):
        """метод для определения, что self < other """
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def is_leap_year(self, year):
        """
        проверяем високосный ли год
        """
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
        
    def days_in_months(self, month, year):
        """
        метод проверяет сколько дней в месяце, с учетом високосного года
        """
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if month == 2 and self.is_leap_year(year) == True:
            return 29
      
        return days_in_month[month - 1]
        
        

    def days_since_epoch(self):
        """
        метод считает общее количество дней
        """
        days = 0
        for y in range(1, self.year):    # цикл проходит по всем годам от 1 до года в объукте
            if self.is_leap_year(y):
                days += 366
            else:
                days += 365
        for m in range(1, self.month):   # цикл проходит по месяцам от января до месяца перед указанным месяцем в объекте
            days += self.days_in_months(m, self.year)
        days += self.day
        return days

    def difference(self, other):
        """
        метод считает количество дней между двумя датами
        """
        return abs(self.days_since_epoch() - other.days_since_epoch())