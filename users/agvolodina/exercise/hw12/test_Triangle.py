from func_Triangle import Triangle
triangle = Triangle (3,4,5)
#тест для проверки вычисления периметра треугольника
def test_perimeter():
    assert triangle.perimeter(3,4,5) == 12

#тест для проверки остроугольности треугольника
def test_acute():
    triangle = Triangle (12,12,5) # такие стороны у остроугольного треугольника 
    assert triangle.triangle_type(12,12,5) ==  "остроугольный"

#тест для проверки тупоугольности треугольника
def test_obtuse():
    triangle = Triangle (5,8,12) # такие стороны у тупоугольного треугольника
    assert triangle.triangle_type(5,8,12) ==  "тупоугольный"

#тест для проверки прямоугольности треугольника
def test_right():
    triangle = Triangle (5,3,4) # такие стороны у прямоугольного треугольника 
    assert triangle.triangle_type(5,3,4) ==  "прямоугольный"

#тест для проверки не треугольника
def test_not_triangle_str():
    triangle = Triangle ('a','b','c')#заданы строковые значение, а не числа
    assert triangle.triangle_type('a','b','c') ==  "не треугольник"
    
#тест для проверки не треугольника
def test_not_triangle():
    triangle = Triangle (5,5,12) #не может быть таких длин сторон
    assert triangle.triangle_type(5,5,12) ==  "не треугольник"
