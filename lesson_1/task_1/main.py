# Посмотреть документацию к API GitHub,
# разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import time
import json


def get_data(url: str, params: dict) -> dict:
    while True:
        time.sleep(1)
        response = requests.get(url, params=params)
        if response.status_code == 200:
            break
    return response.json()


def save_to_json_file(filename: str, data: dict):
    with open(filename, 'w') as file:
        json.dump(data, file)


username = 'dimireme'
url = 'https://api.github.com'
endpoint = f'/users/{username}/repos'

data = get_data(f'{url}{endpoint}', {})
save_to_json_file('data.json', data)

print(1)
