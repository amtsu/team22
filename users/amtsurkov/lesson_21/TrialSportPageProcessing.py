#import urllib3 as urllib
#import urllib as urllib
import urllib.request
import urllib
from bs4 import BeautifulSoup

class Element():
    def get(self):
        #assert self.__is_page_ok()
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
        #assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)
    
    def __get_text(self):
        list_reports_data = self.__soup.findAll('div', class_='price')
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    #def __is_page_ok(self):
    #    list_reports_data = self.__soup.findAll('div', class_='price')
    #    print(list_reports_data)
    #    assert len(list_reports_data) == 10
    #    if len(list_reports_data) != 10:
    #        return False
    #    return True
    
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

class PriceSaleElement(Element):
    def get(self):
        #assert self.__is_page_ok()
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

    #def __is_page_ok(self):
    #    list_reports_data = self.__soup.findAll('div', class_='price price_disc')
    #    assert len(list_reports_data) == 1
    #    if len(list_reports_data) != 1:
    #        return False
    #    return True

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
        #assert self.__is_page_ok()
        text = self.__get_text()
        normalization_text = self.__normalization(text)
        return self.__type_convert(normalization_text)

    def __get_text(self):
        list_reports_data = self.__soup.findAll('h2')
        element_1 = list_reports_data[0]
        return element_1.text

    def __init__(self, soup):
        self.__soup = soup

    #def __is_page_ok(self):
    #    list_reports_data = self.__soup.findAll('h2')
    #    print(list_reports_data)
    #    assert len(list_reports_data) == 5
    #    if len(list_reports_data) != 5:
    #        return False
    #    return True
    
    def __normalization(self, price_bad):
        return price_bad
    
    def __type_convert(self, text):
        return text
        

class OnePageProcessor():
    """
        Not good use BeautifulSoup object, and then use them in coheshe object
    """
    def __init__(self, text_page):
        self.__soup = BeautifulSoup(text_page, features="html.parser")

    def list_dict(self):
        return [
            {
                "title": TitleElement(self.__soup).get(),
                "price": PriceElement(self.__soup).get(),
                "price_sale": PriceSaleElement(self.__soup).get(),
            }
        ]


# модуль trial-sport.ru
class OnePage():
#    def get_price(self):
#        e = PriceElement(self.__soup)
#        #print(e._w())
#        #print(e.__z())
#        return e.get()
#
    def __init__(self, url):
        self.__url = url
        #print(help(urllib.request))
        with urllib.request.urlopen(self.__url) as response:
        #with urllib.urlopen(self.__url) as response:
            self.__page = response.read()
            self.__one_page_processor = OnePageProcessor(self.__page)
            
#    def get_title(self):
#        e = TitleElement(self.__soup)
#        return e.get()

    def list_dict(self):
        return self.__one_page_processor.list_dict()
    

class ListPage():
    pass



dir(urllib)
#dir(urllib.request)
