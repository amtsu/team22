import pytest
from warehouse import Product
from warehouse import Warehouse
from warehouse import Order


@pytest.fixture
def products():
    product1 = Product('яблоко', 35.0, 32)
    product2 = Product('мыло', 20, 100)
    product3 = Product('книга', 40, 160)
    return product1, product2, product3


def test_warehouse_add(products):
    warehouse = Warehouse()
    product1, product2, product3 = products
    
    warehouse.add_product(product1, 15)
    warehouse.add_product(product2, 50)
    warehouse.add_product(product3, 100)
    
    assert warehouse.check_product_quantity('яблоко') == 15
    assert warehouse.check_product_quantity('мыло') == 50
    assert warehouse.check_product_quantity('книга') == 100

    warehouse.remove_product('книга', 10)
    assert warehouse.check_product_quantity('книга') == 90

   
    order = Order()
    order.add_purchase('яблоко', 35, 5)
    order.add_purchase('книга', 40, 10)

    assert order.get_purchases() == {'яблоко': 5, 'книга': 10}
    assert order.sum_shopping_cart(warehouse) == 35.0 * 5 + 40 * 10
         

