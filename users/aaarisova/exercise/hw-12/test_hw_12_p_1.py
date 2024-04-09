import pytest
from car import Car
from student import Student
from book import Book
# from shopping_cart import ShoppingCart


#1.Car

@pytest.mark.parametrize('model, year, color, doors, speed, expected_result',
                        [
        ('Toyota', '2020', 'black', '4', '150',('Toyota', '2020', 'black', '4', '150')),
        ('Honda', 2014, 'white', 5, 180, ('Honda', 2014, 'white', 5, 180)),
                        ]
                        )

def test_init_car_parametrize(model, year, color, doors, speed, expected_result):
    car = Car(model, year, color, doors, speed)
    assert car.model == expected_result[0]
    assert car.year == expected_result[1]
    assert car.color == expected_result[2]
    assert car.doors == expected_result[3]
    assert car.speed == expected_result[4]


def test_car_1(): #str нужно - негатив тест будет
    with pytest.raises(NameError): 
        car1 = Car(model = Lada, year = 1998, color = red, doors = 4, speed = 120)


def test_car_2(): #негатив - не хватает атрибута
    with pytest.raises(TypeError): 
        car2 = Car(model = 'BMW', year = 2024, color = 'gold', doors = 5) 


def test_get_car():
    car = Car('Toyota', 1999, 'orange', 4, 200)
    assert car.get_model() == 'Toyota'
    assert car.get_year() == 1999
    assert car.get_color() == 'orange'
    assert car.get_speed() == 200
    
    

#2.Student

def test_student_1():
    student_1 = Student('Peter', 'Smith', '23.0', 'M Street, Washington 20036', [5, 7, 10])
    assert student_1.name == 'Peter'
    assert student_1.surname == 'Smith'
    assert student_1.age == '23.0'
    assert student_1.address == 'M Street, Washington 20036'
    assert student_1.grades == [5, 7, 10]


def test_student_2():  #float и tuple
    student_2 = Student('Olga', 'Ivanova', 18.0, 'F.Street, Samara, 144987', (10,9,10))
    assert student_2.name == 'Olga'
    assert student_2.surname == 'Ivanova'
    assert student_2.age == 18.0
    assert student_2.address == 'F.Street, Samara, 144987'
    assert student_2.grades == (10,9,10)


#3.Book

book1 = Book('Ведьмак', 'А.Сапкоовский', 320, 'ACT')
book2 = Book('Лабиринт отражений', 'С.Лукьяненко', -470, 'Азбука')

def test_atributes():
    assert book2.title == 'Лабиринт отражений'
    assert book2.author == 'С.Лукьяненко'
    assert book2.pages == -470
    assert book2.publisher == 'Азбука'


def test_get_book1_title():
    assert book1.get_title() == 'Ведьмак'

    
def test_get_book1_author():
    assert book1.get_author() == 'А.Сапкоовский'


def test_get_book1_title():
    assert book1.get_pages() == 320


def test_get_book1_publisher():
    assert book1.get_publisher() == 'ACT'   


def test_set_book1_title():
    excepted_result = 'The Witcher'
    book1.set_title(excepted_result)
    assert excepted_result == book1.get_title()

    
def test_set_book1_author():
    excepted_result = 'Sapkowski Andrzej'
    book1.set_author(excepted_result)
    assert excepted_result == book1.get_author()


def test_set_book1_pages():
    excepted_result = 280
    book1.set_pages(excepted_result)
    assert excepted_result == book1.get_pages()
    

def test_set_book1_publisher():
    excepted_result = 'Orion'
    book1.set_publisher(excepted_result)
    assert excepted_result == book1.get_publisher()






# #4.ShoppingCart
# 'Тест - создание продукта'
# @pytest.mark.parametrize('name, price, expected_result',
#                         [
#                             ('sunglass', 50, ['sunglass', 50]),
                            
#                         ]):
# def test_product_initialization():
#     product1

    
# def test_add_shopping_cart():
    

# def test_remove_shopping_cart():
    

# def test_show_shopping_cart():
    

# def sum_shopping_cart():


# #5. Circle

# def test_initialization(self, radius, color):
#         self.__radius = int(radius)
#         self.__color = color


# def test_circle_area(self)


# def circle_perimeter(self)


# #6. Point
# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def calculate_distance(self, new_point):
#         d = sqrt((self.x — new_point.x)**2 + (self.y — new_point.y)**2)            
#         return d

# #7. Triangle
# class Triangle:

#     def __init__(self, l, a, b, c):
#         self.__length = l
#         self.a = int(a)
#         self.b = int(b)
#         self.c = int(c)


#     def triangle_perimeter(self):
#         p = self.a + self.b + self.c
#         return p

#     def triangle_angle(self):
#         if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
#             return 'Не треугольник'
#         elif a**2 == b**2 + c**2:
#             return 'прямоугольный'
#         elif a == b or a == c or b == c:
#             return 'равнобедренный'
#         elif a == b == c:
#             return 'равносторонний'
#         else:
#             return 'разносторонний'
    
# #8. BankAccount


# class BankAccount:

#     def __init__(self, account_number, holder_name, card_balance):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.card_balance = card_balance

    
#     def deposit_money(self, deposit):
#         if deposit > 0:
#             self.card_balance += deposit
#             return self.card_balance
#         else:
#             return 'Ошибка. Проверьте, что ваша сумма для внесения больше 0'
        

#     def withdraw_money(self, money):
#          if self.card_balance >= money:
#              self.card_balance -= money
#              return self.card_balance
#         else:
#             return 'Ошибка. Запрашиваемая сумма выше баланса на счету'
            
# #9. Date
    





















