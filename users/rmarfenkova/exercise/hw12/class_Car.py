class Car():
    """
    Создайте класс Car, который представляет автомобиль. У него должны быть атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости.
    Добавьте методы которые возвращают год, марку, цвет и текущую скорость автомобиля.
    """
    
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