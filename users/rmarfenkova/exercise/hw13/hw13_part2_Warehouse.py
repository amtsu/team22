class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
        
    
class Warehouse:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        """метод добавления товара на склад"""
        self.products[product.name] = product

    def __str__(self):
        """вывод всех товаров на складе"""
        return "\n".join(str(product) for product in self.products.values())

    def get_product(self, product_name):
        """Метод для получения продукта по имени"""
        return self.products.get(product_name)

    
    def remove_product(self, order: Order):
        """Метод списания товара со склада по заказу"""
        for product_name, quantity in order.items:
            product = self.get_product(product_name)
            if product and product.quantity >= quantity:
                product.quantity -= quantity
            else:
                return False
        return True
        
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

    
        