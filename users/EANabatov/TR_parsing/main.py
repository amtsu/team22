import time

from bs4 import BeautifulSoup
import urllib.request


class BookStoreParser:
    def __init__(self):
        self.__books = []
        self.__parsing()

    def __parsing(self):
        __cw = 0
        for index in range(1156290, 1156291):
            __summary = {}
            # time.sleep(1)
            try:
                page = urllib.request.urlopen("https://www.moscowbooks.ru/book/" + str(index) + "/")
                text = page.read()
                soup = BeautifulSoup(text, features="html.parser")
                if page.getcode() == 200:
                    try:
                        __summary["book_name"] = self.__book_name()
                    except:
                        print("book_name not gound")
                    try:
                        __summary["author_name"] = self.__author_name()
                    except:
                        print("book_name not gound")
                    try:
                        __summary["shop_price"] = self.__shop_price()
                    except:
                        print("book_name not gound")
                    try:
                        __summary["internet_price"] = self.__internet_price()
                    except:
                        print("book_name not gound")
                    try:
                        __summary["the_year_of_publishing"] = self.__year_of_publishing()
                    except:
                        print("book_name not gound")
                    try:
                        __summary["publisher"] = self.__publisher()
                    except:
                        print("book_name not gound")
                    try:
                    __summary["link"] = self.__link()
                    except:
                        print("book_name not gound")
                    try:
                        __summary["pages"] = self.__pages()
                    except:
                        print("book_name not gound")
                    try:
                        __summary["product_code"] = self.__product_code()
                    except:
                        print("book_name not gound")
                    try:
                        __summary["vendor_code"] = self.__vendor_code()
                    except:
                        print("book_name not gound")
                    try:
                        __summary["isbn"] = self.__isbn()
                    except:
                        print("book_name not gound")
                else:
                    print(page.getcode())
            except:
                print(index, "skiped.", "Download: ", __cw)
            if __summary != {}:
                self.__books.append(__summary)
                __cw = __cw + 1
                print(__cw)

    def return_books(self):
        print(self.__books)

    def __book_name(self):
        return self.soup.find("h1", class_="page-header__title").text.split(".")[0].strip()  # название книги

    def __author_name(self):
        return self.soup.find("h1", class_="page-header__title").text.split(".")[1].strip()  # имя автора

    def __shop_price(self):
        return self.soup.find("span", class_="rubs").text.replace(" ","")  # цена в магазине

    def __internet_price(self):
        return self.soup.find("span", class_="silver rubs rubfont").text.replace(" ","")  # цена на сайте

    def __year_of_publishing(self):
        return self.soup.find_all("dt", class_="book__details-value")[1].text.split()[0]  # год издания

    def __publisher(self):
        return self.soup.find_all("dl", class_="book__details-item")[0].text.split()[1]  # издатель

    def __link(self):
        return self.soup.find("link").get("href")  # ссылка на книгу

    def __pages(self):
        return self.soup.find_all("dl", class_="book__details-item")[11].text.split()[1]  # количество страниц в книге

    def __product_code(self):
        return self.soup.find_all("dl", class_="book__details-item")[12].text.split()[2]  # код товара

    def __vendor_code(self):
        """Find vendor code"""
        return self.soup.find_all("dl", class_="book__details-item")[13].text.split()[1]

    def __isbn(self):
        """Find ISBN"""
        return self.soup.find_all("dl", class_="book__details-item")[14].text.split()[1]

# # print(publisher)
# print(info[0])
#
# # soup = BeautifulSoup(text, features="html.parser")
# # list_tag_h1 = soup.findAll("h1")
# # print(list_tag_h1[0].text)


a2 = BookStoreParser()
a2.return_books()
