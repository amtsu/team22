#Расширьте класс автомобиль, реализовав метод ускорения автомоиля на 5 км в час. И метод остановки автомобиля.
    
class Car():
    def __init__(self, model, year, color, doors, speed):
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.speed = speed

    
    def get_model(self):
        return self.model

    
    def get_year(self):
        return self.year 

    
    def get_color(self):
        return self.color  

    
    def get_speed(self):
        return self.speed


    def acceleration(self): 
        self.speed += 5 
        return self.speed


    def stop(self):
        self.speed = 0 
        return self.speed
