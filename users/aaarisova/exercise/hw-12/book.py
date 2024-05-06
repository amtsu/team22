'''3.Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора, количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.'''

class Book():

    def __init__(self, title, author, pages, publisher):
        self.title = title
        self.author = author
        self.pages = pages
        self.publisher = publisher


    def set_title(self, title):
        self.title = title


    def set_author(self,author):
        self.author = author


    def set_pages(self,pages):
        self.pages = pages


    def set_publisher(self,publisher):
        self.publisher = publisher


    def get_title(self):
        return self.title


    def get_author(self):
        return self.author


    def get_pages(self):
        return self.pages


    def get_publisher(self):
        return self.publisher









############################ 
# #не поднимает ошибку с отрицат значением страниц в тесте:
# class Book():
    
#     def __init__(self, title, author, pages, publisher):
#         self.__book_title = title
#         self.__author = author
#         self.__pages = pages
#         self.__publisher = publisher

    
#     @property   
#     def title(self):
#         '''Декоратор @property создает метод получения атрибутов, который представляет собой свойство класса.'''
#         return self.__book_title 

#     @title.setter
#     def title(self,title):  
#         '''Метод setter устанавливает значение атрибута класса, который можно изменить извне класса.'''
#         self.__book_title = title

#     @property 
#     def author(self):
#         return self.__author

#     @author.setter
#     def author(self,author):
#         self.__author = author
        
#     @property    
#     def pages(self):
#         return self.__pages

#     @pages.setter
#     def pages(self, pages):
#         if isinstance(pages, int) and pages > 0:
#             self.__pages = pages
#         else:
#             raise ValueError('Количество страниц должно быть целым числом больше 0.')
    
#     @property   
#     def publisher(self):
#         return self.__publisher
        
#     @publisher.setter
#     def publisher(self, publisher):
#         self.__publisher = publisher

   