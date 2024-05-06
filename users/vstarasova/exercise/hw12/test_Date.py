import pytest
from Date import Date

def test_compare_dates():
    date1 = Date(20, 4, 2024)
    date2 = Date(25, 4, 2024)
    assert date1.compare_dates(date2) == "Первая дата раньше второй"

    print("Тест для метода compare_dates пройден успешно!")

def test_difference():
    date1 = Date(20, 4, 2024)
    date2 = Date(25, 4, 2040)
    assert date1.difference(date2) == 5849
    
    print("Тест для метода difference пройден успешно!")
