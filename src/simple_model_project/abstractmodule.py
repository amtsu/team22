"""
описание абстрактного интерфейса для модуля моделирующей системы
"""
from abc import ABCMeta, abstractmethod
from typing import Tuple


class AbstractModule(metaclass=ABCMeta):
    """
    Абстрактный класс, описываюший интерфейс конкретного модуля
    """

    def __init__(self):
        """
        Конструктор
        """
        return None

    @abstractmethod
    def name(self) -> str:
        """
        возвращает название модуля
        """

    @abstractmethod
    def prepare(self) -> None:
        """
        Выполняется перед началом цикла вызова методов step
        """

    @abstractmethod
    def step(self) -> Tuple[float, int]:
        """
        Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено
        """

    @abstractmethod
    def is_done(self) -> bool:
        """
        Сигнализирует о окончании процесса моделирования
        """
