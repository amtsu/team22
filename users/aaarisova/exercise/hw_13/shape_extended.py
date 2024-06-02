'''3. Расширьте класс Shape для представления различных геометрических фигур сохранением и загрузкой из файла. Напишите тест который проходится по несколькьким фалйам, загружает из них фигуры и выводит их периметр и площадь.'''

import math 
import pickle
    
class Shape():
        
    def area(self):
        '''абстрактный метод для вычисления площади'''
        pass

    def perimeter(self):
        '''абстрактный метод для вычисления периметра'''
        pass

    def save_to_file(self, file_name):
        '''метод сохранения из памяти в файл с помощью сериализации.'''
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(file_name):
        '''метод загрузки фигур из файла в память с помощью десериализации.'''
        with open(file_name, 'rb') as f:
            return pickle.load(f)

 



    