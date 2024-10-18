import requests
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import urlopen


url = "https://www.rbc.ru/short_news" #ссылка на страницу с новостями

#отправляем GET-запрос
response = urlopen(url)
html = response.read().decode("utf-8")

#парсим HTML-страницу
soup = BeautifulSoup(html, 'html.parser')

#выбираем заголовки новостей (теги <a> с классом item__link)
news_title = soup.find_all('a', class_='item__link')

#список для хранения заголовков
title_list = []

#извлекаем текст заголовка и ссылку на новость
for title in news_title:
    news_title = title.get_text(strip=True)
    news_link = title['href']
    title_list.append({'title': news_title, 'link': news_link})


#выводим заголовки со ссылками
for i, item in enumerate(title_list, 1):
    print(f"{i}. {item['title']}")
    print(f"Ссылка: {item['link']}\n")

#печатаем отбивочку
print('*' * 50)

    # url = url + '?PAGEN_1=' + i