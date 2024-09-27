from bs4 import BeautifulSoup
import random
import aiohttp
import asyncio
from celery_app import app


class Parser:
    def __init__(self, url):
        self.url = url

    async def open_html(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                return await response.text()

    def name_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        name_element = soup.find('h1', class_='Product__title js-datalayer-catalog-list-name')
        return name_element.text.strip() if name_element else "Название не найдено"

    def main_price_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        price_element = soup.find('span', class_='js-datalayer-catalog-list-price hidden')
        return price_element.text.strip() if price_element else "Цена не найдена"


# @app.task
# def parse_url(url):
#     parser = Parser(url)
#     try:
#         html = asyncio.run(parser.open_html())
#         # html = await parser.open_html()
#         price = parser.main_price_parser(html)
#         name = parser.name_parser(html)
#         return {name: price}
#     except Exception as e:
#         return {'error': str(e)}


@app.task
def parse_url(url):
    parser = Parser(url)
    result_dict = {}
    try:
        html = asyncio.run(parser.open_html())
        price = parser.main_price_parser(html)
        name = parser.name_parser(html)
        result_dict[name] = price
        print('Данные сохранены:', {name: price})  # Вернул print
    except Exception as e:
        print(f'Ошибка: {e}')  # Вернул print ошибки
        result_dict = {'error': str(e)}
    finally:
        print(result_dict)  # Вернул итоговый print словаря
    return result_dict


@app.task
def main_parser_engin():
    # URL-адреса товаров для парсинга
    coffee_bigest = 'https://vkusvill.ru/goods/drip-kofe-yellow-submarine-48-sht-95071.html'
    coffee_biger = 'https://vkusvill.ru/goods/drip-kofe-yellow-submarine-24-sht-78591.html'
    mini_cakes = 'https://vkusvill.ru/goods/korzinochki-mini-malina-klubnika-s-maslyanym-kremom-4-sht-88403.html'
    pancake_cake = 'https://vkusvill.ru/goods/tort-blinnyy-shokoladnyy-29906.html'
    carrot_cake = 'https://vkusvill.ru/goods/tort-morkovnyy-s-pekanom-postnyy-24734.html'

    urls = [coffee_biger, coffee_bigest, mini_cakes, pancake_cake, carrot_cake]

    result_dict = {}

    # Цикл, который ставит задачи в очередь Celery
    for url in urls:
        result = parse_url.delay(url)  # Отправляем задачу в Celery
        result_dict.update(result.get())  # Получаем результат выполнения задачи
        print(result_dict)
        delay = random.uniform(3, 10)
        asyncio.run(asyncio.sleep(delay)) 

    # # Асинхронный цикл парсинга
    # for url in urls:
    #     parser = Parser(url)

    #     try:
    #         html = await parser.open_html()
    #         price = parser.main_price_parser(html)
    #         name = parser.name_parser(html)
    #         result_dict[name] = price
    #         print('Данные сохранены:', {name: price})
    #     except Exception as e:
    #         print(f'Ошибка: {e}')
    #     finally:
    #         print(result_dict)

    #     # Асинхронная задержка перед следующим запросом
    #     delay = random.uniform(3, 10)
    #     await asyncio.sleep(delay)

    return result_dict

# Чтобы запустить асинхронную функцию
if __name__ == "__main__":
    results = main_parser_engin()
    print(results)
    # asyncio.run(main_parser_engin())
