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
    result = False
    if isinstance(d, int) and isinstance(m, int) and isinstance(y, int):
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap2(y): #для високосного года заменяем количество дней в феврале на 29
            day_count_for_month[2] = 29
        if m >=1 and m <= 12 and d>=1 and d <= day_count_for_month[m]:
            result = True
    return result

