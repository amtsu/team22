from homework_3_func import gip, arithmetic, square_parameters, is_palindrome

def test_1():
    fun = gip(3,4)
    if 4.9 < fun < 5.1:
        assert True
        
def test_2():
    fun = arithmetic(3,4,'+')
    if fun != 7:
        assert False
        
def test_3():
    fun = square_parameters(3)
    if fun[0] != 12:
        assert False
        
def test_4():
    fun = is_palindrome('assa')
    if fun != True:
        assert False
        
def test_all():
    test_1()
    test_2()
    test_3()
    test_4()
    print('all test good')