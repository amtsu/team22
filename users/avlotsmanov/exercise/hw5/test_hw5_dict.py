import pytest
from hw5_dict import *

#тесты к функции create_dictionary

@pytest.mark.parametrize(
    'input_tuples, input_values, expected_result',
    [
        (
            (1, 2, 3, 4, 5, 1),
            ('a', 'b', 'c', 'd', 'e', 'e'),
            {1: 'e', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
        ),
        (
            (1, 2, 3, 4, 5,),
            ('a', 'b', 'c', 'd', 'e',),
            {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
        ),
    ]
)

def test_create_dictionary_positive(input_tuples, input_values, expected_result):
    assert create_dictionary(input_tuples, input_values) == expected_result

@pytest.mark.parametrize(
    'input_tuples, input_values, expected_exception',
    [
        (
            '1, 2, 3, 4, 5', 
            'a, b, c, d, e',
            TypeError
        ),
        (
            1,
            1,
            TypeError
        ),
        (
            (1, 2),
            ('a'),
            ValueError
        )
])
#один из тестов не проходит, тк функция ломается на нем
def test_create_dictionary_negative(input_tuples, input_values, expected_exception):
    with pytest.raises(expected_exception):
        create_dictionary(input_tuples, input_values)

#тесты к функции add_students
@pytest.mark.parametrize(
    'input_dict, input_names, input_ages, expected_result',
    [
        (
            {"Иванов": 22, "Петрова": 21, "Сидоров": 23},
            ('Лоцманов', 'Корчевая'),
            (33, 21),
            {'Иванов': 22, 'Петрова': 21, 'Сидоров': 23, 'Лоцманов': 33, 'Корчевая': 21}
        )
    ]
)

def test_add_students_positive(input_dict, input_names, input_ages, expected_result):
    assert add_students(input_dict, input_names, input_ages) == expected_result

@pytest.mark.parametrize(
    'input_dict, input_names, input_ages, expected_exception',
    [
        (
            {"Иванов": 22, "Петрова": 21, "Сидоров": 23},
            ('Лоцманов', 'Корчевая'),
            (33, 22, 11),
            ValueError
        ),
        (
            "Иванов",
            'Лоцманов',
            '33',
            ValueError
        )
    ]
)

def test_add_students_negative(input_dict, input_names, input_ages, expected_exception):
    with pytest.raises(expected_exception):
        add_students(input_dict, input_names, input_ages)
    
#тесты к функции remove_students
@pytest.mark.parametrize(
    'input_dict, input_names, expected_result',
    [
        (
            {'Иванов': 22, 'Петрова': 21, 'Сидоров': 23, 'Лоцманов': 33, 'Корчевая': 21},
            ('Лоцманов', 'Корчевая'),
            {"Иванов": 22, "Петрова": 21, "Сидоров": 23},
        )
    ]
)

def test_remove_students_positive(input_dict, input_names, expected_result):
    assert remove_students(input_dict, input_names) == expected_result

@pytest.mark.parametrize(
    'input_dict, input_names, expected_exception',
    [
        (
            {"Иванов": 22, "Петрова": 21, "Сидоров": 23},
            ('Лоцманов', 'Корчевая'),
            KeyError
        ),
        (
            {"Иванов": 22, "Петрова": 21, "Сидоров": 23},
            'Лоцманов',
            KeyError
        ),
        (
            {"Иванов": 22, "Петрова": 21, "Сидоров": 23},
            1,
            TypeError
        )
    ]
)

def test_remove_students_negative(input_dict, input_names, expected_exception):
    with pytest.raises(expected_exception):
        remove_students(input_dict, input_names)

#тесты к функции merge_dict
@pytest.mark.parametrize(
    'dict_1, dict_2, expected_result',
    [
        (
            {'Иванов': 18, 'Петрова': 19, 'Сидоров': 20,},
            {'Лоцманов': 33, 'Корчевая': 21},
            {'Иванов': 18, 'Петрова': 19, 'Сидоров': 20,'Лоцманов': 33, 'Корчевая': 21},
        )
    ]
)

def test_merge_dict_positive(dict_1, dict_2, expected_result):
    assert merge_dict(dict_1, dict_2) == expected_result

@pytest.mark.parametrize(
    'dict_1, dict_2, expected_exception',
    [
        (
            "'Иванов': 18, 'Петрова': 19, 'Сидоров': 20,",
            "'Лоцманов': 33, 'Корчевая': 21}",
            AttributeError,
        )
    ]
)

def test_merge_dict_negative(dict_1, dict_2, expected_exception):
    with pytest.raises(expected_exception):
        merge_dict(dict_1, dict_2)

#тесты к функции delete_item
@pytest.mark.parametrize(
    'dict_1, keys, expected_result',
    [
        (
            {'Иванов': 18, 'Петрова': 19, 'Сидоров': 20,},
            ['Иванов','Петрова'],
            {'Сидоров': 20,},
        )
    ]
)

def test_delete_item_positive(dict_1, keys, expected_result):
    assert delete_item(dict_1, keys) == expected_result

@pytest.mark.parametrize(
    'dict_1, keys, expected_exception',
    [
        (
            {'Иванов': 18, 'Петрова': 19, 'Сидоров': 20,},
            'Лоцманов',
            KeyError,
        )
    ]
)

def test_delete_item_negative(dict_1, keys, expected_exception):
    with pytest.raises(expected_exception):
        delete_item(dict_1, keys)
        
#тесты к функции reverse_dict
@pytest.mark.parametrize(
    'dict_1, expected_result',
    [
        (
            {'Иванов': 18, 'Петрова': 19, 'Сидоров': 20,},
            {18 : 'Иванов', 19 : 'Петрова', 20 : 'Сидоров',},
        )
    ]
)

def test_reverse_dict_positive(dict_1, expected_result):
    assert reverse_dict(dict_1) == expected_result

@pytest.mark.parametrize(
    'dict_1, expected_exception',
    [
        (
            "'Иванов': 18, 'Петрова': 19, 'Сидоров': 20,",
            AttributeError,
        )
    ]
)

def test_reverse_dict_negative(dict_1, expected_exception):
    with pytest.raises(expected_exception):
        reverse_dict(dict_1)