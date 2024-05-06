class ShoppingCart:
    """
    Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров. Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиcлите стоимости всей корзины.
    """
    def __init__(self):
        self.good_list = []

    def add(self, gd): 
        self.good_list.append(gd) 
 
    def remove(self, indx): 
        self.good_list.pop(indx) 
 
    def get_list(self): 
        lst = [] 
        for item in self.good_list: 
            lst.append(f"{item.name}: {item.price}") 
        return lst 

    def totalCost(self):
        total = 0
        for item in self.good_list: 
            total += item.price
        return total    


class Good: 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price 

 
class Cart: 
    def __init__(self): 
        self.goods = [] 
 
    def add(self, gd): 
        self.goods.append(gd) 
 
    def remove(self, indx): 
        self.goods.pop(indx) 
 
    def get_list(self): 
        lst = [] 
        for item in self.goods: 
            lst.append(f"{item.name}: {item.price}") 
        return lst 
 
