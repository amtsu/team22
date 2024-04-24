class Product:
    __product_counter = 0

    def __new__(cls, *args, **kwargs):
        cls.__product_counter += 1
        return super().__new__(cls)

    def __init__(self, name: str, price: int | float):
        self.__product_id = self.__product_counter
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, цена - {self.price} руб.'

    @property
    def product_id(self):
        return self.__product_id


class ShoppingCart:
    def __init__(self):
        self.list_of_products = {}

    def __str__(self):
        return ' '.join(product[0].__str__() + f': {product[1]} шт.' for product in self.list_of_products.values())

    def __len__(self):
        return len(self.list_of_products)

    def add_product(self, product: Product, quantity: int = 1):
        if product.product_id in self.list_of_products:
            self.list_of_products[product.product_id][1] += quantity
        else:
            self.list_of_products[product.product_id] = [product, quantity]

    def del_product(self, product: Product):
        if product.product_id in self.list_of_products:
            del self.list_of_products[product.product_id]

    def calc_cost(self):
        return sum(product[0].price * product[1] for product in self.list_of_products.values())


if __name__ == "__main__":
    product_1 = Product('Тетрадь', 12)
    product_2 = Product('Карандаш', 4)
    product_3 = Product('Ластик', 6)
    shopping_cart = ShoppingCart()
    shopping_cart.add_product(product_1, 2)
    shopping_cart.add_product(product_2)
    shopping_cart.add_product(product_3)
    assert len(shopping_cart) == 3
    assert shopping_cart.calc_cost() == 34
    shopping_cart.del_product(product_1)
    assert len(shopping_cart) == 2
    assert shopping_cart.calc_cost() == 10
