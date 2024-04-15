import pytest
from date import Date
from datetime import datetime


def test_date_initialization():
    date = Date(2005, 7, 1)
    assert date.day == 1
    assert date.month == 7
    assert date.year == 2005
    assert date.date == datetime(2005, 7, 1)


def test_subtraction_1():
    '''тест вычисления разницы между двумя датами'''
    date_1 = Date(2023, 12, 31) 
    date_2 = Date(2022, 12, 31)  
    assert date_1.__sub__(date_2) == 365


def test_subtraction_2():  #негативный
    '''тест вычисления разницы между двумя датами'''
    with pytest.raises(ValueError):
        date_1 = Date(2023, -4, 31) 
        date_2 = Date(2022, -4, 31)  
        date_1.__sub__(date_2)


def test_subtraction_3():  #негативный
    '''тест вычисления разницы между двумя датами'''
    with pytest.raises(ValueError):
        date_1 = Date(2023, 0, 31) 
        date_2 = Date(2022, 0, 31)  
        date_1.__sub__(date_2)


def test__lt_1():
    '''тест функции сравнения дата_1 < дата_2'''
    date_1 = Date(2023, 2, 1) 
    date_2 = Date(2022, 12, 31)     
    assert date_1.__lt__(date_2) == False


def test__lt_2():
    '''тест функции сравнения дата_1 < дата_2'''
    date_1 = Date(2022, 12, 31) 
    date_2 = Date(2023, 2, 1)     
    assert date_1.__lt__(date_2) == True
    

def test__lt_3():
    '''тест функции сравнения дата_1 < дата_2'''
    date_1 = Date(2023, 2, 1) 
    date_2 = Date(2023, 2, 1)     
    assert date_1.__lt__(date_2) == False
    