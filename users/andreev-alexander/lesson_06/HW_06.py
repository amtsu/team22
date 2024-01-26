# https://github.com/amtsu/team22/blob/main/library/theory/python_basics_4.ipynb

"""
Создать итератор, который будет возвращать символы
переданной ему строки, по одному символу за итерацию.
"""

class IterBySymbol:
    def __init__(self, iter_string):
        self.iter_string = iter_string
        self.position = -1
        self.__length = len(self.iter_string)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.position += 1
        if self.position == self.__length:
            raise StopIteration
        return self.iter_string[self.position]

# item = IterBySymbol("stroka")
# for i in item:
#     print(i)


"""
Создать итератор, который будет возвращать следующую числовую
последовательность:
1/1, -1/3, 1/5, -1/7, 1/9, -1/11...
"""

class IterFraction:
    def __init__(self, end_value) -> None:
        self.end_value = end_value  # значение до которого идет итерация
        self.numerator = -1  # числитель
        self.denominator = -1  # знаменатель
        self.sign = -1

        if not isinstance(self.end_value, (int, float)):
            raise TypeError("Конечное значение должно быть числом.")

    def __iter__(self):
        return self

    def __next__(self):
        self.numerator *= self.sign
        self.denominator += 2
        if self.denominator > self.end_value:
            raise StopIteration
        return f"{self.numerator}/{self.denominator}"

# item = IterFraction(15)
# for _ in item:
#     print(_)


"""
Доработать предыдущее задание так, чтобы итератор возвращал
не члены последовательности, а их суммы от первого до n-го:
1/1,
1/1 -1/3,
1/1 -1/3 +1/5,
"""

class IterFractionSum:

    items = []

    def __init__(self, end_value) -> None:
        self.end_value = end_value  # значение до которого идет итерация
        self.numerator = -1  # числитель
        self.denominator = -1  # знаменатель
        self.sign = -1

        if not isinstance(self.end_value, (int, float)):
            raise TypeError("Конечное значение должно быть числом.")

    def __iter__(self):
        return self

    def __next__(self):
        self.numerator *= self.sign
        self.denominator += 2
        result = f"{self.numerator}/{self.denominator}"
        self.items.append(result)
        if self.denominator > self.end_value:
            raise StopIteration
        return " ".join(str(num) for num in self.items)

# item = IterFractionSum(15)
# for _ in item:
#     print(_)


"""
Замечание. Справедлива следующая формула (ряд Лейбница):
1/1 -1/3 +1/5 + ... = Sum( -1**n / (2n + 1) ) = Pi/4

Доработать предыдущее решение, чтобы итератор выдавал приближения числа π.
"""

# не сделал

"""
Создать итератор, который будет возвращать последовательность факториалов
натуральных чисел:
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
...
"""

# не сделал
