import json
import os

FILENAME = 'users_links.json'


def save_user_link(user_id, link):
    if not os.path.exists('data'):
        os.makedirs('data')
    file_path = os.path.join('data', FILENAME)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    if str(user_id) in data:
        data[str(user_id)].append(link)
    else:
        data[str(user_id)] = [link]

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return data[str(user_id)]


def get_user_links(user_id):
    file_path = os.path.join('data', FILENAME)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            links = data.get(str(user_id), [])
    else:
        links = []

    return links


def del_user_links(user_id):
    file_path = os.path.join('data', FILENAME)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            data[str(user_id)] = []
            links = data.get(str(user_id), [])
    else:
        links = []

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    if links == []:
        result = "Ссылки успешно удалены"
    else:
        result = "Что-то пошло не так"

    return result
