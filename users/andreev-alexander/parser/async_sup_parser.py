"""
Асинхронный парсинг самолого лучшего сайта :)
"""
import asyncio
import datetime
import pprint
import httpx
import requests
from bs4 import BeautifulSoup


def parse_data_from_page() -> list[dict[str, str]]:
    """
    Парсим все сервисы по страницы `services`, создаем словарь и добавляем
    в словарь информацию по каждому сервису.
    """
    # создаем константы, чтобы остальной код выглядел чище
    SERVICES_URL = "http://101arenda.ru/services/"
    SERVICE_CLASS = "lg:w-1/4 md:w-1/2 p-4 w-full"
    ID_CLASS = "block relative h-48 rounded overflow-hidden"
    NAME_CLASS = "text-gray-900 title-font text-lg font-medium"
    PRICE_CLASS = "mt-1"
    COMPANY_CLASS = "text-gray-500 text-xs tracking-widest title-font mb-1"

    # получаем сырые данные со страницы services
    raw_data_from_page = requests.get(SERVICES_URL).text
    # из сырых данных получаем список с данными сервисов
    html_data_from_page = BeautifulSoup(raw_data_from_page, "lxml")
    services_with_html_tags = html_data_from_page.find_all("div", class_=SERVICE_CLASS)

    services_data: list = []
    for service in services_with_html_tags:
        # получаем и скаченных данных `id`, `name`, `price`, `company`
        service_id = service.find("a", class_=ID_CLASS)["href"].split("/")[-1]
        # если имени нет, то присваиваем `Unknown_name`
        try:
            name = service.find("h2", class_=NAME_CLASS).text
        except AttributeError:
            name = "Unknown_name"
        price = service.find("p", class_=PRICE_CLASS).text
        company = service.find("h3", class_=COMPANY_CLASS).text
        # делаем из полученных данных словарь
        service_data = {
            service_id: {
                "name": name,
                "price": price,
                "company": company
                }
            }
        # добавляем сервис (словарь) в список всех сервисов
        services_data.append(service_data)
    return services_data


async def get_raw_data_from_service_page(URL: str, service_id: str) -> tuple[str, list[str]]:
    """
    Запрашиваем данные со страницы сервиса и отдаем `ID` сервиса и сырой HTML.
    """
    async with httpx.AsyncClient(base_url=URL) as client:
            raw_data_from_service_page = await client.get(service_id)
            return service_id, raw_data_from_service_page


async def parse_data_from_personal_service_page(services_data: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Запрашиваем данные о сервисе с персональной страницы для каждого сервиса
    из доступных в словаре.
    """
    # создаем константы, чтобы остальной код выглядел чище
    SERVICE_URL = "http://101arenda.ru/service/"
    ADDRESS_CLASS = "text-indigo-500 inline-flex items-center ml-auto leading-none"
    QUANTITY_CLASS = "border-b-2 px-4 py-3 text-sm text-gray-900"

    # получаем список `ID` сервисов
    service_ids: list[str] = [list(service.keys())[0] for service in services_data]
    # создаем список задач asyncio, которые будут выполняться параллельно (асинхронно)
    tasks_with_raw_data_from_service_pages: list[asyncio.Task] = [
        asyncio.create_task(get_raw_data_from_service_page(SERVICE_URL, service_id)) for service_id in service_ids
        ]
    # получаем два списка: завершенные и незавершенные запросы
    done_tasks_with_raw_data_from_service_pages, pending_tasks = await asyncio.wait(tasks_with_raw_data_from_service_pages, timeout=10)
    # отменяем незавершенные задачи
    for task in pending_tasks:
        task.cancel()

    for task in done_tasks_with_raw_data_from_service_pages:
        # если в задаче произошло исключение, то отменяем ее
        if not task.exception() is None:
            task.cancel()
        # получаем результат задачи `ID` и данные в виде сырого HTML
        task.result()
        for service_id, raw_data_from_service_page in task:
            # из сырых данных получаем информацию о сервисе
            html_data_from_service_page = BeautifulSoup(raw_data_from_service_page, "lxml")
            # получаем и скаченных данных `quantity`, `address`
            address = html_data_from_service_page.find("a", class_=ADDRESS_CLASS).text
            # если количества нет, то присваиваем `Unknown_quantity`
            try:
                quantity = html_data_from_service_page.find("td", class_=QUANTITY_CLASS).text.strip()
            except AttributeError:
                quantity = "Unknown_quantity"
            # обновляем информацию о сервисе в словаре по ID сервиса
            services_data[service_id].update(
                {
                "address": address,
                "quantity": quantity
            }
            )
    return services_data


async def main():
    start = datetime.datetime.now()
    parsed_services = parse_data_from_page()
    updated_parsed_services = await parse_data_from_personal_service_page(parsed_services)
    finish = datetime.datetime.now()
    delta = finish - start
    # добавил продолжительность выполнения скрипта,
    # чтобы сравнить с синхронной версией
    print("async parse", delta)
    # красиво принтуем результат
    pp = pprint.PrettyPrinter(indent=4, compact=True)
    # pp.pprint(updated_parsed_services)


if __name__ == "__main__":
    asyncio.run(main())
