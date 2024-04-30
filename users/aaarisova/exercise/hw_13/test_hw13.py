import pytest
import pickle
from car_extended import Car
from student_extended import Student

#как получить фалы с расширением pickle?

@pytest.fixture
def car():
    return Car("Toyota", 2024, "silver", 4, 40)
    
def test_save_car_1(car):  #Если писать сначала тест, то надо with open.... 
    #with open("file_car.txt", "wb") as f:
    #    pickle.dump(car, f)  
    file_name = 'file_car.txt'
    assert car.save_car(file_name) == file_name   

def test_load_car_1(car):  
    #with open("file_car.txt", "rb") as f:
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
    car.speed  = 60  #или надо менять от acceleration(),где +5км/ч к первонач скорости?
    car.save_car(file_name)
    loaded_car = Car.load_car(file_name) 
    assert loaded_car.speed == 60
    

# ################################################################
# '''2. Расширьте класс Student, добавив методы сохранения и загрузки обекта студент из памяти в фаил и обратно. Создав тест который загружет студента из файла, добаляет новую оценку и сохраняет в фаил.'''

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
    



