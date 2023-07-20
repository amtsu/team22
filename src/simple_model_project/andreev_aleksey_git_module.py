"""
Реализация абстрактного класса.
"""
import random


from abstractmodule import AbstractModule


class Сountdown(AbstractModule):
    """Отсчет циклов от заданного числа до 0"""

    def __init__(self):
        self.__count_of_cycles = 100
        self.__step = 3

    def name(self) -> str:
        module_name = self.__class__.__name__
        return module_name
    
    def prepare(self) -> None:
        """
        Выполняется перед началом цикла вызова методов step
        """
        if self.__count_of_cycles >= 0:
            return None

    def step(self) -> tuple[float, int]:
        """
        Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено
        """
        self.prepare()
        cnt = self.__count_of_cycles
        step = self.__step
        iteration = 0
        while cnt >= 0:
            if cnt - step < 0:
                break
            else:
                cnt -= step
            iteration += 1
        return (float(iteration), step)

    def is_done(self) -> bool:
        """
        Сигнализирует о окончании процесса моделирования
        """
        return bool(random.choice([0, 1]))


def createinstance() -> Сountdown:
    """Создает экземпляр класса"""
    return Сountdown()


bi = createinstance()
print(bi)
