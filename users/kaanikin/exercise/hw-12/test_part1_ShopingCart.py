import pytest
from part1_ShoppingCart import ShoppingCart, Good

cart = ShoppingCart()

tv1 = Good("LG TV", 500)
tv2 = Good("Samsung TV", 600)
table = Good("Glass table", 200)
notebook1 = Good("Lenovo laptop", 1000)
notebook2 = Good("Dell laptop", 900)
cup = Good("Ceramic mug", 10)

def test_ShoppingCart_getList():
    
    cart.add(tv1)
    cart.add(tv2)
    cart.add(table)
    cart.add(notebook1)
    cart.add(notebook2)
    cart.add(cup)
    expected = ['LG TV: 500', 'Samsung TV: 600', 'Glass table: 200', 'Lenovo laptop: 1000', 'Dell laptop: 900', 'Ceramic mug: 10']
    assert expected == cart.get_list()

def test_ShoppingCart_totalCost():
    expected = 3210 
    assert expected == cart.totalCost()

