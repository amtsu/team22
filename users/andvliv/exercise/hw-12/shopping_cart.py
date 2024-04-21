#Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров. Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиckbnt стоимости всей корзины.
class ShoppingCart:
    def __init__(self, list_of_purchases):
        self.list_of_purchases = list_of_purchases
        
    def add_purchases(self, product, price_and_quantity):
        if product in self.list_of_purchases:
            self.list_of_purchases[product] += price_and_quantity
        else:
            self.list_of_purchases.update({product: price_and_quantity})
        return self.list_of_purchases
    
    def del_purchases(self, product):
        if product in self.list_of_purchases:
            del self.list_of_purchases[product]
            return self.list_of_purchases
        else:
            return self.list_of_purchases

    def show_purchases(self):  
        return self.list_of_purchases

    def sum_of_purchases(self):
        sum = 0
        for i in self.list_of_purchases.values():
            sum += i[0] * i[1]
        return sum

#Создадим объект данного класса
cart1 = ShoppingCart({})
cart2 = ShoppingCart({'apple': [3, 4], 'meat': [1, 6]})
