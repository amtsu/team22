import requests
from bs4 import BeautifulSoup

# Функция для парсинга заголовков новостей с указанного раздела
def parse_rbc_section(url, section_tag):
    # Отправляем GET-запрос на страницу
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Парсим HTML страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем блоки с заголовками новостей
        news_blocks = soup.find_all('a', class_='item__link')

        # Собираем новости в список
        news_list = []
        for block in news_blocks:
            title = block.get_text(strip=True)  # Заголовок новости
            link = block['href']  # Ссылка на новость
            # Добавляем заголовок, ссылку и тег в список
            news_list.append([title, link, section_tag])

        return news_list
    else:
        print(f"Ошибка доступа к сайту: {response.status_code}")
        return []

# Основная функция для парсинга всех разделов
def parse_rbc_news():
    # Список разделов для парсинга
    sections = {
        'https://www.rbc.ru/economics': 'economics',
        'https://www.rbc.ru/politics': 'politics',
        'https://www.rbc.ru/business': 'business',
        'https://www.rbc.ru/technology_and_media': 'technology_and_media'
    }

    all_news = []

    # Проходим по каждому разделу и собираем новости
    for url, tag in sections.items():
        print(f"Парсинг раздела {tag}...")
        news = parse_rbc_section(url, tag)
        all_news.extend(news)

    return all_news

# Пример использования
news_data = parse_rbc_news()

# Выводим собранные новости
for i, item in enumerate(news_data, 1):
    print(f"{i}. Заголовок: {item[0]}\nСсылка: {item[1]}\nТег: {item[2]}\n")
