"""Создать классы книга и библиотека.
Добавить в библиотеку методы: добавления книг в библиоеку, подсчета всех страниц в бибилиотеке, среднего количества страниц.
Расширить класс библиотека: добавить метод поиска книг по жанру, автору и названию.
Создать класс User. Добавить методы учета выдачи книг пользователю(не больше 5 книг в руки), метод возврата книг в библиотеку, метод удаления книг из библиотеки если книги взяли.
Написать тесты."""
class Book():
    
    def __init__(self, title, author, genre, count_pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.count_pages = count_pages

    def __str__(self):
        return f"{self.title} / {self.author} / {self.genre}"

class User():

    def __init__(self, name):
        self.name = name
        self.users_basket = []

    def count_books_for_user(self):
        """возвращает количество книг в корзине"""
        if len(self.users_basket) == 0:
            return None
        else:
            return len(self.users_basket)
        

    def add_books_for_user(self, book: Book):
        """беру книги для чтения"""
        if len(self.users_basket) == 5:
            raise ValueError(f"Ошибка! Нельзя брать больше 5 книг.")
        self.users_basket.append(book)
        
           
    def return_book_in_library(self, book: Book):
        """метод возврата книги в библтотеку"""
        if book not in self.users_basket:
            raise ValueError(f"Ошибка, у пользователя нет такой книги.")
        self.users_basket.remove(book)

class Library():
    
    def __init__(self):
        self.library_list = []

    def find_book(self, title, author, genre):
        """поиск по названию автору и жанру"""
        find_book = []
        for book in self.library_list:
            if title == book.title:
                find_book.append(book)
            elif author == book.author:
                find_book.append(book)
            elif genre == book.genre:
                find_book.append(book)
        return find_book
    

    def add_book(self, book: Book):
        """добавление книги в библиотетку"""
        self.library_list.append(book)
        
    def total_pages_in_library(self):
        """сумма всех страниц в библиотеке"""
        sum = 0
        for book in self.library_list:
            sum += book.count_pages
        return sum

    def avg_pages_in_library(self):
        """среднее количество страниц в библиотеке"""
        for book in self.library_list:
            avg = self.total_pages_in_library() / len(self.library_list)
        return avg
        
    def count_book_in_library(self):
        """количество книг в библиотеке"""
        return len(self.library_list)

    def give_book(self, book: Book, user: User):
        """метод выдачи книги пользователю и удаления ее из библиотеки"""
        if book not in self.library_list:
            raise ValueError(f"Ошибка! Такой книги нет в библиотеке.")
        user.add_books_for_user(book)
        self.library_list.remove(book)

    def take_book(self, user: User, book: Book):
        """метод забирает книгу у пользователя и возвращает в библиотеку"""
        user.return_book_in_library(book)
        self.library_list.append(book)

