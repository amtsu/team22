class Car:
    """
    Создайте класс Car, который представляет автомобиль. У него должны быть атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости. Добавьте методы которые возвращают год, марку, цвет и текущую скорость автомобиля.
    """
    def __init__(self, model, year, color, doors, speed):
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.speed = speed

    def getYear(self):
        return self.year

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getSpeed(self):
        return self.speed

    def acc(self):
        self.speed += 5
        return self.speed

    def brake(self):
        self.speed = 0
        return self.speed
        


