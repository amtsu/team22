#  Создать итератор, который будет возвращать следующую числовую последовательность:

#  1/1, -1/3, 1/5, -1/7, 1/9, -1/11...


class Third:
    def __init__(self):
        self.iteration = -1
        self.dividend = 1
        self.divider = -1
        self.count_of_iterations = 10

    def __iter__(self):
        return self

    def __next__(self):
        self.iteration += 1
        if self.iteration == self.count_of_iterations:
            raise StopIteration
        if self.iteration % 2 != 0:
            self.dividend = self.dividend * -1
        else:
            self.dividend = int((self.dividend ** 2) ** 0.5)
        self.divider += 2
        return "{}/{}".format(self.dividend, self.divider)


three = Third()
print(list(three))

# Подскажите, пожалуйста, нормально ли я написал функционал класса из ДЗ по классам или это костыли?(занятие было 22.02.23)
# Спасибо!