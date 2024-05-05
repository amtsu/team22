from func_ShoppingCart import ShoppingCart

#Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров. Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиckbnt стоимости всей корзины.

#тест, который проверяет добавление товара     
def test_add_basket():
    cart = ShoppingCart({})
    assert cart.add_basket('ананас', 400) == {'ананас':400} 
#тест, который проверяет удаление товара 
def test_del_basket():
    cart = ShoppingCart({'апельсин': 200, 'яблоко': 100})
    assert cart.del_basket('апельсин') == {'яблоко': 100}
#тест, отобращающий товары в корзине
def test_basket():
    cart = ShoppingCart({'апельсин': 200, 'яблоко': 100})
    assert cart.basket == {'апельсин': 200, 'яблоко': 100}
#тест, который проверяет стоимость всей корзины
def test_prises_basket():
    cart = ShoppingCart({'апельсин': 200, 'яблоко': 100})
    assert cart.prises_basket() == 300    
