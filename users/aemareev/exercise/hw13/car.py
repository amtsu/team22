from file_methods import FileMethods


class Car(FileMethods):
    def __init__(self, model: str, year: int, color: str, number_of_doors: int, current_speed: int | float):
        super().__init__()
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

    def speed_up(self, speed: int = 5):
        self.__current_speed += speed

    def stop(self):
        self.__current_speed = 0


if __name__ == "__main__":
    car = Car('Volvo', 2018, 'white', 5, 40)
    car.dump_obj()
    new_car: Car = Car.load_obj('default.pickle')
    new_car.speed_up(17)
    new_car.dump_obj()
    new_car_2: Car = Car.load_obj('default.pickle')
    assert new_car_2.current_speed == car.current_speed + 17
    assert new_car_2.current_speed == new_car.current_speed
