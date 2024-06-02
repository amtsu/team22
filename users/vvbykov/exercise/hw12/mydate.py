from datetime import date

class MyDate:

    def __init__(self, year: int, month: int, day: int):
        self._year = year
        self._month = month
        self._day = day
    
    @property 
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day
    
    def __repr__(self):
        return f"{self.year}-{self.month}-{self.day}"
    
    def __eq__(self, other):
        return (self.year == other.year) and (self.year == other.year) and (self.day == other.day)

    def __sub__(self, other):
        delta = date(self.year, self.month, self.day) - date(other.year, other.month, other.day) 
        return delta.days

