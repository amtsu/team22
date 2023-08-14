from bs4 import BeautifulSoup
import urllib.request

info = []
header_a = []

for index in range(1156290, 1156300):
    try:
        page = urllib.request.urlopen("https://www.moscowbooks.ru/book/" + str(index) + "/")
        if page.getcode() == 200:
            text = page.read()
            soup = BeautifulSoup(text, features="html.parser")
            print(soup.find("h1"))  # название книги
            print(soup.find("span", class_="rubs"))  # цена в магазине
            print(soup.find("span", class_="silver rubs rubfont"))  # цена на сайте
            info.append(soup.find_all("dt", class_="book__details-value"))  # год и место издания
            header_a.append(soup.find_all("a"))  # издательство
    except:
        pass
print(info)
print(header_a)

# soup = BeautifulSoup(text, features="html.parser")
# list_tag_h1 = soup.findAll("h1")
# print(list_tag_h1[0].text)
