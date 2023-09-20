"""

"""
import urllib.request
from bs4 import BeautifulSoup


def ultimate_finder(page, characteristic=str) -> str:
    page = urllib.request.urlopen(page)
    text = page.read()
    soup = BeautifulSoup(text, features="html.parser")
    base = soup.find_all("dt", class_="book__details-name")
    data = soup.find_all("dt", class_="book__details-value")
    for index, base_info in enumerate(base):
        if base_info.__text.replace(" ", "").strip() == characteristic:
            return data[index].text.replace(" ", "").strip()
