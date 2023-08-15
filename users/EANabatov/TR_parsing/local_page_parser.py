from bs4 import BeautifulSoup
import urllib.request

book_name = []
shop_price = []
internet_price = []
publisher = []
info = []

page = urllib.request.urlopen("file:///home/evgeniy/Documents/html/book_parsing.html")

text = page.read()
soup = BeautifulSoup(text, features="html.parser")
book_name.append(soup.find("h1"))  # название книги
shop_price.append(soup.find("span", class_="rubs"))  # цена в магазине
shop_price.append(soup.find("span", class_="silver rubs rubfont"))  # цена на сайте
publisher.append(soup.find_all("dt", class_="book__details-value"))  # год и место издания
info.append(soup.find_all("dl", class_="book__details-item"))  # издательство
info[0][0].text.split()

# print(publisher)
