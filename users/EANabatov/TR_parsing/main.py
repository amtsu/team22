import time

from bs4 import BeautifulSoup
import urllib.request


class BookStoreParser:
    def __init__(self):
        self.__books = []
        self.__parsing()

    def __parsing(self):
        cw = 0
        for index in range(1156290, 1156300):
            summary = {}
            try:
                self.page = urllib.request.urlopen("https://www.moscowbooks.ru/book/" + str(index) + "/")
                time.sleep(1)
                self.text = self.page.read()
                self.soup = BeautifulSoup(self.text, features="html.parser")
                if self.page.getcode() == 200:
                    try:
                        summary["book_name"] = self.__book_name()
                    except:
                        print("book_name not found")
                        summary["book_name"] = ""
                    try:
                        summary["author_name"] = self.__author_name()
                    except:
                        print("author_name not found")
                        summary["author_name"] = ""
                    try:
                        summary["shop_price"] = self.__shop_price()
                    except:
                        print("shop_price not found")
                        summary["shop_price"] = ""
                    try:
                        summary["internet_price"] = self.__internet_price()
                    except:
                        print("internet_price not found")
                        summary["internet_price"] = ""
                    try:
                        summary["the_year_of_publishing"] = self.__year_of_publishing()
                    except:
                        print("the_year_of_publishing not found")
                        summary["the_year_of_publishing"] = ""
                    try:
                        summary["publisher"] = self.__publisher()
                    except:
                        print("publisher not found")
                        summary["publisher"] = ""
                    try:
                        summary["link"] = self.__link()
                    except:
                        print("link not found")
                        summary["link"] = ""
                    try:
                        summary["pages"] = self.__pages()
                    except:
                        print("pages not found")
                        summary["pages"] = ""
                    try:
                        summary["product_code"] = self.__product_code()
                    except:
                        print("product_code not found")
                        summary["product_code"] = ""
                    try:
                        summary["vendor_code"] = self.__vendor_code()
                    except:
                        print("vendor_code not found")
                        summary["vendor_code"] = ""
                    try:
                        summary["isbn"] = self.__isbn()
                    except:
                        print("isbn not found")
                        summary["isbn"] = ""
                else:
                    print(self.page.getcode())
            except:
                print(index, "skiped.", "Download: ", self.cw)

            if summary != {}:
                self.__books.append(summary)
                cw = cw + 1
                print(cw)

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


a2 = BookStoreParser()
a2.return_books()
