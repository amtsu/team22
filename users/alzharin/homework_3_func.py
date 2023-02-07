"""
file with functions for homework3
"""


def gip(num1: float, num2: float) -> float:
    """
    func for finding hypotenuza
    """
    return (num1**2 + num2**2) ** (1 / 2)


def arithmetic(num1: float, num2: float, sign: str):
    """
    func for calc
    """
    result = None
    if sign == "+":
        res = num1 + num2
    elif sign == "-":
        res = num1 - num2
    elif sign == "*":
        res = num1 * num2
    elif sign == "/":
        res = num1 / num2
    else:
        print("Fail")
        return None
    return res


def square_parameters(size: float) -> tuple[float, float, float]:
    """
    func for finding hypotenuza
    """
    perimeter = 4 * size
    ploshad = size**2
    diagonal = size * 2 ** (1 / 2)
    return perimeter, ploshad, diagonal


def is_prime(num: int) -> None:
    """
    func for checking simple or complex
    """
    koef = 0
    for i in range(1, num + 1):
        if num % i == 0:
            koef += 1

    if num <= 0:
        print("NO")
    elif koef == 1:
        print("1 is not simple and complex")
    elif koef == 2:
        print("Simple")
    else:
        print("Complex")


def is_palindrome(stroka: str):
    """
    func for check palindrome
    """
    return stroka == stroka[::-1]
