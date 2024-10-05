from bs4 import BeautifulSoup
import random
import aiohttp
import asyncio
from crud_db import (get_user_links,
                     get_last_min_price,
                     save_or_update_last_min_price)


class Parser:
    def __init__(self, url):
        self.url = url

    async def open_html(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                return await response.text() # if response else "Ошибка доступа к странице"

    def name_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        name_element = soup.find('h1', class_='Product__title js-datalayer-catalog-list-name')
        return name_element.text.strip() if name_element else "Название не найдено"

    def main_price_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        price_element = soup.find('span', class_='js-datalayer-catalog-list-price hidden')
        return price_element.text.strip() if price_element else "Цена не найдена"

    def get_name_and_price(self, html):
        name = self.name_parser(html)
        price = self.main_price_parser(html)
        return name, price


async def main_parser_engin(chat_id):
    urls = get_user_links(chat_id)

    result_dict = {}

    # Асинхронный цикл парсинга
    for url in urls:
        parser = Parser(url)

        try:
            html = await parser.open_html()
            name = parser.name_parser(html) # можно перенести ниже
            price = parser.main_price_parser(html)
            # добавить апдейт минимальной цены, примерно так:
            last_min_price = get_last_min_price(chat_id, url)
            print(last_min_price)
            print(price)
            if last_min_price is None or last_min_price > int(price):
                save_or_update_last_min_price(chat_id, url, price)
                if last_min_price is not None:
                    print('Минимальная цена обновлена:', {name: price})
                    result_dict[name] = price

            # last_min_price = db.filter(link=link, chat_id=chat_id).price
            # if last_min_price = None or last_min_price>price:
            #   db.filter(link=link, chat_id=chat_id).price=price
            #   и если цена снизиалась, уже добавлять в словарь на выдачу
            #   name = parser.name_parser(html)
            #   result_dict[name] = price

            # result_dict[name] = price
            # print('Данные сохранены:', {name: price})
        except Exception as e:
            print(f'Ошибка: {e}')
        finally:
            print(result_dict)

        # Асинхронная задержка перед следующим запросом
        delay = random.uniform(3, 10)
        await asyncio.sleep(delay)

    return result_dict


# Чтобы запустить асинхронную функцию
if __name__ == "__main__":
    asyncio.run(main_parser_engin())
