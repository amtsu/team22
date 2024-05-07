'''Сначала напишите тест, затем реализуйте метод.
1. Расширьте класс автомобиль, добавив метод сохранения объекта автомобиль из памяти в файл. 
2. Добавьте метод загрузки автомобиля их файла в пямять. 
3. Создайте тест который, загружает автомобиль с файла меняет скорость автомобиля и сохраняет автомобиль с новой соростью в файл. (см файл test_classes)'''

import pickle #модуль

class Car():
    def __init__(self, model, year, color, doors, speed): 
        '''конструктор класса, инициализирую атрибуты объекта'''
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.speed = speed

    
    def get_model(self):
        return self.model
   
    def get_year(self):
        return self.year 
   
    def get_color(self):
        return self.color  
    
    def get_speed(self):
        return self.speed

    def acceleration(self): 
        '''Увеличивает скорость автомобиля на 5 км/ч'''
        self.speed += 5 
        return self.speed

    def stop(self):
        '''Останавливает автомобиль'''
        self.speed = 0 
        return self.speed


    def save_to_file(self, file_name):  
        '''метод сохранения объекта автомобиль из памяти в файл.'''
        with open(file_name, 'wb') as fs:
            pickle.dump(self, fs)


    @staticmethod
    def load_from_file(file_name): 
        '''метод загрузки автомобиля их файла в пямять.'''
        with open(file_name, 'rb') as fl:
            return pickle.load(fl)
       
        
