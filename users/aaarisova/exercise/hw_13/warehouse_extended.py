'''Расширте классы Warehouse Product Order для управления складскими запасами, загрузкой и сохранением. Придумаейте тесты.'''

import pickle 

class Product():

    def __init__(
        self, 
        name: str, 
        price: float, 
        quantity: int
    ):
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product{self.name}, Price{self.price}, Quantity{self.quantity}'


class Warehouse(): 

    def __init__(self):
        self.products = {} 

    def add_product(self, product: Product, new_quantity: int):
        '''метод добавления продукта на склад.'''
        if product.name in self.products:
            self.products[product.name].quantity += new_quantity
        else:
            self.products[product.name] = product
            self.products[product.name].quantity = new_quantity
       
        
    def remove_product(self,product_name: str, quantity: int): 
        '''метод удаления продукта со склада'''
        if product_name in self.products:
            if self.products[product_name].quantity >= quantity:
                self.products[product_name].quantity -= quantity
            else:
                raise ValueError('Недостаточное кол-во на складе для удаления')
        else:
            raise ValueError('Продукт не найден на складе')
        
    def check_product_quantity(self, product_name: str):
        '''метод подсчета остатков на складе'''
        if product_name in self.products:
            return self.products[product_name].quantity
        else:
            raise ValueError("Продукт не найден на складе.")

    def save_to_file(self,file_name):
        '''методы сохранения и загрузки обекта из памяти в файл'''
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(file_name):
        '''метод загрузки объекта из файла в память.'''
        with open(file_name, 'rb') as f:
            return pickle.load(f)


class Order(): 

    def __init__(self):
        self.purchases = {}

    def add_purchase(self, name: str, price: float, quantity: int):
        '''Метод добавления покупок в корзину'''
        if name in self.purchases:
            self.purchases[name] += quantity
        else:
            self.purchases[name] = quantity
       
    def get_purchases(self):
        '''метод получения списка покупок'''
        return self.purchases

    def sum_shopping_cart(self, warehouse: Warehouse):
        '''метод подсчета суммы покупок'''
        total_price = 0
        for product_name, quantity in self.purchases.items():
            if product_name in warehouse.products:
                total_price += warehouse.products[product_name].price * quantity
            else:
                return f"Продукт {product_name} не найден на складе"
        return total_price
               




