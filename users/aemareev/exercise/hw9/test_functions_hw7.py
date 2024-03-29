from functions_hw7 import *
import pytest


@pytest.mark.parametrize('input_list, expected_list', [
    ([[1, 4, 7, ], [2, 5, 8, ], [3, 6, 9, ]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ([[1, 3, 5, 7], [2, 4, 6, 8]], [[1, 2], [3, 4], [5, 6], [7, 8]]),
    ([[1, 2, 3]], [[1], [2], [3]]),
    ([], []),
    (['1357', '2468'], [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8']])
])
def test_expand_matrix_positive(input_list, expected_list):
    assert expand_matrix(input_list) == expected_list


@pytest.mark.parametrize('input_list, expected_exception', [
    (123, TypeError),
    (None, TypeError),
    (True, TypeError)
])
def test_expand_matrix_negative(input_list, expected_exception):
    with pytest.raises(expected_exception):
        expand_matrix(input_list)


@pytest.mark.parametrize('input_count, expected_result', [
    (0, 'Функция отработала успешно 0 раз'),
    (1, 'Функция отработала успешно 1 раз'),
    (2, 'Функция отработала успешно 2 раз')
])
def test_ten_times_positive(input_count, expected_result):
    assert ten_times(input_count) == expected_result


@pytest.mark.parametrize('input_count, expected_exception', [
    (-1, ValueError),
    (1.25, TypeError),
    ('2', TypeError)
])
def test_ten_times_negative(input_count, expected_exception):
    with pytest.raises(expected_exception):
        ten_times(input_count)


@pytest.mark.parametrize('input_list_of_str, expected_list, input_func', [
    (["Мой хайку", "Плохой такой", "Вот он"], ["МОЙ ХАЙКУ", "ПЛОХОЙ ТАКОЙ", "ВОТ ОН"], str.upper),
    (
            ["Мой хайку", "Плохой такой", "Вот он"],
            ['\x1b[31mМой хайку\x1b[0m', '\x1b[31mПлохой такой\x1b[0m', '\x1b[31mВот он\x1b[0m'],
            "\033[31m{}\033[0m".format
    ),
    (['Короткий хайку'], ['короткий хайку'], str.lower),
    (['мой новый', 'неплохой такой', 'нормальный'], ['Мой новый', 'Неплохой такой', 'Нормальный'], str.capitalize)
])
def test_print_haiku_positive(input_list_of_str, input_func, expected_list):
    assert print_haiku(input_list_of_str, input_func) == expected_list


@pytest.mark.parametrize('input_list_of_str, input_func, expected_exception', [
    (["Мой хайку", "Плохой такой", "Вот он"], str.upper('Хайку'), TypeError),
    (["Мой хайку", "Плохой такой", "Вот он"], round(3.14), TypeError)
])
def test_print_haiku_negative(input_list_of_str, input_func, expected_exception):
    with pytest.raises(expected_exception):
        print_haiku(input_list_of_str, input_func)


@pytest.mark.parametrize('input_str, expected_str', [
    ('Какая-то строка', 'к- ра'),
    ('123456789', '369'),
    ('12', ''),
    ('', '')
])
def test_every_3rd_char_positive(input_str, expected_str):
    assert every_3rd_char(input_str) == expected_str


@pytest.mark.parametrize('input_str, expected_exception', [
    (123, TypeError),
    (['Строка'], TypeError),
    ({'Строка'}, TypeError),
    (range(5), TypeError),
    (True, TypeError),
    (None, TypeError)
])
def test_every_3rd_char_negative(input_str, expected_exception):
    with pytest.raises(expected_exception):
        every_3rd_char(input_str)


@pytest.mark.parametrize('input_str, expected_str', [
    ('Какая-то строка', '\x1b[31mКакая-то\x1b[0m \x1b[32mстрока\x1b[0m'),
    ('Строка', '\x1b[31mСтрока\x1b[0m'),
    ('', '')
])
def test_different_color_positive(input_str, expected_str):
    assert different_color(input_str) == expected_str


@pytest.mark.parametrize('input_str, expected_exception', [
    ('А, И, Б сидели на трубе', IndexError),
    (123, AttributeError),
    (['Строка'], AttributeError),
    ({'Строка'}, AttributeError),
    (range(5), AttributeError),
    (True, AttributeError),
    (None, AttributeError)
])
def test_different_color_negative(input_str, expected_exception):
    with pytest.raises(expected_exception):
        different_color(input_str)


@pytest.mark.parametrize('input_str, expected_str', [
    ('Длин ная стро ка', 'Длин \x1b[1mная\x1b[0m стро ка'),
    ('Какая-то строка', 'Какая-то \x1b[1mстрока\x1b[0m'),
    ('Строка', 'Строка'),
    ('', '')
])
def test_bold_2nd_word_positive(input_str, expected_str):
    assert bold_2nd_word(input_str) == expected_str


@pytest.mark.parametrize('input_str, expected_exception', [
    (123, AttributeError),
    (['Строка'], AttributeError),
    ({'Строка'}, AttributeError),
    (range(5), AttributeError),
    (True, AttributeError),
    (None, AttributeError)
])
def test_bold_2nd_word_negative(input_str, expected_exception):
    with pytest.raises(expected_exception):
        bold_2nd_word(input_str)


@pytest.mark.parametrize('input_str, expected_str', [
    ('КаКая-То сТРока', '\x1b[34mкакая-то строка\x1b[0m'),
    ('123456789', '\x1b[34m123456789\x1b[0m'),
    ('КУ', '\x1b[34mку\x1b[0m'),
    ('ку', '\x1b[34mку\x1b[0m')
])
def test_blue_and_lower_positive(input_str, expected_str):
    assert blue_and_lower(input_str) == expected_str


@pytest.mark.parametrize('input_str, expected_exception', [
    (123, AttributeError),
    (['Строка'], AttributeError),
    ({'Строка'}, AttributeError),
    (range(5), AttributeError),
    (True, AttributeError),
    (None, AttributeError)
])
def test_blue_and_lower_negative(input_str, expected_exception):
    with pytest.raises(expected_exception):
        blue_and_lower(input_str)
