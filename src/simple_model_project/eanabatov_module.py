""" Реализация наследования абстрактного класса от Сергея """
from __future__ import annotations

import logging
from random import random, randint
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
        self.__status = True
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
        self.__status = False
        logging.info("prepare is done")

    def step(self) -> Tuple[float, int]:
        """Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено"""
        __step = None
        if self.__status is False:
            __step = (randint(1, 10) + random(), randint(1, 100))
        else:
            logging.critical("self.__status is True")
        logging.info("step is done")
        return __step

    def is_done(self) -> bool:
        """Сигнализирует о окончании процесса моделирования"""
        self.__status = True
        logging.info("is_done is done :)")
        return self.__status


def create_instance() -> EANabatovModule:
    """создает экземпляр класса и возвращает его в виде объекта"""
    return EANabatovModule()
