import pytest
from hw5_if import *

#тесты функции check_fruit_price
@pytest.mark.parametrize(
    'input_dict, input_name, expected_result',
    [
        (
            {
                'Яблоки' : 1,
                'Виноград' : 1.2,
                'Вишня' : 1.5,
                "Груша" : 1.85, 
                "Апельсин" : 3,
                "Мандарин" : 2
            },
            'груша',
            'дорогой товар'
        ),
    ]
)

def test_check_fruit_price_positive(input_dict, input_name, expected_result):
    assert check_fruit_price(input_dict, input_name) == expected_result

@pytest.mark.parametrize(
    'input_dict, input_name, expected_result',
    [
        (
            {
                'Яблоки' : 1,
                'Виноград' : 1.2,
                'Вишня' : 1.5,
                "Груша" : 1.85, 
                "Апельсин" : 3,
                "Мандарин" : 2
            },
            'яблоко',
            'Ошибка! Такого фрукта в словаре не существует'
        ),
        (
            {
                'Яблоки' : 1,
                'Виноград' : 1.2,
                'Вишня' : 1.5,
                "Груша" : 1.85, 
                "Апельсин" : 3,
                "Мандарин" : 2
            },
            'яблоки',
            'товар не дорогой'
        ),
    ]
)

def test_check_fruit_price_negative(input_dict, input_name, expected_result):
    assert check_fruit_price(input_dict, input_name) == expected_result


#тесты функции check_age
@pytest.mark.parametrize(
    'input_dict, input_name, expected_result',
    [
        (
            {'Иванов': 22, 'Петрова': 21, 'Сидоров': 23, 'Лоцманов': 33, 'Корчевая': 21},
            'Лоцманов',
            'Совершеннолетний'
        ),
    ]
)

def test_check_age_positive(input_dict, input_name, expected_result):
    assert check_age(input_dict, input_name) == expected_result

@pytest.mark.parametrize(
    'input_dict, input_name, expected_result',
    [
        (
            {'Иванов': 15, 'Петрова': -1, 'Сидоров': 23, 'Лоцманов': 33, 'Корчевая': 21},
            'Иванов',
            'Несовершеннолетний'
        ),
        (
            {'Иванов': 15, 'Петрова': -1, 'Сидоров': 23, 'Лоцманов': 33, 'Корчевая': 21},
            'Петрова',
            'Ошибка!'
        ),
        (
            {'Иванов': 15, 'Петрова': -1, 'Сидоров': 23, 'Лоцманов': 33, 'Корчевая': 21},
            'Бубнов',
            'Ошибка! Такого студента в словаре не существует'
        ),
    ]
)

def test_check_age_negative(input_dict, input_name, expected_result):
    assert check_age(input_dict, input_name) == expected_result

#тесты функции even_odd
@pytest.mark.parametrize(
    'input_number, expected_result',
    [
        (456,'Четное'),
        (455,'Нечетное'),
        (-456,'Четное')
    ]
)

def test_even_odd_positive(input_number, expected_result):
    assert even_odd(input_number) == expected_result

@pytest.mark.parametrize(
    'input_number, expected_exception',
    [
        ('455',TypeError),
        (0.7, TypeError),
        ('213sd', TypeError),
    ]
)

def test_even_odd_negative(input_number, expected_exception):
    with pytest.raises(expected_exception):
        even_odd(input_number)
    
#тесты функции leap_year
@pytest.mark.parametrize(
    'input_number, expected_result',
    [
        (1600,'Високосный'),
        (1700,'Обычный'),
        (4,'Обычный'),
        (1804,'Високосный'),
        (2024,'Високосный'),
    ]
)

def test_leap_year_positive(input_number, expected_result):
    assert leap_year(input_number) == expected_result

@pytest.mark.parametrize(
    'input_number, expected_exception',
    [
        ('455',TypeError),
        (0.7, TypeError),
        ('aqwssd', TypeError),
        ([1, 1800], TypeError),
    ]
)

def test_even_odd_negative(input_number, expected_exception):
    with pytest.raises(expected_exception):
        leap_year(input_number)
        
#тесты функции is_pallindrom
@pytest.mark.parametrize(
    'input_string, expected_result',
    [
        ('qwertyytrewq', True),
        ('qwer tyytrewq', False),
        ('QwerTyyTrewQ', True),
        ('QwerTyyTrewq', False),
        ('1234554321', True),
        ('12345', False),
        ('1a2b345543b2a1', True),
        ('12345', False),
    ]
)

def test_is_pallindrom_positive(input_string, expected_result):
    assert is_pallindrom(input_string) == expected_result

@pytest.mark.parametrize(
    'input_string, expected_exception',
    [
        (1234554321,TypeError),
        (0.7, TypeError),
        ((1, 'ssd'), TypeError),
        ([1, 1800], TypeError),
    ]
)

def test_even_odd_negative(input_string, expected_exception):
    with pytest.raises(expected_exception):
        is_pallindrom(input_string)

#тесты функции time_of_day
@pytest.mark.parametrize(
    'input_string, expected_result',
    [
        ('08 00', 'Утро'),
        ('12 00', 'День'),
        ('18 00', 'Вечер'),
        ('21 00', 'Ночь'),

    ]
)

def test_time_of_day_positive(input_string, expected_result):
    assert time_of_day(input_string) == expected_result

@pytest.mark.parametrize(
    'input_string, expected_exception',
    [
        (2100,TypeError),
        (0.7, TypeError),
        ([1, 1800], TypeError),
    ]
)

def test_time_of_day_negative(input_string, expected_exception):
    with pytest.raises(expected_exception):
        time_of_day(input_string)

#тесты функции is_prime

#тесты функции is_letter
@pytest.mark.parametrize(
    'input_string, expected_result',
    [
        ('qwertyytrewq', True),
        ('qwer tyytrewq', False),
        ('QwerTyyTrewQ', True),
        ('QwerTyyTrewq', True),
        ('1234554321', False),
        ('1a2b345543b2a1', False),
    ]
)

def test_is_letter_positive(input_string, expected_result):
    assert is_letter(input_string) == expected_result

@pytest.mark.parametrize(
    'input_string, expected_exception',
    [
        (12345,TypeError),
        (0.7, TypeError),
        ([1, 1800], TypeError),
    ]
)

def test_is_letter_negative(input_string, expected_exception):
    with pytest.raises(expected_exception):
        is_letter(input_string)

#тесты функции is_date_correct

#тесты функции d_o_w