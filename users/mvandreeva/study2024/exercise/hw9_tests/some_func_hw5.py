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

