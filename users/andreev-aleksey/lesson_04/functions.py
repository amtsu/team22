import math 

# функция вычисления процента факта от плана 
def percent_fact_plan_diff(plan, fact):
    percent_fact_plan = round((fact/plan*100), 2)
    diff = fact - plan
    print(f"diff = {diff}")
    print(f"percent_fact_plan = {percent_fact_plan}")


"""
Реализовать функцию, вычисляющую длину гипотенузы прямоугольного треугольника. Параметры – длины катетов.

plan_time_take = 15
fact_time_take = 26
diff = 11
percent_fact_plan = 173.33
"""
def hypotenuse_length(cat1: int | float, cat2: int | float) -> int | float | bool:
    """
    По двум заданным катетам вычисляет гипотенузу
    """
    if (cat1 <= 0) or (cat2 <= 0):
        return False
    gip = math.sqrt(cat1**2 + cat2**2)
    return gip



"""
Перепешите функцию из предыдущего задания используя следующие воодные:
Указание: для вычисления квадратного корня можно возвести число в степень 0, 5.
Можно использовать функцию, написанную в предыдущей задаче.

plan_time_take = 15
fact_time_take = 2
diff = -13
percent_fact_plan = 13.33
"""
def hypotenuse_length_05(cat1: int | float, cat2: int | float) -> int | float | bool:
    """
    По двум заданным катетам вычисляет гипотенузу
    """
    if (cat1 <= 0) or (cat2 <= 0):
        return False
    gip = (cat1**2 + cat2**2)**0.5
    return gip



"""
Написать функцию arithmetic, принимающую 3 аргумента: первые два - числа, третий - операция, которая должна быть произведена над ними.

Если третий аргумент равен ‘+’, сложить их
‘—’ -вычесть
‘*’ — умножить
‘/’ — разделить. В остальных случаях вернуть строку "Неизвестная операция". 
Ожидаемый результат

plan_time_take = 10
fact_time_take = 30
diff = 20
percent_fact_plan = 300.0
"""
def arithmetic(num1: int | float, num2: int | float, operator: str) -> int | float | bool:
    """Выполняет заданное математическое действие надо числами"""
    if num2 == 0:
        return False
    if operator not in ("+", "-", "/", "*"):
        return False
    operators = {
        "+": (num1 + num2),
        "-": (num1 - num2),
        "/": (num1 / num2),
        "*": (num1 * num2)
    }
    return operators[operator]



""" 
Написать функцию square_parameters, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.

plan_time_take = 10
fact_time_take = 28
diff = 18
percent_fact_plan = 280.0
"""
def square_parameters(side: int | float) -> tuple | bool:
    """По заданное стороне выдает
    * периметр
    * площадь
    * диагональ квадрата
    """
    if not (isinstance(side, int)) or (isinstance(side, float)):
        return False
    if side < 0:
        return False
    P = side*4
    S = side**2
    diag = side*(2**0.5)
    return (P, S, diag)



"""Написать функцию is_prime, принимающую 1 аргумент — число, и определяющее, простое оно или составное.

Простые числа делятся без остатка только на 1 и на самого себя. Если число делится без остатка на какое-то другое число, то оно составное.
"""
def is_prime(some_int):
    pass
# Сам не догадался. Посмотрел, что в интернете реализуют циклом while



"""
Написать функцию is_palindrome, принимающую 1 аргумент — строку (без пробелов, строчные буквы), и определяющее, является ли она палиндромом, т.е. читается одинаково слева направо и справа налево. 
Если да, вернуть True, иначе False.

plan_time_take = 10
fact_time_take = 20
diff = 10
percent_fact_plan = 200.0
"""

def is_palindrome(string: str) -> bool | int:
    """Проверяет палиндром"""
    if not isinstance(string, str):
        return -1
    if len(string.split(" ")) != 1:
        return -1
    if string == string[::-1]:
        return True
    else:
        return False



"""
Как решить предыдущую задачу с помощью срезов?
#plan_time_take = 10
"""
# Решил срезом сразу


"""
Как решить предыдущую задачу если сразу вернуть результат?
#plan_time_take = 15
Не понял задание. Имеется ввиду в одну строку? 

plan_time_take = 15
fact_time_take = 5
diff = -10
percent_fact_plan = 33.33
"""
def is_palindrome_one_string(string: str) -> bool | int:
    """Проверяет палиндром"""
    if not isinstance(string, str):
        return -1
    if len(string.split(" ")) != 1:
        return -1
    return True if string == string[::-1] else False



""" 
Усовершенствовать предыдущую функцию, чтобы проверяемая строка могла содержать пробелы, а также прописные и строчные буквы.
Кидал в зубра арбуз Владик
#plan_time_take = 15

plan_time_take = 15
fact_time_take = 17
diff = 2
percent_fact_plan = 113.33
"""
def is_palindrome_all_type_string(string: str) -> bool | int:
    """Проверяет строку на палиндром"""
    if not isinstance(string.lower(), str):
        return -1
    return True if string.lower().replace(" ", "") == string[::-1].lower().replace(" ", "") else False

