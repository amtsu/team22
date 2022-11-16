from parsers.chitai_gorod_parser import ChitaiGorodParser
from mailer import Mailer
from config import sender_email_data, recipient_list
from product import Product

mailer = Mailer(
    login=sender_email_data['login'],
    password=sender_email_data['password'],
    domen=sender_email_data['domen'],
    port=sender_email_data['port'],
    recipient_list=recipient_list,
)

url = 'https://www.chitai-gorod.ru/catalog/book/2881570/'
critical_price = 1000
parser = ChitaiGorodParser

product = Product(url, critical_price, parser)

if product.get_price() <= product.get_critical_price():
    message = "{} - this product price below critical price!".format('url')
    mailer.send_message(message)
    print("Письмо отправлено.")
else:
    print("{} - это больше {}. Письмо не отправлено.".format(product.get_price(), product.get_critical_price()))
