import pytest
import sys
sys.path.append("..") 
from shoppingcart import *

def test_shoppingcart():

    p1 = ShoppingItem(12051, "Table", 1, 1500.00)
    p2 = ShoppingItem(12052, "Chair", 4, 450.00)
    p3 = ShoppingItem(12053, "Cabinet", 1, 4550.00)

    cm = ShoppingCart()

    cm.cart_add(p1)
    cm.cart_add(p2)
    cm.cart_add(p3)

    assert len(cm) == 3
    assert cm.total == 7850

    cm.cart_remove(p2.id)

    assert len(cm) == 2
    assert cm.total == 6050

