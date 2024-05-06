from datetime import datetime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def data_handler(cls, date):
        if not isinstance(date, Date):
            raise TypeError(f'{date} не является объектом класса Date.')
        return datetime(date.year, date.month, date.day)

    def __sub__(self, other):
        return abs(self.data_handler(self) - self.data_handler(other))

    def __eq__(self, other):
        return self.data_handler(self) == self.data_handler(other)

    def __lt__(self, other):
        return self.data_handler(self) < self.data_handler(other)

    def __le__(self, other):
        return self.data_handler(self) <= self.data_handler(other)


if __name__ == "__main__":
    date_1 = Date(2024, 4, 14)
    date_2 = Date(1985, 4, 10)
    date_3 = Date(2024, 4, 14)
    print(date_1 - date_2)
    assert (date_1 == date_3) == True
    assert (date_1 > date_2) == True
    assert (date_1 <= date_2) == False
