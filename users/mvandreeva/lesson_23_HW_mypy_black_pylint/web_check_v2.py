import urllib
import urllib.request
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


class CheckPrice:
    def get_price(self, tag: str, class_name: str) -> list:
        page = urllib.request.urlopen(self.__url)
        if page.getcode() == 200:
            text = page.read()
            if not text == []:
                soup = BeautifulSoup(text)
                price_list = soup.findAll(tag, class_=class_name)
                prices = []
                for i in range(len(price_list)):
                    prices.append(price_list[i].text)
                    print((i + 1), price_list[i].text)
                return prices
            else:
                assert False

        else:
            assert False

    def read_page(self):
        page = urllib.request.urlopen(self.__url)
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
    def clean_data(self, remove: str, to_int: bool) -> int:
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


class ClearDataChitaiGorod(ClearData):
    def clean_data_chitai_gorod(self) -> int:
        bad_data = self.__data.replace("\n          ", "")
        bad_data = self.__data.replace("\xa0", "")
        bad_data = self.__data.replace("\u20bd\n", "")
        good_data = int(bad_data)
        return good_data

    def __init__(self, bad_data: str):
        self.__data = bad_data

    def __repr__(self):
        return self.__data

    def __str__(self):
        return self.__data


class SendMail:
    def __init__(self, price: int):
        self.__price = price

    def is_discount(
        self, discount_price: int, from_whom: str, to_whom: str, subject: str
    ):  # = 'The price discount test'):
        # ??? как сделать один из параметров необязательным, если не стоит указывать значение по умолчанию???
        if self.__price < discount_price:
            msg = MIMEText("Price less then %s" % discount_price)
        else:
            msg = MIMEText("Price is higher then %s" % discount_price)

        me = from_whom
        you = to_whom

        msg["Subject"] = subject
        msg["From"] = me
        msg["To"] = you

        s = smtplib.SMTP("localhost")
        s.sendmail(me, [you], msg.as_string())
        s.quit()
