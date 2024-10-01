from urllib.parse import urljoin
from urllib.request import urlopen

from bs4 import BeautifulSoup

from db_managers.content_manager import ContentDatabaseManager

url = "https://trial-sport.ru/news.php"

response = urlopen(url)
html = response.read().decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

news_s = soup.find_all('div', class_='article')
# print(news_s)

for new_1 in news_s:
    header_1 = new_1.find('a').text
    print(header_1)

    tags = [item.text for item in new_1.find('p', class_='lite').find_all('a')]
    tags = ','.join(tags)
    print(tags)

    website = (new_1.find('a', class_='more_lnk')).get('href')
    # print(website)
    print(urljoin(url, website))

    textnew = new_1.find_all('p', class_='')
    # print(textnew)
    for textnew2 in textnew:
        list1 = textnew2.text
    print(list1)

    print("\n")

    # with ContentDatabaseManager('content_trial_sport_ru') as db:
    #     db.add_content(header_1, website, tags, list1)

if __name__ == "__main__":
    pass
