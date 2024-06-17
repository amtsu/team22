class Car:
    """
    Автомобиль
    """

    def __init__(self, brand, year, colour, doors_number, current_speed):
        self.brand = brand
        self.year = year
        self.colour = colour
        self.doors_number = doors_number
        self.current_speed = current_speed

    def get_year(self):
        return self.year
 
    def get_brand(self):
        return self.brand
 
    def get_colour(self):
        return self.colour
 
    def get_current_speed(self):
        return self.current_speed