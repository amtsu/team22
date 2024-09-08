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
import telegram
import asyncio
import time
from pprint import pprint  # type: ignore
import os
import subprocess

async def send_tg(msg, chat_id, token):
    bot = telegram.Bot(token=token)
    await bot.sendMessage(chat_id=chat_id, text=msg)

async def send_photo_tg(photo_path,  chat_id, token):
    bot = telegram.Bot(token=token)
    await bot.send_photo(chat_id, photo=open(photo_path, 'rb'))

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')  # отключает открытие браузера
options.add_argument('--window-size=414x896')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
chrome = webdriver.Chrome(options=options)
project_list = [
    {
        'url': 'https://mftickets.technolab.com.ru/mc/66a8ec3a0e7b49001f7c8277',
        'slug': 'serf_moscow_park_gorkogo',
        'type': 'html',
    },
    {
        'url': 'https://mftickets.technolab.com.ru/mc/66a8ee6604b149e0b19069cf',
        'slug': 'aerotruba_moscow_park_gorkogo',
        'type': 'html',
    },
    {

        'url': 'https://mf.technolab.com.ru/v1/place/dates-list?place_id=66a8ec3a0e7b49001f7c8277',
        'slug': 'serf_moscow_park_gorkogo_date',
        'type': 'all',
    },
    {

        'url': 'https://mf.technolab.com.ru/v1/place/dates-list?place_id=66a8ee6604b149e0b19069cf',
        'slug': 'aerotruba_moscow_park_gorkogo_date',
        'type': 'all',
    },
    {'url': 'https://mftickets.technolab.com.ru/mc/66a8ec3a0e7b49001f7c8277','slug': 'serf_moscow_park_gorkogo','type': 'html',},
    #{'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    #{'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    {'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    {'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    {'url': 'https://mftickets.technolab.com.ru/mc/66a8ec3a0e7b49001f7c8277','slug': 'serf_moscow_park_gorkogo','type': 'html',},
     {'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    {'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    {'url': 'https://mftickets.technolab.com.ru/mc/66a8ec3a0e7b49001f7c8277','slug': 'serf_moscow_park_gorkogo','type': 'html',},
     {'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    {'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    {'url': 'https://mftickets.technolab.com.ru/mc/66a8ec3a0e7b49001f7c8277','slug': 'serf_moscow_park_gorkogo','type': 'html',},
    # {'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    #{'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    #{'url': 'https://mftickets.technolab.com.ru/mc/66a8ec3a0e7b49001f7c8277','slug': 'serf_moscow_park_gorkogo','type': 'html',},
    #{'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    #{'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    #{'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    #{'url': 'https://101a.ru','slug': 'delete','type': 'html',},
    #{'url': 'https://mftickets.technolab.com.ru/mc/66a8ec3a0e7b49001f7c8277','slug': 'serf_moscow_park_gorkogo','type': 'html',},
 ]
for obj in project_list:
        url = obj['url']
        chrome.get(url)
        time.sleep(2)
        page = chrome.page_source
        if obj['type'] == 'html':
            soup = BeautifulSoup(page, features="html.parser")
            d = soup.find_all("div", class_="DetailLayout_Body__2LOxJ")
            text = []
            for t in d :
                text.append(t.text)
            page = "\n".join(text)
        elif obj['type'] == 'all':
            pass
        else:
            print(f"Errrrrooorr -TYPE = {obj['type']}")
        now = datetime. now()
        print("now =", now)
        dt_string = now.strftime("%Y_%m_%d_%H_%M")
        minut = int(now.strftime("%M")) - 1
        if minut >= 10:
            minut = str(minut)
        elif  0<= minut < 10:
            minut = '0' + str(minut)
        else:
            minut = '0'
        f_l = now.strftime("%Y_%m_%d_%H_") + minut
        print("date and time =", dt_string)
        print(f_l)
        dt_string = obj['slug'] + '_' + dt_string
        f_l = obj['slug'] + '_' + f_l
        try:
            with open('/data/' + dt_string, "w") as file:
                file.write(page)
            ss = ''
            with open('/data/' + f_l, "r") as f:
                ss = f.read()
            print(len(ss), len(page))
            token = ''
            my_chat_id = '383332826'
            my_token = token
            print('ddddd')
            my_token =
            photo_path = f"/data/{obj['slug']}_screenshot.png"
            if ss != page or len(ss) != len(page):
                print('!!!!!!!!!!!!!!')
                print(url)
                mm = url
                asyncio.run(send_tg(mm, my_chat_id, my_token))
                print(len(ss) , len(page))
                chrome.get_screenshot_as_file(photo_path)
                asyncio.run(send_photo_tg(photo_path,  my_chat_id, my_token))
                with open('/data/' + f_l, "w") as file:
                    file.write(page)
        except Exception as e:
            print(f"Error ----- {e}")
        time.sleep(1)

print('----123--')
