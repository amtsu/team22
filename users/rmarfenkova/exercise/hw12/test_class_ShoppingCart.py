import pytest
from class_ShoppingCart import ShoppingCart

@pytest.fixture
def shopping_cart():
    return ShoppingCart()
    
@pytest.mark.parametrize("items, expected", [
    ({"milk": 90, "aggs": 120, "bread": 50}, ["milk", "aggs", "bread"]),
    ({"book": 1000, "pen": 30}, ["book", "pen"]),
    ({}, [])
])
def test_str_add(shopping_cart, items, expected):
    """
    проверяем как метод выводит товары, находящиеся в корзине
    """
    for item, price in items.items():
        shopping_cart.add(item, price)
    assert str(shopping_cart) == f"Всего товаров в корзине:{expected}"

@pytest.mark.parametrize("items, expected", [
    ({"milk": 90, "aggs": 120, "bread": 50}, 260),
    ({"book": 1000, "pen": 30}, 1030),
    ({}, 0)
])
def test_get_sum_items(shopping_cart, items, expected):
    for item, price in items.items():
        shopping_cart.add(item, price)
    assert shopping_cart.get_sum_items() == f"Общая стоимость покупок:{expected}"
    
def test_remove_method(shopping_cart):
    shopping_cart.add("apple", 10)
    shopping_cart.add("banana", 20)
    shopping_cart.add("orange", 15)
    shopping_cart.remove("apple")
    assert str(shopping_cart) == "Всего товаров в корзине:['banana', 'orange']"    
                         
                         
    
                         