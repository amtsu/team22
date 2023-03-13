#!/usr/local/bin/python
# coding: utf-8
"""
в этом файле пример создания собственного перечислимого типа в питоне
так как встроенного механизма нет, перечислимые типы создаются как наследники класса
Enum из модуля enum
"""
import enum

@enum.unique # не пропустит одинаковых значений
class Numbers(enum.Enum):
    """
    просто именованные константы, которые можно складывать и сравнивать
    """
    ZERO = 0
    ONE = enum.auto()
    TWO = enum.auto()
    THREE = enum.auto()
    FOUR = enum.auto()
    FIVE = enum.auto()
    SIX = enum.auto()
    SEVEN = enum.auto()
    EIGHT = enum.auto()
    NINE = enum.auto()
    TEN = enum.auto()
    #ZEROO = 0 # с декоратором @enum.unique такое не пройдёт, если уже есть ZERO


# ==============================================================================


def main():
    """
    пример работы с перечислимым типом
    """
    var_one = Numbers.ONE
    if var_one in Numbers:
        print(f"var_one = {var_one} является одним из Numbers, его значение: {var_one.value}")
    var_two = Numbers.TWO
    if var_two in Numbers:
        print(f"var_two = {var_two} является одним из Numbers, его значение: {var_two.value}")


# ===============================================================================
if __name__ == "__main__":
    main()
