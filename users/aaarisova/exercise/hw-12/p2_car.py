#Расширьте класс автомобиль, реализовав метод ускорения автомоиля на 5 км в час. И метод остановки автомобиля.
from car import Car


class Car2(Car):

    def acceleration(self): 
        '''Увеличивает скорость автомобиля на 5 км/ч'''
        self.speed += 5 
        return self.speed


    def stop(self):
        '''Останавливает автомобиль'''
        self.speed = 0 
        return self.speed







