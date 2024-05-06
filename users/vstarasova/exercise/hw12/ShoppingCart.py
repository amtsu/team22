'''
Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров. Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиcления стоимости всей корзины.
'''
class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def add_product(self, product, price):
        self.products[product] = price
        return self.products

    def del_product(self, product):
        if product in self.products:
            del self.products[product]
        else:
            print(f"{product} не найден в корзине.")

    def show_products(self):
        return self.products
 #           for product, price in self.products.items():
 #               print(f"{product}: {price}")
 #       else:
 #           print("Корзина пуста.")
        

    def calculate_total(self):
        total = sum(self.products.values())
        return total

# Пример использования класса
cart = ShoppingCart({'cola': 4, 'meat': 6})
cart.add_product("apple", 87)
cart.add_product("banana", 139)
cart.add_product("orange", 104)

cart.show_products()
print("Общая стоимость корзины:", cart.calculate_total())

cart.del_product("banana")

cart.show_products()
print("Общая стоимость корзины:", cart.calculate_total())