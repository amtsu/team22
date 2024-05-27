import datetime

from wh_warehouse import Warehouse
from wh_product import Product
# from wh_order_register import OrderRegister


class Order:
    """
    Класс заказ. Имеет номер
    Имеет информацию о заказанных продуктах, количествах, цене.
    """

    def __init__(self):
        # self.__order_num = next(OrderRegister.get_number())
        # self._order_date = OrderRegister.get_timestamp()
        # self.__order_num = order_number
        # self._order_date = order_date
        self.__order_list = []

    def add_to_order(self, warehouse_name, goods_name, num = 1):
        if isinstance(num, int) and num >= 1:
            for item in warehouse_name.remains():
                if goods_name in item.values():
                    ordered_product = warehouse_name.outcome(goods_name, num)
                    ordered_product["Количество"] = num
                    self.__order_list.append(ordered_product) #добавляем в лист заказа данные о продукте и количество
        else:
            print("Количество должно быть числом, большим нуля")
       
    def del_from_order(self, warehouse_name, goods_name, num = 1):
        for item in self.__order_list:
            if goods_name in item.values():
                if item["Количество"] > num:
                    item["Количество"] -= num
                else:
                    self.__order_list.remove(item)
                warehouse_name.income(item["Наименование"], item["Категория"], item["Цена"], num) #Возвращаем продукты на склад
                    
    def show_order_list(self):
        return self.__order_list

    def count_cost(self):
        total_cost = 0
        for item in self.__order_list:
            total_cost += item["Количество"] * item["Цена"]
        return total_cost

    # def show_order_details(self):
    #     order_details = [{"Номер заказа": self.__order_num, "Дата заказа":self._order_date},  self.__order_list]
    #     return order_details
