'''Расширте классы Warehouse Product Order для управления складскими запасами, загрузкой и сохранением. Придумаейте тесты.'''

import pikle


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


class Warehouse(): 

    def __init__(self):
        self.products = {} 

    def add_product(self, product: Product, new_quantity: int):
        if product.name in self.products:
            self.products[product.name].quantity += new_quantity
        else:
            self.products[product.name] = product
            self.products[product.name].quantity = new_quantity
       
        
    def remove_product(self,product_name: str, quantity: int): # удалить, потому что купили 
        try:
            if product_name in self.products:
                if self.products[product_name].quantity >= quantity:
                    self.products[product_name].quantity -= quantity
                else:
                    print('Недостаточное кол-во на складе для удаления')  #лучше выбрасывввать ошибку 
            else:
                print('Продукт не найден')
        
    # def check_product_quantity(self, product_name: str): - в методе не учит добавл и удал/покупка продуктов - реализ в инвент
    #     '''метод подсчета остатков'''
    #     if product_name in self.products:
    #         return self.products[product_name].quantity
    #     else:
    #         return "Продукт не найден."

    def get_inventory_report(self):
        report = "Отчет инвентаризации"
        for product_name, product in self.products.items():
            report += f'Продукт: {product_name}, Кол-во: {product.quantity}'
            report += f'Нужно учесть кол-во добаленных и удаленных продуктов!'  #доработать
        return report
               
    def save_warehouse(self,file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_warehouse(file_name):
        with open(file_name, 'rb') as f:
            return pickle.load(f)


class Order(): 

    def __init__(self):
        self.purchases = {}

    def add_purchase(self, product: Product, quantity: int):
        if product.name in self.purchases:
            self.purchases[product.name] += quantity
        else:
            #self.purchases[product.name] = product
            self.purchases[product.name] = quantity
       
    def get_purchases(self):
        return self.purchases

    def sum_shopping_cart(self, warehouse: Warehouse):
        total_price = 0
        for product_name, quantity in self.purchases.items():
            if product_name in warehouse.products:
                total_price += warehouse.products[product_name].price * quantity
            else:
                return f"Продукт {product_name} не найден на складе"
        return total_price




