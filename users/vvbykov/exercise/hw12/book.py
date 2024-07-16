
class Book:

    def __init__(self, title: str, author: str, pages: int, publisher: str):
        self._title = title
        self._author = author
        self._publisher = publisher
        if (type(pages) is int) and (pages > 0):
            self._pages = pages
        else:
            raise ValueError("Invalid pages value")

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    @property
    def publisher(self):
        return self._publisher

    @title.setter
    def title(self, value: str):
        if type(value) is str:
            self._title = value
        else:
            raise TypeError("Invalid type for the field 'title'")

    @author.setter
    def author(self, value: str):
        if type(value) is str:
            self._author = value
        else:
            raise TypeError("Invalid type for the field 'author'")

    @publisher.setter
    def publisher(self, value: str):
        if type(value) is str:
            self._publisher = value
        else:
            raise TypeError("Invalid type for the field 'publisher'")
    
    @pages.setter
    def pages(self, value: str):
        if (type(value) is int) and (value > 0):
            self._pages = value
        else:
            raise ValueError("Invalid pages value")
        
    
    
