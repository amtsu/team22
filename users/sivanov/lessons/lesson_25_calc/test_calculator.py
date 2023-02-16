"""
файл с описанием тестов класса calculator
"""
import pytest
import calculator


def test_calculator_1():
    """
    один из тестов  класса калькулятор
    простое вычитание
    """
    calc = calculator.Calculator()
    assert calc("1-4") == -3


def test_calculator_2():
    """
    один из тестов  класса калькулятор
    вычитание с унарным оператором в качестве
    первого аргумента
    """
    calc = calculator.Calculator()
    assert calc("-1-4") == -5


def test_calculator_3():
    """
    один из тестов  класса калькулятор
    вычитание двух унарных операторов
    """
    calc = calculator.Calculator()
    assert calc("-1 - -4") == 3


def test_calculator_4():
    """
    один из тестов  класса калькулятор
    деление
    """
    calc = calculator.Calculator()
    assert calc("1/4") == 0.25


def test_calculator_5():
    """
    один из тестов  класса калькулятор
    умножение на унарный оператор
    """
    calc = calculator.Calculator()
    assert calc("5*(-4.1)") == -20.5


def test_calculator_6():
    """
    один из тестов  класса калькулятор
    """
    calc = calculator.Calculator()
    with pytest.raises(AssertionError):
        calc("5*()")


def test_calculator_7():
    """
    один из тестов  класса калькулятор
    некорректные входные данные, assertion error
    """
    calc = calculator.Calculator()
    with pytest.raises(AssertionError):
        calc("5*6+7")


def test_calculator_8():
    """
    один из тестов  класса калькулятор
    деление унарного оператора на 0, zero division error
    """
    calc = calculator.Calculator()
    with pytest.raises(ZeroDivisionError):
        calc("-5/0")


def test_calculator_9():
    """
    один из тестов  класса калькулятор
    унарный оператор от плохого операнда, type error
    """
    calc = calculator.Calculator()
    with pytest.raises(TypeError):
        calc("-'fuck' * 5")


def test_calculator_10():
    """
    один из тестов  класса калькулятор
    умножение строки на число
    """
    calc = calculator.Calculator()
    assert calc("'duck ' * 5") == "duck duck duck duck duck "


def test_calculator_11():
    """
    один из тестов  класса калькулятор
    умножение строки на отрицательное число, лол кек
    """
    calc = calculator.Calculator()
    assert calc("'fuck ' * -5") == ""
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> исправил область видимости члена класса Calculator, откорректировал комментарии, применил flake8, добавил несколько тестов

def test_calculator_12():
    """
    один из тестов  класса калькулятор
    умножение двух унарных операторов
    """
    calc = calculator.Calculator()
    assert calc("+4 * -5") == -20

def test_calculator_13():
    """
    один из тестов  класса калькулятор
    вычитание двух унарных операторов
    """
    calc = calculator.Calculator()
    assert calc("+4 - -5") == 9

def test_calculator_14():
    """
    один из тестов  класса калькулятор
    плохой унарный оператор
    """
    calc = calculator.Calculator()
    with pytest.raises(SyntaxError):
         calc("/4 * -5")

<<<<<<< HEAD
=======
>>>>>>> добавил тесты
=======
>>>>>>> исправил область видимости члена класса Calculator, откорректировал комментарии, применил flake8, добавил несколько тестов
