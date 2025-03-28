#Создайте класс Car, который представляет автомобиль. У него должны быть атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости. Добавьте методы которые возвращают год, марку, цвет и текущую скорость автомобиля.

class Car():
    def __init__(self, model, year, color, door, speed):
        self.model = model
        self.year = year
        self.color = color
        self.door = door
        self.speed = speed
    
    def Getyear (self):
         return self.year
    def Getmodel (self):
         return self.model
    def Getcolor (self):
         return self.color
    def Getspeed (self):
         return self.speed