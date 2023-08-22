from bs4 import BeautifulSoup
import urllib.request

summary = {}


page = urllib.request.urlopen("file:///home/evgeniy/Documents/html/book_parsing.html")
text = page.read()
soup = BeautifulSoup(text, features="html.parser")

book_name = soup.find("h1", class_="page-header__title").text.strip()  # название книги
print(book_name)
shop_price = soup.find("span", class_="rubs").text  # цена в магазине
print(shop_price)
internet_price = soup.find("span", class_="silver rubs rubfont").text  # цена на сайте
print(internet_price)
year = soup.find_all("dt", class_="book__details-value")[0].text.split()  # год и место издания
print(year)
publisher = soup.find_all("dl", class_="book__details-item")[0].text.split()

# print(info[0][0].text.split())  # издательство

print(publisher)
