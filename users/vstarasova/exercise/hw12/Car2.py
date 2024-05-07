"""
Расширьте класс автомобиль, реализовав метод ускорения автомоиля на 5 км в час. И метод остановки автомобиля.
"""
from Car import Car

class Car2(Car):
    def increase_speed(self):
        self.speed += 5
        return self.speed

    def stop(self):
        self.speed = 0
        return self.speed

# Пример использования класса
car2 = Car2("Toyota Camry", 2022, "black", 4, 180)
car3 = Car2("Tesla Model S", 2023, "red", 4, 250)
