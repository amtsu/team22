import pytest
from warehouse_extended import Product
from warehouse_extended import Warehouse
from warehouse_extended import Order


def test_warehouse():
    product1 = Product('яблоко', 35.0, 32)
    product2 = Product('мыло', 20, 100)
    product3 = Product('книга', 40, 160)
    
    warehouse = Warehouse()
    
    warehouse.add_product(product1, 10)
    warehouse.add_product(product2, 20)
    warehouse.add_product(product3, 60)

    file = 'warehouse.pkl'
    warehouse.save_to_file('warehouse.pkl')
    load = warehouse.load_from_file('warehouse.pkl')
   
    expected_products = {
        'яблоко': Product('яблоко', 35.0, 10),
        'мыло': Product('мыло', 20, 20),
        'книга': Product('книга', 40, 60)
    }
    
    assert len(load.products) == len(expected_products)
    for name, product in load.products.items():
        assert product.name == expected_products[name].name
        assert product.price == expected_products[name].price
        assert product.quantity == expected_products[name].quantity





