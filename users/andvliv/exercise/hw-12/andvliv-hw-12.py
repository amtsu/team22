#Создайте класс Car, который представляет автомобиль. У него должны быть атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости. Добавьте методы которые возвращают год, марку, цвет и текущую скорость автомобиля.

class Car:
    def __init__(self, model, year, color, doors, current_speed):
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.current_speed = current_speed

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_doors(self):
        return self.doors

    def get_current_speed(self):
        return self.current_speed

#проверяем, правильно ли создан класс на примере:
car1 = Car(model='Toyota', year=2000, color='blue', doors=4, current_speed=0)
car2 = Car('Ford', 2005, 'black', 4, 0)


#Создайте класс Student, который представляет студент. У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.
class Student:
    def __init__(self, name, surname, age, adress, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.adress = adress
        self.marks = marks


#Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора, количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.
class Book:
    def __init__(self, name, author, pages, publishers):
        self.name = name
        self.author = author
        self.pages = pages
        self.publishers = publishers

    def set_name(self, name): #добавляем методы установки и получения аттрибутов
        self.name = name
    def get_name(self):
        return self.name

    def set_author(self, author):
        self.author = author
    def get_author(self):
        return self.author

    def set_pages(self, pages):
        if pages is int and pages > 0:
            self.pages = pages
        else:
            print("Wrong attribute, must be at least 1 page")
    def get_pages(self):
            return self.pages
        
    def set_publishers(self, publishers):
        self.publishers = publishers
    def get_publishers(self):
        return self.publishers
        
#Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров. Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиckbnt стоимости всей корзины.
class ShoppingCart:
    def __init__(self, list_of_purchases):
        self.list_of_purchases = {}
        
    def add_purchases(self, key, value):
        if key not in self.list_of_purchases:
            self.list_of_purchases[key] = value
        elif key in self.list_of_purchases:
            self.list_of_purchases[key] += value
        return self.list_of_purchases
    
    def del_purchases(self, key, value):
        if item in self.list_of_purchases:
            del self.list_of_purchases[key]
        else:
            print(f"No {item} in list of purchases")
        return self.list_of_purchases

    def show_purchases(self):  
        return self.list_of_purchases

    def sum_of_purchases(self):
        sum = 0
        for i in self.list_of_purchases.values():
            sum += i[0] * i[1]
        return sum

#Создадим объект данного класса
cart1 = ShoppingCart({})
cart2 = ShoppingCart({'apple': (3, 4), 'meat': (1, 6)})


#Создайте класс Circle, который представляет круг. У него должен быть атрибут для хранения радиуса и цвета. Добавьте методы для вычисления площади и периметра круга.
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)
        
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

#Создадим объект класса Circle
circle1 = Circle(3, 'white')
circle2 = Circle(5, 'black')

#Создайте класс Point, который представляет точку в двумерном пространстве. У него должны быть атрибуты для хранения координат x и y. Добавьте методы для вычисления расстояния между двумя точками.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def calculate_distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

#создадим объекты данного класса
point1 = Point(2, 6)
point2 = Point(6, 9)

#!!!!!!
#Создайте класс Triangle, который представляет треугольник. У него должны быть атрибуты длины сторон. Добавьте методы для вычисления перимера треугольника и методы вычисления типа треугольника ( равностороннйи, павнобедренный, прямоуголный или разносторонний).

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def calculate_perimeter(self):
        if (self.a + self.b) > self.c and (a.self + c.self) > self.b and (b.self + c.self) > self.a:
            return self.a + self.b + self.c
        else:
            return 'not triangle'
        
    def triangle_type(self):
        sides = [a, b, c]
        sides = sorted(sides)
        if (sides[0] == sides[1]) and (sides[1] == sides[2]) and (sides[0] == sides[2]) and ((sides[0] + sides[1] > sides[2])):
            return 'equilateral'
        elif (sides[0] == sides[1] or sides[0] == sides[2] or sides[2] == sides[1]) and ((sides[0] + sides[1] > sides[2])):
            retturn 'equicrural'
        elif ((sides[0] ** 2 + sides[1] ** 2) == sides[2] ** 2) and ((sides[0] + sides[1] > sides[2])):
            return 'right'
        elif (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[2] != sides[1]) and ((sides[0] + sides[1] > sides[2])):
            return 'scalene'

#Сооздадим несколько объектов данного класса
triangle1 = Triangle(3, 3, 3)
triangle2 = Triangle(3, 3, 4)
triangle3 = Triangle(4, 5, 3)
triangle4 = Triangle(6, 7, 8)

#Создайте класс BankAccount, который представляет банковский счет. У него должны быть атрибуты для хранения номера счета, имени владельца и баланса. Добавьте методы для внесения и снятия денег со счета.

class BankAccount:
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance

    def deposit_money(self, x):
        return self.balance + x

    def withdrawal_money(self, x):
        return self.balance - x

#Создадим объект данного класса
bank_acc1 = BankAccount(123456, 'Andrey Ivanchenko', 500)

#Создайте класс Date, который представляет дату. У него должны быть атрибуты для хранения дня, месяца и года. Добавьте методы для сравнения двух дат и вычисления разницы между ними.
from datetime import datetime
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.__date = datetime(year, month, day)

    def compare(self, other_date):
        diff = self.date - other_date.date
        return diff.days

#Создадим объект данного класса
date1 = Date(1998, 5, 15)
date2 = Date(2000, 4, 16)

    
        
        
