""""""
import urllib.request
from bs4 import BeautifulSoup


def ultimate_finder(page, characteristic=str) -> str:
    __page = urllib.request.urlopen(page)
    __text = __page.read()
    __soup = BeautifulSoup(__text, features="html.parser")
    __base = __soup.find_all("dt", class_="book__details-name")
    __data = __soup.find_all("dt", class_="book__details-value")
    for index, base_info in enumerate(__base):
        if base_info.text.replace("-", "").strip() == characteristic:
            return __data[index].text.replace("-", "").strip()
