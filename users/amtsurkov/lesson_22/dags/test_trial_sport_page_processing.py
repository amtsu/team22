from TrialSportPageProcessing import OnePage, OnePageProcessor, TrialSportServiceProcessing
import pytest

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
            'brand_url': '/gds.php?s=51530&c1=1070639&brand=189643&c2=1084245',
            'image_url': '/images/catalog/_12_13_dr_blin_x6_goalie_bloker_1232831.jpg',
            'source_url': 'https://trial-sport.ru/goods/51530/1179889.html',
            'url': 'https://trial-sport.ru/goods/51530/1179889.html',
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
    p = OnePageProcessor(read_from_flie_responce_goods_1179889, '')
    assert p.list_dict() == [
        {
            "title": 'Блин вратаря DR X6 GOALIE BLOKER',
            'price': 6864,
            'price_sale': 2402,
            'brand': 'Главная / Каталог / Коньки ледовые / Снаряжение / Блины вратаря / DR',
            'brand_url': '/gds.php?s=51530&c1=1070639&brand=189643&c2=1084245',
            'image_url': '/images/catalog/_12_13_dr_blin_x6_goalie_bloker_1232831.jpg',
            'source_url': '',
            'url': '',
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
    p = OnePageProcessor(read_from_flie_responce_goods_2174237, 'x')
    assert p.list_dict() == [
        {
            "title": "Горнолыжные ботинки Dalbello LUPO PRO HD",
            "price": 87360,
            'price_sale': 56784,
            'brand': 'Главная / Каталог / Лыжи горные / Обувь / Горнолыжные ботинки / Dalbello',
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=192987&c2=1078207',
            'image_url': '/images/catalog/D210700100-Dalbello-skiboot-Lupo_Pro_HD-caraibiblue-_2199100.jpg',
            'source_url': 'x',
            'url': 'x',
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
            'image_url': '/images/catalog/d210720100_dalbello_skiboot_chakra_elevate_115_id_ti_2538672.jpg',
            'source_url': 'https://trial-sport.ru/goods/51527/2175792.html',
            'url': 'https://trial-sport.ru/goods/51527/2175792.html',
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
            'image_url': '/images/catalog/d210700300_dalbello_skiboot_lupo_ax_120_grey_black_2199083.jpg',
            'source_url': 'https://trial-sport.ru/goods/51527/2175355.html',
            'url': 'https://trial-sport.ru/goods/51527/2175355.html',
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
            'image_url': '/images/catalog/d210800700_dalbello_skiboot_quantum_free_110_black_a_2538725.jpg',
            'source_url': 'https://trial-sport.ru/goods/51527/2174687.html',
            'url': 'https://trial-sport.ru/goods/51527/2174687.html',
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
            'image_url': '/images/catalog/d210710100_dalbello_skiboot_krypton_130_id_ti_racegr_2538668.jpg',
            'source_url': 'https://trial-sport.ru/goods/51527/2174362.html',
            'url': 'https://trial-sport.ru/goods/51527/2174362.html',
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
            'brand_url': '/gds.php?s=51527&c1=1070485&brand=263003&c2=1078207',
            'image_url': '/images/catalog/lbi9250_world_cup_rs_zb_power_blue_rvb72dpi_01_1534667_15347.jpg',
            'source_url': 'https://trial-sport.ru/goods/51527/1525157.html',
            'url': 'https://trial-sport.ru/goods/51527/1525157.html',
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
            'image_url': '/images/catalog/rbj3000_alltrack_elite_130_l_rgb72dpi_01_1543978.jpg',
            'source_url': 'https://trial-sport.ru/goods/51527/1525371.html',
            'url': 'https://trial-sport.ru/goods/51527/1525371.html',
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
            'image_url': '/images/catalog/lbj7000_xt3_130_lv_storm_blue_rgb300dpi_2539265.jpg',
            'source_url': 'https://trial-sport.ru/goods/51527/2174317.html',
            'url': 'https://trial-sport.ru/goods/51527/2174317.html',
        },
    ]
    assert p.list_dict() == expected

    
#TrialSportServiceProcessing
def test_trial_sport_service_processing():
    tssp =  TrialSportServiceProcessing()
    tssp.load_url_by_default()
    #tssp.process()
    tssp.save_in_file_with_current_datetime()
    #tssp.send_in_api()


