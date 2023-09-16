"""
это генератор значений факториала числа от 0 до count-1
"""


class Factorial:
    """
    итератор, возвращающий факториал числа
    рано или поздно закончится место в типе данных,
    70! например это где-то 10^100. что делать в этом случае -
    я решил ничего. переполнится так переполнится. попробовал до 300, вывозит,
    очень интересно но уже малоинформативно
    """

    def __init__(self, count):
        self.__prev = 1  # начальное значение, 0!
        self.__elem = (self.__prev * (i) for i in range(count))

    def __iter__(self):
        return self

    def __next__(self):
        currentvalue = next(self.__elem)
        self.__prev = currentvalue if currentvalue > 0 else 1
        return self.__prev


# -------------------------------------------------------------------------------
def main():
    """
    демонстрация работы факториала
    """
    count = 20
    a_factorial_iterator = Factorial(count)
    numberer = (i for i in range(count))
    print("вычисление значения факториала")
    for value in a_factorial_iterator:
        print(f"{next(numberer)}! = {value}")


# ===============================================================================
if __name__ == "__main__":
    main()
