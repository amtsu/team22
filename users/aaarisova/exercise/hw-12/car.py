'''1. Создайте класс Car, который представляет автомобиль. У него должны быть атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости. Добавьте методы которые возвращают год, марку, цвет и текущую скорость автомобиля.'''

class Car():
    def __init__(self, model, year, color, doors, speed):
        self.__model = model
        self.__year = year
        self.__color = color
        self.__doors = doors
        self.__speed = speed

    def new_car(self):
        return self.__model, self.__year, self.__color, self.__doors, self.__speed


