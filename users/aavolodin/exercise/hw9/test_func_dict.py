from func_dict import create_dictionary, add_student, remove_student, unification, del_dict, dict_shift, dict_sorting, max_element, max_element1, check_fruit_price, check_age, compare_sets_length, proverka, leap_year, triangle_type, prover, simple, check_string, correct_date, palindrom, weekday, factorial

def test_create_dictionary():
    assert {'name': 'Ivan', 'age': 26, 'city': 'Samara'} == create_dictionary(name='Ivan', age=26, city='Samara')
test_create_dictionary()

def test_add_student():
    student = { 'anna': 20, 'misha': 22}
    assert {'anna': 20, 'misha': 22, 'sasha': 21} == add_student(student, 'sasha', 21)
test_add_student()

def test_remove_student():
    student = {'anna': 20, 'misha': 22, 'sasha': 21}
    assert {'misha': 22, 'sasha': 21} == remove_student(student, 'anna')
test_remove_student()   

def test_unification():
    a = {'a': 1, 'b': 2}
    b = {'c': 3, 'd': 4}
    assert {'a': 1, 'b': 2, 'c': 3, 'd': 4} == unification(a, b)
test_unification()   

def test_del_dict():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    assert {'a': 1, 'c': 3} == del_dict(my_dict, 'b')
test_del_dict()

def test_dict_shift():
    dict1 = {'a': 1, 'b': 2, 'c': 3} 
    assert {1: 'a', 2: 'b', 3: 'c'} == dict_shift (dict1)
test_dict_shift ()

def test_dict_sorting():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    assert {'c': 3, 'b': 2, 'a': 1} == dict_sorting(dict1)
test_dict_sorting()

def test_max_element():
    dict = {'a': 10, 'b': 5, 'c': 15}
    assert ('c', 15) == max_element(dict)
test_max_element()

def test_max_element1():
    dict = {'a': 10, 'b': 5, 'c': 15}
    assert 15 == max_element1(dict)
test_max_element1()

def test_check_fruit_price():
    prices = {"яблоко": 1.5, "банан": 2,"апельсин": 1.2} 
    assert 'приемлимая цена' == check_fruit_price(prices,"апельсин")
test_check_fruit_price()

def test_check_fruit_price1():
    prices = {"яблоко": 1.5, "банан": 2,"апельсин": 1.2} 
    assert 'дорогой товар' == check_fruit_price(prices,"банан")
test_check_fruit_price()

def test_check_age():
    students = {"Иванов": 22, "Петрова": 13, "Сидоров": 23} 
    assert 'Несовершеннолетний' == check_age(students, "Петрова")  
test_check_age()

def test_check_age1():
    students = {"Иванов": 22, "Петрова": 13, "Сидоров": 23} 
    assert 'Совершеннолетний' == check_age(students, "Иванов")  
test_check_age()

def test_compare_sets_length():
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3}
    assert 'set1 длиннее set2' == compare_sets_length(set1, set2)
test_compare_sets_length()

def test_compare_sets_length1():
    set2 = {1, 2, 3, 4, 5}
    set1 = {1, 2, 3}
    assert 'set2 длиннее set1' == compare_sets_length(set1, set2)
test_compare_sets_length()

def test_proverka():
    a = 6
    assert 'Четное число' == proverka(a)
test_proverka()

def test_proverka1():
    a = 5
    assert 'Нечетное число' == proverka(a)
test_proverka()

def test_leap_year():
    year = 2000
    assert True == leap_year((year))
test_leap_year()

def test_leap_year1():
    year = 2001
    assert False == leap_year((year))
test_leap_year()

def test_acute_1():
    input = [12,12,5]  
    expected =  "остроугольный"
    assert expected == triangle_type(*input)
test_acute_1()

def test_acute_2():
    input = [5,8,12] 
    expected =  "тупоугольный"
    assert expected == triangle_type(*input)
test_acute_2() 

def test_acute_3():
    input = [5,3,4] 
    expected =  "прямоугольный"
    assert expected == triangle_type(*input)
test_acute_3()

def test_prover():   
    name = 'anna'
    assert 'палиндром' == prover(name)
test_prover() 

def test_prover1():   
    name = 'saha'
    assert 'не палиндром' == prover(name)
test_prover1()

def test_simple():
    g = 4
    assert 'составное число' == simple(g)  
test_simple()

def test_simple1():
    g = 2
    assert 'простое число' == simple(g)  
test_simple1()

def test_check_string():
    string = "sde5e5"
    assert False == check_string(string)
test_check_string()

def test_check_string1():
    string = "sasdcasv"
    assert True == check_string(string)
test_check_string1()

#def test_correct_date():
    #input_date = '2024-02-30'
    #assert "Дата введена некорректно" == correct_date(input_date)
#test_correct_date()
      
def test_palindrom():
    name = "121"
    assert 'палиндром' == palindrom(name)
test_palindrom() 
    
def test_palindrom1():
    name = "124"
    assert 'не палиндром' == palindrom(name)
test_palindrom1() 

def test_weekday():
    n = 1
    assert 'понедельник' == weekday(n)
test_weekday()  

def test_weekday1():
    n = 2
    assert 'вторник' == weekday(n)
test_weekday1()

def test_weekday2():
    n = 3
    assert 'среда' == weekday(n)
test_weekday2() 

def test_weekday3():
    n = 4
    assert 'четверг' == weekday(n)
test_weekday3() 

def test_weekday4():
    n = 5
    assert 'пятница' == weekday(n)
test_weekday4() 

def test_weekday5():
    n = 6
    assert 'суббота' == weekday(n)
test_weekday5() 

def test_weekday6():
    n = 7
    assert 'воскресенье' == weekday(n)
test_weekday6() 

def test_factorial():
    q = 5
    assert 120 == factorial(q)
test_factorial()
   
