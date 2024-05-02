'''3. Расширьте класс Shape для представления различных геометрических фигур сохранением и загрузкой из файла. Напишите тест который проходится по несколькьким фалйам, загружает из них фигуры и выводит их периметр и площадь.'''

import math 
import pickle
    
class Shape():

    def __init__(self):
        pass
        
    def area(self):
        pass

    def perimeter(self):
        pass

    def save_shape(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_shape(file_name):
        with open(file_name, 'rb') as f:
            return pickle.load(f)

 



    