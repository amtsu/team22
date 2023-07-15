from bs4 import BeautifulSoup
import urllib.request

page = urllib.request.urlopen("https://www.moscowbooks.ru/book/1156180/")
if page.getcode() == 200:
    text = page.read()

soup = BeautifulSoup(text, features="html.parser")
list_tag_h1 = soup.findAll("h1")
print(list_tag_h1[0].text)

