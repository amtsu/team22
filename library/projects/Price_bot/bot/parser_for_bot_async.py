from bs4 import BeautifulSoup
import random
import aiohttp
import asyncio


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


async def main_parser_engin(links):
    # URL-адреса товаров для парсинга
    # coffee_bigest = 'https://vkusvill.ru/goods/drip-kofe-yellow-submarine-48-sht-95071.html'
    # coffee_biger = 'https://vkusvill.ru/goods/drip-kofe-yellow-submarine-24-sht-78591.html'
    # mini_cakes = 'https://vkusvill.ru/goods/korzinochki-mini-malina-klubnika-s-maslyanym-kremom-4-sht-88403.html'
    # pancake_cake = 'https://vkusvill.ru/goods/tort-blinnyy-shokoladnyy-29906.html'
    # carrot_cake = 'https://vkusvill.ru/goods/tort-morkovnyy-s-pekanom-postnyy-24734.html'

    # urls = [coffee_biger, coffee_bigest, mini_cakes, pancake_cake, carrot_cake]
    urls = links

    result_dict = {}

    # Асинхронный цикл парсинга
    for url in urls:
        parser = Parser(url)

        try:
            html = await parser.open_html()
            price = parser.main_price_parser(html)
            name = parser.name_parser(html)
            result_dict[name] = price
            print('Данные сохранены:', {name: price})
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
