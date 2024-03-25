from functions_hw5 import check_repeated_chars, get_nod, is_palindrome, day_of_week
import pytest


@pytest.mark.parametrize('input_str, expected_result', [
    ('AAaazb 01234444', [('A', 2), ('a', 2), ('4', 4)]),
    ('asdfgh12345', -1),
    ('Русские буквы', [('у', 2), ('с', 2), ('к', 2)]),
    ('    ', [(' ', 4)]),
    ('', -1)
])
def test_check_repeated_chars_positive(input_str, expected_result):
    assert check_repeated_chars(input_str) == expected_result


@pytest.mark.parametrize('input_str, expected_error', [
    (123, TypeError),
    (['Строка'], TypeError),
    ({'Строка'}, TypeError),
    (range(5), TypeError),
    (True, TypeError),
    (None, TypeError)
])
def test_check_repeated_chars_negative(input_str, expected_error):
    with pytest.raises(expected_error):
        check_repeated_chars(input_str)


@pytest.mark.parametrize('input_a, input_b, expected_result', [
    (10, 20, 10),
    (1, 2, 1),
    (4, 8, 4),
    (64, 8192, 64),
    (4096, 128, 128),
    (3, True, 1)
])
def test_get_nod_positive(input_a, input_b, expected_result):
    assert get_nod(input_a, input_b) == expected_result


@pytest.mark.parametrize('input_a, input_b, expected_error', [
    (0, 0, ZeroDivisionError),
    (0, 1, ZeroDivisionError),
    ('10', '20', TypeError),
    (float('-inf'), float('inf'), TypeError),
    (-10, -20, ValueError),
    (-10, 50, ValueError),
    (10, -50, ValueError)
])
def test_get_nod_negative(input_a, input_b, expected_error):
    with pytest.raises(expected_error):
        get_nod(input_a, input_b)


@pytest.mark.parametrize('input_str, expected_result', [
    ('А роза упала на лапу Азора', True),
    ('топоТ', True),
    ('топо Т', True),
    ('Топор', False),
    ('123454321', True),
    ('1234554321', True),
    ('1234564321', False),
    ('', True)
])
def test_is_palindrome_positive(input_str, expected_result):
    assert is_palindrome(input_str) == expected_result


@pytest.mark.parametrize('input_str, expected_error', [
    (12321, TypeError),
    (['Строка'], TypeError),
    ({'Строка', 'Еще строка'}, TypeError),
    (range(5), TypeError),
    (True, TypeError),
    (None, TypeError)
])
def test_is_palindrome_negative(input_str, expected_error):
    with pytest.raises(expected_error):
        is_palindrome(input_str)


@pytest.mark.parametrize('input_number, expected_result', [
    (1, 'понедельник'),
    (2, 'вторник'),
    (3, 'среда'),
    (4, 'четверг'),
    (5, 'пятница'),
    (6, 'суббота'),
    (7, 'воскресенье'),
    (8, 'не день недели')
])
def test_day_of_week_positive(input_number, expected_result):
    assert day_of_week(input_number)


@pytest.mark.parametrize('input_number, expected_error', [
    ('1', TypeError),
    (-1.0, TypeError),
    ([1], TypeError),
    (range(1), TypeError),
    (True, TypeError),
    (None, TypeError)
])
def test_day_of_week_negative(input_number, expected_error):
    with pytest.raises(expected_error):
        day_of_week(input_number)
