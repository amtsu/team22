from bs4 import BeautifulSoup
import urllib.request

from team22.users.EANabatov.TR_parsing.parsing_helper import ultimate_finder


class LocalPageParsing:
    def __init__(self):
        self.__summary = {}
        self.__pars()

    def __pars(self):
        page = urllib.request.urlopen("file:///home/evgeniy/Documents/html/book_parsing.html")
        text = page.read()
        soup = BeautifulSoup(text, features="html.parser")

        book_name = soup.find("h1", class_="page-header__title").text.split(".")[0].strip()  # название книги
        author_name = soup.find("h1", class_="page-header__title").text.split(".")[1].strip()  # имя автора
        shop_price = soup.find("span", class_="rubs").text.replace(" ","")  # цена в магазине
        internet_price = soup.find("span", class_="silver rubs rubfont").text.replace(" ","")  # цена на сайте
        year = soup.find_all("dt", class_="book__details-value")[1].text.split()[0]  # год издания
        publisher = soup.find_all("dl", class_="book__details-item")[0].text.split()[1]  # издатель
        link = soup.find("link").get("href")  # ссылка на книгу
        pages = soup.find_all("dl", class_="book__details-item")[11].text.split()[1]  # количество страниц в книге
        product_code = soup.find_all("dl", class_="book__details-item")[12].text.split()[2]  # код товара
        vendor_code = soup.find_all("dl", class_="book__details-item")[13].text.split()[1]  # артикул
        isbn = soup.find_all("dl", class_="book__details-item")[14].text.split()[1]  # ISBN

        self.__summary["book_name"] = book_name
        self.__summary["author_name"] = author_name
        self.__summary["shop_price"] = shop_price
        self.__summary["internet_price"] = internet_price
        self.__summary["the_year_of_publishing"] = year
        self.__summary["publisher"] = ultimate_finder(page, "Издательство:")
        self.__summary["link"] = link
        self.__summary["pages"] = pages
        self.__summary["product_code"] = product_code
        self.__summary["vendor_code"] = vendor_code
        self.__summary["isbn"] = isbn

    def pars_dictionary(self):
        return self.__summary


a1 = LocalPageParsing()
print(a1.pars_dictionary())
