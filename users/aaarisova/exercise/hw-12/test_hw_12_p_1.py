import pytest
from car import Car
from student import Student
from book import Book
from shopping_cart import ShoppingCart


#1.Car

def test_car_1():
    car1 = Car(model = 'Toyota', year = '2020', color = 'black', doors = '4', speed = '150')
    assert car1.new_car() == ('Toyota', '2020', 'black', '4', '150')  

def test_car_2():
    car2 = Car(model = 'Honda', year = 2014, color = 'white', doors = 5, speed = 180)
    assert car2.new_car() ==  ('Honda', 2014, 'white', 5, 180) #int

def test_car_3(): #str нужно - негатив тест будет
    with pytest.raises(NameError): 
        car3 = Car(model = Lada, year = 1998, color = red, doors = 4, speed = 120)


def test_car_4(): #негатив - не хватает атрибута
    with pytest.raises(TypeError): 
        car4 = Car(model = 'BMW', year = 2024, color = 'gold', doors = 5)
        car4.new_car() 


#2.Student

def test_student_1():
    student_1 = Student('Peter', 'Smith', '23.0', 'M Street, Washington 20036', [5, 7, 10])
    expected = ('Peter', 'Smith', '23.0', 'M Street, Washington 20036', [5, 7, 10])
    assert expected == student_1.new_student()


def test_student_2():  #float и tuple(кортеж) и вывел кортеж, а не список - негативный?
    student_2 = Student('Olga', 'Ivanova', 18.0, 'F.Street, Samara, 144987', (10,9,10))
    expected = ('Olga', 'Ivanova', 18.0, 'F.Street, Samara, 144987', (10,9,10))
    assert expected == student_2.new_student()


def test_student_3():  #возраст отрицат. в реальной жизни требуется дораьотка.нет имени и отрицат возраст
    student_3 = Student(None, 'Smith', -5, 'M Street, Washington 20036', [5,7,10])
    expected = (None, 'Smith', -5, 'M Street, Washington 20036', [5,7,10])
    assert expected == student_3.new_student()


def test_student_4():  ##в идеале не должен возраст=0, оценки как у меня, но у нас в функции нет ограничений, поэтому тест положит
    student_4 = Student('Vasia', 'Sidorov', 0, 'Lenina Street, N.Novgorod', [-5,0,5000])
    expected = ('Vasia', 'Sidorov', 0, 'Lenina Street, N.Novgorod', [-5,0,5000])
    assert expected == student_4.new_student()


#3.Book

def test_my_book_1():
    my_book_1 = Book('Ведьмак', 'А.Сапкоовский', 320, 'ACT')  
    expected = ('Ведьмак', 'А.Сапкоовский', 320, 'ACT')
    assert expected == my_book_1.my_book()


def test_my_book_2():       #отрицат число нельзя, но проходит. т к нет огранич в функц
    my_book_2 = Book('Лабиринт отражений', 'С.Лукьяненко', -470, 'Азбука') 
    expected = ('Лабиринт отражений', 'С.Лукьяненко', -470, 'Азбука')
    assert expected == my_book_2.my_book() 


def test_my_book_3():  # негативный. отсутствует 1 аргумент       
    with pytest.raises(TypeError):
        my_book_3 = Book('Сто лет одиночества', ' Г.Г.Маркес', 550)  
        my_book_3.my_book()


def test_my_book_4():  # негативный. нет кавычек у 1 стр аргумента       
    with pytest.raises(NameError):
        my_book_4 = Book(Камчатка, 'Фигерас Марсело', 400, 'Иностранка')  
        my_book_4.my_book() 
    

#4.ShoppingCart
'Тест - создание продукта'
@pytest.mark.parametrize('name, price, expected_result',
                        [
                            ('sunglass', 50, ['sunglass', 50]),
                            
                        ]):
def test_product_initialization():
    product1

    
def test_add_shopping_cart():
    

def test_remove_shopping_cart():
    

def test_show_shopping_cart():
    

def sum_shopping_cart():


#5. Circle

#6. Point
#7. Triangle
#8. BankAccount
#9. Date
    





















