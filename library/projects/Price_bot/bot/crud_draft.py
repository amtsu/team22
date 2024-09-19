import json
import os


def save_user_link(user_id, link, filename='users_links.json'):
    if not os.path.exists('data'):
        os.makedirs('data')
    file_path = os.path.join('data', filename)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    data[user_id] = link

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return data


def get_user_links(user_id, link, filename='users_links.json'):
    "добавить фильтрацию по айди"
    file_path = os.path.join('data', filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    return data
