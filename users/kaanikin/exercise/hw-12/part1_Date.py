class Date:
    """
    Создайте класс Date, который представляет дату. У него должны быть атрибуты для хранения дня, месяца и года. Добавьте методы для сравнения двух дат и вычисления разницы между ними.
    """
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def __repr__(self):
        return f"date: {self.__day}/{self.__month}/{self.__year}"
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("объекты Date можно стравнить только между собой")
        return (self.__day == other.__day) and (self.__month == other.__month) and (self.__year == other.__year)
    
    def dateComparrison(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("объекты Date можно стравнить только между собой")
        if self.__year != other.__year :
            if self.__year == max(self.__year, other.__year):
                return f"Дата: {self.__day}/{self.__month}/{self.__year} больше чем {other.__day}/{other.__month}/{other.__year}"
            elif self.__year == min(self.__year, other.__year):
                return f"Дата: {self.__day}/{self.__month}/{self.__year} меньше чем {other.__day}/{other.__month}/{other.__year}"    
            else:
                if self.__month == max(self.__month, other.__month):
                    return f"Дата: {self.__day}/{self.__month}/{self.__year} больше чем {other.__day}/{other.__month}/{other.__year}"
                elif self.__month == min(self.__month, other.__month):
                    return f"Дата: {self.__day}/{self.__month}/{self.__year} меньше чем {other.__day}/{other.__month}/{other.__year}"
                else:
                    if self.__day == max(self.__day, other.__day):
                        return f"Дата: {self.__day}/{self.__month}/{self.__year} больше чем {other.__day}/{other.__month}/{other.__year}"
                    else:
                        self.__day == min(self.__day, other.__day)
                        return f"Дата: {self.__day}/{self.__month}/{self.__year} меньше чем {other.__day}/{other.__month}/{other.__year}"
            
    def dateDelta(self, other):        
        if not isinstance(other, self.__class__):
            raise TypeError("объекты Date можно стравнить только между собой")
        if self.__year != other.__year :
            return f"Разница между датами: {abs(self.__year - other.__year)} лет, {abs(self.__month - other.__month)} месяцев, {abs(self.__day - other.__day)} дней."
        else:
            return 'Даты равны!'        
                        
            
"""            
            
            
            year1 = self.__year*1000 + self.__month*100 + self.__day
            year2 = other.__year*1000 + other.__month*100 + other.__day

            if year1 > year2:
                return f"Дата: {self.__day}/{self.__month}/{self.__year} больше чем {other.__day}/{other.__month}/{other.__year}"

            else:
                f"Дата: {self.__day}/{self.__month}/{self.__year} меньше чем {other.__day}/{other.__month}/{other.__year}"

        else:
             f"Дата: {self.__day}/{self.__month}/{self.__year} равна {other.__day}/{other.__month}/{other.__year}"   
"""        
            
    
"""            
            
            
            
"""            

            

"""a_date = Date(12,4,2024)
another_date = Date(12,4,2024)
third_date = Date(11,4,2024)
test1 = a_date.dateDelta(a_date, another_date)
print(a_date)
print(another_date)
print(third_date)
print(a_date == another_date)
print(a_date == third_date)    
print(test1)"""