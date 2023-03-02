"""
это генератор последовательности типа 1/1, -1/3, 1/5, -1/7, 1/9, -1/11
"""
class QuaPiRow:
	"""
	итератор, возвращающий элементы последовательности -1**n / (2n + 1) для
	всех натуральный n меньше заданного
	"""
	def __init__(self, count):
		self.__result = (f"{(1 - 2*(i%2))}/{2*i+1}" for i in range(count))

	def __iter__(self):
		return self

	def __next__(self):
		return next(self.__result)
