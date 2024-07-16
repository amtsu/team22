class ShoppingCart:
    """
    Класс представляет корзину покупок. 
    Имеет атрибут для хранения списка товаров. 
    Имеет методы для добавления, удаления, отображения товаров в корзине и вычиckbnt стоимости всей корзины.
    """
    def __init__(self):
        self.__goods_list = {}
        self.__pricelist = {}

    def add_to_cart(self, goods_name, num = 1):
        if goods_name in self.__goods_list:
            self.__goods_list[goods_name] += num
        else:
            self.__goods_list[goods_name] = num

    def del_from_cart(self, goods_name, num = 1):
        if goods_name in self.__goods_list and self.__goods_list[goods_name] > num:
            self.__goods_list[goods_name] -= num
        elif goods_name in self.__goods_list and self.__goods_list[goods_name] <= num:
            self.__goods_list.pop(goods_name)

    def show_cart(self):
        return self.__goods_list

    def set_pricelist(self, price_dict):
        self.__pricelist = price_dict

    def count_cost(self):
        total_cost = 0
        if self.__pricelist and self.__goods_list:
            for good in self.__goods_list:
                total_cost += self.__goods_list[good] * self.__pricelist[good]
        return total_cost