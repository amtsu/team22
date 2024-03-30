def check_fruit_price(
    prices_dict,
    fruit
):
    '''Функция выводит сообщение о том, что товар дорогой, если его цена больше 1.5
    :param prices_dict: Словарь с парами фрукт - цена (название фруктов следует писать с заглавной буквы)
    :param fruit: название фрукта для поиска в словаре (следует писать с заглавной буквы)
    :return:
    '''
    ret = ''
    if fruit.capitalize() not in prices_dict.keys():
        ret = 'Ошибка! Такого фрукта в словаре не существует'
    else:
        if prices_dict[fruit.capitalize()] > 1.5:
            ret = 'дорогой товар'
        else:
           ret = 'товар не дорогой'
    return ret

def check_age(
    students,
    name  
):
    '''Функция выводит сообщение о том, Является ли запрашиваемый студент совершеннолетним
    :param students: Словарь с парами фамилия стдуента - возраст (фамилии следует писать с заглавной буквы)
    :param name: фамилия студента (следует писать с заглавной буквы)
    :return:
    '''
    ret = ''
    if name not in students.keys():
        ret = 'Ошибка! Такого студента в словаре не существует'
    else:
        if students[name] >= 18:
            ret = 'Совершеннолетний'
        elif students[name] <= 0:
            ret = 'Ошибка!'
        else:
            ret = 'Несовершеннолетний'
    return ret

def even_odd(num):
    '''Проверяет является ли число четным
    :param n: целое число
    :return: True or False
    '''
    if type(num) is not int:
        raise TypeError
    else:
        if num % 2 == 0:
            answer = 'Четное'
        else:
            answer = 'Нечетное'
    return answer

def leap_year(num):
    '''Проверяет является ли год високосным
    :param n: вещественное число
    :return: Строка 'високосный' или 'обычный' 
    '''
    if type(num) is not int:
        raise TypeError
    if num <= 45:
        ret = 'Обычный'
    elif num % 4 == 0 and num % 100 != 0:
        ret = 'Високосный'
    else:
        if num % 400 == 0:
            ret = 'Високосный'
        else:
            ret = 'Обычный'
    return ret

def is_pallindrom(string):
    '''Проверяет является ли строка палиндромом
    :param string: строка
    :return: True or False
    '''
    if type(string) is not str:
        raise TypeError
    if string == string[::-1]:
        return True
    else:
        return False

def time_of_day(time):
    '''Определяет время суток по введенному времени
    :param time:  текущее время в формате часы, минуты через пробел
    :return:
    '''
    if type(time) is not str:
        raise TypeError
    t = time.split()
    minute = int(t[0]) * 60 + int(t[1])
    if 0 <= minute < 180 or 1260 <= minute <= 1440:
        ret = 'Ночь'
    if 180 <= minute < 540:
        ret = 'Утро'
    if 540 <= minute < 900:
        ret = 'День'
    if 900 <= minute < 1260:
        ret = 'Вечер'
    return ret

def is_prime(n):
    '''Проверяет является ли число простым
    :param n: целое число
    :return: True or False
    '''
    if n <= 1 or n % 2 == 0:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
        return True 

def is_letter(
    string
):
    '''Проверяет строку на наличие только буквенных симоволов
    :param string: строка
    :return: True or False
    '''
    if type(string) is not str:
        raise TypeError
    if string.isalpha():
        return True
    else:
        return False

def is_date_correct(
):
    '''Проверяет является ли дата корректной
    :param:
    :return: True or False
    '''
    i = 0
    date = [int(i) for i in input('Введите дату(через пробел):\n').split()]
    d = date[0]
    m = date[1]
    y = date[2]
    answer = True
    if d > 31 or d < 1 or m > 12 or m < 1 or 45 >= y:
        answer = False
    else:
        if m == 4 or m ==6 or m == 9 or m == 11:
            if d == 31:
                answer = False
    if y % 4 == 0 and y % 100 != 0:
        if m == 2 and (d == 30 or d == 31):
            answer = False
    else:
        if y % 400 == 0 and m == 2 and (d == 30 or d == 31):
            answer = False
        else:
            if m == 2 and (d == 29 or d == 30 or d == 31):
                answer = False
    return answer

def d_o_w(n):
    '''Определяет день недели по введенному номеру дня
    :param n: числа от 1 до 7
    :return: день недели
    '''
    if n < 1 or n > 7:
        print('Такого дня не существует')
    else:
        day = {
            '1':'Понедельник',
            '2':'Вторник',
            '3':'Среда',
            '4':'Четверг', 
            '5':'Пятница', 
            '6':'Суббота',
            '7':'Воскресенье'
              }
    return day[str(n)]