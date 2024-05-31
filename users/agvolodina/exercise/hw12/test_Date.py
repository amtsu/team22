from func_Date import Date

#тест для проверки метода для проверки 2х дат
def test_compare_days ():
    date1 =  Date(year = 2000, month = 12, day = 30)  
    date2 =  Date(year = 2000, month = 12, day = 10) 
    date3 =  Date(year = 2000, month = 12, day = 31)
    date4 =  Date(year = 2000, month = 12, day = 30)
    assert date1.compare_days(date2) == 'больше'
    assert date1.compare_days(date3) == 'меньше'
    assert date1.compare_days(date4) == 'равны' 
    
#тест для проверки разницы между 2мя датами
def test_difference_dates ():
    date1 =  Date(year = 2000, month = 12, day = 30)  
    date2 =  Date(year = 2000, month = 12, day = 10) 
    date3 =  Date(year = 2000, month = 12, day = 31)
    date4 =  Date(year = 2000, month = 12, day = 30)
    assert date1.difference_dates(date2) == 20
    assert date1.difference_dates(date3) == -1
    assert date1.difference_dates(date4) == 0 