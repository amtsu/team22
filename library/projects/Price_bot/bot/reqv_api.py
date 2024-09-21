import requests


URL = "http://127.0.0.1:8000/links/"


def save_user_link(user_id, link):
    data = {
        "user_id": str(user_id),
        "link": link
    }
    return requests.post(URL, json=data).text


def get_user_links(user_id):
    url = f"http://127.0.0.1:8000/links/{user_id}"
    return requests.get(url).text


def del_user_links(user_id):
    url = f"http://127.0.0.1:8000/links/{user_id}"
    requests.delete(url)
    return "Ссылки успешно удалены"
