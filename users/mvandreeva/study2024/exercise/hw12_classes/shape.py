class Shape:

    def __init__(self, figure):
        self._figure = figure

    def count_area(self):
        area = None
        if self._figure == "circle":
            area = round(3.14 * (self._radius ** 2),2)
        elif self._figure == "rectangle":
            area = round((self._a * self._b), 2)
        elif self._figure == "triangle":
            p = self.count_perimeter()
            area = (p * (p - self._a) * (p - self._b) * (p - self._c))**0.5
        return area

    def count_perimeter(self):
        perimeter = None
        if self._figure == "circle":
            perimeter = round(2 * 3.14 * self._radius,2)
        elif self._figure == "rectangle":
            perimeter = 2 * (self._a + self._b)
        elif self._figure == "triangle":
            perimeter = (self._a + self._b + self._c) / 2
        return perimeter