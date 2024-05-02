import pytest
from datetime import datetime, date

from dates import Date

@pytest.mark.parametrize("date1, date2,  expected",[
    ([30,4,2024], date(2024,4,30), "Равны"),
    ([1,4,2024], date(2024,4,30), "Меньше"),
    ([3,5,2024], date(2024,4,30), "Больше")
])

def test_compare_date(date1, date2,  expected):
    current_date = Date(*date1)
    assert current_date.compare_date(date2) == expected

@pytest.mark.parametrize("date1, date2,  expected",[
    ([30,4,2024], date(2024,4,30), 0),
    ([1,4,2024], date(2024,4,30), 29),
    ([3,5,2024], date(2024,4,30), 3)
])

def test_count_diff(date1, date2,  expected):
    current_date = Date(*date1)
    assert current_date.count_diff(date2) == expected
