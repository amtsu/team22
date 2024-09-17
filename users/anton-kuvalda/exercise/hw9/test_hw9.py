from function_hw9 import triangle_type, apple_search

######## Тестируем остроугольность треугольника
def test_acute():
    input = [12,12,5] # такие стороны у остроугольного треугольника 
    expected =  "остроугольный"
    assert expected == triangle_type(*input)


def test_obtuse():
    """
    тестируем тупоугольность треугольника
    """
    input = [12,12,20] # такие стороны у тупоугольного треугольника 
    expected =  "тупоугольный"
    assert expected == triangle_type(*input)

def test_right():
    """
    тестируем прямоугольность треугольника
    """
    input = [3,4,5] # такие стороны у прямоугольного треугольника 
    expected =  "прямоугольный"
    assert expected == triangle_type(*input)

def test_untriangle():
    """
    тестируем НЕтреугольниковость треугольника
    """
    input = [1,2,500] # такие стороны у НЕ треугольника 
    expected =  "не треугольник"
    assert expected == triangle_type(*input)

def test_inp_minus():
    """
    подаём отрицательные числа на вход
    """
    input = [-1,0,-500] # отрицательные числа на вход 
    expected =  "не треугольник"
    assert expected == triangle_type(*input)
test_inp_minus()

def test_inp_str():
    """
    подаём str на вход
    """
    input = ['ыва','veg','34'] # str на вход 
    type(input)
    expected =  "не треугольник"
    assert expected == triangle_type(*input)
test_inp_str()


########## from hw5

def test_apple_search():
    expected == apple_search(spisok)
    assert expected == apple_search(spisok)

def apple_search(spisok):
    #spisok = []
    for fruit in spisok:
        if fruit == 'apple':
            #print ('яблоко есть')
            return True
    #print ('яблоко нет')
    return False