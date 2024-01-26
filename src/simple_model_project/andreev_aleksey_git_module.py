"""
Реализация абстрактного класса.
"""
from abstractmodule import AbstractModule
import pickle

ABSOLUTE_PATH = "/home/aleksey/python_projects/team22/src/simple_model_project"

# подготовка параметров в файл
# params = {"main_number": 13, "number_to_check": 5.2}
# with open(f"{ABSOLUTE_PATH}/andreev_aleksey_git_module.pickle", "wb") as f:
#     pickle.dump(params, f)

class Countdown(AbstractModule):
    """
    Основная задача класса - посчитать сколько раз число (self.__number_to_check)
    содержится в другом числе (self.__main_number).
    Аналог целочисленного деления, но пошагово.
    """

    def __init__(self):
        self.__main_number = 0
        self.__number_to_check = 0
        self.__iteration = 0

    def name(self) -> str:
        module_name = self.__class__.__name__
        return module_name

    def prepare(self) -> None:
        """
        Выполняется перед началом цикла вызова методов step
        """
        with open(f"{ABSOLUTE_PATH}/andreev_aleksey_git_module.pickle", "rb") as f:
            param = pickle.load(f)

            self.__main_number = param["main_number"]
            self.__number_to_check = param["number_to_check"]

    def step(self) -> tuple[float, int]:
        """
        Возвращает состояние модуля на данном шаге,
        выполняется на каждом шаге, пока разрешено
        """
        if self.is_done():
            raise StopIteration
        self.__main_number -= self.__number_to_check
        self.__iteration += 1
        return (float(self.__number_to_check), self.__iteration)

    def is_done(self) -> bool:
        """
        Сигнализирует о окончании процесса моделирования
        """
        if self.__main_number - self.__number_to_check < 0:
            return True
        return False


def createinstance() -> Countdown:
    """Создает экземпляр класса"""
    return Countdown()
