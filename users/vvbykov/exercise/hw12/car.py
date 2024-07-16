import datetime

class Car:
    
    colours = ("red", "blue", "black", "white")
    
    def __init__(self, model: str, colour: str, year: int, doors: int):
        self._speed = 0
        self._model = model
        self._year = year
        self._doors = doors

        if len(model) > 0:
            self._model = model
        else:
            raise ValueError("Invalid model value")

        if colour in Car.colours:
            self._colour = colour
        else:
            raise ValueError("Invalid colour value")

        if 1990 <= year <= datetime.date.today().year:
            self._year = year
        else:
            raise ValueError("Invalid year value")
    
        if 2 <= doors <= 5:
            self._doors = doors
        else:
            raise ValueError("Invalid doors number value")

    @property
    def model(self):
        return self._model
        
    @property
    def colour(self):
        return self._colour

    @property
    def year(self):
        return self._year

    @property
    def doors(self):
        return self._doors

    @property
    def speed(self):
        return self._speed

    def go(self):
        self._speed = 40

    def stop(self):
        self._speed = 0

    def speed_up(self):
        self._speed += 5
        if self._speed > 80:
            self._speed = 80

    def speed_down(self):
        self._speed -= 5
        if self._speed < 0:
            self._speed = 0


    