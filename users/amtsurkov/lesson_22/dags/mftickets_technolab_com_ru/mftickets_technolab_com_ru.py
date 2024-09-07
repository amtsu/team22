import re
import urllib.request
import urllib
from bs4 import BeautifulSoup
import json

from datetime import datetime

from multiprocessing import freeze_support
freeze_support()

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.webdriver import WebDriver


from selenium import webdriver


from selenium.webdriver.chrome.service import Service


import time
from pprint import pprint  # type: ignore

   
import os

import subprocess

#        self.__soup = BeautifulSoup(text_page, features="html.parser")
#
#            d = i.find_all("span", class_="product-card__name")
#            for t in d :
#                title = t.text
#                title = title.replace(" / ", "")
#
#
#
#        with urllib.request.urlopen(self.__url) as response:
#            self.__page = response.read()
#            self.__one_page_processor = OnePageProcessor(self.__page, self.__url)


options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--headless')  # отключает открытие браузера
options.add_argument('--window-size=1280x1696')
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')


#import undetected_chromedriver as uc
#options = uc.ChromeOptions()
#driver = uc.Chrome(options = options, browser_executable_path="/usr/bin/chromium", driver_executable_path="/tmp/chromedriver")
#driver = uc.Chrome(options = options)#, driver_executable_path="/tmp/chromedriver")
#driver.get('https://mftickets.technolab.com.ru/mc/66a8ec3a0e7b49001f7c8277')


#chrome = uc.Chrome(options=options, browser_executable_path="/usr/bin/chromium")#, driver_executable_path="/tmp/chromedriver")


#service = Service(executable_path="./chromedriver")
#
#chrome = webdriver.Chrome(service=service,
#                              options=options)

chrome = webdriver.Chrome(options=options)

url_list = ['https://mftickets.technolab.com.ru/mc/66a8ec3a0e7b49001f7c8277']
for url in url_list:
        #try:
            chrome.get(url)
            time.sleep(3)
            page = chrome.page_source
            #self.__list_page_processor = ListPageProcessor(page, url)
            print(page)

            now = datetime. now()
            print("now =", now)
            dt_string = now.strftime("%d_%m_%Y_%H_%M")
            minut = int(now.strftime("%M")) - 1
            f_l = now.strftime("%d_%m_%Y_%H_") + (str(minut) if minut >= 0 else '0')

            print("date and time =", dt_string)
            print(f_l)


            os.system('ls /data/')
            output = subprocess.run(['ls', '-la', '/data/'], capture_output=True, text=True)
            print(output.stdout)



            with open('/data/' + dt_string, "w") as file:
                file.write(page)


            os.system('ls /data/')
            output = subprocess.run(['ls', '-la', '/data/'], capture_output=True, text=True)
            print(output.stdout)

           
            ss = ''
            with open('/data/' + f_l, "r") as f:
                ss = f.read()


            os.system('ls /data/')
            output = subprocess.run(['ls', '-la', '/data/'], capture_output=True, text=True)
            print(output.stdout)


            if ss != page:
                print('!!!!!!!!!!!!!!')
                assert 1111



        #except AttributeError as e:
        #    print(f"Неудалось получить общий каталог, ошибка - {e}")

print('----123--')
