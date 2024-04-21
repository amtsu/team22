import pytest
from date import Date

def test_date():
    date1 = Date(1998, 5, 15)
    date2 = Date(2000, 4, 16)
    assert date1.compare(date2) == -702