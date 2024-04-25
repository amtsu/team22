from shopping_cart import Product, ShoppingCart
from file_methods import FileMethods


class PaymentStatusError(Exception):
    def __str__(self):
        return 'Заказ не оплачен!'


class StockAvailabilityError(Exception):
    def __str__(self):
        return 'Нет достаточного количества на складе для выполнения заказа'


class Order(FileMethods):
    def __init__(self, list_of_products: ShoppingCart):
        super().__init__()
        self.__list_of_products = list_of_products.list_of_products
        self.__payment_status = False
        self.__issue_status = False
        self.file_name = 'order.pickle'

    def __str__(self):
        return ' '.join(product[0].__str__() + f': {product[1]} шт.' for product in self.__list_of_products.values())

    @property
    def list_of_products(self):
        return self.__list_of_products

    @property
    def payment_status(self):
        return self.__payment_status

    @payment_status.setter
    def payment_status(self, status: bool = False):
        self.__payment_status = status

    @property
    def issue_status(self):
        return self.__issue_status

    @issue_status.setter
    def issue_status(self, status: bool = False):
        self.__issue_status = status


class Warehouse(FileMethods):
    def __init__(self):
        super().__init__()
        self.__stocks = {}
        self.file_name = 'warehouse.pickle'

    def __str__(self):
        return ' '.join(product[0].__str__() + f': {product[1]} шт.' for product in self.__stocks.values())

    def __len__(self):
        return sum(product[1] for product in self.__stocks.values())

    def add_products(self, product: Product, quantity: int = 1):
        if product.product_id in self.__stocks:
            self.__stocks[product.product_id][1] += quantity
        else:
            self.__stocks[product.product_id] = [product, quantity]

    def write_off_products(self, list_of_products: Order):
        if not list_of_products.payment_status:
            raise PaymentStatusError

        for p_id, product in list_of_products.list_of_products.items():
            quantity = product[1]
            if p_id not in self.__stocks or quantity > self.__stocks[p_id][1]:
                raise StockAvailabilityError
            self.__stocks[p_id][1] -= product[1]

        list_of_products.issue_status = True


if __name__ == "__main__":
    product_1 = Product('Тетрадь', 12)
    product_2 = Product('Карандаш', 4)
    product_3 = Product('Ластик', 6)
    shopping_cart = ShoppingCart()
    shopping_cart.add_product(product_1, 2)
    shopping_cart.add_product(product_2)
    shopping_cart.add_product(product_3)
    order = Order(shopping_cart)
    order.dump_obj()
    order.payment_status = True
    order.dump_obj()
    new_order: Order = Order.load_obj('order.pickle')
    assert order.payment_status == new_order.payment_status
    warehouse = Warehouse()
    warehouse.add_products(product_1, 10)
    warehouse.add_products(product_2, 10)
    warehouse.add_products(product_3)
    warehouse.dump_obj()
    new_warehouse: Warehouse = Warehouse.load_obj('warehouse.pickle')
    warehouse.write_off_products(order)
    new_warehouse.write_off_products(new_order)
    new_warehouse.dump_obj()
    new_warehouse_2: Warehouse = Warehouse.load_obj('warehouse.pickle')
    assert len(warehouse) == len(new_warehouse_2)