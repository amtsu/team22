'''4.Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров. Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиcления стоимости всей корзины.'''
    
class ShoppingCart():  
    
    def __init__(self):
        self.purchases = {}


    def add_purchase(self, name, price):    
        self.purchases[name] = price 
        return self.purchases


    def del_purchase(self, name):
        if name in self.purchases:
            del self.purchases[name]
            return self.purchases
        else: 
            print ('Товар в корзине не найден')
            return self.purchases

    
    def show_shopping_cart(self):
    '''функция отображения товаров в корзине'''
        return self.purchases


    def sum_shopping_cart(self): 
        sum_purchases = 0
        for name, price in self.purchases.items():
            sum_purchases += price
            return sum_purchases
       










