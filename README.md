# datamining
Homework at geekbrains course "Datamining".

<details>
<summary>

### Урок 1. Основы клиент-серверного взаимодействия. Парсинг API

</summary>

##### Задача 1. 

Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

##### Задача 2.

Изучить список открытых API.
Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

##### Задача 3.
Рессурс к парсингу `https://5ka.ru/`. Необходимо собрать все данные с раздела товаров по акции и сохранить в json файлы, где имя файла это имя категории товара.

Структура данных в виде:

```text
{
    category_id: str,  - уникальный идентификатор категории
    category_name: str, - человекочитаемое имя категории
    items: list - список товаров пренадлежищий к данной категории
}
```

</details>

<details>
<summary>

### Урок 2. Парсинг HTML. BeautifulSoup, MongoDB.

</summary>

##### Задача.

Используя `bs4` и рессурс `https://geekbrains.ru/posts` пройти ленту статей блога, получить страницу с статьей, извлечь следующие данные:

* заголовок статьи
* дата публикации
* url статьи
* список тегов
* имя автора
* url автора

При помощи `sqlalchemy` сохранить данные в базу. Обязательно теги и автор должны существовать отдельными таблицами, и должны быть корректно реализованы соответсвующие связи.

</details>