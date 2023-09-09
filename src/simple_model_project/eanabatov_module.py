""" Реализация наследования абстрактного класса от Сергея """
import logging
from random import random

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
        self.__status = False
        self.number = []
        logging.basicConfig(
            level=logging.DEBUG,
            filename="eanabatov_py_log.log",
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

    def step(self) -> [(int, float)]:
        """Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено"""
        if self.__status:
            with open("eanabatov_module.txt", "a") as data:
                data.write(str(random()) + "\n")
            logging.debug("Ну вроде работает")
            logging.info("step is done")
            with open("eanabatov_module.txt", "r") as data:
                self.number = [float(number.strip()) for number in data]
                return [line for line in enumerate(self.number)]
        else:
            logging.critical("self.__status is False")

    def is_done(self) -> bool:
        """Сигнализирует о окончании процесса моделирования"""
        self.__status = False
        logging.info("is_done is done :)")
        return self.__status

    def clear_txt(self):
        with open("eanabatov_module.txt", "w") as logs:
            logging.info("txt is clear")


def create_instance() -> EANabatovModule:
    """создает экземпляр класса и возвращает его в виде объекта"""
    return EANabatovModule()

a1 = EANabatovModule()
a1.prepare()
print(a1.step())

