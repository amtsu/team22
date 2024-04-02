import pytest
from hw5_part2 import (dict_add, dict_remove, total_fruit_cost)

def test_dict_add1():
    test_dict = {"name": 'Konstantin', "age": 37, "city": 'Moscow'}
    test_key = 'e-mail'
    test_value = 'kostia.anikin@gmail.com'
    expected = {'name': 'Konstantin', 'age': 37, 'city': 'Moscow', 'e-mail': 'kostia.anikin@gmail.com'}
    assert expected == dict_add(test_dict, test_key, test_value) , "Неверно посчитано объединение"

def test_dict_add2():
    test_dict = {"Иванов": 22, "Петрова": 13, "Сидоров": 23}
    test_key = "Смирнова"
    test_value = 20
    expected = {'Иванов': 22, 'Петрова': 13, 'Сидоров': 23, 'Смирнова': 20}
    assert expected == dict_add(test_dict, test_key, test_value) , "Неверно посчитано объединение"

def test_dict_add_notadict():
    test_dict = 15
    test_key = "Смирнова"
    test_value = 20
    with pytest.raises(TypeError):
        dict_add(test_dict, test_key, test_value) , "Неверно посчитано объединение"


def test_dict_remove1():
    test_dict = {'name': 'Konstantin', 'age': 37, 'city': 'Moscow', 'e-mail': 'kostia.anikin@gmail.com'}
    test_key = "city"
    expected = {'name': 'Konstantin', 'age': 37, 'e-mail': 'kostia.anikin@gmail.com'}
    assert expected == dict_remove(test_dict, test_key) , "Неверно сделано удаление"

def test_dict_remove2():
    test_dict = {'Иванов': 22, 'Петрова': 13, 'Сидоров': 23, 'Смирнова': 20}
    test_key = "Петрова"
    expected = {'Иванов': 22, 'Сидоров': 23, 'Смирнова': 20}
    assert expected == dict_remove(test_dict, test_key) , "Неверно сделано удаление"

def test_dict_remove_negative1():
    test_dict = {'name': 'Konstantin', 'age': 37, 'city': 'Moscow', 'e-mail': 'kostia.anikin@gmail.com'}
    test_key = "second_name"
    with pytest.raises(ValueError ):
        dict_remove(test_dict, test_key) , "Неверно посчитано объединение"
    
   
def test_total_fruit_cost1():
    test_qty = {"яблоко": 5, "банан": 10, "апельсин": 7}
    test_price = {"яблоко": 1.5, "банан": 2, "апельсин": 1.2} 
    expected = 35.9
    assert expected == total_fruit_cost(test_qty, test_price) , "Неверно посчитана стоимость"

"""def test_total_fruit_cost1():

def test_total_fruit_cost1():"""