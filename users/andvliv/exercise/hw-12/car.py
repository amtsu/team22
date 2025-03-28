#Создайте класс Car, который представляет автомобиль. У него должны быть атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости. Добавьте методы которые возвращают год, марку, цвет и текущую скорость автомобиля.

class Car:
    def __init__(self, model, year, color, doors, current_speed):
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.current_speed = current_speed

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_doors(self):
        return self.doors

    def get_current_speed(self):
        return self.current_speed
