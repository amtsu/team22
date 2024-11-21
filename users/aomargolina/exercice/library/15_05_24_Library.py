class Book:
    def __init__(self, name, author, pages, genre):
        self.name = name
        self.author = author
        self.pages = pages
        self.genre = genre

class User:
    def __init__(self, name: str):
        self.name = name
        self.user_books: list[Book] = []

    def take_book(self, book: Book):
        if len(self.user_books) >= 5:
            raise ValueError(f'Ошибка! Невозможно добавить книгу. У пользователя {self.name} уже максимальное количество книг книг!')
        self.user_books.append(book)
        
     def retun_book(self, book: Book):
         if book not in self.user_books:
             raise ValueError(f'Ошибка! Такой книги у пользователя {self.name} такой книнги нет')
         self.user_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.books_on_hand = []

    def total_book(self):
        return len(self.books)

    def avg_pages(self):
        all_pages = []
        for book in self.books:
            all_pages.append(book.pages) 
        avg_pages = sum(all_pages) / self.total_book()
        return avg_pages
    
    #def add_book(self, book):
        #self.books.append(book)
    # по красоте - дописать метод remove

    def search_book(self, request: str) -> tuple[tuple]:
        """функция поиска книг"""
    request = request.lower().strip()
    name_list = []
    author_list = []
    genre_list = []
    for book in self.books:
        if request in book.name.lower():
            name_list.append(book)
        if request in book.author.lower():
            author_list.append(book)
        if request in book.genre.lower():
            genre_list.append(book)
    if len(name_list) == 0 and len(author_list) == 0 and len(genre_list) == 0:
        raise ValueError(f'По вашему запросу "{requst}" ничего не найдено!')
    return (tuple(name_list), tuple(author_list), tuple(genre_list))

    
    def give_book(self, user: User, book: Book): 
        """метод выдачи книги из библиотеки пользователю"""
        if book not in self.books:
            raise ValueError(f'Ошибка! Такой книги {book.name} нет в библиотеке')
        user.take_book(book)
        self.books.remove(book)
        self.books_on_hand.append((user, book))

    def give_back_book(self, user: User, book: Book):
        """метод забирает книгу у пользователя и возвращает в библиотеку"""
        user.return_book(book)
        self.books.append(book)
        self.books_on_hand.remove((user, book))
