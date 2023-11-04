"""

"""
import urllib.request
from bs4 import BeautifulSoup
from typing import Type


def ultimate_finder(characteristic: str, soup: Type[object]) -> str:
    base = soup.find_all("dt", class_="book__details-name")
    data = soup.find_all("dt", class_="book__details-value")
    for index, base_info in enumerate(base):
        if base_info.text.replace(" ", "").strip() == characteristic:
            return data[index].text.replace(" ", "").strip()
