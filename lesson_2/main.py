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
from lesson_2.database.db import BlogDb
from lesson_2.database.models import (Base, BlogPost, Writer, Tag)
import requests
import time


base_url = 'https://geekbrains.ru'


def get_text(uri: str) -> dict:
    while True:
        time.sleep(1)
        response = requests.get(f'{base_url}{uri}')
        if response.status_code == 200:
            break
    return response.text


def get_next_page(soup):
    link = soup \
        .find('ul', attrs={'class': 'gb__pagination'}) \
        .find_all('li', attrs={'class': 'page'})[-1] \
        .find('a', attrs={'rel': 'next'})
    return link["href"] if link else None


def get_blog_date(soup):
    return soup\
        .find('div', attrs={'class': 'blogpost-date-views'})\
        .find('time')\
        .get('datetime')


def get_blog_writer(soup):
    author = soup.find('div', attrs={'itemprop': 'author'})
    return {
        'url': author.parent.get('href'),
        'name': author.text,
    }


def get_blog_tags(soup):
    tags = soup.find_all('a', attrs={'class': 'small'})
    return [tag.text for tag in tags]


def get_blog_data(preview_soup):
    title = preview_soup.text
    uri = preview_soup.get("href")

    blog_text = get_text(uri)
    blog_soup = BeautifulSoup(blog_text, 'lxml').find('article', attrs={'class': 'blogpost__article-wrapper'})

    date = get_blog_date(blog_soup)
    writer = get_blog_writer(blog_soup)
    tags = get_blog_tags(blog_soup)

    return uri, title, date, writer, tags


list = []
# next_page = '/posts'
next_page = '/posts?page=52'

db_url = 'sqlite:///blogpost.sqlite'
db = BlogDb(db_url)

while next_page:
    text = get_text(next_page)
    soup = BeautifulSoup(text, 'lxml')

    blogs = soup\
        .find('div', attrs={'class': 'post-items-wrapper'})\
        .find_all('a', attrs={'class': 'post-item__title'})

    for blog in blogs:
        url, title, date, writer, tags = get_blog_data(blog)

        blogpost = BlogPost(title, url, writer, tags)
        db.session.add(blogpost)

        tags = [Tag(itm) for itm tags]
        db.session.add()
        # db.session.commit()
        # db.session.add_all(tags)
        # db.session.commit()

        # db.session.add(Tag('tag_1')) # приводит к ошибке, так как такое имя уже есть
        # db.session.rollback() # сбрасывает сессию, которая повисла из-за ошибки

        # db.session.query(BlogPost).all() # выборка всех объектов
        # tmp = db.session.query(BlogPost).first() # выборка первого объекта
        # tmp.writer.name
        # temp = db.session.query(Tag).filter_by(name='tag_1').all()

        dict = {
            'url': url,
            'title': title,
            'date': date,
            'writer': writer,
            'tags': tags,
        }

        list.append(dict)

    next_page = get_next_page(soup)

print(1)
