"""
Реализация абстрактного класса.
"""
import random

from abstractmodule import AbstractModule


class Modeling(AbstractModule):
    """Конструктор класса"""
    def __init__(self):
        pass

    def name(self) -> str:
        """
        Возвращает название модуля
        """
        return __file__.rsplit('/', maxsplit=1)[-1].split(".")[0]

    def prepare(self) -> None:
        """
        Выполняется перед началом цикла вызова методов step
        """
        return print("Preparing")

    def step(self) -> tuple[float, int]:
        """
        Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено
        """
        self.prepare()
        if self.is_done():
            return random.random(), random.randint(0, 10)
        return (0.0, 0)

    def is_done(self) -> bool:
        """
        Сигнализирует о окончании процесса моделирования
        """
        return bool(random.getrandbits(1))


def createinstance() -> Modeling:
    """Создает экземпляр класса"""
    return Modeling()
