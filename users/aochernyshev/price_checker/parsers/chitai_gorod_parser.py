from urllib.request import urlopen
from bs4 import BeautifulSoup


class ChitaiGorodParser:
    @classmethod
    def get_price(cls, url):
        page_text = urlopen(url).read()
        soup = BeautifulSoup(page_text, 'html.parser')
        price_str = soup.find('div', class_='price').text
        price_int = int(price_str.replace('₽', ''))
        return price_int


# if __name__ == "__main__":
#     price = ChitaiGorodParser.get_price("https://www.chitai-gorod.ru/catalog/book/2881570/")
#     print(price)
