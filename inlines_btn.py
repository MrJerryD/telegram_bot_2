import random
from bs4 import BeautifulSoup as bs
import requests
spisok_horror_film = []

def spisok_horror():
    global spisok_horror_film
    if len(spisok_horror_film) == 0:
        response_get = requests.get('url')
        soup = bs(response_get.text, features='html.parser')  # парсим страницу
        quotes_films = soup.find_all('a')
        for horror_f in quotes_films:
            spisok_horror_film.append(horror_f.text)
        return random.choice(spisok_horror_film)
    else:
        return random.choice(spisok_horror_film)