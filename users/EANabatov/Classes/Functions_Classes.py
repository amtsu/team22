print("Создать итератор, который будет возвращать следующую числовую последовательность: ")
print()


#  1/1, -1/3, 1/5, -1/7, 1/9, -1/11...


class Third:
    def __init__(self, count_of_iterations):
        self.iteration = -1
        self.dividend = -1
        self.divider = -1
        self.count_of_iterations = count_of_iterations

    def __iter__(self):
        return self

    def __next__(self):
        self.dividend = self.dividend * -1
        self.divider += 2
        self.iteration += 1
        if self.iteration == self.count_of_iterations:
            raise StopIteration
        return "{}/{}".format(self.dividend, self.divider)


three = Third(15)
print(list(three))
print("___________ FINISH __________")
print()

print(
    "Доработать предыдущее задание так, чтобы итератор возвращал не члены последовательности, а их суммы от первого "
    "до n-го: ")
#  1/1,
#  1/1 -1/3,
#  1/1 -1/3 +1/5,
print()


#  Замечание. Справедлива следующая формула (ряд Лейбница):
#  1/1 -1/3 +1/5 + ... = Sum( -1**n / (2n + 1) ) = Pi/4

class Leibniz:
    def __init__(self, count_of_iterations: int):
        self.iteration = -1
        self.n = 0
        self.result = 0.000
        self.count_of_iterations = count_of_iterations

    def __iter__(self):
        return self

    def __next__(self):
        self.result += pow(-1, self.n) / (2 * self.n + 1)
        self.n += 1
        self.iteration += 1
        if self.iteration == self.count_of_iterations:
            raise StopIteration
        return f"{self.result:.3f}"


sums = Leibniz(15)
print(list(sums))
print("___________ FINISH __________")
print()

print("Доработать предыдущее решение, чтобы итератор выдавал приближения числа π. ")
print()


class NearPi:
    def __init__(self, count_of_iterations: int):
        self.iteration = -1
        self.n = 0
        self.result = 0
        self.count_of_iterations = count_of_iterations
        self.keks = []

    def __iter__(self):
        return self

    def __next__(self):
        self.iteration += 1
        self.result += (pow(-1, self.n) / (2 * self.n + 1)) * 4
        self.n += 1
        if self.iteration == self.count_of_iterations:
            raise StopIteration
        self.keks.append(str(self.result))
        return f"{self.result:.3f}"


Pi = NearPi(400)
print("Приближение к числу Pi: {}".format(list(Pi)))
print("Приближение к числу Pi на {} итерации: {}".format(Pi.count_of_iterations, f"{Pi.result:.3f}"))
print("___________ FINISH __________")
print()

print("Создать итератор, который будет возвращать последовательность факториалов натуральных чисел:")
# 1! = 1
# 2! = 1 * 2 = 2
# 3! = 1 * 2 * 3 = 6
# ...
print()


class Factorial:
    def __init__(self, n=int):
        self.n = n + 1
        self.multipliers = []
        self.result = 1
        self.iteration = 0
        self.output = []

    def __iter__(self):
        return self

    def __next__(self):
        self.iteration += 1
        if self.iteration >= self.n:
            raise StopIteration
        else:
            self.result *= self.iteration
            self.multipliers.append(str(self.iteration))
            if self.iteration == 1:
                self.output = "{}! = {}".format(self.iteration, self.result)
            else:
                self.output = "{}! = {} = {}".format(self.iteration, " * ".join(self.multipliers), self.result)
        return self.output


n5 = Factorial(10)
for i in n5:
    print(i)
print("___________ FINISH __________")
print()
