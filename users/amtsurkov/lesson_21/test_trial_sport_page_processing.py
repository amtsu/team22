import pytest
from TrialSportPageProcessing import OnePage, OnePageProcessor

#def test_price_goods_1179889():
#    import sys
#    print(sys.version_info.major)
#    print(sys.version_info.minor)
#    print(sys.version_info)
#    
#    p = OnePage("https://trial-sport.ru/goods/51530/1179889.html")
#    assert p.get_price() == 2402
#    
#def test_title_goods_1179889():
#    p = OnePage("https://trial-sport.ru/goods/51530/1179889.html")
#    assert p.get_title() == 'Блин вратаря DR X6 GOALIE BLOKER'

def test_web_page_title_goods_1179889():
    p = OnePage("https://trial-sport.ru/goods/51530/1179889.html")
    expected = [
        {
            "title": 'Блин вратаря DR X6 GOALIE BLOKER',
            'price': 6864,
            'price_sale': 2402,
            'brand': 'Главная / Каталог / Коньки ледовые / Снаряжение / Блины вратаря / DR',
            'brand_url': '/gds.php?s=51530&c1=1070639&brand=189643&c2=1084245'
        },
    ]
    assert p.list_dict() == expected


@pytest.fixture()
def read_from_flie_responce_goods_1179889():
    #before write code you shell download responce ttps://trial-sport.ru/goods/51530/1179889.html 
    #curl https://trial-sport.ru/goods/51530/1179889.html -O
    text = ''
    with open('download/1179889.html','r') as response:
        text = response.read() 
    return text

def test_page_title_goods_1179889(read_from_flie_responce_goods_1179889):
    p = OnePageProcessor(read_from_flie_responce_goods_1179889)
    assert p.list_dict() == [
        {
            "title": 'Блин вратаря DR X6 GOALIE BLOKER',
            'price': 6864,
            'price_sale': 2402,
            'brand': 'Главная / Каталог / Коньки ледовые / Снаряжение / Блины вратаря / DR',
            'brand_url': '/gds.php?s=51530&c1=1070639&brand=189643&c2=1084245'
        },
    ]

@pytest.fixture()
def read_from_flie_responce_goods_2174237():
    #before write code you shell download responce https://trial-sport.ru/goods/51527/2174237.html
    #curl https://trial-sport.ru/goods/51527/2174237.html -O
    text = ''
    with open('download/2174237.html','r') as response:
        text = response.read() 
    return text

def test_page_title_goods_2174237(read_from_flie_responce_goods_2174237):
    p = OnePageProcessor(read_from_flie_responce_goods_2174237)
    assert p.list_dict() == [
        {
            "title": "Горнолыжные ботинки Dalbello LUPO PRO HD",
            "price": 87360,
            'price_sale': 56784,
            'brand': 'Главная / Каталог / Лыжи горные / Обувь / Горнолыжные ботинки / Dalbello',
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=192987&c2=1078207',
        },
    ]

# add online checker
def test_web_page_title_goods_2175792():
    p = OnePage("https://trial-sport.ru/goods/51527/2175792.html")
    expected = [
        {
            "title": "Горнолыжные ботинки Dalbello CHAKRA ELEVATE 115 T.I. ID",
            "price": 66142,
            'price_sale': 42992,
            'brand': 'Главная / Каталог / Лыжи горные / Обувь / Горнолыжные ботинки / Dalbello',
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=192987&c2=1078207',
        },
    ]
    assert p.list_dict() == expected

def test_web_page_title_goods_2175355():
    p = OnePage("https://trial-sport.ru/goods/51527/2175355.html")
    expected = [
        {
            "title": "Горнолыжные ботинки Dalbello LUPO AX 120",
            "price": 68640,
            'price_sale': 44616,
            'brand': 'Главная / Каталог / Лыжи горные / Обувь / Горнолыжные ботинки / Dalbello',
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=192987&c2=1078207',
        },
    ]
    assert p.list_dict() == expected

def test_web_page_title_goods_2174687():
    p = OnePage("https://trial-sport.ru/goods/51527/2174687.html")
    expected = [
        {
            "title": "Горнолыжные ботинки Dalbello QUANTUM FREE 110",
            "price": 69887,
            'price_sale': 45426,
            'brand': 'Главная / Каталог / Лыжи горные / Обувь / Горнолыжные ботинки / Dalbello',
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=192987&c2=1078207',
        },
    ]
    assert p.list_dict() == expected

def test_web_page_title_goods_2174362():
    p = OnePage("https://trial-sport.ru/goods/51527/2174362.html")
    expected = [
        {
            "title": "Горнолыжные ботинки Dalbello KRYPTON 130 T.I. ID",
            "price": 74880,
            'price_sale': 48672,
            'brand': 'Главная / Каталог / Лыжи горные / Обувь / Горнолыжные ботинки / Dalbello',
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=192987&c2=1078207',
        },
    ]
    assert p.list_dict() == expected

def test_web_page_title_goods_1525157():
    p = OnePage("https://trial-sport.ru/goods/51527/1525157.html")
    expected = [
        {
            "title": "Горнолыжные ботинки Lange WORLD CUP RS ZB",
            "price": 67120,
            'price_sale': 53696,
            'brand': 'Главная / Каталог / Лыжи горные / Обувь / Горнолыжные ботинки / Lange',
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=263003&c2=1078207'
        },
    ]
    assert p.list_dict() == expected

def test_web_page_title_goods_1525371():
    p = OnePage("https://trial-sport.ru/goods/51527/1525371.html")
    expected = [
        {
            "title": "Горнолыжные ботинки Rossignol ALLTRACK ELITE 130 LT GW",
            "price": 62559,
            'price_sale': 50047,
            'brand': 'Главная / Каталог / Лыжи горные / Обувь / Горнолыжные ботинки / Rossignol',
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=465845&c2=1078207',
        },
    ]
    assert p.list_dict() == expected

def test_web_page_title_goods_2174317():
    p = OnePage("https://trial-sport.ru/goods/51527/2174317.html")
    expected = [
        {
            "title": "Горнолыжные ботинки Lange XT3 130 LV",
            'price': 81119,
            'price_sale': 52727,
            'brand': 'Главная / Каталог / Лыжи горные / Обувь / Горнолыжные ботинки / Lange',
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=263003&c2=1078207',
        },
    ]
    assert p.list_dict() == expected


