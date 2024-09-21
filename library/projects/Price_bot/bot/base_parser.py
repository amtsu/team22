from crud_draft import get_user_links


def parse_prices(user_id):
    links = get_user_links(user_id)
    result = f'Парсер пока не настроен.\nОн будет парсить сохраненные ссылки:\n{links}'
    return result
    # return "Парсер пока не настроен"
