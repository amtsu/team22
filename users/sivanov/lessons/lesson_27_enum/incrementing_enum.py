#!/usr/local/bin/python
# coding: utf-8
"""
в этом файле пример создания собственного перечислимого типа в питоне
так как встроенного механизма нет, перечислимые типы создаются как наследники класса
Enum из модуля enum
"""
import enum


@enum.unique  # не пропустит одинаковых значений
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
    # ZEROO = 0 # с декоратором @enum.unique такое не пройдёт, если уже есть ZERO
    def __add__(self, other):
        """
        операция +. 
        наверное, можно как-то по-другому это написать
        """
        if self.__class__ is other.__class__:
            # если выходит за границы, падает
            # нужно поправить            
            return Numbers(self.value + other.value)
        return NotImplemented    
    def __gt__(self, other):
        """
        gt это операция >
        нужно описать ещё ge, le и lt
        """
        if(self.__class__ is other.__class__):
            return self.value > other.value
        return NotImplemented
# ==============================================================================


def main():
    """
    пример работы с перечислимым типом
    """
    var_one = Numbers.ONE
    if var_one in Numbers:
        print(
            f"var_one = {var_one} является одним из Numbers, его значение: {var_one.value}"
        )
    var_two = Numbers.TWO
    if var_two in Numbers:
        print(
            f"var_two = {var_two} является одним из Numbers, его значение: {var_two.value}"
        )
        
    if var_two > var_one:
        print(f"var_two is greater than var_one")
    else:
        print(f"var_one is greater than var_two wtf???")
    print(f"var_one + var_two = {(var_one + var_two)}")
    print("вот это - особенность Enum, получили Numbers.THREE")
    var_six = Numbers.SIX
    #print(f"var_six + 1 is {var_six + 1}")
    print(f"Numbers(3) is {Numbers(3)}")
    #print(f"[overflow] var_six + var_six = {(var_six + var_six)}")
    print("Но - корректно побороть выход за зону доступных enum мне не удалось,")
    print("то есть Numbers(6) + numbers(7) должно закончится чем-то логичным")
# ===============================================================================
if __name__ == "__main__":
    main()
