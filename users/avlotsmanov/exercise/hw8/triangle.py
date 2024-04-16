def triangle_type(
        a: float,
        b: float,
        c: float
) -> str:
    """
    Функция, определяющая тип треугольника по длинам его сторон
    """
    if type(a) is not int or type(b) is not int or type(c) is not int:
        raise TypeError

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
    return result