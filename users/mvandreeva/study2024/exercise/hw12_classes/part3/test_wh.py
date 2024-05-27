import pytest

from wh_product import Product
from wh_warehouse import Warehouse
from wh_order import Order
# from wh_order_register import OrderRegister

##############################################
# Product
##############################################
def test_get_product():
    prod = Product("MilkMilk", "Молоко", 89)
    assert prod.get_product() == {"Наименование": "MilkMilk", "Категория": "Молоко", "Цена": 89}

def test_get_price():
    prod = Product("MilkMilk", "Молоко", 89)
    assert prod.get_price() == 89

def test_get_category():
    prod = Product("MilkMilk", "Молоко", 89)
    assert prod.get_category() == "Молоко"

def test_get_name():
    prod = Product("MilkMilk", "Молоко", 89)
    assert prod.get_name() == "MilkMilk"

def test_set_price():
    prod = Product("MilkMilk", "Молоко", 89)
    prod.set_price(100)
    assert prod.get_price() == 100

def test_set_category():
    prod = Product("MilkMilk", "Молоко", 89)
    prod.set_category("Малако")
    assert prod.get_category() == "Малако"

def test_set_name():
    prod = Product("MilkMilk", "Молоко", 89)
    prod.set_name("MilkyMilk")
    assert prod.get_name() == "MilkyMilk"

##############################################
# Warehouse
##############################################
def test_income():
    new_wh = Warehouse()
    new_wh.income("MilkMilk", "Молоко", 89, 100)
    assert new_wh.remains() == [{"Наименование": "MilkMilk", "Категория": "Молоко", "Цена": 89, "Количество": 100}]

def test_outcome():
    new_wh = Warehouse()
    new_wh.income("MilkMilk", "Молоко", 89, 100)
    new_wh.outcome("MilkMilk", 12)
    assert new_wh.remains() == [{"Наименование": "MilkMilk", "Категория": "Молоко", "Цена": 89, "Количество": 88}]

##############################################
# Order
##############################################
# @pytest.fixture()
# def register_order():
#     order_register = OrderRegister()
#     order_number = next(order_register.get_number())
    # order_date = OrderRegister.get_timestamp()
    # return order_number, order_date

def test_add_to_order():
    new_wh = Warehouse()
    new_wh.income("MilkMilk", "Молоко", 89, 100)
    new_wh.income("Dove", "Шоколад", 180, 200)
    # new_order = Order(register_order[0], register_order[1])
    new_order = Order()
    new_order.add_to_order(new_wh,"Dove", 3)
    assert new_order.show_order_list() == [{"Наименование": "Dove", "Категория": "Шоколад", "Цена": 180, "Количество":3}]
    assert new_order.count_cost() == 540

# def test_show_order_details():
#     new_wh = Warehouse()
#     new_wh.income("MilkMilk", "Молоко", 89, 100)
#     new_wh.income("Dove", "Шоколад", 180, 200)
#     new_order = Order()
#     new_order.add_to_order(new_wh,"Dove", 3)
#     assert new_order.show_order_details() == [{"Номер заказа": 1, "Дата заказа": 0}, ]

##############################################
# OrderRegister
##############################################
# def test_get_number():
#     register = OrderRegister()
#     assert 
