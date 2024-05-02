##### Матросова Ирина >>>>>>>>>>>>>
'''
Есть список: книга, название, страница.
Написать методы:
1) Сколько всего страниц во всех книгах?
2) Вернуть среднее кол-во страниц во всех книгах

написать на это всё тесты
'''

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

#стилистика
def test_SumNumberPages_2():
    input = (["книга1","автор1", 100],["книга2","автор2", 750],)
    expected = 850
    library = TaskBook()
    for book in input:
         library.set_book(book)
    assert library.SumNumberPages() == expected, 'неправильно суммировали страницы книг'

test_SumNumberPages_2()

#тест на 2 метод
def test_AverageNumberPages_1():
    input = TaskBook()
    input.set_book(["книга1","автор1", 80])
    input.set_book(["книга2","автор2", 800])
    expected = 440
    assert input.AverageNumberPages() == expected, 'неправильно нашли среднее арифм страниц книг'

##### Матросова Ирина <<<<<<<<<<<<<