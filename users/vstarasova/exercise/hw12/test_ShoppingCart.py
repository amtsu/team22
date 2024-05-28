import pytest
from ShoppingCart import ShoppingCart

def test_add_product():
    cart = ShoppingCart({'cola': 4, 'meat': 6})
    assert cart.add_product('apple', 87) == {'cola': 4, 'meat': 6, 'apple': 87}

def test_del_product():
    cart = ShoppingCart({'cola': 4, 'meat': 6})
    cart.add_product("apple", 87)
    cart.add_product("banana", 139)
    cart.del_product("banana")
    assert cart.show_products() == {'apple': 87, 'cola': 4, 'meat': 6}

def test_show_products1():
    cart = ShoppingCart({'cola': 4, 'meat': 6})
    assert cart.show_products() == {'cola': 4, 'meat': 6}


def test_calculate_total():
    cart = ShoppingCart({'cola': 4, 'meat': 6})
    cart.add_product("apple", 87)
    cart.add_product("banana", 139)
    assert cart.calculate_total() == 236 
