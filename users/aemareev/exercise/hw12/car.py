class Car:
    def __init__(self, model: str, year: int, color: str, number_of_doors: int, current_speed: int | float):
        self.__model = model
        self.__year = year
        self.__color = color
        self.__number_of_doors = number_of_doors
        self.__current_speed = current_speed

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @property
    def current_speed(self):
        return self.__current_speed

    def speed_up(self):
        self.__current_speed += 5

    def stop(self):
        self.__current_speed = 0


if __name__ == "__main__":
    car = Car('Volvo', 2018, 'white', 5, 40)
    assert car.model == 'Volvo'
    assert car.year == 2018
    assert car.color == 'white'
    assert car.number_of_doors == 5
    assert car.current_speed == 40
    car.speed_up()
    assert car.current_speed == 45
    car.stop()
    assert car.current_speed == 0
