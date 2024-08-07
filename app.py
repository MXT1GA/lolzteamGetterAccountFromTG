from flask import Flask
import requests
import json
from settings import *
app = Flask(__name__)

@app.route('/')
def main_page():
    return 'write user'
@app.route('/<username_tg>/')
def get_id(username_tg):  # put application's code here
    url = f"https://api.zelenka.guru/users/find?custom_fields[telegram]={username_tg}"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {zelenka_token}"
    }

    response = requests.get(url, headers=headers)
    response = response.json()
    answer = {
        'username_tg': username_tg,
        'username_zel': response['users'][0]['username'],
        'status': response['users'][0]['user_title'],
        'avatar': response['users'][0]['links']['avatar'],
        'link': response['users'][0]['links']['permalink']
    }
    a = f"Telegram: @{answer['username_tg']}\nZelenka: {answer['username_zel']}\nСтатус: {answer['status']}\nАватар: {answer['avatar']}\nСсылка на профиль: {answer['link']}"
    return a


if __name__ == '__main__':
    app.run()
