#import urllib3 as urllib
#import urllib as urllib
import urllib.request
import urllib
from bs4 import BeautifulSoup

class Element():
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)
    
    def __get_text(self):
        assert Flase

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        return True
    
    def __normalization(self, price_bad):
        return price_bad
    
    def __type_convert(self, text):
        return text
    
    def _w(self):
        return 'w'
        
    def __z(self):
        return 'z'
    

class PriceElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)
    
    def __get_text(self):
        list_reports_data = self.__soup.findAll('div', class_='price price_disc')
        #list_reports_data = self.__soup.findAll('span', id_='price price_disc')
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_reports_data = self.__soup.findAll('div', class_='price price_disc')
        if len(list_reports_data) != 1:
            return False
        return True
    
    def __normalization(self, price_bad):
        price_bad = price_bad.replace(u'\u2009', '') # ' '
        price_bad = price_bad.replace(u'\u20bd', '') # '₽'
        price_bad = price_bad.replace(u' ', '') # ' '
        return price_bad
        price_good = int(price_bad)
        return price_good
    
    def __type_convert(self, text):
        assert text.isnumeric()
        return int(text)
    
    def __z(self):
        return 'z'

    
class TitleElement(Element):
    def get(self):
        assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)
    
    def __get_text(self):
        list_reports_data = self.__soup.findAll('h2')
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    def __is_page_ok(self):
        list_reports_data = self.__soup.findAll('h2')
        if len(list_reports_data) != 5:
            return False
        return True
    
    def __normalization(self, price_bad):
        return price_bad
    
    def __type_convert(self, text):
        return text
        

# модуль trial-sport.ru
class OnePage():
    def get_price(self):
        e = PriceElement(self.__soup)
        #print(e._w())
        #print(e.__z())
        return e.get()

    def __init__(self, url):
        self.__url = url
        #print(help(urllib.request))
        with urllib.request.urlopen(self.__url) as response:
        #with urllib.urlopen(self.__url) as response:
            self.__page = response.read()
            self.__soup = BeautifulSoup(self.__page)
            
    def get_title(self):
        e = TitleElement(self.__soup)
        return e.get()
    
class ListPage():
    pass



dir(urllib)
#dir(urllib.request)
