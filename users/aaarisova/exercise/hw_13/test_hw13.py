import pytest
import pickle
from car_extended import Car
from student_extended import Student

from shape_circle import Circle
from shape_rectangle import Rectangle
from shape_triangle import Triangle


@pytest.fixture
def car():
    return Car("Toyota", 2024, "silver", 4, 40)


def test_load_car_1(car):  
    #with open("file_car.txt", "rb") as f:  #.txt или .pkl надо расширение? 
    #    loaded_car = pickle.load(f)       
    file_name = 'file_car.txt'
    loaded_car = Car.load_car(file_name)    
    assert loaded_car.get_model() == "Toyota"  #Проверка,что загруж-ые данные соотв-ют ожидаемым знач
    assert loaded_car.get_year() == 2024
    assert loaded_car.get_color() == "silver"
    assert loaded_car.doors == 4
    assert loaded_car.speed == 60 #после изменения скорости в тесте ниже на +10=60 стал тут 60 ожидать. после первого сохранения тесты проходят, после второго выдают ошибку и наоборот

'''1.3. Создайте тест который, загружает автомобиль с файла меняет скорость автомобиля и сохраняет автомобиль с новой соростью в файл'''
 
def test_change_speed_car_1(car):
    file_name = 'file_car.txt'
    car.speed  = 60  
    car.save_car(file_name)
    loaded_car = Car.load_car(file_name) 
    assert loaded_car.speed == 60
    

#################################################################
'''2. Расширьте класс Student, добавив методы сохранения и загрузки обекта студент из памяти в фаил и обратно. Создав тест который загружет студента из файла, добаляет новую оценку и сохраняет в фаил.'''

@pytest.fixture
def student():
    return Student('Ivan Vasilievich', 'Bunsha', 65, "Moscow", [5])

def test_new_grade(student): 
    file_name = 'file_student.txt' 
    student.save_students(file_name)
    student.load_students(file_name) 
    student.add_grade(3) 
    student.save_students(file_name) 
    update_student = Student.load_students(file_name) 
    assert update_student.grades == [5, 3]
    
#################################################################
'''Напишите тест который проходится по несколькьким фалйам, загружает из них фигуры и выводит их периметр и площадь'''

def test_shapes():
    triangle = Triangle(6, 6, 6)
    rectangle = Rectangle(4, 6)
    circle = Circle(3, 'red')
    triangle.save_shape('triangle.pkl')
    rectangle.save_shape('rectangle.pkl')
    circle.save_shape('circle.pkl')
    triangle.load_shape('triangle.pkl')
    rectangle.load_shape('rectangle.pkl')
    circle.load_shape('circle.pkl')
    assert (triangle.side1, triangle.side2, triangle.side3) == (6, 6, 6)
    assert (rectangle.width, rectangle.height) == (4, 6)
    assert (circle.radius, circle.color) == (3, 'red')

    assert (triangle.area(), triangle.perimeter()) == (15.59, 18)
    assert (rectangle.area(), rectangle.perimeter()) == (24, 20)
    assert (circle.area(), circle.perimeter()) == (28.27, 18.85)











