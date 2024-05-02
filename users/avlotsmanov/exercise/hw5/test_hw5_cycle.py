import pytest
from hw5_cycle import *

#тесты функции print_squares_while
@pytest.mark.parametrize(
    'input_number, expected_result',
    [
        (11, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]),
        (-11, 'Ошибка! Число должно быть больше нуля'),
        (0, 'Ошибка! Число должно быть больше нуля'),
    ]
)

def test_print_squares_while_positive(input_number, expected_result):
    assert print_squares_while(input_number) == expected_result

@pytest.mark.parametrize(
    'input_number, expected_exception',
    [
        ('455',TypeError),
        (0.7, TypeError),
        ([213, 'sd'], TypeError),
    ]
)

def test_print_squares_while_negative(input_number, expected_exception):
    with pytest.raises(expected_exception):
        print_squares_while(input_number)

#тесты функции print_factorial
@pytest.mark.parametrize(
    'input_number, expected_result',
    [
        (9, 362880),
        (0, 1),
        (1, 1),
    ]
)

def test_print_factorial_while_positive(input_number, expected_result):
    assert print_factorial(input_number) == expected_result

@pytest.mark.parametrize(
    'input_number, expected_exception',
    [
        ('455',TypeError),
        (0.7, TypeError),
        ([213, 'sd'], TypeError),
        (-1, ValueError),
    ]
)

def test_print_factorial_negative(input_number, expected_exception):
    with pytest.raises(expected_exception):
        print_factorial(input_number)

#тесты функции sum_in_range
@pytest.mark.parametrize(
    'input_number_1, input_number_2, expected_result',
    [
        (119, 1000, 493479),
        (-111, 111, 0),
    ]
)

def test_sum_in_range_positive(input_number_1, input_number_2, expected_result):
    assert sum_in_range(input_number_1, input_number_2) == expected_result

@pytest.mark.parametrize(
    'input_number_1, input_number_2, expected_exception',
    [
        ('119', '1000',TypeError),
        ('119', 1000,TypeError),
        (119, '1000',TypeError),
        (0.1, 5.2, TypeError),
    ]
)

def test_sum_in_range_negative(input_number_1, input_number_2, expected_exception):
    with pytest.raises(expected_exception):
        sum_in_range(input_number_1, input_number_2)

#тесты функции primes

#тесты функции gsv
@pytest.mark.parametrize(
    'input_number_1, input_number_2, expected_result',
    [
        (25, 225, 25),
        (1, 2, 1),
    ]
)

def test_gsv_positive(input_number_1, input_number_2, expected_result):
    assert gsv(input_number_1, input_number_2) == expected_result

@pytest.mark.parametrize(
    'input_number_1, input_number_2, expected_exception',
    [
        ('25', '225', TypeError),
        ('25', 1000, TypeError),
        (25, '1000', TypeError),
        (0, 1, ZeroDivisionError),
        (-5, 1, ValueError),
    ]
)

def test_gsv_negative(input_number_1, input_number_2, expected_exception):
    with pytest.raises(expected_exception):
        gsv(input_number_1, input_number_2)