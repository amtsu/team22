"""
Класс для участия в моделирующей системе
"""

from typing import Tuple
from abstractmodule import AbstractModule

class PlantTrees(AbstractModule):
    """
    Класс, описываюший процесс посадки деревьев
    При создвнии объекта класса необходимо передать параметры:
    1) площадь посадки (кв.м)
    2) кол-во деревьев для посадки
    Итого, одно дерево занимает 4 кв.м
    """
    # Расстояние между деревьями в ряду должно быть не менее 3м,
    # расстояние между рядами - не менее 5м

    # def __init__(self, area, trees_amount):
    def __init__(self):
        """
        Конструктор
        """
        # self.__area = area
        # self.__trees_amount = trees_amount
        self.__area = 50
        self.__trees_amount = 5
        self.__planed_trees = 0
        self.__trees_fit = 0

    def name(self) -> str:
        """
        возвращает название модуля
        """
        module_name = str(self.__module__)
        return module_name

    def prepare(self) -> None:
        """
        Выполняется перед началом цикла вызова методов step
        Определяет количество деревьев (<= self.__trees_amount),
        которое может быть посажено на заданном участке площадью <=self.__area
        """
        # Предположим, одно дерево занимает 4 кв.м.
        trees_to_area = self.__area / 4 #сколько деревьев можно посадить
        if self.__trees_amount <= trees_to_area:
            self.__trees_fit = self.__trees_amount
        elif self.__trees_amount > trees_to_area:
            self.__trees_fit = trees_to_area

    def step(self) -> Tuple[float, int]:
        """
        Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено
        возвращает значение засаженной площади,
        кол-во посаженных деревьев на данном шаге
        """
        # self.prepare()
        # step = 0
        # while self.__trees_fit:
        self.__planed_trees +=1
        self.__trees_fit -=1
        step +=1
        return (self.__planed_trees, step)

    def is_done(self) -> bool:
        """
        Сигнализирует об окончании процесса моделирования
        Критерии окончания посадки:
        1) закончились деревья
        2) закончилась площадь посадки
        ?3) закончился рабочий день =) ?
        """
        is_done = False
        if self.__trees_fit == 0:
            print("Посадили, сколько смогли")
            is_done = True
        return is_done

def createinstance() -> PlantTrees:
    """
    создает экземпляр класса PlantTrees
    """
    return PlantTrees()
