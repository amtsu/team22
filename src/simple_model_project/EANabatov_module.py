""" Реализация наследования абстрактного класса от Сергея """
from typing import Tuple
from abstractmodule import AbstractModule


class EANabatovModule(AbstractModule):
    """реализация абстрактного класса с использованием паттерна Singleton"""

    def __new__(cls):
        """Реализация Singleton"""
        if not hasattr(cls, "instance"):
            cls.instance = super(EANabatovModule, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        """Инициализация атрибутов класса"""
        instance = None
        self.__status = False

    def name(self) -> str:
        """возвращает название класса"""
        return "EANabatovModule"

    def prepare(self) -> None:
        """Выполняется перед началом цикла вызова методов step"""
        return None

    def step(self) -> Tuple[float, int]:
        """Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено"""
        return 0.0, self.__status

    def is_done(self) -> bool:
        """Сигнализирует о окончании процесса моделирования"""
        self.__status = False
        return self.__status


def create_instance():
    """создает экземпляр класса и возвращает его в виде объекта"""
    nabatov_object = EANabatovModule()
    return nabatov_object
