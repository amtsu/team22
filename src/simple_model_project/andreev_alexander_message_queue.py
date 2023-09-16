"""
Реализация абстрактного класса.
"""
import random

from abstractmodule import AbstractModule


class MessageQueue(AbstractModule):
    """Реализация отправки очереди сообщений."""

    def __init__(self) -> None:
        """Конструктор класса."""
        self.queue: list[int] = []  # пустая очередь сообщений
        self.message_quantity: int = 10  # количество сообщений в очереди

    def name(self) -> str:
        """
        Возвращает название модуля.
        """
        return __file__.rsplit('/', maxsplit=1)[-1].split(".")[0]

    def prepare(self) -> None:
        """
        Создается очердь из ID сообщений длинной в `self.message_quantity`.
        """
        self.queue = list(range(self.message_quantity))

    def step(self) -> tuple[float, int]:
        """
        На каждом шаге из очереди 'отправляется' (удаляется) одно сообщение.
        Метод возвращает ID сообщения и время за которое оно было отправлено.
        """
        if self.is_done():
            raise StopIteration
        message = self.queue[0] # берем первое сообщение из очереди
        self.queue.pop(0) # `отправляем` сообщение
        time_spent = random.random() # Random float: 0.0 <= x < 1.0 (затраченное время отправки)
        return time_spent, message

    def is_done(self) -> bool:
        """
        Если очередь пуста, то возвращается `True`.
        """
        if not self.queue:
            return True
        return False


def createinstance() -> MessageQueue:
    """Создает экземпляр класса"""
    return MessageQueue()
