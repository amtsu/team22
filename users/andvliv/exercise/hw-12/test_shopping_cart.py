import pytest
from shopping_cart import ShoppingCart

def test_add_purchases():
    cart1 = ShoppingCart({})
    cart2 = ShoppingCart({'apple': [3, 4], 'meat': [1, 6]})
    assert cart1.add_purchases('juice', [1, 5]) == {'juice': [1, 5]}
    assert cart2.add_purchases('juice', [1, 5]) == {'apple': [3, 4], 'meat': [1, 6], 'juice': [1, 5]}

def test_del_purchases():
    cart2 = ShoppingCart({'apple': [3, 4], 'meat': [1, 6]})
    assert cart2.del_purchases('juice') == {'apple': [3, 4], 'meat': [1, 6]}
    assert cart2.del_purchases('apple') == {'meat': [1, 6]}

def test_show_purchases():
    cart1 = ShoppingCart({})
    cart2 = ShoppingCart({'apple': [3, 4], 'meat': [1, 6]})
    assert cart1.show_purchases() == {}
    assert cart2.show_purchases() == {'apple': [3, 4], 'meat': [1, 6]}

def test_sum_of_purchases():
    cart1 = ShoppingCart({})
    cart2 = ShoppingCart({'apple': [3, 4], 'meat': [1, 6]})
    assert cart1.sum_of_purchases() == 0
    assert cart2.sum_of_purchases() == 18
    

