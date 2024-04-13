from func_dict import create_dictionary, add_student, remove_student, add_fruit, add_fruit_2, remove_fruit, remove_fruit_2, dict_update, dict_pop, dict_shift, dict_sorting, dict_max_elements, dict_max

#Создайте функцию create_dictionary для создания словаря с заданными ключами и значениями.
def test_create_dictionary ():
    assert {'c':5} == create_dictionary('c',5)
test_create_dictionary()
    
#Напишите функции add_student и remove_student для добавления и удаления студентов из словаря.
def test_add_student ():
    d1 = {'one':1, 'b':2}
    assert {'one':1, 'b':2, 'name':'Anna'} == add_student(d1, 'name', 'Anna')
test_add_student()

def test_remove_student ():
    d2 = {'Anna':17, 'Shaha':20, 'Andrej':18}
    assert {'Anna':17, 'Shaha':20} == remove_student (d2, 'Andrej')
test_remove_student()
    
#Напишите функции add_fruit и remove_fruit для добавления и удаления фруктов, их количества и стоимости в списки fruits_quantity и fruits_prices.
#функция добавляет фрукт и его количество в словарь
def test_add_fruit ():
    fruits_quantity = {'яблоко':20,'груша':10,'апельсин':5}
    assert {'яблоко': 20, 'груша': 10, 'апельсин': 5, 'киви': 10} == add_fruit (fruits_quantity, 'киви', 10)
test_add_fruit()

#функция добавляет опреденное количество к имеющимся фруктам
def test_add_fruit_2 ():
    fruits_quantity = {'яблоко':20,'груша':10,'апельсин':5}
    assert {'яблоко': 30, 'груша': 10, 'апельсин': 5} == add_fruit_2 (fruits_quantity, 'яблоко', 10)
test_add_fruit_2()

def test_add_fruit_3():
    fruits_quantity = {'яблоко':20,'груша':10,'апельсин':5}
    input = [fruits_quantity, 'киви', 10]
    expected = {'яблоко': 20, 'груша': 10, 'апельсин': 5, 'киви': 10}
    assert expected == add_fruit (*input)
test_add_fruit_3()

#функция удаляет фрукт из словаря
def test_remove_fruit ():
    fruits_quantity = {'яблоко':20,'груша':10,'апельсин':5}
    assert {'яблоко':20,'груша':10} == remove_fruit(fruits_quantity, 'апельсин')
test_remove_fruit()

#функция удаляет определенное количество фруктов из словаря
def test_remove_fruit_2 ():
    fruits_quantity = {'яблоко':20,'груша':10,'апельсин':5}
    assert {'яблоко':20,'груша':10,'апельсин':2}  == remove_fruit_2(fruits_quantity, 'апельсин', 3)
test_remove_fruit_2()

#Создайте функцию для объединения двух словарей.
def test_dict_update ():
    d1 = {'one':1, 'b':2}
    d2 = {'c':3, 'd':4}
    assert {'one': 1, 'b': 2, 'c': 3, 'd': 4} == dict_update(d1,d2)
test_dict_update()

#Создайте функцию для удаления элемента из словаря по заданному ключу.
def test_dict_pop ():
    d1 = {'one':1, 'b':2}
    assert {'one':1} == dict_pop (d1,"b")
test_dict_pop()

#Создайте функцию для переворачивания значений и ключей в словаре (принимает на вход словарь, возвращает другой словарь, ключами которого являются значения входного словаря, а значениями - ключи.
def test_dict_shift ():
    d4 = {"san":"вс", 'mon':'пон'}
    assert {'вс': 'san', 'пон': 'mon'} == dict_shift(d4)
test_dict_shift()

#Создайте функцию для сортировки словаря по ключам в обратном порядке.
def test_dict_sorting():
    d5 = {5:'friday', 7:'san', 1:'mon'}
    assert {7: 'san', 5: 'friday', 1: 'mon'} == dict_sorting(d5)
test_dict_sorting ()

#Создайте функцию возвращающую наибольшее значение элемента словаря.
def test_dict_max_elements():
    d5 = {5:'friday', 7:'san', 1:'mon'}
    assert 7, 'san' == dict_max_elements(d5)
test_dict_max_elements()

#Создайте функцию для поиска наибольшего значения в словаре.
def test_dict_max():
    d5 = {5:'friday', 7:'san', 1:'mon'}
    assert 'san' == dict_max(d5)
test_dict_max()