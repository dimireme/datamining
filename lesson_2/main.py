# Используя `bs4` и рессурс `https://geekbrains.ru/posts`
# пройти ленту статей блога, получить страницу с статьей, извлечь следующие данные:
# * заголовок статьи
# * дата публикации
# * url статьи
# * список тегов
# * имя автора
# * url автора
#
# При помощи `sqlalchemy` сохранить данные в базу.
# Обязательно теги и автор должны существовать отдельными таблицами,
# и должны быть корректно реализованы соответсвующие связи.

from bs4 import BeautifulSoup
import requests
import time


def get_data(url: str, params: dict) -> dict:
    while True:
        time.sleep(1)
        response = requests.get(url, params=params)
        if response.status_code == 200:
            break
    return response.text


url = "https://geekbrains.ru/posts"
text = get_data(url, {})

soup = BeautifulSoup(text, 'html.parser')
# inner_html = soup.find('span',  class_="total-users").string
# count = re.search(r'\d[\d\s]+\d', inner_html).group().replace(' ', '')
# print(count)

print(1)
