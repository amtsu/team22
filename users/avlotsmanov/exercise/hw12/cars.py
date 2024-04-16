class Cars():
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

tesla = Cars(
    model='Tesla',
    year=2020,
    color='Black')

print(tesla.color_ret(), tesla.speed_ret(), tesla.year_ret())

tesla.speed_up(60)

print(tesla.speed_ret())






