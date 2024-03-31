import pytest
from hw3 import calculate, round_remains_number, conditioner, q_equation, slice_3_7

#тесты для функции calculate
@pytest.mark.parametrize(
    'input_a, input_b, input_operation, expected_result',
    [
        (5.1, 2.1, '+', 7.2),
        (5, 2, '-', 3),
        (4, 2, '/', 2),
        (5, 2, '**', 25),
        (10, 3, '//', 3),
        (10, 3, '%', 1),
        (5, 0, '**', 1),
    ]
)

def test_calculate_positive(input_a, input_b, input_operation, expected_result):
    assert calculate(input_a, input_b, input_operation) == expected_result

@pytest.mark.parametrize(
    'input_a, input_b, input_operation, expected_exception',
    [
        ('5', '2', '*', TypeError),
        (5.1, 2.1, '++', ValueError),
        (4, 0, '/', ZeroDivisionError),
        (10, 0, '//', ZeroDivisionError),
        (10, 0, '%', ZeroDivisionError),
    ]
)

def test_calculate_negative(input_a, input_b, input_operation, expected_exception):
    with pytest.raises(expected_exception):
        calculate(input_a, input_b, input_operation)

#тесты для функции round_remains_number
@pytest.mark.parametrize(
    'input_a, expected_result',
    [
        (5.13234, (5, '0.13')),
        (5.13634, (5, '0.14'))
        
    ]
)
def test_round_remains_number_positive(input_a, expected_result):
    assert round_remains_number(input_a) == expected_result

@pytest.mark.parametrize(
    'input_a, expected_exception',
    [
        (5, TypeError),  
    ]
)
def test_round_remains_number_negative(input_a, expected_exception):
    with pytest.raises(expected_exception):
        round_remains_number(input_a)
  
#тесты для функции conditioner
@pytest.mark.parametrize(
    'input_tuple, expected_result',
    [
        ((3.5, 6.4, 3.4, 4, 3.1, 11), 145.7),
        
    ]
)
def test_conditioner_positive(input_tuple, expected_result):
    assert conditioner(input_tuple) == expected_result

@pytest.mark.parametrize(
    'input_tuple, expected_exception',
    [
        ([3.5, 6.4, 3.4, 4, 3.1, 11], TypeError),  
    ]
)
def test_conditioner_negative(input_tuple, expected_exception):
    with pytest.raises(expected_exception):
        conditioner(input_tuple)

#тесты для функции q_equation
@pytest.mark.parametrize(
    'input_a, input_b, input_c, expected_result',
    [
        (2, 8, -10, (1.0, -5.0)),
        (2.2, 8.2, -10.4, (1.0, -4.727))
    ]
)

def test_q_equation_positive(input_a, input_b, input_c, expected_result):
    assert q_equation(input_a, input_b, input_c) == expected_result

@pytest.mark.parametrize(
    'input_a, input_b, input_c, expected_exception',
    [
        ('2', '8', '-10', TypeError),
        (0, 2.1, 8, ZeroDivisionError),
    ]
)

def test_q_equation_negative(input_a, input_b, input_c, expected_exception):
    with pytest.raises(expected_exception):
        q_equation(input_a, input_b, input_c)

#тесты для функции slice_3_7
@pytest.mark.parametrize(
    'input_list, expected_result',
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 5, 6, 7, 8]),
        
    ]
)
def test_slice_3_7_positive(input_list, expected_result):
    assert slice_3_7(input_list) == expected_result

@pytest.mark.parametrize(
    'input_list, expected_exception',
    [
        ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), TypeError),  
        ([1, 2, 3], ValueError)
    ]
)
def test_slice_3_7_negative(input_list, expected_exception):
    with pytest.raises(expected_exception):
        slice_3_7(input_list)

