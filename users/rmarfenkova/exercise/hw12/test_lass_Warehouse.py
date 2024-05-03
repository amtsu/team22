from class_Warehouse import Order, Product, Warehouse
from bank_account import BankAccount


def test_str_pruduct():
    ball = Product("ball", 1000, 35)
    expected = "ball - 1000 руб. - 35 шт."
    assert str(ball) == expected
    
def test_add_product():
    warehouse = Warehouse()
    product = Product("Тетрадь", 50, 100)
    warehouse.add_product(product)
    assert product in warehouse.products    

def test_buy_item_():
    warehouse = Warehouse()
    product = Product("Тетрадь", 50, 100)
    warehouse.add_product(product)
    bank_account = BankAccount(12345, "Regina", 500)
    order = Order()
    order.add_item("Тетрадь", 2, warehouse)
    order.buy_item(warehouse, bank_account)
    assert warehouse.products[0].quantity == 98
    assert bank_account.balance == 400

def test_calculate_total_cost():
    warehouse = Warehouse()
    product1 = Product("Тетрадь", 50, 2)
    product2 = Product("Ручка", 20, 5)
    warehouse.add_product(product1)
    warehouse.add_product(product2)
    order = Order()
    order.add_item("Тетрадь", 2, warehouse)
    order.add_item("Ручка", 3, warehouse)
    assert order.calculate_total_cost() == (50 * 2) + (20 * 3)