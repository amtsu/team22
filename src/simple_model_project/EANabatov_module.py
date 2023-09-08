""" Реализация наследования абстрактного класса от Сергея """
from abstractmodule import AbstractModule
import logging


class EANabatovModule(AbstractModule):
    """реализация абстрактного класса с использованием паттерна Singleton"""
    def __new__(cls):
        """Реализация Singleton"""
        if not hasattr(cls, "instance"):
            cls.instance = super(EANabatovModule, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        """Инициализация атрибутов класса"""
        self.__status = False
        self.number = 0
        logging.basicConfig(
            level=logging.DEBUG,
            filename="EANabatov_py_log.log",
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s",
        )

    def name(self) -> str:
        """возвращает название класса"""
        logging.info("name is done")
        return self.__class__.__name__

    def prepare(self):
        """Выполняется перед началом цикла вызова методов step"""
        self.__status = True
        logging.info("prepare is done")

    def step(self):
        """Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено"""
        if self.__status:
            self.number += 1
            logging.debug("Ну вроде работает")
        logging.info("step is done")

    def is_done(self) -> bool:
        """Сигнализирует о окончании процесса моделирования"""
        self.__status = False
        logging.info("is_done is done :)")
        return self.__status

    def the_end(self) -> int:
        """Выводит значение переменной number"""
        logging.info("the_end is done")
        return self.number


def create_instance() -> EANabatovModule:
    """создает экземпляр класса и возвращает его в виде объекта"""
    return EANabatovModule()
