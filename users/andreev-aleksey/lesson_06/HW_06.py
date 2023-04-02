"""
Создать итератор, который будет возвращать следующую числовую последовательность:
1/1, -1/3, 1/5, -1/7, 1/9, -1/11...
"""

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

"""
Доработать предыдущее задание так, чтобы итератор возвращал не члены последовательности, а их суммы от первого до n-го:
1/1,
1/1 -1/3,
1/1 -1/3 +1/5,
"""



""""
Замечание. Справедлива следующая формула (ряд Лейбница):
1/1 -1/3 +1/5 + ... = Sum( -1**n / (2n + 1) ) = Pi/4

Доработать предыдущее решение, чтобы итератор выдавал приближения числа π.
"""




""" 
Создать итератор, который будет возвращать последовательность факториалов натуральных чисел:
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
...
"""