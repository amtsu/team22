from bs4 import BeautifulSoup
import urllib.request

book_name = []
shop_price = []
internet_price = []
publisher = []
info = []

for index in range(1156290, 1156300):
    try:
        page = urllib.request.urlopen("https://www.moscowbooks.ru/book/" + str(index) + "/")
        if page.getcode() == 200:
            text = page.read()
            soup = BeautifulSoup(text, features="html.parser")
            book_name.append(soup.find("h1"))  # название книги
            shop_price.append(soup.find("span", class_="rubs"))  # цена в магазине
            shop_price.append(soup.find("span", class_="silver rubs rubfont"))  # цена на сайте
            publisher.append(soup.find_all("dt", class_="book__details-value"))  # год и место издания
            info.append(soup.find_all("a"))  # издательство
    except:
        pass
# print(publisher)
print(info[0])

# soup = BeautifulSoup(text, features="html.parser")
# list_tag_h1 = soup.findAll("h1")
# print(list_tag_h1[0].text)
