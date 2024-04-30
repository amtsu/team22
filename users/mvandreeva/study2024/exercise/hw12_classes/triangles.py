class Triangle:
    """
    Класс, который представляет треугольник. 
    Атрибуты - длины сторон.
    Имеет методы для вычисления перимера треугольника и методы вычисления типа треугольника 
    ( равностороннйи, равнобедренный, прямоуголный или разносторонний)
    """
    def __init__(self, a, b, c):
        self.__triangle_flg = self.__is_triangle(a, b, c)
        if self.__triangle_flg:
            self.__a = a
            self.__b = b
            self.__c = c
            self.__triangle_type = []
        else: 
            print("Не треугольник")

    def __is_triangle(self, a, b, c):
        triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and triangle_exist:
            return True

    def count_perimeter(self):
        """
        Методы вычисления перимера треугольника
        """
        if self.__triangle_flg:
            perimeter = self.__a +  self.__b + self.__c
            return perimeter

    def define_type(self):
        """
        Метод вычисления типа треугольника: равностороннйи, равнобедренный, прямоуголный или разносторонний
        """
        if self.__triangle_flg:
            sides_list = [self.__a, self.__b, self.__c]
            max_side = max(sides_list)
            less_sides_list = sides_list[:]
            less_sides_list.remove(max_side)
            if (max_side ** 2) == ((less_sides_list[0] ** 2) + (less_sides_list[1] ** 2)):
                self.__triangle_type.append("Прямоугольный треугольник")
            if self.__a != self.__b and self.__a != c and self.__b != self.__c:
                self.__triangle_type.append("Разносторонний треугольник")
            elif self.__a == self.__b and self.__a == self.__c:
                self.__triangle_type.append("Равносторонний треугольник")
            else:
                self.__triangle_type.append("Равнобедренный треугольник")
            return self.__triangle_type