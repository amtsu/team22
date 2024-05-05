class Book:
    def __init__(self, name, author, number_pages, publishing):
        self.name = name
        self.author = author
        self.number_pages = number_pages
        self.publishing = publishing

    def Getname(self):
        return self.name
    def Getauthor(self):
        return self.author
    def Getnumber_pages(self):
        return self.number_pages
    def Getpublishing(self):
        return self.publishing