"""
Создайте класс Car, который представляет автомобиль. У него должны быть атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости. Добавьте методы которые возвращают год, марку, цвет и текущую скорость автомобиля.
"""
class Car:
    
    def __init__(self, model, year, color, doors, speed):
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.speed = speed
    
    def get_year(self):
        return self.year

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_speed(self):
        return self.speed

# Пример использования класса
car1 = Car("Toyota Camry", 2022, "black", 4, 180)

# Получаем информацию о модели, годе выпуска, цвете и скорости автомобиля
print("Модель автомобиля:", car1.get_model())
print("Год выпуска автомобиля:", car1.get_year())
print("Цвет автомобиля:", car1.get_color())
print("Максимальная скорость автомобиля:", car1.get_speed(), "км/ч")

# Создаем новый объект автомобиля
car2 = Car("Tesla Model S", 2023, "red", 4, 250)

# Получаем информацию о новом автомобиле
print("\nМодель автомобиля:", car2.get_model())
print("Год выпуска автомобиля:", car2.get_year())
print("Цвет автомобиля:", car2.get_color())
print("Максимальная скорость автомобиля:", car2.get_speed(), "км/ч")
