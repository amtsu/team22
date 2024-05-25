# from time import time
import datetime

class OrderRegister:
    """
    Класс регистрирует созданные заказы
    """
    def __init__(self):
        self.__register_data = {}

    def get_number(self):
        num = 0
        while True:
            yield num
            # self.__register_data["Номер заказа"] = num
            num += 1
        # return self.__register_data["Номер заказа"]

    def get_timestamp():
        # self.__register_data["Номер заказа"] = time.localtime()
        # return  self.__register_data["Номер заказа"]
        order_time = datetime.now()
        # timestamp_data = time.strftime("%H:%M", t)
        return order_time