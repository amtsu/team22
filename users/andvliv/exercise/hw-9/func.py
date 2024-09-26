#ФУНКЦИИ ИЗ ДЗ №5
#Создайте функции set_union и set_difference для операций объединения и разности множеств.
#  - Функции должны принимать два множества и возвращать соответствующий результат.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
def set_union(set1, set2):
    return set1 | set2
set_union(set1, set2)

#Создайте функцию для проверки, является ли одно множество подмножеством другого.
def set_subset(set1, set2):
    result = 0
    if set1 >= set2:
        result = True
    else:
        result = False
    return result
set_subset(set1, set2)

#Создайте функцию для удаления конкретного элемента из множества.
set1 = {5, 4, 3, 2, 1}
n = 5

def set_remove(set1, n):
    set1.discard(n)
    return set1
    
set_remove(set1, n)

#Создайте функцию для проверки на равенство двух множеств.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 4, 5, 6}
def set_same(set1, set2):
    if set1 == set2:
        return True
    else:
        return False
set_same(set1, set2)

#Создайте функцию для проверки, являются ли два множества дизъюнктными (не имеют общих элементов).
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 4, 5, 6}
def sets_disjoint(set1, set2):
    if set1.isdisjoint(set2):
        result = True
    else:
        result = False
    return result
sets_disjoint(set1, set2)

#Создайте функцию для определения симметрической разности двух множеств.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 4, 5, 6}
def sets_symm_diff(set1, set2):
    return set1 ^ set2
sets_symm_diff(set1, set2)

#Создайте функцию для объединения двух словарей.
dict1 = {'Petrov': 'fat', 'Ivanov': 'hungry'}
dict2 = {'Sidorov': 'angry', 'Petrov': 'happy'}
def dicts_union(dict1, dict2):
    dict1.update(dict2)
    return dict1
dicts_union(dict1, dict2)

#Создайте функцию для поиска наибольшего значения в словаре.
dict_sample = {'Petrov': 20, 'Ivanov': 10, 'Apolon': 500, 'Zeus': 1000}
def dict_max(dict_sample):
    max_v = 0
    for i in dict_sample:
        if dict_sample[i] > max_v:
            max_v = dict_sample[i]
    return max_v
dict_max(dict_sample)

#Создайте функцию compare_sets_length, которая сравнивает длину двух множеств и выводит информацию о  том, какое из множеств длиннее.
#   - Функция должна принимать два множества и выводить соответствующее сообщение.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
def compare_sets_length(set1, set2):
    if len(set1) > len(set2):
        return 'set1 longer'
    elif len(set1) == len(set2):
        return 'same length'
    elif len(set1) < len(set2):
        return 'set2 longer'
        
compare_sets_length(set1, set2)

#Создайте функцию для определения четности или нечетности числа.
n = 5
def even_or_no(n):
    if n % 2 == 0:
        return 'n is even'
    elif n % 2 == 1:
        return 'n is no even'
even_or_no(n)

#Создайте функцию для определения високосного года.
age = 1998
def visokos_age(age):
    if age % 4 == 0:
        return True
    elif age % 4 != 0:
        return False
visokos_age(age)

#Создайте функцию для проверки, является ли строка палиндромом.
sentence = 'assa'
def palindrom_li(sentence):
    sentence = sentence.lower().split()
    sentence = ''.join(sentence)
    if sentence == sentence[::-1]:
        return True
    else:
        return False
palindrom_li(sentence)

#Создайте функцию для определения времени суток по введенному времени (утро, день, вечер, ночь).
time = '18:00'
def period_time(time):
    time = time.split(':')
    if int(time[0]) >= 0 and int(time[0]) < 6:
        return 'night'
    elif int(time[0]) >= 6 and int(time[0]) < 10:
        return 'morning'
    elif int(time[0]) >= 10 and int(time[0]) < 19:
        return 'day'
    elif int(time[0]) >= 19 and int(time[0]) < 24:
        return 'evening'
period_time(time)

#Создайте функцию, которая определяет, является ли введенное число простым.
n = 5
def prime_number(n):
    counter = 0
    for i in range(1, n):
        if n % i == 0:
            counter += 1
    if counter <= 1:
        return 'n is prime number'
    else:
        return 'n is not prime number'
prime_number(n)

#Создайте функцию для проверки входящей строки на наличие только буквенных символов.
s = '3, 2, 1, go'
def only_letters(s):
    if s.isalpha() == True:
        return 'string s has only letters'
    else:
        return 'string s has NOT only letters'
only_letters(s)

#Создайте функцию для определения дня недели по введенному номеру дня (1 - Понедельник, 2 - Вторник и т.д.)
n = 1
day_of_the_week = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
def whats_the_day(day_of_the_week, n):
    return day_of_the_week[n]
whats_the_day(day_of_the_week, n)

#Создайте функцию print_squares_while, которая использует цикл while для вывода квадратов чисел от 1 до 5.
n = 1
def print_squares_while(n):
    square_list = []
    while n < 6:
        square_list.append(n**2)
        n += 1
    return square_list    
print_squares_while(n)

#Создайте функцию для вывода факториала заданного числа.
n = 3
fact = 1
def factorial(n, fact):
    while n > 1:
        fact = fact*n
        n -= 1
    return fact
factorial(n, fact)

#Создайте функцию для поиска суммы чисел в заданном диапазоне.
x = 5
y = 10
sum = 0
def sum_numb(x, y, sum): 
    if x < y:
        for i in range(x, y + 1):
            sum += i
    elif x > y:
        for i in range(y, x + 1):
            sum += i
    if x == y:
        sum = y
    return sum
sum_numb(x, y, sum)

#Создайте функцию для генерации и вывода всех простых чисел до заданного числа.
n = 5
def all_prime_numbers(n):
    prime_list = []
    for i in range(1, n):
        counter = 0
        for j in range(1, i):   
            if i % j == 0:
                counter += 1
        if counter <= 1:
            prime_list.append(i)
    return prime_list
all_prime_numbers(n)

#Создайте функцию для проверки строки на палиндромность без учёта регистра и знаков препинания.
s = 'ASsa'
def pal_li(s):
    s = s.lower()
    list_s = list(s)
    s_free_list = []
    for i in range(len(list_s)):
        if str(list_s[i]).isalnum() == True:
           s_free_list.append(list_s[i])
    s_free = ''.join(s_free_list)
    if s_free == s_free[::-1]:
        return True
    else:
        return False
pal_li(s)

#Создайте функцию для поиска наибольшего общего делителя (НОД) двух чисел.
n = 10
m = 15
def nod(n, m):
    set_n = set()
    set_m = set()
    for i in range(1, n + 1):
        if n % i == 0:
            set_n.add(i)
    for k in range(1, m + 1):
        if m % k == 0:
            set_m.add(k)
    return(max(set_n & set_m))
nod(n, m)

#Создайте функцию, которая будет проверять введенную пользователем строку на наличие повторяющихся символов.
#   - Если такие символы найдены, программа должна выводить их список.
s = 'Abracadabra'
def same_symbol(s):
    set_same = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                set_same.add(s[j])
    return set_same
same_symbol(s)

#Создайте функцию, которая определяет, является ли введенная дата корректной.
date = '12.2.2012'
def correct_date(date):
    date = date.split('.')
    months = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    if len(date) == 3 and int(date[0]) <= months[date[1]] and int(date[0]) > 0 and int(date[1]) < 13 and int(date[1]) > 0 and ''.join(date).isdigit() == True:
        return True
    else:
        return False
correct_date(date)