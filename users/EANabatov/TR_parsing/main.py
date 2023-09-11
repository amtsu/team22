"""модуль парсинга сайта книжного магазина (онлайн)"""

from bs4 import BeautifulSoup
import urllib.request


class BookStoreParser:
    """класс парсинга сайта книжного магазина"""

    def __init__(self, start_parsing_index, end_parsing_index):
        self.__books = []
        self.__parsing(start_parsing_index, end_parsing_index)

    def __parsing(self, start_parsing_index, end_parsing_index):
        for index in range(start_parsing_index, end_parsing_index + 1):
            __summary = {}
            try:
                self.page = urllib.request.urlopen(
                    "https://www.moscowbooks.ru/book/" + str(index) + "/"
                )
                # time.sleep(1)
                self.text = self.page.read()
                self.soup = BeautifulSoup(self.text, features="html.parser")
                if self.page.getcode() == 200:
                    try:
                        __summary["in_stock"] = self.__in_stock()
                    except:
                        __summary["in_stock"] = ""
                    try:
                        __summary["book_name"] = self.__book_name()
                    except:
                        __summary["book_name"] = ""
                    try:
                        __summary["author_name"] = self.__author_name()
                    except:
                        __summary["author_name"] = ""
                    try:
                        __summary["shop_price"] = self.__shop_price()
                    except:
                        __summary["shop_price"] = ""
                    try:
                        __summary["internet_price"] = self.__internet_price()
                    except:
                        __summary["internet_price"] = ""
                    try:
                        __summary[
                            "the_year_of_publishing"
                        ] = self.__year_of_publishing()
                    except:
                        __summary["the_year_of_publishing"] = ""
                    try:
                        __summary["publisher"] = self.__publisher()
                    except:
                        __summary["publisher"] = ""
                    try:
                        __summary["link"] = self.__link()
                    except:
                        __summary["link"] = ""
                    try:
                        __summary["product_code"] = self.__product_code()
                    except:
                        __summary["product_code"] = ""
                    try:
                        __summary["vendor_code"] = self.__vendor_code()
                    except:
                        __summary["vendor_code"] = ""
                    try:
                        __summary["isbn"] = self.__isbn()
                    except:
                        __summary["isbn"] = ""
                    try:
                        __summary["pegi"] = self.__pegi()
                    except:
                        __summary["pegi"] = ""
                else:
                    print(self.page.getcode())
            except:
                pass

            if __summary != {}:
                self.__books.append(__summary)

    def return_books(self):
        print(self.__books)

    def __book_name(self):
        """название книги"""
        return (
            self.soup.find("h1", class_="page-header__title")
            .text.replace(" ", " ")
            .strip()
        )

    def __author_name(self):
        """имя автора (отсутствует если это журнал)"""
        return self.soup.find("a", class_="author-name").text

    def __shop_price(self):
        """цена в магазине (отсутствует если товара нет в наличии)"""
        return self.soup.find("span", class_="rubs").text.replace(" ", "").strip()

    def __internet_price(self):
        """цена на сайте (отсутствует если товара нет в наличии)"""
        return (
            self.soup.find("span", class_="silver rubs rubfont")
            .text.replace(" ", "")
            .strip()
        )

    def __year_of_publishing(self):
        """год издания книги (нет если книга не в наличии)"""
        __result = ""
        book_details = self.soup.find_all("dt", class_="book__details-value")
        for detail in book_details:
            if len(detail.text.replace(" ", " ").strip()) == 4:
                __result = detail.text.replace(" ", " ").strip()
                break
        return __result

    def __publisher(self):
        """находит издателя"""
        return self.soup.find_all("dt", class_="book__details-value")[0].text.strip()

    def __link(self):
        """находит ссылку на страницу с книгой"""
        return self.soup.find("link").get("href")  # ссылка на книгу

    def __product_code(self):
        """находит код продукта"""
        __result = ""
        book_details = self.soup.find_all("dt", class_="book__details-value")
        for detail in book_details:
            if len(detail.text.strip()) == 7:
                __result = detail.text.strip()
        return __result

    def __vendor_code(self):
        """находит артикул"""
        __result = ""
        book_details = self.soup.find_all("dt", class_="book__details-value")
        for detail in book_details:
            if detail.text.strip()[0] == "К" and len(detail.text.strip()) == 6:
                __result = detail.text.strip()
        return __result

    def __isbn(self):
        """находит международный идентификатор книги (ISBN)"""
        __result = ""
        book_details = self.soup.find_all("dt", class_="book__details-value")
        for detail in book_details:
            if len(detail.text.replace("-", "").strip()) == 13:
                __result = detail.text.replace("-", "").strip()
        return __result

    def __in_stock(self):
        """определяет в наличии ли книга в магазине на данный момент"""
        __stock = None
        try:
            __stock = (
                self.soup.find("span", class_="book__shop-instock")
                .text.replace(" ", " ")
                .strip()
            )
        except:
            __stock = (
                self.soup.find("span", class_="instock1")
                .text.replace(" ", " ")
                .strip()
                .lower()
            )
        return __stock

    def __pegi(self):
        """находит возрастное ограничение для книг (PEGI)"""
        __result = ""
        book_details = self.soup.find_all("dt", class_="book__details-value")
        for detail in book_details:
            if detail.text.strip()[::-1][0] == "+":
                __result = detail.text.strip()
        return __result


a2 = BookStoreParser(1156290, 1156297)
a2.return_books()
