"""Создайте класс Car, который представляет автомобиль.
У него должны быть атрибуты для хранения модели,
года выпуска, цвета, количества дверей и текущей скорости.
Добавьте методы, которые возвращают год, марку,
цвет и текущую скорость автомобиля."""
from datetime import datetime


class Car:
    def __init__(
        self,
        model: str,
        year_of_car_manufacture: int,
        car_color: str,
        count_of_doors: int,
        current_speed_km_h: int,
    ):
        self.__validation(
            model,
            year_of_car_manufacture,
            car_color,
            count_of_doors,
            current_speed_km_h,
        )
        self.__model: str = model.strip()
        self.__year_of_car_manufacture: int = year_of_car_manufacture
        self.__car_color: str = car_color.strip()
        self.__count_of_doors: int = count_of_doors
        self.__current_speed_km_h: int = current_speed_km_h

    def get_year_of_car_manufacture(self):
        return self.__year_of_car_manufacture

    def get_model(self):
        return self.__model

    def get_car_color(self):
        return self.__car_color

    def get_current_speed_km_h(self):
        return self.__current_speed_km_h

    @staticmethod
    def __validation(
        model: str,
        year_of_car_manufacture,
        car_color: str,
        count_of_doors: int,
        current_speed_km_h: int,
    ):
        """
        Валидация данных инициализации объекта класса
        """
        is_valid_model: bool = isinstance(model, str)

        YEAR_OF_CREATING_FIRST_AUTOMOBILE: int = 1885
        is_valid_year_of_car_manufacture: bool = (
            (isinstance(year_of_car_manufacture, int))
            and (year_of_car_manufacture > YEAR_OF_CREATING_FIRST_AUTOMOBILE)
            and (year_of_car_manufacture <= int(datetime.now().today().strftime("%Y")))
        )

        is_valid_car_color: bool = isinstance(car_color, str)

        MAXIMUM_NUMBER_OF_DOORS: int = 5
        is_valid_count_of_doors: bool = (
            (isinstance(count_of_doors, int)) and (count_of_doors > 0)
        ) and (count_of_doors <= MAXIMUM_NUMBER_OF_DOORS)

        is_valid_current_speed_km_h: bool = (isinstance(current_speed_km_h, int)) and (current_speed_km_h > 0)

        is_not_valid: bool = not (
            is_valid_model
            and is_valid_year_of_car_manufacture
            and is_valid_car_color
            and is_valid_count_of_doors
            and is_valid_current_speed_km_h
        )
        if is_not_valid:
            raise TypeError("Ошибка инициализации. Некорректные данные")


c = Car("audi", 1999, "brown", 4, 135)
