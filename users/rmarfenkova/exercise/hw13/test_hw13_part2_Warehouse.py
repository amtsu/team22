import pytest
from class_PickleHandler import PickleHandler
from hw13_part2_Warehouse import Warehouse, Order, Product

def test_load_file():
    ball = Product("ball", 1000, 35)
    sport_master = Warehouse()
    sport_master.add_product(ball)
    
    order = Order()
    order.add_item("ball", 2, sport_master)
    order.buy_item(sport_master)
    
    PickleHandler.save_to_file(sport_master, "warehouse.pkl")
    load_sport_master = PickleHandler.load_from_file("warehouse.pkl")
    
    # получение продукта из загруженного склада
    loaded_ball = load_sport_master.get_product("ball")
    assert loaded_ball == Product("ball", 1000, 33)