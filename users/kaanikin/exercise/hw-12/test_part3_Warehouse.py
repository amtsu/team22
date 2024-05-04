import pytest
from part3_Warehouse import Product, Warehouse, Order

def test_add_product_warehouse():
    axe = Product("Топор", 3000, 25)
    saw = Product("Пила", 2000, 20)
    
def test_add_product():
    warehouse = Warehouse()
    product = Product("Отвертка", 550, 100)
    warehouse.add_product(product)
    assert product in warehouse.inventory_item   

def test_total_cost():
    warehouse = Warehouse()
    paint = Product("Краска", 450, 3)
    brush = Product("Кисть", 320, 6)
    warehouse.add_product(paint)
    warehouse.add_product(brush)
    order = Order()
    order.add_item("Краска", 2, warehouse)
    order.add_item("Кисть", 3, warehouse)
    assert order.total_cost() == (450 * 2) + (320 * 3)