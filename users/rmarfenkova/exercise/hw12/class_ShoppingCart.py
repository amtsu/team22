class ShoppingCart():
    """
    Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров.
    Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиckbnt стоимости всей корзины.
    """
    
    def __init__(self):   
        self.items = {}   
    
    def add(self, item, price):
        """ метод добавления товаров в корзину """
        self.items[item] = price
        
        
    def remove(self, rm_item):
        """ метод удаления товаров из корзины """
        if rm_item in self.items: 
             del self.items[rm_item]
        else:
            print("Такого товара нет в корзине")
            
            
    def __str__(self):
        """ выводит все товары в корзине """
        items_list = list(self.items.keys())
        return f"Всего товаров в корзине:{items_list}"
        
        
    def get_sum_items(self):
        """ считает общую сумму товаров в корзине """
        total = 0
        for value in self.items.values():
            total += value 
        return  f"Общая стоимость покупок:{total}"