#part1 Создайте класс Car, который представляет автомобиль.
#У него должны быть атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости.
#Добавьте методы которые возвращают год, марку, цвет и текущую скорость автомобиля.

#part2 Расширьте класс автомобиль, реализовав метод ускорения автомоиля на 5 км в час.
# И метод остановки автомобиля.
class Cars:
    def __init__(self, model, year, color, speed = 0):
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed
        self.doors = 4

    def speed_up(self, delta):
        self.speed += delta

    def speed_down(self, delta):
        self.speed -= delta

    def year_ret(self):
        return self.year

    def color_ret(self):
        return self.color

    def speed_ret(self):
        return self.speed

    def stop_car(self):
        return self.speed == 0

tesla = Cars(
    model='Tesla',
    year=2020,
    color='Black')

print(tesla.color_ret(), tesla.speed_ret(), tesla.year_ret())

tesla.speed_up(60)

print(tesla.speed_ret())






