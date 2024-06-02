import pytest

from cart import ShoppingCart

def test_add_to_cart():
    any_cart1 = ShoppingCart()
    any_cart1.add_to_cart("chocolate", 3)
    assert any_cart1.show_cart() == {"chocolate": 3}

def test_del_from_cart():
    any_cart2 = ShoppingCart()
    any_cart2.add_to_cart("milk", 1)
    any_cart2.add_to_cart("pizza", 2)
    any_cart2.add_to_cart("bread", 1)
    any_cart2.del_from_cart("bread")
    assert any_cart2.show_cart() == {"milk": 1, "pizza": 2}

def test_set_pricelist_count_cost():
    any_cart3 = ShoppingCart()
    pricelist = {"chocolate": 110, "milk": 90, "pizza": 850, "bread": 59}
    any_cart3.add_to_cart("chocolate", 3)
    any_cart3.add_to_cart("milk", 1)
    any_cart3.add_to_cart("pizza", 1)
    any_cart3.add_to_cart("bread", 1)
    any_cart3.set_pricelist(pricelist)
    assert any_cart3.count_cost() == 1329