import pytest
from date import Date


def test_date_initialization():
    date = Date(1, 7, 2005)
    assert (date.day, date.month, date.year) == (1, 7, 2005)


def test_string():
    '''тест функции преобразование в строку'''
    date = Date(13, 4, 2021)   
    assert date.__str__() == '13.4.2021'


def test_equal_1():
    '''тест функции сравнения двух дат'''
    date_1 = Date(3, 12, 1800) 
    date_2 = Date(1, 10, 1900) 
    assert date_1.__eq__(date_2) == False


def test_equal_2():
    '''тест функции сравнения двух дат-2'''
    date_1 = Date(5, 6, 2000) 
    date_2 = Date(5, 6, 2000) 
    assert date_1.__eq__(date_2) == True


def test_lessthan():
    '''тест функции сравнения дата_1 < дата_2'''
    date_1 = Date(1, 2, 2023) 
    date_2 = Date(31, 12, 2022)     
    assert date_1.__lt__(date_2) == False

def test_subtraction():
    '''тест вычисления разницы между двумя датами (приблизительный, месяц=30 дней, нет високос)'''
    date_1 = Date(1, 2, 1000) 
    date_2 = Date(10, 1, 2000)  
    assert date_1.__sub__(date_2) == 364979

    #days_self = 1+ 2 * 30 + 1000 * 365 = 61+365000 = 365.061
    #days_other = 10 + 30 + 2000 * 365 = 730.040

    

