""" Реализация наследования абстрактного класса от Сергея """
from __future__ import annotations

import logging
from random import random, randint
from typing import Dict

from abstractmodule import AbstractModule


class EANabatovModule(AbstractModule):
    """Реализация абстрактного класса с использованием паттерна Singleton"""

    def __new__(cls):
        """Реализация Singleton"""
        if not hasattr(cls, "instance"):
            cls.instance = super(EANabatovModule, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        """Инициализация атрибутов класса"""
        logging.basicConfig(
            level=logging.INFO,
            filename="eanabatov_py_log.log",
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s",
        )
        self.__status: bool = True
        self.__counter: int = 0
        self.__limit: int = 5
        self.__state: dict[str, str] = {}

    def name(self) -> str:
        """Возвращает название класса"""
        logging.info("name is done")
        return self.__class__.__name__

    def prepare(self) -> None:
        """Выполняется перед началом цикла вызова методов step"""
        self.__status = False
        logging.info("prepare is done")

    def step(self) -> None:
        """Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено"""
        self.__counter += 1
        if self.__counter <= self.__limit and self.__status is False:
            self.__state = {
                "var A": str(randint(1, 10) + random()),
                "var B": str(randint(1, 100)),
            }
            logging.info("step is done. " "counter is: %s", self.__counter)
            if self.__counter >= self.__limit:
                self.__status = True
        else:
            self.__counter -= 1
            self.__status = True
            logging.critical("self.__status is %s", self.__status)
            logging.info("step dont done. " "counter is: %s", self.__counter)
        logging.info("step is over")

    def get_state(self) -> Dict[str, str]:
        logging.info("get_state is done (counter is %s)", self.__counter)
        return self.__state

    def is_done(self) -> bool:
        """Сигнализирует об окончании процесса моделирования"""
        logging.info("is_done is done :)")
        return self.__status


def create_instance() -> EANabatovModule:
    """Создает экземпляр класса и возвращает его в виде объекта"""
    return EANabatovModule()
