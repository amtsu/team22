"""
Создайте класс Car, который представляет автомобиль. У него должны быть атрибуты для хранения модели, года выпуска, цвета, количества дверей и текущей скорости. Добавьте методы которые возвращают год, марку, цвет и текущую скорость автомобиля.
"""
class Car:
    
    def __init__(self, model, year, color, doors, speed):
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.speed = speed
    
    def get_year(self):
        return self.year

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_speed(self):
        return self.speed

# Пример использования класса
car1 = Car("Toyota Camry", 2022, "black", 4, 180)

# Получаем информацию о модели, годе выпуска, цвете и скорости автомобиля
print("Модель автомобиля:", car1.get_model())
print("Год выпуска автомобиля:", car1.get_year())
print("Цвет автомобиля:", car1.get_color())
print("Максимальная скорость автомобиля:", car1.get_speed(), "км/ч")

# Создаем новый объект автомобиля
car2 = Car("Tesla Model S", 2023, "red", 4, 250)

# Получаем информацию о новом автомобиле
print("\nМодель автомобиля:", car2.get_model())
print("Год выпуска автомобиля:", car2.get_year())
print("Цвет автомобиля:", car2.get_color())
print("Максимальная скорость автомобиля:", car2.get_speed(), "км/ч")

"""
Создайте класс Student, который представляет студент. У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок
"""
class Student:
    
    def __init__(self, name, surname, age, address, rates):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.rates = rates

# Пример использования класса
student1 = Student("Иван", "Иванов", 20, "ул. Пушкина, д. 10", [4, 5, 3, 4, 5])

# Получаем информацию о студенте
print("ФИО студента:", student1.get_full_name())
print("Возраст студента:", student1.get_age())
print("Адрес студента:", student1.get_address())
print("Средний балл студента:", student1.get_average_rate())

"""
Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора, количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.
"""
class Book:

    def __init__(self, title, author, pages, publisher):
        self.title = title
        self.author = author
        self.pages = pages
        self.publisher = publisher

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_pages(self, pages):
        self.pages = pages

    def get_pages(self):
        return self.pages

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

# Пример использования класса
book1 = Book("1984", "George Orwell", 328, "Penguin Books")

# Получаем информацию о книге
print("Название книги:", book1.get_title())
print("Автор книги:", book1.get_author())
print("Количество страниц:", book1.get_pages())
print("Издательство:", book1.get_publisher())

# Изменяем издательство книги
book1.set_publisher("Random House")

# Повторно получаем информацию о книге
print("\nИзмененное издательство:", book1.get_publisher())

'''
Создайте класс ShoppingCart, который представляет корзину покупок. У него должен быть атрибут для хранения списка товаров. Добавьте методы для добавления, удаления, отображения товаров в корзине и вычиcления стоимости всей корзины.
'''
class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, price):
        self.products[product] = price

    def del_product(self, product):
        if product in self.products:
            del self.products[product]
        else:
            print(f"{product} не найден в корзине.")

    def show_products(self):
        if self.products:
            for product, price in self.products.items():
                print(f"{product}: {price}")
        else:
            print("Корзина пуста.")

    def calculate_total(self):
        total = sum(self.products.values())
        return total

# Пример использования класса
cart = ShoppingCart()
cart.add_product("apple", 2.99)
cart.add_product("banana", 1.99)
cart.add_product("orange", 3.49)

cart.show_products()
print("Общая стоимость корзины:", cart.calculate_total())

cart.del_product("banana")

cart.show_products()
print("Общая стоимость корзины:", cart.calculate_total())


'''
Создайте класс Circle, который представляет круг. У него должен быть атрибут для хранения радиуса и цвета. Добавьте методы для вычисления площади и периметра круга.
'''
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def square(self):
        square = 3.14*(self.radius)**2
        return square
    
    def perimeter(self):
        perimeter = 3.14*self.radius*2
        return perimeter

# Пример использования класса
circle1 = Circle(5, "blue")

# Вычисляем площадь и периметр круга
print("Площадь круга:", circle1.square())
print("Периметр круга:", circle1.perimeter())

# Изменяем радиус круга
circle1.radius = 7

# Повторно вычисляем площадь и периметр круга
print("Площадь круга (после изменения радиуса):", circle1.square())
print("Периметр круга (после изменения радиуса):", circle1.perimeter())

'''
Создайте класс Point, который представляет точку в двумерном пространстве. У него должны быть атрибуты для хранения координат x и y. Добавьте методы для вычисления расстояния между двумя точками.
'''
import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance

# Пример использования класса
point1 = Point(3, 4)
point2 = Point(6, 8)

distance = point1.distance_to(point2)
print("Расстояние между точками:", distance)

'''
Создайте класс Triangle, который представляет треугольник. У него должны быть атрибуты длины сторон. Добавьте методы для вычисления перимера треугольника и методы вычисления типа треугольника ( равностороннйи, павнобедренный, прямоуголный или разносторонний).
'''
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Равнобедренный"
        elif self.side1**2 == self.side2**2 + self.side3**2 or self.side2**2 == self.side1**2 + self.side3**2 or self.side3**2 == self.side1**2 + self.side2**2:
            return "Прямоугольный"
        else:
            return "Разносторонний"

# Пример использования класса
triangle1 = Triangle(3, 4, 5)
print("Периметр треугольника:", triangle1.perimeter())
print("Тип треугольника:", triangle1.triangle_type())

triangle2 = Triangle(5, 5, 5)
print("Периметр треугольника:", triangle2.perimeter())
print("Тип треугольника:", triangle2.triangle_type())

triangle3 = Triangle(4, 4, 6)
print("Периметр треугольника:", triangle3.perimeter())
print("Тип треугольника:", triangle3.triangle_type())


'''
Создайте класс BankAccount, который представляет банковский счет. У него должны быть атрибуты для хранения номера счета, имени владельца и баланса. Добавьте методы для внесения и снятия денег со счета.
'''

class BankAccount:
    def __init__(self, number, owner_name, balance):
        self.number = number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Сумма {amount} успешно зачислена на счет.")
        else:
            print("Неверная сумма для зачисления.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Сумма {amount} успешно снята со счета.")
        else:
            print("Недостаточно средств на счете или неверная сумма для снятия.")

    def get_balance(self):
        return self.balance

# Пример использования класса
account1 = BankAccount("123456789", "Иванов Иван", 1000)

print("Текущий баланс:", account1.get_balance())

account1.deposit(500)
print("Текущий баланс после зачисления:", account1.get_balance())

account1.withdraw(200)
print("Текущий баланс после снятия:", account1.get_balance())

account1.withdraw(1500)

'''
Создайте класс Date, который представляет дату. У него должны быть атрибуты для хранения дня, месяца и года. Добавьте методы для сравнения двух дат и вычисления разницы между ними.
'''
class Date:
    def __init__(self, date):
        self.dd = date[0:2]
        self.mm = date[2:4]
        self.mm = date[4:6]
#    def date_print(self):
 #       print(self.dd)
    def date_compare(self, )
    
    





    