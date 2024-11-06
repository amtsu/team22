import warnings
import requests  # Библиотека для отправки запросов
import time  # Библиотека для времени
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import hashlib
import os
import psycopg2
from psycopg2 import sql

warnings.filterwarnings("ignore")

# Подключение к PostgreSQL
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "myanimelist_db"
DB_USER = "myanimelist_db"
DB_PASSWORD = "myanimelist_dbmyanimelist_db"

conn = psycopg2.connect(
    host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
)
cursor = conn.cursor()

# Создадим таблицу, если она еще не существует
cursor.execute(
    """  
    CREATE TABLE IF NOT EXISTS anime (        
        id SERIAL PRIMARY KEY,        
        anime_id INTEGER UNIQUE,        
        ranked INTEGER,        
        popularity INTEGER,        
        members INTEGER,        
        rating DECIMAL(4, 2),        
        description TEXT,        
        url TEXT, 
        title TEXT,
        set INTEGER     
    )    """
)
conn.commit()


def get_md5_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def get_with_cache(page_link: str) -> (str, bool):
    hash_name = get_md5_hash(page_link)
    cache_path = f"files/{hash_name}.html"
    if os.path.exists(cache_path):
        with open(cache_path, encoding="utf-8") as file:
            return file.read(), True
    else:
        response = requests.get(page_link, headers={"User-Agent": UserAgent().chrome})
        if response:
            page_content = response.text
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            with open(cache_path, "w", encoding="utf-8") as file:
                file.write(page_content)
            return page_content, False
        else:
            print("no response")


def get_title_data(link: str):
    (title_text, is_cached) = get_with_cache(link)
    soup = BeautifulSoup(title_text, "html.parser")

    # Извлечение рейтинга (rating)
    try:
        rating = soup.find("span", itemprop="ratingValue").text.strip()
    except AttributeError:
        rating = None  # 'N/A' означает "нет данных"

    # Извлечение места в рейтинге (ranked)
    try:
        ranked = (
            soup.find("div", {"data-id": "info2"})
            .find("span", class_="dark_text")
            .next_sibling.strip()
        )
        ranked = ranked.replace("#", "")  # Убираем символ #
        ranked = int(ranked)
    except AttributeError:
        ranked = None
    except Exception:
        ranked = None

        # Извлечение популярности (popularity)
    try:
        popularity = soup.find("span", string="Popularity:").next_sibling.strip()
        popularity = popularity.replace("#", "")  # Убираем символ #
    except AttributeError:
        popularity = None

        # Извлечение количества членов (members)
    try:
        members = soup.find("span", string="Members:").next_sibling.strip()
        members = members.replace(",", "")  # Убираем запятые для преобразования в число
    except AttributeError:
        members = None

        # Извлечение описания (description)
    try:
        description = soup.find("p", itemprop="description").get_text(separator=" ").strip()
    except AttributeError:
        description = None

    return rating, ranked, popularity, members, description, is_cached


def insert_data_to_db(anime_id, ranked, popularity, members, rating, description, url, title):
    try:
        cursor.execute(
            sql.SQL(
                """  
                INSERT INTO anime (anime_id, ranked, popularity, members,  rating, description, url, title)                
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)                
                ON CONFLICT (anime_id) DO NOTHING                """
            ),
            (anime_id, ranked, popularity, members, rating, description, url, title),
        )
        conn.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")


def parse_all_pages():
    page_link = "https://myanimelist.net/topanime.php"
    # page_link = "https://myanimelist.net/topanime.php?limit=23500"

    for i in range(1, 1000):
        # page_link = "https://myanimelist.net/topanime.php?limit=50"
        print(get_md5_hash(page_link))

        (page_text, is_cached) = get_with_cache(page_link)

        soup = BeautifulSoup(page_text, "html.parser")
        # Ищем все элементы <li>, содержащие <span> с классом 'rank' и <a> внутри
        links = soup.find_all("tr", {"class": lambda x: x == "ranking-list"})

        # Фильтруем только те элементы <tr>, которые соответствуют условиям
        filtered_links = []
        for tr in links:
            if tr.find("a"):
                href = tr.find("a")["href"]
                if isinstance(href, str) and href.startswith(
                        "https://myanimelist.net/anime/"
                ):
                    filtered_links.append(tr.find("a")["href"])

        for link in filtered_links:
            try:
                anime_id = int(link.split("/")[-2])
                rating, ranked, popularity, members, description, cached = get_title_data(link)
                insert_data_to_db(anime_id, ranked, popularity, members, rating, description, link, link.split("/")[-1])
                print(
                    f"{link.split("/")[-1]}: Rating: {rating}, Ranked: {ranked}, Popularity: {popularity}, Members: {members}"
                )
                if not cached:
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                continue

        next_link = soup.find("link", {"rel": lambda x: x == "next"})
        if next_link:
            next = next_link["href"]
            print(f"Next: {next}")
            page_link = next
            # time.sleep(3)
        else:
            break


parse_all_pages()
