class Car:
    def __init__(self, model, year, color, doors, speed):
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.speed = speed
        
    def car_year(self):
        return self.year 

    def car_model(self):
        return self.model
    
    def car_color(self):
        return self.color
    
    def current_speed(self):
        return self.speed 

    def acceleration(self):
        new_speed = self.speed + 5
        return new_speed
    
    def stop(self):
        stop = self.speed - self.speed 
        #stop = 0
        return stop
        

