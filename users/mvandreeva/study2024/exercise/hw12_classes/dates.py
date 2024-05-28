from datetime import datetime, date

class Date:
    """
    Класс, который представляет дату. 
    У него должны быть атрибуты для хранения дня, месяца и года. 
    Добавьте методы для сравнения двух дат и вычисления разницы между ними
    """
    def __init__(self, day, month, year):
        self.__date = date(year, month, day)
        print(self.__date)
        self.__day = day
        self.__month = month
        self.__year = year

    def compare_date(self, compared_date):
        """
        Метод сравнения двух дат
        """
        result = ""
        if isinstance(compared_date, date):
            if self.__date > compared_date:
                result = "Больше"
            elif self.__date < compared_date:
                result = "Меньше"
            elif self.__date == compared_date:
                result = "Равны"
        return result

    def count_diff(self, compared_date):
        """
        Метод  вычисления разницы между датами в днях
        """
        if isinstance(compared_date, date):
            result = abs(self.__date - compared_date).days
            return result