from TrialSportPageProcessing import OnePage

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

def test_title_goods_1179889():
    p = OnePage("https://trial-sport.ru/goods/51530/1179889.html")
    assert p.list_dict() == [
        {
            "title": 'Блин вратаря DR X6 GOALIE BLOKER',
            "price": 2402,
        },
    ]


