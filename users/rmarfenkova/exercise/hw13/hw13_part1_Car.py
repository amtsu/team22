import pickle

class Car():
    def __init__(self, model, year_of_issue, color, door, speed):
        self.model = model
        self.year_of_issue = year_of_issue
        self.color = color 
        self.door = door 
        self.speed = speed
        
    def get_year_of_issue(self):
        return self.year_of_issue

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_speed(self):
        return self.speed
    
    def accelerate(self):
        """ускорение автомобиля"""
        self.speed += 5
        
    def stop(self):
        """остановка автомобиля"""
        self.speed = 0
          

