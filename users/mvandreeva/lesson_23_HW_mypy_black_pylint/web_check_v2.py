""" модуль открытия и обработки url """
import urllib
import urllib.request
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

class CheckPrice:
    """ Класс обрабатывает web-страницу и находит цену  """
    def get_price(self, tag: str, class_name: str) -> list:
        """ метод получает блок с ценой """
        with urllib.request.urlopen(self.__url) as page:
            if page.getcode() == 200:
                text = page.read()
                if not text == []:
                    soup = BeautifulSoup(text)
                    price_list = soup.findAll(tag, class_=class_name)
                    prices = []
                    for i, price in enumerate(price_list):
                        prices.append(price.text)
                        print((i + 1), price.text)
                    return prices
                assert False
            assert False
    #            """ Unnecessary "else" after "return", remove the "else" ... """
    #            else: """ выдавал ошибку Parsing failed: 'invalid syntax """
    #                assert False """засунуть вывод ошибок в тесты"""
    #        else:
    #            assert False

    def read_page(self): 
        """ метод обрабатывает web-страницу """
        with urllib.request.urlopen(self.__url) as page:
            print("Page code: ", page.getcode())
            text = page.read()
            return text

    def __init__(self, link: str):
        self.__url = link

    def __repr__(self):
        return self.__url

    def __str__(self):
        return self.__url


class ClearData:
    """ Класс очищает данные от посторонних символов"""
    def clean_data(self, remove: str, to_int: bool) -> int:
        """ метод очистки данных"""
        if to_int:
            bad_data = self.__data.replace(remove, "")
            good_data = int(bad_data)
        else:
            bad_data = self.__data.replace(remove, "")
        return good_data

    def __init__(self, bad_data: str):
        self.__data = bad_data

    def __repr__(self):
        return self.__data

    def __str__(self):
        return self.__data


class ClearDataChitaiGorod(ClearData): #наследование здесь не нужно, просто так добавила, чтоб учиться
    """ Класс очистки данных для сайта читай-город """
    def clean_data_chitai_gorod(self) -> int:
        """ метод получения итоговой цены """
        bad_data = self.__data.replace("\n          ", "")
        bad_data = self.__data.replace("\xa0", "")
        bad_data = self.__data.replace("\u20bd\n", "")
        good_data = int(bad_data)
        return good_data

    def __init__(self, bad_data: str): #__init__ method from base class 'ClearData' is not called
        self.__data = bad_data
#    def __init__(self, bad_data: str): #__init__ method from base class 'ClearData' is not called
#                 = bad_data
#class Fruit:
#    def __init__(self, name="fruit"):
#        self.name = name
#        print("Creating a {self.name}")
#class Apple(Fruit):
#    def __init__(self):
#        super().__init__("apple")

#    def __repr__(self):
#        return self.__data

#    def __str__(self):
#        return self.__data


class SendMail: #Too few public methods (1/2)
    """ Класс для отправки e-mail"""
    def __init__(self, price: int):
        self.__price = price

    def is_discount(
        self, discount_price: int, from_whom: str, to_whom: str, subject: str
    ):  # = 'The price discount test'):
        """ проверяет, есть ли скидка и отправляет сообщение """
        # как сделать один из параметров необязательным, если не указывать значение по умолчанию?
        if self.__price < discount_price:
            msg = MIMEText("Price less then %s" % discount_price) 
            #Formatting a regular string which could be a f-string
        else:
            msg = MIMEText("Price is higher then %s" % discount_price)

        me = from_whom #Variable name "me" doesn't conform to snake_case naming style
        you = to_whom

        msg["Subject"] = subject
        msg["From"] = me
        msg["To"] = you

        s = smtplib.SMTP("localhost") #Variable name "me" doesn't conform to snake_case naming style
        s.sendmail(me, [you], msg.as_string())
        s.quit()
