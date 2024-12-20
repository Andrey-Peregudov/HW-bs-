import requests
from bs4 import BeautifulSoup

def get_curs():
    url = 'https://www.cbr.ru'

    response = requests.get(url)
    list = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        lst = soup.findAll('div', class_='col-md-2 col-xs-9 _right mono-num')


        return f'Курс доллара на сегодня: {lst[2].text}''\n'f'Курс евро на сегодня: {lst[4].text}'

