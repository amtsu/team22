from bank_account import BankAccount

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price} руб. - {self.quantity} шт."
        
class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        """метод добавления товара на склад"""
        self.products.append(product)

    def check_inventory(self):
        """вывод всех товаров на складе"""
        for product in self.products:
            print(product)
            
class Order:
    def __init__(self):
        self.cart_of_orders = []

    def add_item(self, item: str, quantity: int, warehouse: Warehouse):
        """Метод добавления товара в корзину с учетом товаров на складе"""
        for product in warehouse.products:
            if product.name == item and quantity <= product.quantity:
                self.cart_of_orders.append((product, quantity))
                break
        else:
            print(f"Товар '{item}' не был добавлен в корзину из-за нехватки на складе или его отсутствия.")
       
       
    # def buy_item(self, warehouse: Warehouse, bank_account: BankAccount):
    #     """Метод покупки товара со склада с учетом средств на счете и списания товара со склада"""
    #     total_cost = self.calculate_total_cost()
    #     if bank_account.balance >= total_cost:
    #         for item, quantity in self.cart_of_orders:
    #             for product in warehouse.products:
    #                 if item.name == product.name:
    #                     product.quantity -= quantity
                        
    #         bank_account.withdraw(total_cost)
    #         print("Покупка совершена успешно.")
    #     else:
    #         print("Недостаточно средств на карте.")    

    def buy_item(self, warehouse: Warehouse, bank_account: BankAccount):
        """Метод покупки товара со склада с учетом средств на счете и списания товара со склада"""
        if bank_account.balance >= self.calculate_total_cost():
            for item, quantity in self.cart_of_orders:
                for product in warehouse.products:
                    if item.name == product.name:
                        if quantity <= product.quantity:
                            product.quantity -= quantity
                            bank_account.withdraw(item.price * quantity)
                            print(f"Покупка {item.name} совершена успешно.")
                        else: 
                            print(f"Вы превысили количество имеющегося товара '{item.name}' на складе.")
                        break
                else:
                    print(f"Товар '{item.name}' отсутствует на складе.")
        else:
            print("Недостаточно средств на счете.")
    
    def calculate_total_cost(self):
        """метод подсчета общей суммы товаров в корзине"""
        total_cost = 0
        for product, quantity in self.cart_of_orders:
            item_cost = product.price * quantity
            total_cost += item_cost
        return total_cost
        
    def display_my_order(self):
        """метод выводит товары в корзине и сумму покупки"""
        total_cost = self.calculate_total_cost()  
        for product, quantity in self.cart_of_orders:
            item_cost = product.price * quantity
            print(f"{product.name}: {quantity} шт - {item_cost} руб.")
        print(f"Общая стоимость покупки: {total_cost} руб.")

