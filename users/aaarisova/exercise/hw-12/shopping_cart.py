'''4.Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров. Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиcления стоимости всей корзины.'''

# class Purchase(): #создаем класс продукт

#     def __init__(self, name, price):
#         self.name = str(name)
#         self.price = int(price) 

    
class ShoppingCart():  
    
    # def __init__(self, name, price):
    #     self.__purchase = []
    #     self.__name = name
    #     self.__price = price

    def __init__(self):
    '''функция иницилизации словаря для покупок''' 
        self.__purchases = {}


    def add_purchase(self, name, price):
    '''функция добавления продукта в словарь'''
        # if isinstance(purchase,Purchase): #является ли покупка экземпляром класса Purchase
        
        self.__purchases[name] = price 
        return self.__purchases

        # else:
        #     return f'ошибка добавления покупки'
        


    def remove_purchase(self, name):
    '''функция удаления продукта из словаря'''
        if name in self.__purchases:
            self.__purchases.remove(name)
            return self.__purchases
        else: 
            print ('Товар в корзине не найден')
            return self.__purchases

    
    def show_shopping_cart(self):
    '''функция отображения товаров в корзине'''
        return self.__purchases


    def sum_shopping_cart(self): 
    '''функция вычиcления стоимости всей корзины'''
        sum_purchases = 0
        for name in self.__purchases.values():
            sum_purchases += purchase.price
            return sum_purchases
       










