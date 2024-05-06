'''4.Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров. Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиcления стоимости всей корзины.'''
    
class ShoppingCart:  
    
    def __init__(self):
        self.purchases = {}


    def add_purchase(self, name, price):    
        self.purchases[name] = price 
        return self.purchases


    def del_purchase(self, name):
        removed_item = self.purchases.pop(name, None)
        if removed_item is None:
            return 'Товар в корзине не найден'
        return self.purchases

    
    def get_purchases(self):  
        '''функция отображения товаров в корзине'''
        return list(self.purchases.keys())

    def sum_shopping_cart(self): 
        sum_purchases = 0
        for price in self.purchases.values():
            sum_purchases += float(price)
        return sum_purchases
       










