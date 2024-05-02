import pytest
from functions_hw_5_p5 import (set_union, set_difference, is_subset, create_dictionary, add_student, check_age, remove_student)


'''Множества'''
# 1. Тест - объединение и разность множеств.

def test_set_union1():   
    set1 = {2, 1, 8, 3}
    set2 = {0, 4, 3, 7}
    assert set_union(set1, set2) == {0, 1, 2, 3, 4, 7, 8}, 'Ошибка объединения множеств'


def test_set_union2():   
    set1 = {'a', 5} #str
    set2 = {0, 4}
    assert set_union(set1, set2) == {0, 5, 4, 'a'}, 'Ошибка объединения множеств'


def test_set_union3():   
    set1 = {3.1, 5} #float
    set2 = {0.4, 4}
    assert set_union(set1, set2) == {0.4, 3.1, 4, 5}, 'Ошибка объединения множеств'


def test_set_union4():   
    set1 = {-2, 1} #отриц
    set2 = {0, 7}
    assert set_union(set1, set2) == {-2, 0, 1, 7}, 'Ошибка объединения множеств'


def test_set_union5(): 
    set1 = {2, 1}
    set2 = [0, 3] #список, вместо множества
    assert set_union(set1, set2) == {0, 1, 2, 3}, 'Ошибка объединения множеств'


def test_set_union6():  
    set1 = {0, 1}
    set2 = 'abc' #стр
    assert set_union(set1, set2) == {0, 1, 'a', 'b', 'c'}, 'Ошибка объединения множеств'


def test_set_union7():   #негативный
    set1 = 123  #int
    set2 = {0, 4} 
    with pytest.raises(TypeError):
        set_union(set1, set2)


def test_set_union8():   #негативный
    set1 = 1234  #int
    set2 = {0, 2} 
    try:
        set_union(set1, set2)
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

#тесты на объединение множеств с помощью параметризации

@pytest.mark.parametrize('set1, set2, expected_result', 
                        [
                            ({2, 1, 8, 3}, {0, 4, 3, 7}, {0, 1, 2, 3, 4, 7, 8}),
                            ({'a', 5}, {0, 4}, {0, 5, 4, 'a'}),
                            ({3.1, 5}, {0.4, 4}, {0.4, 3.1, 4, 5}),
                        ]
                            )

def test_set_union_parametrize(set1, set2, expected_result):
    result = set_union(set1, set2)
    assert result == expected_result
     

def test_set_difference1(): #отлич set1 от set2
    set1 = {2, 1, 8, 3}
    set2 = {0, 4, 3, 7}    
    assert set_difference(set1, set2) == {8, 1, 2}, 'Ошибка разности множеств'


def test_set_difference2():
    set1 = {2, 2+2}  #вычисляет 4 ? 
    '''попробовать с помощью циклов.''' 
    set2 = {1, 4}   
    assert set_difference(set1, set2) == {2}, 'Ошибка разности множеств'


def test_set_difference3():   #негативный
    set1 = 123  #int
    set2 = {0, 4} 
    with pytest.raises(AttributeError):
        set_difference(set1, set2)


#2. Является ли одно множество подмножеством другого.

def test_is_subset1():  #set1 подмножеством set2
    set1 = {3,4}
    set2 = {1,2,3,4}
    assert is_subset(set1, set2) == True


def test_is_subset2(): 
    set1 = {1,2,3,4}
    set2 = {3,4}
    assert is_subset(set1, set2) == False


def test_is_subset3(): #негативный 
    set1 = [3]  #список
    set2 = {3,4}
    with pytest.raises(AttributeError):
        is_subset(set1, set2)



'''Словари'''
#1. Тест -создание словаря с заданными ключами и значениями. 

def test_create_dictionary1():
    kwargs = {'1': 'blue', '2':'red', '3':'brown'}
    assert create_dictionary(**kwargs) == {'1': 'blue', '2':'red', '3':'brown'}


def test_create_dictionary2():
    kwargs = create_dictionary(x=1, y=2, z=3)
    assert create_dictionary(**kwargs) == {'x': 1, 'y': 2, 'z': 3}


def test_create_dictionary3(): #негативный 
    kwargs = {1: 'blue', 2: 'red', 3: 'brown'} #str без ''
    with pytest.raises(TypeError):
        create_dictionary(**kwargs)


#2. Тест - функции для добавления студентов в словарь. 


def test_add_student1():
    students = {}
    add_student(students, 'Peter', 18, 'Math')
    add_student(students, 'Kate', 19, 'Art')
    add_student(students, 'John', 18, 'Physics')
    excepted_result = {'Peter': {'age': 18, 'major': 'Math'}, 
                       'Kate': {'age': 19, 'major': 'Art'}, 
                       'John': {'age': 18, 'major': 'Physics'}}
    
    assert students == excepted_result


def test_add_student2():
    students = {'Peter': {'age': 18, 'major': 'Math'}}
    assert add_student(students, 'Peter', 18, 'Math') == 'Student Peter already exists.'


def test_add_student3(): #тест негативный. После теста видно, что функцию нужно доработать, т к студенту '0' лет
    students = {}
    assert add_student(students, 'Peter', 0, 'Math') == 'Student Peter added.'


def test_add_student4():      #негативный, но ошибки нет. нет имени студента
    students = {}
    assert add_student(students, '', 18, 'Math') == 'Student  added.'


def test_add_student6(): #негативный планировался, но прошел успешно - None добавлен в словарь
    students = {} 
    assert add_student(students, None, 'ten', 'Math') == 'Student None added.'


#2. Тест - функции удаления студента из словаря. 

def test_remove_student():  #успешный, если студент с таким именем один.
    '''Тест функции удаления студентов из словаря.'''
    students = {'Peter': {'age': 18, 'major': 'Math'},
                'Kate': {'age': 19, 'major': 'Art'},
                'John': {'age': 18, 'major': 'Physics'}}
    assert remove_student(students, 'Kate') == 'Student Kate removed.'


'''Условия и циклы'''

#1. Тест функции для проверки возраста студента и вывода соответствующего сообщения.


def test_check_age1():
    my_students = {"Petrov": 16, "Sidorov": 18, "Ivanov": 36}
    assert check_age(my_students, 'Petrov') == 'Petrov - несовершеннолетний'
    assert check_age(my_students, 'Sidorov') == 'Sidorov - совершеннолетний'
    assert check_age(my_students, 'Ivanov') == 'Ivanov - совершеннолетний'
    

def test_check_age2():      #негативный.словарь пустой
    my_students = {}
    with pytest.raises(KeyError):
        check_age(my_students, 'Petrov')







