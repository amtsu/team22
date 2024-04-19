def compare_sets_length(set1,set2):
    """Функция сравнения длин двух множеств"""
    result = None
    if isinstance(set1, set) and isinstance(set2,set):
        if len(set1) > len(set2):
            result = f"Длина set1 больше, чем длина set2"
        elif len(set1) < len(set2):
            result = f"Длина set1 меньше, чем длина set2"
        elif len(set1) == len(set2):
            result = f"Длины равны"
    return result

def define_triangle_type(a,b,c):
    """
    Функция определения типа треугольника по длинам сторон 
    Принимает длины сторон, возвращает "остроугольный, прямоугольный, тупоугольный, разносторонний, равносторонний, равнобедренный или не треугольник"
    """
    result = "Не треугольник"
    triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and triangle_exist:
        sides_list = [a,b,c]
        # print(sides_list)
        max_side = max(sides_list)
        # print(30*'=')
        # print(max_side)
        less_sides_list = sides_list[:]
        less_sides_list.remove(max_side)
        # print(30*'=')
        # print(less_sides_list)
        if (max_side ** 2) < ((less_sides_list[0] ** 2) + (less_sides_list[1] ** 2)):
            result = "Остроугольный треугольник"
        elif (max_side ** 2) > ((less_sides_list[0] ** 2) + (less_sides_list[1] ** 2)):
            result = "Тупоугольный треугольник"
        elif (max_side ** 2) == ((less_sides_list[0] ** 2) + (less_sides_list[1] ** 2)):
            result = "Прямоугольный треугольник"
    return result
    

def define_day_part(any_time):
    """
    Функция определения времени суток по введенному времени 
    Принимает текущее время в формате часы, минуты, возвращает утро, день, вечер, ночь
    """
    hours_str = any_time[:2]
    hours = int(hours_str)
    if hours >= 0 and hours <5:
        result = "Ночь"
    elif hours >= 5 and hours <12:
        result = "Утро"
    elif hours >= 12 and hours <17:
        result = "День"
    elif hours >= 17 and hours <24:
        result = "Вечер"
    return result

def check_all_letters(some_str):
    """
    Функция проверки входящей строки на наличие только буквенных символов
    """
    result = False
    if some_str.isalpha():
        result = True
    return result

def deff_week_day(num):
    """
    Функция определения дня недели по введенному номеру дня
    """
    week = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6:"Суббота", 7: "Воскресение"}
    if num >= 1 and num <= 7: 
        for day in week.keys():
            return week[num]

def count_factorial(num):
    """
    Функция вывода факториала заданного числа
    """
    result = None
    if num >= 0 and num <= 1:
        result = 1
    elif num > 1:
        result = num * count_factorial(num - 1)
    return result

def sum_cummulat(num1, num2):
    """
    Функция для поиска суммы чисел в заданном диапазоне
    """
    cu_sum = 0
    for i in range(num1, (num2 + 1)):
        cu_sum += i
    return cu_sum

def is_prime(any_num):
    """
    Функция определяет, является ли введенное число простым
    """
    result = False
    if any_num >= 2: 
        divider_list = []
        for i in range (2, any_num): 
            if any_num % i == 0:
                divider_list.append(i)
        if divider_list == []:
            result = True
    return result

def generate_prime(num):
    """
    Функция генерации и вывода всех простых чисел до заданного числа
    """
    prime_list = []
    for i in range(2, num):
        if is_prime(i):
           prime_list.append(i) 
    return prime_list

def print_students(student_dict):
    """
    Функция вывода информации о студентах из словаря
    """
    student_info_list = []
    for student in student_dict.keys():
        student_info_list.append(f"Студент: {student}, возраст: {student_dict[student]} годик(ов)")
    return student_info_list

def has_repeats():
    """
    Функция проверки введенной пользователем строки на наличие повторяющихся символов
    """
    user_str = input("Здесь можно что-то написать")
    counter = {}
    result = {}
    user_str_list = list(user_str)
    for i in user_str_list:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 1
    for letter, count in counter.items():
        if count > 1:
            result[letter] = count
    return result

def check_age():
    """
    Функция Проверяет введенныйпользователем возраст с выводом возрастной категории пользователя 
    """
    result = ""
    user_age = input("Введите Ваш возраст")
    try:
        ua_int = int(user_age)
    except:
        print("Неверный ввод")
    else:
        if 0 < ua_int < 18:
            result = "Несовершеннолетний"
        elif 18 <= ua_int <= 65:
            result = "Совершеннолетний"
        elif ua_int > 65:
            result = "Пенсионер"
    return result

def is_palindrome(some_str):
    """Функция проверки, является ли строка палиндромом"""
    result = False
    if isinstance(some_str, str):
        lower_str = some_str.lower()
        str_filter = filter(lambda x: x.isalpha(), lower_str)
        str_list = list(str_filter)
        reversed_str_list = list(reversed(str_list[:]))
        if str_list != [] and str_list == reversed_str_list:
            print("Палиндром")
            result = True
        else:
            print("Не палиндром")
    else:
        print("Неверный аргумент")
        result = None
    return result

def great_com_divide(num1, num2):
    """
    Функция определения наибольшего общего делителя двух чисел
    """
    result = None
    if isinstance(num1, int) and isinstance(num2, int):
        min_num = min([num1, num2])
        dev_list = []
        for i in range(1, min_num + 1):
            if num1 % i == 0 and num2 % i == 0:
                dev_list.append(i)
        
        if dev_list != []:
            result = max(dev_list)
    return result

def is_leap2(any_year):
    """Функция определения високосного года"""
    result = False
    if isinstance(any_year, int):
        if any_year % 4 != 0:
            print('Год не високосный.')
        elif any_year % 100 == 0:
            if any_year % 400 == 0:
                print('Год високосный.')
                result = True
            else:
                print('Год не високосный.')
        else:
            print('Год високосный.')
            result = True
    else:
        print(f"{any_year} не является годом")
        result = None
    return result

def is_correct_date(d, m, y):
    """
    Функция определяет корректность даты
    """
    result = False
    if isinstance(d, int) and isinstance(m, int) and isinstance(y, int):
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap2(y): #для високосного года заменяем количество дней в феврале на 29
            day_count_for_month[2] = 29
        if m >=1 and m <= 12 and d>=1 and d <= day_count_for_month[m]:
            result = True
    return result

def show_fruits_info(product_quantity_dict, product_price_dict):
    """Функция выводит для каждого фрукта его стоимость и количество из соответствующих словарей"""
    result_list = []
    if isinstance(product_quantity_dict, dict) and isinstance(product_price_dict, dict):
        if product_quantity_dict != {} and product_price_dict != {}:
            for product in product_quantity_dict.keys():
                result_list.append(f"{product}, количество: {product_quantity_dict[product]}, цена: {product_price_dict[product]}")
    return result_list

def show_squares_while():
    """Функция использует цикл while для вывода квадратов чисел от 1 до 5"""
    result_list = []
    i = 1
    while i < 5:
        result_list.append(i**2)
        i += 1
    return result_list


def get_value_from_user(threshold_num):
    result = False
    if isinstance(threshold_num, int):
        user_input = input(f"Введите число больше {threshold_num}")
        try:
            ui_int = int(user_input)
        except ValueError:
            print("Неверный ввод")
            get_value_from_user(threshold_num)
        if ui_int > threshold_num:
            print("Поздравляю, всё верно")
            result = True
        else:
            print("Вы ввели не то число")
            get_value_from_user(threshold_num)
    else:
        print("Неверный параметр функции")
    return result








