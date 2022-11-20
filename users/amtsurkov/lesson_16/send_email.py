#!/usr/local/bin/python
# coding: utf-8

import urllib
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

page = urllib.urlopen("https://trial-sport.ru/goods/51530/1179889.html")
if page.getcode() == 200:
    text = page.read()
    
    soup = BeautifulSoup(text, features="html.parser")
    list_reports_data = soup.findAll('div', class_='price price_disc')
    element_1 = list_reports_data[0]
    price_bad = element_1.text
    price_bad = price_bad.replace(u'\u2009', '') # ' '
    price_bad = price_bad.replace(u'\u20bd', '') # '₽'
    price_bad = price_bad.replace(u' ', '') # ' '
    price_good = int(price_bad)
    if price_good < 3000:
        msg = MIMEText('Price less then 3000 !!!!')
    else:
        msg = MIMEText('Price greate then 3000 !!!')

    me = 'artem@101katok.ru'
    you = 'artemtemp@mail.ru'

    msg['Subject'] = 'The test price'
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP('localhost')
    s.sendmail(me, [you], msg.as_string())
    s.quit()
