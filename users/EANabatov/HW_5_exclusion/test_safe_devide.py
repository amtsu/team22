import pytest

from safe_divide import safe_divide_ver_2

def test_input():
    assert safe_divide_ver_2(1, 1) == 1


def test_input2():
    assert safe_divide_ver_2(2, 1) == 2

def test_exception():
    with pytest.raises(ZeroDivisionError):
        safe_divide_ver_2(3, 0)