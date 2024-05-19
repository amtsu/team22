
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
        
    def __eq__(self, other):
        if isinstance(other, Product):
            return (self.name, self.price, self.quantity) == (other.name, other.price, other.quantity)
            
        return False
        
class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        """метод добавления товара на склад"""
        self.products.append(product)

    def __str__(self):
        """вывод всех товаров на складе"""
        for product in self.products:
            return "\n".join(str(product) for product in self.products)

    def get_product(self, product_name):
        """Метод для получения продукта по имени"""
        for product in self.products:
            if product.name == product_name:
                return product
        return None

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product_name: str, quantity: int, warehouse: Warehouse):
        """Метод добавления товара в корзину с учетом товаров на складе"""
        product = warehouse.get_product(product_name)
        if product and product.quantity >= quantity:
            self.items.append((product_name, quantity))
            return True
        return False

    def buy_item(self, warehouse: Warehouse):
        """Метод покупки товара и списания его со склада со склада"""
        for product_name, quantity in self.items:
            product = warehouse.get_product(product_name)
            if product:
                product.quantity -= quantity
            return True
        return False
        