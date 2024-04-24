# Ruslan Yusupov
# дан список книг, у книги есть название, автор количество страниц
# список дан в виде таплов [(назв, автор, кол-во страниц)]
# посчитать общее количество страниц у всех книг и среднее количество, сделать тесты
# cделать объект книга, сделать тесты

books = [('book1', 'author1', 111), ('book2', 'author2', 222), ('book3', 'author3', 333)];

def total_pages(books):
    return sum([book[2] for book in books])

def avg_pages(books):
    if len(books) == 0:
        return 0

    return total_pages(books) / len(books)


def test_total_pages():
    books = [('book1', 'author1', 111), ('book2', 'author2', 222), ('book3', 'author3', 333)];
    assert total_pages(books) == 666


def test_avg_pages():
    books = [('book1', 'author1', 111), ('book2', 'author2', 222), ('book3', 'author3', 333)];
    assert avg_pages(books) == 222


test_total_pages()
test_avg_pages()

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

books2 = [Book('book1', 'author1', 111), Book('book2', 'author2', 222), Book('book3', 'author3', 333)]

def total_pages2(books):
    return sum([book.pages for book in books])


def avg_pages2(books):
    if len(books) == 0:
        return 0

    return total_pages2(books) / len(books)


def test_total_pages2():
    books2 = [Book('book1', 'author1', 111), Book('book2', 'author2', 222), Book('book3', 'author3', 333)]
    assert total_pages2(books2) == 666


def test_avg_pages2():
    books2 = [Book('book1', 'author1', 111), Book('book2', 'author2', 222), Book('book3', 'author3', 333)]
    assert avg_pages2(books2) == 222

test_total_pages2()
test_avg_pages2()

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def total_pages(self):
        return sum([book.pages for book in self.books])

    def avg_pages(self):
        if len(books) == 0:
            return 0

        return self.total_pages() / len(books)


def test_library():
    library = Library()
    library.add_book(Book('book1', 'author1', 111))
    library.add_book(Book('book2', 'author2', 222))
    library.add_book(Book('book2', 'author2', 333))
    assert library.total_pages() == 666
    assert library.avg_pages() == 222


def test_empty_library():
    library = Library()
    assert library.total_pages() == 0
    assert library.avg_pages() == 0

test_library()
test_empty_library()
    
#Andrey Ivanchenko
#дан список книг, название, автор, количестов страниц
#нужно посчитать общее кол-во страниц у этих книг
#среднее кол-во страниц
#тесты
list_books = [['The old man and sea', 'Hemingway', 134], ['For whom the bell tolls', 'Hemingway', 112], ['White fang', 'Jack London', 140]]

def total_pages(books):
    total = 0
    for i in books:
        total += i[2]
    return total
    
def mean_pages(books):
    total = 0
    for i in books:
        total += i[2]
    av = total/len(books)
    return av

def test_total_pages():
    list_books = [['The old man and sea', 'Hemingway', 134], ['For whom the bell tolls', 'Hemingway', 113], ['White fang', 'Jack London', 140]]
    assert total_pages(list_books) == 387
test_total_pages()

def test_mean_pages():
    list_books = [['The old man and sea', 'Hemingway', 134], ['For whom the bell tolls', 'Hemingway', 112], ['White fang', 'Jack London', 140]]
    assert mean_pages(list_books) == 129
test_total_pages()
class Library:
    def __init__(self, books_list):
        self.books_list = []
    
    def total_pages(self):
        





# Vera Tarasova

#дан список книг, название, автор, количестов страниц
books = [['Name1','Author1',100],['Name2','Author2',200],['Name3','Author3',300]]
def sum_pages(books):
    sum = 0
    for i in range(len(books)):
        a = books[i]
        sum += books[i][2]
    return sum, sum/len(books)


def test_sum_pages():
    books = [['Name1','Author1',100],['Name2','Author2',200],['Name3','Author3',300]]
    assert sum_pages(books) == 600, 200.0

class Books:
   
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    
    def 




#Lotsmanov
#книга автор название количество страниц 
#посчитать количество страниц во всех книгах
#сделать объект книга
#cсреднее количество страниц
class Books():
    '''Класс книг
    '''
    def __init__(
        self,
        name,
        author,
        count
    ):
        self.name = name
        self.author = author
        self.count = count
    
    books = []
    

    def sum_pages():
        sum = 0
        for book in Books:
            sum += book.count
        return sum

    def count_books():
        count = 0
        for book in Books:
            count += 1
        return count
        
    def average_pages():
        average = Books.sum_pages() / Books.count_books()

library = [
    ('name1', 'author1', 123),
    ('name2', 'author2', 344),
    ('name3', 'author3', 13),
    ('name4', 'author4', 73)
]

for book in library:
    Books(book[0], book[1], book[2])

def sum_pages(spisok):
    sum = 0
    for book in spisok:
        sum += book[2]
    return sum
def average_pages(library, sum_pages):
    average = sum_pages(library) / len(library)
    return average


print(sum_pages(library))
print(average_pages(library, sum_pages))









#Maksimovkons
#посчитать общее кол-во страниц во всех книгах
#среднее
#сделать объект "книга"
#название: автор: кол-во

Books = [["a","a",1], ["b", "b", 2]]
    
def all_pages(Books):
    sum = 0
    for book in Books:
        sum = sum + book[2]
    return sum
            
def ave_pages(Books):
    sum = 0
    for book in Books:
        sum = sum + book[2]
    return sum = len(Books)




    



class Books:
    def __init__(self, name, author, pagenum):
        self.name = name
        self.author = author
        self.pagenum = pagenum
        

    def all_pages():
        sum = 0
        for book in Books:
            sum = sum + book.pagenum
        return sum
            
    def ave_pages():
        sum = 0
        for book in Books:
            sum = sum + book.pagenum
        return sum = len(Books)


class Book_set:
    def __init__(self)


##### Матросова Ирина >>>>>>>>>>>>>
Есть список: книга, название, страница.
Написать методы:
1) Сколько всего страниц во всех книгах?
2) Вернуть среднее кол-во страниц во всех книгах

написать на это всё тесты


class TaskBook():
    def __init__(self):
        self.sum_number_pages = 0
        self.average_number_book = 0
        self.sum_number_page = 0
        self.spisok_book = []

    def set_book(self, masiv):
        self.spisok_book.append(masiv)

    def out_book(self):
        for spisok in self.spisok_book:
            print (spisok)

    def SumNumberPages(self):
        for spisok in self.spisok_book:
            self.sum_number_pages += spisok[2]
        return self.sum_number_pages

    def AverageNumberPages(self):
        for spisok in self.spisok_book:
            self.sum_number_pages += spisok[2]
            self.average_number_book += 1
        self.average_number_boo = self.sum_number_pages/self.average_number_book
        return self.average_number_boo
      
#создала объект
objectMyTaskBook = TaskBook()
objectMyTaskBook.set_book(["книга1","автор1", 100])
objectMyTaskBook.set_book(["книга2","автор2", 200])
objectMyTaskBook.set_book(["книга3","автор3", 300])

objectMyTaskBook.out_book()
'''
['книга1', 'автор1', 100]
['книга2', 'автор2', 200]
['книга3', 'автор3', 300]
'''
print(objectMyTaskBook.SumNumberPages())
#600
print(objectMyTaskBook.AverageNumberPages())
#400.0

#тест на 1 метод
def test_SumNumberPages_1():
    input = TaskBook()
    input.set_book(["книга1","автор1", 100])
    input.set_book(["книга2","автор2", 750])
    expected = 850
    assert input.SumNumberPages() == expected, 'неправильно суммировали страницы книг'

test_SumNumberPages_1()

#тест на 2 метод
def test_AverageNumberPages_1():
    input = TaskBook()
    input.set_book(["книга1","автор1", 80])
    input.set_book(["книга2","автор2", 800])
    expected = 440
    assert input.AverageNumberPages() == expected, 'неправильно нашли среднее арифм страниц книг'

test_AverageNumberPages_1()


##### Матросова Ирина <<<<<<<<<<<<<









bookshelf = [
            {'name': "es':450},
            {'name': "Незнайка", 'author': "Носов", 'numpages':450}
            {'name': "Тканб космоса", 'author': "Брайан Грин", 'numpages':450},
            {'name': "Тканб космоса", 'author': "Брайан Грин", 'numpages':450}]х


# Danila Timopheev
#дан список книг, название, автор, кол-во страниц. посчитать общее кол-во страниц в книгах. 
#второе - среднее кол-во страниц
#третье - объект
books1 = [('книга первая', 'пушкин', 100), ('книга вторая', 'азбука', 50)]

class Booklist:
    def __init__ (self, books):
        self.books = books 
   
    def amount_of_pages(self):
        sum = 0
        for i in self.books:
            sum += i[2]
        return sum

    def avg_pages(self):
        sum = 0
        for i in self.books:
            sum += i[2]
        return sum / len(self.books)

def test_amount_of_pages():
        books1 = [('книга первая', 'пушкин', 100), ('книга вторая', 'азбука', 50)]
        expected = 150
        assert amount_of_pages(books1) == expected
    
def test_avg_pages():
        books1 = [('книга первая', 'пушкин', 100), ('книга вторая', 'азбука', 50)]
        expected = 75
        assert avg_pages(books1) == expected











###
Костя
class Book:
    def __init__(self, name, author, num_pages):
        self.name = name
        self.author = author
        self.num_pages = num_pages
        
    def total_pages(self, books):
        total = 0
        for item in books:
            total += item.self.num_pages
            
        return total
        
    def median_pages(self, books):
        return total_pages(books)/len(books)
        
        

voyna_i_mir = Book('Война и мир', 'Tolstoy', 1500)
bukvar = Book('Букварь', 'просвещение', 100)

book_list = [voyna_i_mir, bukvar]

    def test_total_pages():
        expected = 1650
        assert expected = total_pages(book_list)
        
    def test_median_pages():
        expected = 825
        assert expected = median_pages(book_list)





#########
#Регина
ddde





# Мария Андреева
# Список книг , книга название, автор, кол-во страниц
# мет общ. кол-во во всех книгах
# метод считает среднее кол-во страниц в книгах
# сделать объект книга, написать тесты проверки методов 
class Book():
    def __init__(self, name, author, count_pages):
        self.name = name
        self.count_pages = count_pages
        
    def count_page(self):
        return self.count_pages
    

class Library:
    
    def __init__(self, books_list):
        self.__book_list = books_list
        self.__workers = []
        
        
    def count_pages(self):
        pages = []
        for book in self.__book_list:
            pages.append(book.count_page())
        sum_pages = sum(pages)
        print(sum_pages)
        return sum_pages
    
    def count_avg_pages(self):
        avg_pages = self.count_pages()/len(self.__book_list)
        return avg_pages
    
    
def test_count_pages():
    new_library = Library(Book( "War and peace", "Tolstoy",  3000), Book( "Idiot", "Dostoevskiy",  800)])
    count_p = new_library.count_pages()
    assert count_p == 3800
    

class Library:
    
    def __init__(self, books_list):
        self.__book_list = books_list
        
    def count_pages(self):
        pages = []
        for book in self.__book_list:
            pages.append(book["pages"])
        sum_pages = sum(pages)
        print(sum_pages)
        return sum_pages
    
    def count_avg_pages(self):
        avg_pages = self.count_pages()/len(self.__book_list)
        return avg_pages
        
def test_count_pages():
    new_library = Library([{"name": "War and peace","author": "Tolstoy", "pages": 3000}, {"name": "Idiot","author": "Dostoevskiy", "pages": 800}])
    count_p = new_library.count_pages()
    assert count_p == 3800
    
test_count_pages()
    
def test_count_avg_pages():
    new_library = Library([{"name": "War and peace","author": "Tolstoy", "pages": 3000}, {"name": "Idiot","author": "Dostoevskiy", "pages": 800}])
    count_p = new_library.count_avg_pages()
    assert count_p == 1900

test_count_avg_pages()

# Roman Tarasov

# Дан списорк книг. есть название, автор колво страниц. общее страниц, среднее страниц.

class Books:
    def __init__(self, name, autor, count):
        self.name = name
        self.autor = autor
        self.count = count
        


book1 = Books('HP', 'JR', 330)
book2 = Books('COC', 'HP', 250)
book3 = Books('PPP', 'HOP', 110)

def count(*pages):
    
    return sum(pages)
    
count(book1.count, book2.count, book3.count)

def test_count():
    input1 = 330 
    input2 = 250
    input3 = 110
    expected = 690
    assert expected == count(input1, input2, input3)

test_count()


# ANTON_KUVALDA_START_____________________________

books_list = [['W and P', 'Tolstoy', 70], ['Lukomorie', 'Pushkin', 234], ['Dead souls_2', 'Gogol', 250]]

#print (books_list[0][2])
              
def sheets_quantity (some_list):
    x = 0
    for a in some_list:
        x = x + a[2]
    #print (x)
    return x
                  
print (sheets_quantity (books_list))

def average_sheets_quantity (some_list):
    ave = sheets_quantity ((books_list)) / (len (books_list))
    return ave
    
print (average_sheets_quantity (books_list))

#TEST

def test_sheets_quantity ():
    assert sheets_quantity (books_list) == 554

test_sheets_quantity ()


def test_average_sheets_quantity ():
    assert average_sheets_quantity (books_list) == 184.66666666666666
    
test_average_sheets_quantity ()

              
# ANTON_KUVALDA_END________________







какой