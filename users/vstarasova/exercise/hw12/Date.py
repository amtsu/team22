class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def compare_dates(self, other_date):
        if self.year == other_date.year and self.month == other_date.month and self.day == other_date.day:
            return "Даты совпадают"
        elif (self.year, self.month, self.day) > (other_date.year, other_date.month, other_date.day):
            return "Первая дата позже второй"
        else:
            return "Первая дата раньше второй"

    def difference(self, other_date):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total_days_self = self.day
        total_days_other = other_date.day

        for i in range(1, self.month):
            total_days_self += days_in_month[i]
        for i in range(1, other_date.month):
            total_days_other += days_in_month[i]

        total_days_self += self.year * 365 + self.year // 4 - self.year // 100 + self.year // 400
        total_days_other += other_date.year * 365 + other_date.year // 4 - other_date.year // 100 + other_date.year // 400

        return abs(total_days_self - total_days_other)

# Пример использования класса
date1 = Date(20, 4, 2024)
date2 = Date(25, 4, 2024)

print("Результат сравнения дат:", date1.compare_dates(date2))
print("Разница между датами в днях:", date1.difference(date2))
