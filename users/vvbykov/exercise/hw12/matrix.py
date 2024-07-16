import numpy as np

class Matrix:

    def __init__(self, matrix):
        self._elements = matrix

    @property
    def elements(self):
        return self._elements

    @staticmethod
    def lenght_check(m1, m2) -> bool:
        if (len(m1) == len(m2)) and (len(m1[0]) == len(m2[0])):
            return True
        else:
            raise ValueError('Matrix must be the same size')
        

    def  __add__(self, other):
        if Matrix.lenght_check(self.elements, other.elements):
            result = [ [0]*len(self.elements[0]) for i in range(len(self.elements)) ]
            for i in range(len(self.elements)):
                for j in range(len(self.elements[0])):
                    result[i][j] = self.elements[i][j] + other.elements[i][j]
            return result

    def  __sub__(self, other):
        if Matrix.lenght_check(self.elements, other.elements):
            result = [ [0]*len(self.elements[0]) for i in range(len(self.elements)) ]
            for i in range(len(self.elements)):
                for j in range(len(self.elements[0])):
                    result[i][j] = self.elements[i][j] - other.elements[i][j]
            return result

    def  __mul__(self, other):
        if Matrix.lenght_check(self.elements, other.elements):
            result = [ [0]*len(self.elements[0]) for i in range(len(self.elements)) ]
            for i in range(len(self.elements)):
                for j in range(len(self.elements[0])):
                    sum = 0
                    for k in range(len(self.elements[0])):
                        sum += self.elements[i][k] * other.elements[k][j]
                    result[i][j] = sum
            return result

    def trans(self):
        result = [ [0]*len(self.elements[0]) for i in range(len(self.elements)) ]
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                result[i][j] = self.elements[j][i]
        return result

    def det(self):
        return round(np.linalg.det(self.elements), 2)

    def inv(self):
        result = np.linalg.inv(self.elements).tolist()
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] = round(result[i][j], 2)
        return result


                
        