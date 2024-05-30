
########## from hw8

def triangle_type(a: float, b: float, c: float) -> str:
    """
    Функция, определяющая тип треугольника по длинам его сторон
    """
    result = "не треугольник"
    triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
    if triangle_exist:
        sides = [a, b, c]
        sides.sort()
        acuteTriangle = (sides[0]**2 + sides[1]**2) > sides[2]**2
        obtuseTriangle = (sides[0]**2 + sides[1]**2) < sides[2]**2
        rightTriangle = abs((sides[0]**2 + sides[1]**2) - sides[2]**2) <= 0.01

        if acuteTriangle:
            result = "остроугольный"
        elif obtuseTriangle:
            result = "тупоугольный"
        elif rightTriangle:
            result  = "прямоугольный"

    print (result)
    return result


########## from hw5

fruits = ['apple', 'orange', 'lemon']
fruits2 = ['granat', 'orange', 'lemon']
fruits3 = ['granat', 'orange', 'lemon', 'apple', 'apple']

def apple_search(spisok):
    #spisok = []
    for fruit in spisok:
        if fruit == 'apple':
            #print ('яблоко есть')
            return True
    #print ('яблоко нет')
    return False

def fruits_y(x):
    if apple_search(x) == True:
        print ('яблоко есть')
    elif apple_search(x) == False:
        print ('яблоко нет') 

print ('---Корзина1:')
fruits_y(fruits)
print ('---Корзина2:')
fruits_y(fruits2)
print ('---Корзина3:')
fruits_y(fruits3)