import pytest
from shopping_cart import ShoppingCart


def test_initialization():
    shopping_cart = ShoppingCart()
    assert shopping_cart.purchases == {}


@pytest.mark.parametrize('name, price, expected_result', [
    ('soap', '2', {'soap': '2'}),
    ('juice', 0, {'juice': 0}),
    ('apple', 7.2, {'apple': 7.2}),
     ('fish',-4, {'fish':-4}),
])

def test_add_purchase(name, price, expected_result):  
    '''тест добавления товара в корзину'''
    shopping_cart = ShoppingCart()
    shopping_cart.add_purchase(name, price) 
    assert shopping_cart.purchases == expected_result


@pytest.fixture
def my_shopping_cart():
    my_cart = ShoppingCart()
    my_cart.add_purchase('soap', '2')
    my_cart.add_purchase('juice', 0)
    my_cart.add_purchase('apple', 7.2)
    my_cart.add_purchase('fish', -4)
    my_cart.add_purchase('milk', 3)
    return my_cart


def test_del_purchase(my_shopping_cart):
    '''тест удаления из корзины товара'''
    my_shopping_cart.del_purchase('juice')
    assert my_shopping_cart.purchases == {'soap': '2', 'apple': 7.2, 'fish':-4, 'milk': 3} 


def test_del_purchase(my_shopping_cart):
    '''тест удаления из корзины несуществующего товара'''
    result = my_shopping_cart.del_purchase('fork')
    assert result == 'Товар в корзине не найден'


def test_get_purchases(my_shopping_cart):  
    '''тест функции отображения товаров в корзине'''
    result = my_shopping_cart.get_purchases()
    assert result == ['soap', 'juice', 'apple', 'fish', 'milk'] 


def test_sum_shopping_cart(my_shopping_cart): 
    '''тест функции вычисления стоимости всей корзины '''
    result = my_shopping_cart.sum_shopping_cart()   
    assert result == sum([2+7.2-4+3])
       




