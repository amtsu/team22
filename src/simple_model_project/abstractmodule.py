"""
описание абстрактного интерфейса для модуля моделирующей системы
"""
from abc import ABCMeta, abstractmethod
from typing import Dict


class AbstractModule(metaclass=ABCMeta):
    """
    Абстрактный класс, описываюший интерфейс конкретного модуля
    """

    @abstractmethod
    def __init__(self):
        """
        Конструктор
        """

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
    def step(self) -> None:
        """
        выполняет один шаг расчета модуля
        """

    @abstractmethod
    def get_state(self) -> Dict[str, str]:
        """
        метод возвращает значение переменных, описывающих состояние модуля
        на текущем шаге в виде словаря {имя переменной:значение}, например
        {"скорость, м/c" : "15", "пройденный путь, м":"12563"}
        """

    @abstractmethod
    def is_done(self) -> bool:
        """
        Сигнализирует о окончании процесса моделирования
        """
