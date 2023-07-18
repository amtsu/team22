from bs4 import BeautifulSoup
import urllib.request

for index in range(1156290, 1156300):
    try:
        page = urllib.request.urlopen("https://www.moscowbooks.ru/book/" + str(index) + "/")
        if page.getcode() == 200:
            text = page.read()
            soup = BeautifulSoup(text, features="html.parser")
            print(page)
            print(soup.find("h1"))
            print(soup.find("span", class_= "rubs"))
    except:
        pass

# soup = BeautifulSoup(text, features="html.parser")
# list_tag_h1 = soup.findAll("h1")
# print(list_tag_h1[0].text)
