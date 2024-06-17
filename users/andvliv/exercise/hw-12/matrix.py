#Созлдайте класс для работы с матрицами. Который будет представлять матрицы и поддреживать основные операции сложение, вычитание, умножение, транспонирование. 
#Затем добавьте методы для вычисления определителя матрицы и вычисления обраной матрицы.
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def shape(self):
        return len(self.matrix), len(self.matrix[0])
       
    def plus_matrix(self, other):
        plus_matrix = [[0]*len(self.matrix[0]) for _ in range(len(self.matrix))]
        if self.shape() == other.shape():
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    plus_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return plus_matrix

    def minus_matrix(self, other):
        minus_matrix = [[0]*len(self.matrix[0]) for _ in range(len(self.matrix))]
        if self.shape() == other.shape():
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    minus_matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return minus_matrix

    def trans_matrix(self):
        tr_matrix = [[0]*len(self.matrix) for _ in range(len(self.matrix[0]))]
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                tr_matrix[i][j] = self.matrix[j][i]
        return tr_matrix

            
                    

