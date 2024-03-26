from hw_5 import (set_union,set_difference,set_union_many,delete_value,set_intersection_many,equality_sets,disjunctive,create_set,merge_dict,revert_dict,
                  max_element_v,check_age,compare_sets_length,even_or_odd_number,is_palindrome,times_of_day,day_week,povtor)

# Создайте функции set_union и set_difference для операций объединения и разности множеств

def test_set_union_1():
    input1 = {1, 3, 3, 4, 5, 6}
    input2 = {4, 5, 6, 7, 8}
    expected = {1, 3, 4, 5, 6, 7, 8}
    assert set_union(input1,input2) == expected, 'неправильно объединили множества'

def test_set_union_2():
    input1 = {1, 2, 3}
    input2 = {3, 3, 3, 3, 4}
    expected = {1, 2, 3, 4}
    assert set_union(input1,input2) == expected, 'неправильно объединили множества'

def test_set_union_3():
    input1 = {}
    input2 = {}
    expected = {}
    assert set_union(input1,input2) == expected, 'неправильно объединили множества'

def test_set_difference_1():
    input1 = {2,5,6,7,9}
    input2 = {4,5,7,8,9}
    expected = {2,6}
    assert set_difference(input1,input2) == expected, 'неправильно нашли разность множеств'

def test_set_difference_2():
    input1 = {2,5,6,7,9}
    input2 = {1,3,4,8}
    expected = {2,5,6,7,9}
    assert set_difference(input1,input2) == expected, 'неправильно нашли разность множеств'

def test_set_difference_3():
    input1 = {4}
    input2 = {4,5,7}
    expected = set()
    assert set_difference(input1,input2) == expected, 'неправильно нашли разность множеств'

# Создайте функцию для объединения нескольких множеств

def test_set_union_many_1 ():
    input1 = {1,2,3}
    input2 = {1,4,4,5}
    input3 = {2,4,6,5}
    input4 = {8,7,4,1}
    expected = {1, 2, 3, 4, 5, 6, 7, 8}
    assert set_union_many(input1,input2,input3,input4) == expected, 'неправильно объединили несколько множеств'

def test_set_union_many_2 ():
    input1 = {1}
    input2 = {}
    input3 = {6,5}
    input4 = {8,7}
    expected = {1, 5, 6, 7, 8}
    assert set_union_many(input1,input2,input3,input4) == expected, 'неправильно объединили несколько множеств'

def test_set_union_many_3 ():
    input1 = {}
    input2 = {}
    input3 = {}
    expected = set()
    assert set_union_many(input1,input2,input3) == expected, 'неправильно объединили несколько множеств'

# Создайте функцию для удаления конкретного элемента из множества

def test_delete_value_1 ():
    input1 = {1,2,4,88,6}
    input2 = 5
    expected = {1, 2, 4, 6, 88}
    assert delete_value(input1,input2) == expected, 'неправильно удален конкретный элемент из множества'

def test_delete_value_2 ():
    input1 = {1,2,3}
    input2 = 2
    expected = {1, 3}
    assert delete_value(input1,input2) == expected, 'неправильно удален конкретный элемент из множества'

def test_delete_value_3 ():
    input1 = {}
    input2 = 5
    expected = {}
    assert delete_value(input1,input2) == expected, 'неправильно удален конкретный элемент из множества'

# Создайте функцию для поиска пересечения нескольких множеств

def test_set_intersection_many_1 ():
    input1 = {1,2,3,10}
    input2 = {1,4,2,5,3}
    input3 = {2,4,3,5}
    input4 = {8,3,4,1}
    expected = {3}
    assert set_intersection_many(input1,input2,input3,input4) == expected, 'неправильно нашли пересечения нескольких множеств'

def test_set_intersection_many_2 ():
    input1 = {1,2,3,10}
    input2 = {1,4,2,5,3}
    input3 = {1,2,4,3,5}
    input4 = {8,3,4,1}
    expected = {1, 3}
    assert set_intersection_many(input1,input2,input3,input4) == expected, 'неправильно нашли пересечения нескольких множеств'

def test_set_intersection_many_3 ():
    input1 = {1,2,10}
    input2 = {1,4,2}
    input3 = {3,5}
    expected = set()
    assert set_intersection_many(input1,input2,input3) == expected, 'неправильно нашли пересечения нескольких множеств'

# Создайте функцию для проверки на равенство двух множеств.

def test_equality_sets_1():
    input1 = {1, 3, 3, 4, 5, 6}
    input2 = {1, 3, 4, 5, 6}
    expected = True
    assert equality_sets(input1,input2) == expected, 'неправильно проверили на равенство двух множеств'

def test_equality_sets_2():
    input1 = {1, 3, 3, 4, 5, 6}
    input2 = {1, 3, 4, 5, 6 , 7}
    expected = False
    assert equality_sets(input1,input2) == expected, 'неправильно проверили на равенство двух множеств'

def test_equality_sets_3():
    input1 = {}
    input2 = {}
    expected = True
    assert equality_sets(input1,input2) == expected, 'неправильно проверили на равенство двух множеств'

# Создайте функцию для проверки, являются ли два множества дизъюнктными (не имеют общих элементов).

def test_disjunctive_1():
    input1 = {1, 3, 3, 4, 5, 6}
    input2 = {1, 3, 4, 5, 6}
    expected = False
    assert disjunctive(input1,input2) == expected, 'неправильно проверили два множества на дизъюнкцию'

def test_disjunctive_2():
    input1 = {1, 3}
    input2 = {4, 5, 6}
    expected = True
    assert disjunctive(input1,input2) == expected, 'неправильно проверили два множества на дизъюнкцию'

def test_disjunctive_3():
    input1 = set()
    input2 = set()
    expected = False
    assert disjunctive(input1,input2) == expected, 'неправильно проверили два множества на дизъюнкцию'

# Функция должна принимать переменное количество аргументов и возвращать новое множество.

def test_create_set_1 ():
    input1 = 2
    input2 = "привет"
    input3 = 1.5
    input4 = ("mir",555)
    expected = {1.5, 2, 'привет', ('mir', 555)}
    assert create_set(input1,input2,input3,input4) == expected, 'неправильно нашли новое множество'

def test_create_set_2 ():
    input1 = 2
    input2 = 7777
    expected = {2, 7777}
    assert create_set(input1,input2) == expected, 'неправильно нашли новое множество'

def test_create_set_3 ():
    input1 = 2
    input2 = "привет"
    input3 = 1.7
    input4 = "привет"
    expected = {'привет', 2, 1.7}
    assert create_set(input1,input2,input3,input4) == expected, 'неправильно нашли новое множество'

# Создайте функцию для объединения двух словарей.

def test_merge_dict_1():
    input1 = {"Irina": 25, "Ivan" : 24, "Anton" : 33}
    input2 = {"Ivan": 11, "Dima" : 56, "Oleg" : 63}
    expected = {'Irina': 25, 'Ivan': 11, 'Anton': 33, 'Dima': 56, 'Oleg': 63}
    assert merge_dict(input1,input2) == expected, 'неправильно объединили два словаря'

def test_merge_dict_2():
    input1 = {"Ivan" : 33, "Anton" : 1}
    input2 = {"Dima" : 3}
    expected = {'Ivan': 33, 'Anton': 1, 'Dima': 3}
    assert merge_dict(input1,input2) == expected, 'неправильно объединили два словаря'

def test_merge_dict_3():
    input1 = {}
    input2 = {}
    expected = {}
    assert merge_dict(input1,input2) == expected, 'неправильно объединили два словаря'

def test_revert_dict_1():
    input1 = {}
    expected = {}
    assert revert_dict(input1) == expected, 'неправильно перевернули словарь'

def test_revert_dict_2():
    input1 = {
    'Война и мир': 500,
    'Незнайнка': 3000,
    'Остров сокровищь': 1500,
}
    expected = {500: 'Война и мир', 3000: 'Незнайнка', 1500: 'Остров сокровищь'}
    assert revert_dict(input1) == expected, 'неправильно перевернули словарь'

def test_revert_dict_3():
    input1 = {'Груша': 30,'Банан': 25,'Апельсин': 15,'Клубника': 35,}
    expected = {30: 'Груша', 25: 'Банан', 15: 'Апельсин', 35: 'Клубника'}
    assert revert_dict(input1) == expected, 'неправильно перевернули словарь'

# Создайте функцию возвращающую наибольшее значение элемента словаря.

def test_max_element_v_1():
    input1 = {
    'Война и мир': 500,
    'Незнайнка': 3000,
    'Остров сокровищь': 1500,
}
    expected = 3000
    assert max_element_v(input1) == expected, 'неправильно нашли наибольшее значение словаря'

def test_max_element_v_2():
    input1 = {'Груша': 30,'Банан': 25,'Апельсин': 15,'Клубника': 35,}
    expected = 35
    assert max_element_v(input1) == expected, 'неправильно нашли наибольшее значение словаря'

def test_max_element_v_3():
    input1 = {}
    expected = None
    assert max_element_v(input1) == expected, 'неправильно нашли наибольшее значение словаря'

def test_max_element_v_5():
    input1 = {'Груша': 370,'Банан': 25,'Апельсин': 15,'Клубника': 35,}
    expected = 370
    assert max_element_v(input1) == expected, 'неправильно нашли наибольшее значение словаря'

# Создайте функцию check_age для проверки возраста студента и вывода соответствующего сообщения.
# Функция должна принимать словарь студентов и имя студента, а затем выводить сообщение о совершеннолетии или несовершеннолетии.

def test_check_age_1():
    input1 = {"Irina": 25, "Ivan" : 14, "Anton" : 33}
    input2 = "Ivan6"
    expected = "нет такого"
    assert check_age(input1,input2) == expected, 'неправильно вывели сообщение о совершеннолетии или несовершеннолетии'

def test_check_age_2():
    input1 = {"Irina": 25, "Ivan" : 14, "Anton" : 33}
    input2 = "Ivan"
    expected = "Несовершеннолетний"
    assert check_age(input1,input2) == expected, 'неправильно вывели сообщение о совершеннолетии или несовершеннолетии'

def test_check_age_3():
    input1 = {"Irina": 25, "Ivan" : 14, "Anton" : 33}
    input2 = "Anton"
    expected = "Совершеннолетний"
    assert check_age(input1,input2) == expected, 'неправильно вывели сообщение о совершеннолетии или несовершеннолетии'

def test_check_age_4():
    input1 = {"Irina": 25, "Ivan" : 14, "Anton" : 33}
    input2 = "Irina"
    expected = "Совершеннолетний"
    assert check_age(input1,input2) == expected, 'неправильно вывели сообщение о совершеннолетии или несовершеннолетии'

def test_check_age_5():
    input1 = {"Irina": 25, "Ivan" : 14, "Anton" : 33}
    input2 = "Тима"
    expected = "нет такого"
    assert check_age(input1,input2) == expected, 'неправильно вывели сообщение о совершеннолетии или несовершеннолетии'

def test_check_age_6():
    input1 = {"Irina": 25, "Ivan" : 14, "Anton" : 33}
    input2 = "Ant0n"
    expected = "нет такого"
    assert check_age(input1,input2) == expected, 'неправильно вывели сообщение о совершеннолетии или несовершеннолетии'

def test_compare_sets_length_1():
    set1 = {1, 5, 6, 7, 8}
    set2 = {4, 5, 6, 7, 8}
    expected = "set1 и set2 одинаковы"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_compare_sets_length_2():
    set1 = {1, 3}
    set2 = {4, 5, 6, 7, 8}
    expected = "set1 меньше set2"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_compare_sets_length_3():
    set1 = {1, 5, 6, 7, 8}
    set2 = {4, 5, 6, 7, 8, 7, 5, 3}
    expected = "set1 меньше set2"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_compare_sets_length_4():
    set1 = {1, 5, 6, 7, 8}
    set2 = {1, 5, 6, 7, 8}
    expected = "set1 и set2 одинаковы"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_compare_sets_length_5():
    set1 = set()
    set2 = set()
    expected = "set1 и set2 одинаковы"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_compare_sets_length_6():
    set1 = set()
    set2 = {4, 5, 6, 7, 8, 7, 5, 3}
    expected = "set1 меньше set2"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_compare_sets_length_7():
    set1 = {4, 5, 6, 7, 8, 7, 5, 3}
    set2 = set()
    expected = "set1 больше set2"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_compare_sets_length_8():
    set1 = {4, 5, 6, 7, 8, 7, 5, 3}
    set2 = {4, 8, 7, 5, 3}
    expected = "set1 больше set2"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_compare_sets_length_9():
    set1 = {1, 1, 1, 1, 2, 1, 1}
    set2 = {9, 9, 9, 9, 9}
    expected = "set1 больше set2"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_compare_sets_length_10():
    set1 = {1}
    set2 = set()
    expected = "set1 больше set2"
    assert compare_sets_length(set1,set2) == expected, "задача про сравнение длины множеств"

def test_even_or_odd_number_1():
    input1 = 6
    expected = "6 четное"
    assert even_or_odd_number(input1) == expected, 'четность/нечетность'

def test_even_or_odd_number_2():
    input1 = 8
    expected = "8 четное"
    assert even_or_odd_number(input1) == expected, 'четность/нечетность'

def test_even_or_odd_number_3():
    input1 = -10
    expected = "-10 четное"
    assert even_or_odd_number(input1) == expected, 'четность/нечетность'

def test_even_or_odd_number_4():
    input1 = 7
    expected = "7 нечетное"
    assert even_or_odd_number(input1) == expected, 'четность/нечетность'

def test_even_or_odd_number_5():
    input1 = -11
    expected = "-11 нечетное"
    assert even_or_odd_number(input1) == expected, 'четность/нечетность'

def test_even_or_odd_number_6():
    input1 = 0
    expected = "0 четное"
    assert even_or_odd_number(input1) == expected, 'четность/нечетность'

def test_even_or_odd_number_7():
    input1 = -157
    expected = "-157 нечетное"
    assert even_or_odd_number(input1) == expected, 'четность/нечетность'

def test_even_or_odd_number_8():
    input1 = -43
    expected = "-43 нечетное"
    assert even_or_odd_number(input1) == expected, 'четность/нечетность'

def test_is_palindrome_1():
    input1 = "12321"
    expected = True
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_is_palindrome2():
    input1 = 'тут как тут'
    expected = True
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_is_palindrome_3():
    input1 = "тор"
    expected = False
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_is_palindrome_4():
    input1 = "fjfjfjfkjf"
    expected = False
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_is_palindrome_5():
    input1 = "05he9k3ejf7f"
    expected = False
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_is_palindrome_6():
    input1 = "шабаш"
    expected = True
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_is_palindrome_7():
    input1 = "комок"
    expected = True
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_is_palindrome_8():
    input1 = "3"
    expected = True
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_is_palindrome_9():
    input1 = "3п3п3"
    expected = True
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_is_palindrome_10():
    input1 = "апапывапап"
    expected = False
    assert is_palindrome(input1) == expected, 'строка палиндромом: да нет'

def test_times_of_day_1():
    input1 = 18
    input2 = 44
    expected = "вечер"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_2():
    input1 = 18
    input2 = 00
    expected = "вечер"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_3():
    input1 = 17
    input2 = 59
    expected = "день"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_4():
    input1 = 00
    input2 = 00
    expected = "ночь"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_5():
    input1 = 24
    input2 = 00
    expected = "ночь"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_6():
    input1 = 00
    input2 = 1
    expected = "ночь"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_7():
    input1 = 2
    input2 = 5
    expected = "ночь"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_8():
    input1 = 6
    input2 = 5
    expected = "утро"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_9():
    input1 = 6
    input2 = 0
    expected = "утро"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_9():
    input1 = 11
    input2 = 59
    expected = "утро"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_10():
    input1 = 12
    input2 = 0
    expected = "день"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_11():
    input1 = 20
    input2 = 32
    expected = "вечер"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_12():
    input1 = 23
    input2 = 21
    expected = "вечер"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_13():
    input1 = 18
    input2 = 59
    expected = "вечер"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_times_of_day_14():
    input1 = 19
    input2 = 44
    expected = "вечер"
    assert times_of_day(input1,input2) == expected, 'задача о времени суток'

def test_day_week_1():
    input1 = 1
    expected = "понедельник"
    assert day_week(input1) == expected, 'задача день недели'

def test_day_week_2():
    input1 = 2
    expected = "вторник"
    assert day_week(input1) == expected, 'задача день недели'

def test_day_week_3():
    input1 = 3
    expected = "среда"
    assert day_week(input1) == expected, 'задача день недели'

def test_day_week_4():
    input1 = 4
    expected = "четверг"
    assert day_week(input1) == expected, 'задача день недели'

def test_day_week_5():
    input1 = 5
    expected = "пятница"
    assert day_week(input1) == expected, 'задача день недели'

def test_day_week_6():
    input1 = 6
    expected = "суббота"
    assert day_week(input1) == expected, 'задача день недели'

def test_day_week_7():
    input1 = 7
    expected = "воскресенье"
    assert day_week(input1) == expected, 'задача день недели'

def test_day_week_8():
    input1 = 8
    expected = "не правильное число"
    assert day_week(input1) == expected, 'задача день недели'

def test_day_week_9():
    input1 = 0
    expected = "не правильное число"
    assert day_week(input1) == expected, 'задача день недели'

def test_day_week_10():
    input1 = -43
    expected = "не правильное число"
    assert day_week(input1) == expected, 'задача день недели'

def test_povtor_1():
    input1 = 'fgdgfgdgdg'
    expected = {'d': 3, 'f': 2, 'g': 5}
    assert povtor(input1) == expected, 'задача на наличие повторяющихся символов'

def test_povtor_2():
    input1 = 'ftlj'
    expected = {}
    assert povtor(input1) == expected, 'задача на наличие повторяющихся символов'

def test_povtor_3():
    input1 = 'rrr444u7fffff'
    expected = {'4': 3, 'f': 5, 'r': 3}
    assert povtor(input1) == expected, 'задача на наличие повторяющихся символов'

def test_povtor_4():
    input1 = '1234567ывапрол'
    expected = {}
    assert povtor(input1) == expected, 'задача на наличие повторяющихся символов'

def test_povtor_5():
    input1 = '1234567ывапрол7'
    expected = {'7': 2}
    assert povtor(input1) == expected, 'задача на наличие повторяющихся символов'

def test_povtor_6():
    input1 = '1234567ыва6прол7'
    expected = {'6': 2, '7': 2}
    assert povtor(input1) == expected, 'задача на наличие повторяющихся символов'

def test_povtor_7():
    input1 = 'f456нркиву845р4рка9у85ц4рк5г4в0хша'
    expected = {'4': 5, '5': 4, '8': 2, 'а': 2, 'в': 2, 'к': 3, 'р': 4, 'у': 2}
    assert povtor(input1) == expected, 'задача на наличие повторяющихся символов'

def test_povtor_8():
    input1 = ''
    expected = {}
    assert povtor(input1) == expected, 'задача на наличие повторяющихся символов'