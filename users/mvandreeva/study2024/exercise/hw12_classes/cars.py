class Car:
    """
    Класс представляет собой автомобиль.
    Имеет атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости,
    методы которые возвращают год, марку, цвет и текущую скорость автомобиля
    """
    def __init__(self, model, year, color, doors_num, current_speed = 0):
        self.__model = model
        self.__year = year
        self.__color = color
        self.__doors_num = doors_num
        self.__current_speed = current_speed

    def year(self):
        return self.__year

    def model(self):
        return self.__model    

    def color(self):
        return self.__color

    def current_speed(self):
        return self.__current_speed