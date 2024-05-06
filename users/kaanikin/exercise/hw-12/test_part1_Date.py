import pytest
from part1_Date import Date 


a_date = Date(12,4,2024)
another_date = Date(12,4,2024)
third_date = Date(11,4,2030)

def test_date_delta():
    expected = 'Даты равны!'
    assert a_date.dateDelta(another_date) == expected

def test_date_delta1():
    expected = 'Разница между датами: 6 лет, 0 месяцев, 1 дней.'
    assert a_date.dateDelta(third_date) == expected

def test_dateComparrison1():
    expected = 'Дата: 12/4/2024 меньше чем 11/4/2030'
    assert a_date.dateComparrison(third_date) == expected

def test_dateComparrison2():
    expected = 'Дата: 11/4/2030 больше чем 12/4/2024'
    assert third_date.dateComparrison(a_date) == expected