from unicodedata import decimal

from bs4 import BeautifulSoup
import urllib.request

summary = {}


page = urllib.request.urlopen("file:///home/evgeniy/Documents/html/book_parsing.html")
text = page.read()
soup = BeautifulSoup(text, features="html.parser")

# book_name_author_name = soup.find("h1", class_="page-header__title").text.strip().split(".")  # название книги
book_name = soup.find("h1", class_="page-header__title").text.split(".")[0].strip()  # название книги
print("book_name: ", book_name)
summary["book_name"] = book_name
author_name = soup.find("h1", class_="page-header__title").text.split(".")[1].strip()  # имя автора
print("author_name: ", author_name)
summary["author_name"] = author_name
shop_price = soup.find("span", class_="rubs").text.strip()  # цена в магазине
print("shop_price:", shop_price)
summary["shop_price"] = shop_price
internet_price = soup.find("span", class_="silver rubs rubfont").text.strip()  # цена на сайте
print("internet_price:", internet_price)
summary["internet_price"] = internet_price
year = soup.find_all("dt", class_="book__details-value")[0].text.split()[0]  # год издания
print("the_year_of_publishing:", year)
summary["the_year_of_publishing"] = year
publisher = soup.find_all("dl", class_="book__details-item")[0].text.split()[1]  # издатель
print("publisher:", publisher)
summary["publisher"] = publisher

print(summary)
# print(info[0][0].text.split())  # издательство


