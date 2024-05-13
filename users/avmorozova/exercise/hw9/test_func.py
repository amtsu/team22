import pytest
from func import (
make_set,
element_in_set,
cycle_number,
opr_person,
podset,
sravn_set,
quadratic_equation_solution,
string_concatenation_function,
string_multiplication_function,
list_modification,
union_sets,
dorog_prod,
add_element,
swap_elements,
fibonacci_list_check,
check_fibonacci_numbers,
fractional_calculation,
calculat_air_volume_for_conditioner,
raznost_set,
student18,
add_student,
add_in_set,
is_disjoint,
set_difference,
remove_element,
find_intersection,
check_equality,
union_of_sets,
create_lists,
creat_list,
len_list,




)
def test_make_set():
    number = 1, 2, 3, "3",5
    assert make_set(number) == {1, 2, 3, '3', 5}

def test_element_in_set():
    my_set = {1, 2, 3, '3', 5}
    assert element_in_set(my_set, 3) == True


a_poem = """За стеклом лежал Питон, 
Большой и толстый, как батон.
Вверх пополз,
Затем вернулся,
Круглым бубликом свернулся."""

fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]


def test_create_lists():
    """
    туст на функцию добавления элемента в конец списка
    """
    assert create_lists() == [1, 2, 3, 4, 5, 6, 9, 789], "Элемент добавлен неудачно"

def test_creat_list():
    assert creat_list(a_poem)[0] == ['З', 'а', ' ', 'с', 'т', 'е', 'к', 'л', 'о', 'м', ' ', 'л', 'е', 'ж', 'а', 'л', ' ', 'П', 'и', 'т', 'о', 'н', ',', ' ', '\n', 'Б', 'о', 'л', 'ь', 'ш', 'о', 'й', ' ', 'и', ' ', 'т', 'о', 'л', 'с', 'т', 'ы', 'й', ',', ' ', 'к', 'а', 'к', ' ', 'б', 'а', 'т', 'о', 'н', '.', '\n', 'В', 'в', 'е', 'р', 'х', ' ', 'п', 'о', 'п', 'о', 'л', 'з', ',', '\n', 'З', 'а', 'т', 'е', 'м', ' ', 'в', 'е', 'р', 'н', 'у', 'л', 'с', 'я', ',', '\n', 'К', 'р', 'у', 'г', 'л', 'ы', 'м', ' ', 'б', 'у', 'б', 'л', 'и', 'к', 'о', 'м', ' ', 'с', 'в', 'е', 'р', 'н', 'у', 'л', 'с', 'я', '.']

def test_creat_list2():    
    assert creat_list(a_poem)[1] == ['За', 'стеклом', 'лежал', 'Питон,', '\nБольшой', 'и', 'толстый,', 'как', 'батон.\nВверх', 'пополз,\nЗатем', 'вернулся,\nКруглым', 'бубликом', 'свернулся.']
    
def test_creat_list3():    
    assert creat_list(a_poem)[2] == ['За стеклом лежал Питон, ', 'Большой и толстый, как батон.', 'Вверх пополз,', 'Затем вернулся,', 'Круглым бубликом свернулся.']


def test_swap_elements():
    a_list = [1, 2, 5, 4, 3, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert swap_elements(a_list) == expected

def test_fibonacci_list_check():
    expected_length = 23
    assert fibonacci_list_check(fibonacci_list)[0] == expected_length
    
def test_fibonacci_list_check2():
    exepected_repeating_element = 2
    assert fibonacci_list_check(fibonacci_list)[1] == exepected_repeating_element

def test_fractional_calculation1():
    assert fractional_calculation()[0] == -3, "Ошибка вычисления"

def test_fractional_calculation2():
    assert fractional_calculation()[1] == - 0.14, "Ошибка вычисления"
    
    
def test_check_fibonacci_numbers():
    expected_results = {21: True, 33: False, 987: True, 9999: False}
    actual_results = check_fibonacci_numbers(fibonacci_list)
    assert actual_results == expected_results

def test_calculat_air_volume_for_conditioner():
    assert calculat_air_volume_for_conditioner() == 145.70000000000002

 
def test_element_in_set_2():
    my_set = {1, 2, 3, '3', 5}
    assert element_in_set(my_set, 4) == False

def test_cycle_number():
    assert cycle_number(1,6) == [1, 4, 9, 16, 25, 36]

def test_opr_person():
    my_dict = {'name': 16,'age':33,'city':12}
    assert opr_person(my_dict,'name') == False

def test_podset():
    assert podset({5,6},{1,2,3,4,5,6}) == True

def test_2podset():
    assert podset({1,2,3,4,5,6},{3,4}) == False


def test_sravn_test():
    assert sravn_set({1,2,3,4,5,6},{1,2,3}) == True

def test_2sravn_test():
    assert sravn_set({1,2,3},{1,2,3,4,5,6}) == False

def test_union_set():
    assert union_sets({1,2,3,4},{5,6,7,8}) == {1, 2, 3, 4, 5, 6, 7, 8}

def test_d_prod():
    assert dorog_prod({"яблоко": 1.5, "банан": 2, "апельсин": 1.2}) == True

def test_raznost_set():
    assert raznost_set({1,2,3,4},{3,4}) == {1, 2}

def test_student18():
    assert student18(my_dict,my_key) == False

my_dict = {"Иванов": 18, "Сидорова":13, "Лавандов": 3, "Мукин": 84}
my_key =  "Лавандов"

def test_2student18():
    assert student18(my_dict,"Мукин") == True

my_dict = {"Иванов": 18, "Сидорова":13, "Лавандов": 3, "Мукин": 84}

def test_add_in_set():
    my_set = {1, 2, 3, 4, 5}
    number = 6
    expected = {1, 2, 3, 4, 5, 6}
    assert add_in_set(my_set, number) == expected

def test_add_in_set2():
    my_set = (1, 2, 3, 4, 5)
    number = 6
    with pytest.raises(AttributeError):
        add_in_set(my_set, number)

def test_add_in_set3():
    my_set = {1, 2, 3, 4, 5}
    number = ["6"]
    with pytest.raises(TypeError):
        add_in_set(my_set, number)

def test_add_in_set4():
    my_set = [1, 2, 3, 4, 5]
    number =  2
    with pytest.raises(AttributeError):
        add_in_set(my_set, number)


def test_len_list():
    assert len_list(a_poem)[0] == 112

def test_len_list2():
    assert len_list(a_poem)[1] == 13

def test_quadratic_equation_solution():
    assert quadratic_equation_solution() == (-2.0, -2.5)


def test_string_concatenation_function():
    assert string_concatenation_function() == "Hello, world!", "Неверный вывод"


def test_string_multiplication_function():
    assert string_multiplication_function() == "la la la la la la la la la la la la la la la la la la la la la la la la la "

def test_list_modification():
    assert list_modification() == [1, 'hi', 3, [8, 6, 4], 5]

def test_len_list3():
    assert len_list(a_poem)[2] == 5


def test_add_student():
    assert add_student(my_dict,'ivanov',13) == {'Иванов': 18, 'Сидорова': 13, 'Лавандов': 3, 'Мукин': 84, 'ivanov': 13}

my_dict = {"Иванов": 18, "Сидорова":13, "Лавандов": 3, "Мукин": 84}


def test_2add_student():
    with pytest.raises(TypeError):
        add_student(my_dict,'ivanov',13,13)

def test_is_disjoint():
    assert is_disjoint({1,2,3},{4,5,6}) == True

def test_2is_disjoint():
    assert is_disjoint({1,2,3},{3,5,6}) == False

def test_set_difference():
    assert set_difference({1,2,3},{3,4,5}) == {1, 2}


def test_2set_difference():
    assert set_difference({1,2,3},{2,3,6}) == {1}

def test_remove_element():
    assert remove_element({1, 2, 3, 4, 5},3) == True

def test_2remove_element():
    assert remove_element({1, 2, 3, 4, 5},6) == False

def test_find_intersection():
    assert find_intersection({1, 2, 3, 4, 5},{3, 4, 5, 6, 7}) == {3, 4, 5}

def test_check_equality():
    assert check_equality({1, 2, 3},{3, 2, 1}) == True

def test_check_equality2():
    assert check_equality({4, 2, 3},{3, 2, 1}) == False

def test_check_equality3():
    assert check_equality({1, 2, 3},{"3", 2, 1}) == False

def test_union_of_sets():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set3 = {5, 6, 7}
    assert union_of_sets(set1, set2, set3) == {1, 2, 3, 4, 5, 6, 7}

def test_2union_of_sets():
    set1 = {1, 2, 3}
    set2 = {3}
    set3 = {}
    assert union_of_sets(set1, set2, set3) == {1, 2, 3}

def test_3union_of_sets():
    set1 = {1, 2, 3}
    set2 = {"3"}
    set3 = {}
    assert union_of_sets(set1, set2, set3) == {1, 2, 3, "3"}





 
    
