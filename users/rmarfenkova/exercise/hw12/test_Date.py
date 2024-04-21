import pytest
from class_Date import Date

@pytest.mark.parametrize("day1, month1, year1, day2, month2, year2, expected_difference", [
    (1, 1, 2022, 1, 1, 2022, 0),  
    (1, 1, 2022, 2, 1, 2022, 1),  
    (1, 1, 2022, 31, 12, 2021, 1),
    (1, 1, 2020, 31, 12, 2020, 365),
    (1, 1, 1931, 31, 12, 1931, 364)
 
])
def test_difference(day1, month1, year1, day2, month2, year2, expected_difference):
    date1 = Date(day1, month1, year1)
    date2 = Date(day2, month2, year2)
    assert date1.difference(date2) == expected_difference

def test_leap_year():
    assert Date(29, 2, 2020).is_leap_year(2020) == True
    assert Date(29, 2, 1900).is_leap_year(1900) == False
    assert Date(29, 2, 2000).is_leap_year(2000) == True

def test_days_in_months():
    assert Date(1, 1, 2021).days_in_months(2, 2021) == 28
    assert Date(1, 1, 2020).days_in_months(2, 2020) == 29
    assert Date(1, 3, 2021).days_in_months(3, 2021) == 31
    assert Date(1, 4, 2021).days_in_months(4, 2021) == 30
    assert Date(1, 5, 2021).days_in_months(5, 2021) == 31

def test_comparison():
    assert Date(1, 1, 2021) == Date(1, 1, 2021)
    assert Date(1, 1, 2021) < Date(1, 2, 2021)
    assert Date(1, 1, 2021) > Date(1, 1, 2020)
    assert Date(1, 1, 2021) != Date(1, 1, 2020)

