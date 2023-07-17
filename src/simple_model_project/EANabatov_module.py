""" Реализация наследования абстрактного класса от Сергея """
from typing import Tuple

from abstractmodule import AbstractModule


class EANabatovModule(AbstractModule):
    """  """

    def __init__(self):
        """  """

    def name(self) -> str:
        """  """

    def prepare(self) -> None:
        """  """

    def step(self) -> Tuple[float, int]:
        """  """

    def is_done(self) -> bool:
        """  """

    def create_instance(self) -> object:
        """ создает экземпляр класса и возвращает его в виде объекта """
        nabatov_object = EANabatovModule()
        return self
