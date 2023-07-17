""" Реализация наследования абстрактного класса от Сергея """
from typing import Tuple

from abstractmodule import AbstractModule


class EANabatovModule(AbstractModule):
    """ реализация абстрактного класса с использованием паттерна Singleton """

    __instance = None

    def __new__(cls):
        """ Реализация Singleton """
        if not hasattr(cls, '__instance'):
            cls.__instance = super(EANabatovModule, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        """ Инициализация атрибутов класса """

    def name(self) -> str:
        """ возвращает название класса """

    def prepare(self) -> None:
        """ Выполняется перед началом цикла вызова методов step """

    def step(self) -> Tuple[float, int]:
        """ Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено """

    def is_done(self) -> bool:
        """ Сигнализирует о окончании процесса моделирования """

    def create_instance(self) -> object:
        """ создает экземпляр класса и возвращает его в виде объекта """
        nabatov_object = EANabatovModule()
        return self
