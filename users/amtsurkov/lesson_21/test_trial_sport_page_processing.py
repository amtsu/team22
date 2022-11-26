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
            "price": 2402,
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
            "price": 2402,
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
            "price": 56784,
        },
    ]


