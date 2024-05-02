#Создайте функцию check_fruit_price для проверки стоимости фрукта и вывода соответствующего сообщения.
#Функция должна принимать словарь цен на фрукты и название фрукта, а затем выводить сообщение "дорогой товар", если цена фрукта больше 1.5.
# функция выводит стоимость всех фруктов словаря, название фрукта цена которого больше 1.5
def check_fruit_price (dict_fruit_price):
    for k in dict_fruit_price.keys():
        print (k, 'стоит', dict_fruit_price[k])
    if dict_fruit_price[k]>1.5:
        print (k, 'дорогой товар')

#Создайте функцию check_age для проверки возраста студента и вывода соответствующего сообщения.
#Функция должна принимать словарь студентов и имя студента, а затем выводить сообщение о совершеннолетии или несовершеннолетии.
def check_age (dict_student, name):
    #for k in dict_student.keys():
        if dict_student[name]>=18:
            result = 'совершеннолетний'
        elif dict_student[name]<18:
            result = 'несовершеннолетний'
        return result
            
#Создайте функцию compare_sets_length, которая сравнивает длину двух множеств и выводит информацию о  том, какое из множеств длиннее.
#Функция должна принимать два множества и выводить соответствующее сообщение.
def compare_sets_length (set1,set2):
    if len(set1)>len(set2):
        result = ('множество 1 больше множества 2')
    elif len(set2)>len(set1):
        result = ('множество 2 больше множества 1')
    return result
    
#Создайте функцию для определения четности или нечетности числа.
def number (num):
    if num%2==0:
        #print (num, '- четное число')
        return True
    if num%2>0:
        #print (num, '- нечетное число')
        return False

#високосным считается год, который кратен 4 и не кратен 100 или кратен 400def leap_year (year):
def leap_year (year):
    #result = True 
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print (year, '-високосный год')
        return True
    else:
        print (year, '- невисокосный год')
        return False
    

#Создайте функцию для определения типа треугольника по длинам сторон (принимает длины сторон, возвращает "остроугольный, прямоугольный, тупоугольный или не треугольник").
def triangle_type(a: float, b: float, c: float) -> str:
    """
    Функция, определяющая тип треугольника по длинам его сторон
    """
    result = "не треугольник"
    triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
    if triangle_exist:
        sides = [a, b, c]
        sides.sort()
        acuteTriangle = (sides[0]**2 + sides[1]**2) > sides[2]**2
        obtuseTriangle = (sides[0]**2 + sides[1]**2) < sides[2]**2
        rightTriangle = abs((sides[0]**2 + sides[1]**2) - sides[2]**2) <= 0.01

        if acuteTriangle:
            result = "остроугольный"
        elif obtuseTriangle:
            result = "тупоугольный"
        elif rightTriangle:
            result  = "прямоугольный"
    return result 

#Создайте функцию для определения времени суток по введенному времени ( принимает текущее время в формате часы, минуты, возвращает утро, день, вечер, ночь).
#Утро - с 06:00 до 12:00 День - с 12:00 до 18:00 Вечер - с 18:00 до 24:00 Ночь - с 00:00 до 06:00.
def identify_time (hour, min):
    if (hour >=6 and hour < 12) and (min>=0 and min <=59):
        result = 'утро'
    elif (hour >= 12 and hour <18) and (min>=0 and min <=59):
        result = 'день'
    elif (hour >= 18 and hour <24) and (min>=0 and min <=59):
        result = 'вечер'
    elif (hour >= 0 and hour <6) and (min>=0 and min <=59):
        result = 'ночь'
    return result


#Создайте функцию, которая определяет, является ли введенное число простым.
def determine_number(numer):
    i=0
    for k in range(2, numer):
        if numer%k == 0:
            i+=1
    if i == 0:
        print ('простое число')
        return True
    else:
        print ('не простое число')
        return False
print (determine_number(8))


#Создайте функцию для проверки входящей строки на наличие только буквенных символов.
def check_string (string):
    if string.isalpha():
        print ('строка состоит только из буквенных символов')
        return True
    else:
        print('строка состоит не только из буквенных символов')
        return False

def check_word(word):
    word2=word[::-1]
    if word==word2:
        result  = 'палиндром'
    else:
        result = 'не палиндром'
    return result

#Создайте функцию для определения дня недели по введенному номеру дня (1 - Понедельник, 2 - Вторник и т.д.).
def check_day(day):
    if day==1:
        result = ('понедельник')
    elif day==2:
        result = ('вторник')
    elif day==3:
        result = ('среда')
    elif day==4:
        result = ('четверг')  
    elif day==5:
        result = ('пятница')  
    elif day==6:
        result = ('суббота') 
    elif day==7:
        result = ('воскресенье')
    else:
        result = ('число неверное')
    return result 

def sum_problem(a, b):
    return (a + b) * (abs(a - b) + 1) // 2

#Создайте функцию для генерации и вывода всех простых чисел до заданного числа.
#def prime_numbers (numer):
    #list_prime_numbers = []
    #for k in range(2, numer):
        #if determine_number(k):
        #list_prime_numbers.append(k)  
    #return list_prime_numbers

#Создайте функцию для проверки строки на палиндромность без учёта регистра и знаков препинания.
def check_str(str):
    #удаляю пробелы из строки
    str = str.replace(' ','')
    #привожу буквы к нижнему регистру
    str = str.lower()
    #удаляю знаки припинания
    import string
    str = str.translate(str.maketrans('', '', string.punctuation))
    #переворачиваю строку присваиваю ей новую переменную
    str2 = str[::-1]
    #сравниваю строки
    if str==str2:
        result = ('палиндром')
    else:
        result = ('не палиндром')
    return result

#Создайте функцию для поиска наибольшего общего делителя (НОД) двух чисел.
def find_NOD (num1, num2):
#нахожу все делители для числа №1, записываю в список
    list_num1 = []
    for i in range(1, num1+1):
        if num1%i == 0:
            list_num1.append(i)
#нахожу все делители для числа №2, записываю в список
    list_num2 = []
    for i in range(1, num2+1):
        if num2%i == 0:
            list_num2.append(i) 
    #print (list_num1, list_num2)
#нахожу пересечение списков и в нем нахожу максимальное значение
    list_num3 = []
    for a in list_num1:
        for b in list_num2:
            if a == b:
                list_num3.append(a)
                list_max = max(list_num3)
    return list_max
