from  calc_x  import hard_func

#какие тесты нужны
#x = 5
#x = 20
#x = 300

#x = 9
#x = 10
#x = 100
#x = 101

def test_hard_func_x_5():
    assert hard_func(5) == 25
    
def test_hard_func_x_20():
    assert hard_func(20) == 20
    
def test_hard_func_x_300():
    assert hard_func(300) == 1

    
def test_hard_func_x_9():
    assert hard_func(9) == 81
    
def test_hard_func_x_10():
    assert hard_func(10) == 10
    
def test_hard_func_x_99():
    assert hard_func(99) == 99
    
def test_hard_func_x_100():
    assert hard_func(100) == 1
    
def test_hard_func_x_101():
    assert hard_func(101) == 1