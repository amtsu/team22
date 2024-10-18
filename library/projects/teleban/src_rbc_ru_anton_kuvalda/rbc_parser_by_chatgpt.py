import requests
from bs4 import BeautifulSoup

# Функция для парсинга заголовков с сайта РБК
def parse_rbc_short_news_titles():
    # URL страницы с короткими новостями
    url = 'https://www.rbc.ru/short_news'

    # Отправляем GET-запрос
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Парсим HTML-страницу
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем все заголовки новостей (теги <a> с классом item__link)
        news_titles = soup.find_all('a', class_='item__link')
        #print(news_titles)

        # Список для хранения заголовков
        title_list = []
        #print(title_list)

        # Извлекаем текст заголовка и ссылку на новость
        for title in news_titles:
            news_title = title.get_text(strip=True)
            news_link = title['href']
            title_list.append({'title': news_title, 'link': news_link})

        return title_list
    else:
        print(f"Ошибка доступа к сайту: {response.status_code}")
        return []

# Пример использования
titles = parse_rbc_short_news_titles()

# Вывод заголовков
for i, item in enumerate(titles, 1):
    print(f"{i}. {item['title']}")
    print(f"Ссылка: {item['link']}\n")
