#Создайте класс ShoppingCart, который представляет корзину покупок.
#У него должен быть атрибут для хранения списка товаров.
# Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиcления стоимости всей корзины

class ShoppingCart:

    def __init__(
            self,
            cart ={}
    ):
        self.cart = cart

    def add_pur(self, name, price):
        self.cart[name] = price

    def del_pur(self, name):
        del self.cart['name']
    def show_cart(self):
        return self.cart

    def summary(self):
        sum = 0
        for key, values in self.cart.items():
            sum += values
        return sum

cart1 = ShoppingCart()
print(cart1.show_cart())
cart1.add_pur('apple', 24)
cart1.add_pur('pen', 30)
cart1.add_pur('pineapple', 240)
print(cart1.show_cart())
print(cart1.summary())