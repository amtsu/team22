class Product():

    def __init__(self, name: str, price: float, quantity: int):
        
        self.name = name
        self.price = price
        self.quantity = quantity

class Warehouse(): 
    def __init__(self):
        self.inventory_item = []

    def add_product(self, product: Product):
        """метод добавления товара на склад"""
        self.inventory_item.append(product)

    def remove_product(self, product: Product):
        self.inventory_item.append(product)
    
    def check_inventory(self):
        """вывод всех товаров на складе"""
        for product in self.inventory_item:
            print(product)
    
class Order:
    
    def __init__(self):
        self.shopping_cart = []

    def add_item(self, product_name: str, quantity: int, warehouse: Warehouse):
        """Метод добавления товара в корзину"""
        for product in warehouse.inventory_item:
            if product.name == product_name and quantity <= product.quantity:
                self.shopping_cart.append((product, quantity))
                break
        else:
            print("Нет нужного товара мало или отсутствует на складе")
       
  
    
    def get_purchases(self):
        return self.shopping_cart
        
        
    def total_cost(self):
        """метод подсчета общей суммы товаров в корзине"""
        total_cost = 0
        for product, quantity in self.shopping_cart:
            item_cost = product.price * quantity
            total_cost += item_cost
        return total_cost
        
    def display_my_order(self):
        """метод выводит товары в корзине и сумму покупки"""
        total_cost = self.total_cost()  
        for product, quantity in self.shopping_cart:
            item_cost = product.price * quantity
            print(f"{product.name}: {quantity} шт - {item_cost} руб.")
        print(f"Итого: {total_cost} руб.")    
    
    


