from func_if_and_for import check_age, compare_sets_length, number, leap_year, triangle_type, identify_time, determine_number, check_string, check_word, check_day, sum_problem, check_str, find_NOD

#Создайте функцию check_age для проверки возраста студента и вывода соответствующего сообщения.
def test_check_age ():
    student = {'anna':20, 'ivan':18, 'shaha':17}
    assert 'совершеннолетний' == check_age(student, 'anna')#студент является совершеннолетним
test_check_age()

def test_check_age_2():
    student = {'anna':20, 'ivan':18, 'shaha':17}
    assert 'несовершеннолетний' == check_age(student, 'shaha')#студент является несовершеннолетним
test_check_age_2()

#Создайте функцию compare_sets_length, которая сравнивает длину двух множеств и выводит информацию о  том, какое из множеств длиннее.
def test_compare_sets_length ():
    set1 = (1,2,3,4)
    set2 = (5,6,7)
    assert 'множество 1 больше множества 2' == compare_sets_length(set1,set2)
test_compare_sets_length()

def test_compare_sets_length_2():
    set1 = (1,2,3,4)
    set2 = (5,6,7,8,9)
    assert 'множество 2 больше множества 1' == compare_sets_length(set1,set2)
test_compare_sets_length_2()

#Создайте функцию для определения четности или нечетности числа.
def test_number ():
    num = 6
    assert True == number(num)
test_number()

def test_number_2():
    num = 5
    assert False == number(num)
test_number()

#високосным считается год, который кратен 4 и не кратен 100 или кратен 400
def test_leap_year ():
    assert True == leap_year(2024)
test_leap_year ()

def test_leap_year_2 ():
    assert True == leap_year(2020)
test_leap_year_2()

def test_leap_year_3():
    assert False == leap_year(1900)
test_leap_year_3()

#Создайте функцию для определения типа треугольника по длинам сторон (принимает длины сторон, возвращает "остроугольный, прямоугольный, тупоугольный или не треугольник").

def test_acute():
    """
    тестируем остроугольность треугольника
    """
    input = [12,12,5] # такие стороны у остроугольного треугольника 
    expected =  "остроугольный"
    assert expected == triangle_type(*input)
test_acute()

def test_obtuse():
    """
    тестируем тупоугольность треугольника
    """
    input = [5,8,12] # такие стороны у тупоугольного треугольника
    expected =  "тупоугольный"
    assert expected == triangle_type(*input)
test_obtuse()

def test_right():
    """
    тестируем прямоугольность треугольника
    """
    input = [5,3,4] # такие стороны у прямоугольного треугольника 
    expected =  "прямоугольный"
    assert expected == triangle_type(*input)
test_right()

def test_not_triangle():
    """
    тестируем не треугольник
    """
    input = [5,5,12] #не может быть таких длин сторон
    expected =  "не треугольник"
    assert expected == triangle_type(*input)
test_not_triangle()

def test_not_triangle_str():
    """
    тестируем не треугольник
    """
    input = ['a','b','c'] #заданы строковые значение, а не числа
    expected =  "не треугольник"
    assert expected == triangle_type(*input)
test_not_triangle_str()

def test_negative():
    """
    негативный тест
    """
    input = [-5,-4,-3] #заданы отрицательные значения в функции для проверки остроугольности треугольника
    expected =  "остроугольный"
    assert expected != triangle_type(*input)
test_negative()

#Создайте функцию для определения времени суток по введенному времени ( принимает текущее время в формате часы, минуты, возвращает утро, день, вечер, ночь).
#Утро - с 06:00 до 12:00 День - с 12:00 до 18:00 Вечер - с 18:00 до 24:00 Ночь - с 00:00 до 06:00.
def test_identify_time ():
    assert 'утро' == identify_time (6,40)
test_identify_time()

def test_identify_time_2():
    assert 'день' == identify_time (14,30)
test_identify_time()

def test_identify_time_3():
    assert 'вечер' == identify_time (19,30)
test_identify_time()

def test_identify_time_4():
    assert 'ночь' == identify_time (2,10)
test_identify_time()

#Создайте функцию, которая определяет, является ли введенное число простым.
def test_determine_number():
    numer = 17
    assert True == determine_number(numer) 
test_determine_number()

def test_determine_number_2():
    numer = 6
    assert False == determine_number(numer) 
test_determine_number_2()

#Создайте функцию для проверки входящей строки на наличие только буквенных символов.
def test_check_string ():
    string = 'Anna'
    assert True == check_string(string)
test_check_string()

def test_check_string_2():
    string = 'An123na'
    assert False == check_string(string)
test_check_string_2()

def test_check_word():
    word = 'anna'
    assert 'палиндром' == check_word(word)
test_check_word()

def test_check_word_2():
    word = 'ежик'
    assert 'не палиндром' == check_word(word)
test_check_word_2()

#Создайте функцию для определения дня недели по введенному номеру дня (1 - Понедельник, 2 - Вторник и т.д.).
def test_check_day():
    day=1
    assert 'понедельник' == check_day(day)
test_check_day()

def test_check_day_2():
    day=5
    assert 'пятница' == check_day(day)
test_check_day_2()

def test_check_day_3():
    day=10
    assert 'число неверное' == check_day(day)
test_check_day_3()

#Создайте функцию для поиска суммы чисел в заданном диапазоне (принимает на вход два числа, возвращает сумму чисел находящихся между ними, включительно.)
def test_sum_problem():
    num1 = 2
    num2 = 4
    assert 9 == sum_problem(2,4)
test_sum_problem()

#Создайте функцию для проверки строки на палиндромность без учёта регистра и знаков препинания.
'''тест на проверку строки на палиндромность учитывая наличие пробелов в строке '''
def test_check_str():
    line = 'леша на полке клопа нашел'
    assert 'палиндром' == check_str(line)
test_check_str()

'''тест на проверку строки на палиндромность учитывая регистр '''
def test_check_str_2():
    line = 'Леша на Полке клопа нашел'
    assert 'палиндром' == check_str(line)
test_check_str_2()

'''тест на проверку строки на палиндромность учитывая наличие знаков препинания'''
def test_check_str_3():
    line = 'леша, на полке? клопа нашел.'
    assert 'палиндром' == check_str(line)
test_check_str_3()

'''тест на проверку строки на палиндромность учитывая наличие пробелов,знаков препинания и регистр'''
def test_check_str_4():
    line = 'Леша, на полке? Клопа нашел.'
    assert 'палиндром' == check_str(line)
test_check_str_4()
'''тест на проверку строки, которая не является палиндромом'''

def test_check_not_str():
    line = 'не палиндром'
    assert 'не палиндром' == check_str(line)
test_check_not_str() 

#Создайте функцию для поиска наибольшего общего делителя (НОД) двух чисел.
def test_find_NOD ():
    num1 = 4
    num2 = 8
    assert 4 == find_NOD(num1,num2)
test_find_NOD()