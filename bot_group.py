import random
import telebot
from config import token
from bs4 import BeautifulSoup as bs
from keyboard_app import keyboard_pusk
import requests
from inlines_btn import spisok_horror

bot = telebot.TeleBot(token) # экземпляр
name = ''
spisok_films = []

# spisok_horror_film = []
# spisok_comdy_film = []
# spisok_mult_film = []

# обычные кнопки
def spisok_500():
    global spisok_films
    if len(spisok_films) == 0:
        response_get = requests.get('url')
        soup = bs(response_get.text, features='html.parser')  # парсим страницу
        qutes_films = soup.find_all('b')
        for film in qutes_films:
            spisok_films.append(film.text)
        return random.choice(spisok_films)
    else:
        return random.choice(spisok_films)


# inline кнопки (import inlines_btn.py)


@bot.message_handler(commands=['start']) # запускаем обработчик
def start_command(message):
    poem = 'Привет мой дорогой друг!\nКак тебя зовут?'
    bot.send_message(message.chat.id, poem)
    bot.register_next_step_handler(message, reqister_name) # регаем с этой коммандой Имя юзера которое он ввел
def reqister_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, f'Приятно познакомится, {name} \nДля старта нажмите /pusk\nЕсли нужна какая-либо помощь, нажмите /help')


@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = '''
Для начала выбора фильмов нажмите комманду /pusk
Для помощи нажмите комманду /help
Чтобы начать сначала /start
Не забывайте использовать клавиатуру, так удобнее
    '''
    bot.send_message(message.chat.id, help_text)


# def keyboard_pusk(): тут клавиатура, которую импортнули с другого файла (keyboard_app.py)


# создали клавиатуру inline
def keyboadr_genre():
    keyb_genre_reply = telebot.types.InlineKeyboardMarkup()
    key_comedy = telebot.types.InlineKeyboardButton(text='Комедии', callback_data='comedy')
    key_mult = telebot.types.InlineKeyboardButton(text='Мультфильмы', callback_data='mult')
    key_fantasy = telebot.types.InlineKeyboardButton(text='Фентези', callback_data='fantasy')
    key_horror = telebot.types.InlineKeyboardButton(text='Ужасы', callback_data='horror')
    # добавляем
    keyb_genre_reply.add(key_comedy, key_mult, key_fantasy, key_horror)
    return keyb_genre_reply


@bot.message_handler(commands=['pusk'])
def pusk_name(message):
    bot.send_message(message.chat.id, 'GO!', reply_markup=keyboard_pusk()) # привязали клавиатуру

@bot.message_handler(content_types=['text']) # для keyboard_pusk и прикрепляем keyboadr_genre
def genre_reply(message):
    if message.text == 'Жанры фильмов':
        bot.send_message(message.chat.id, 'Выберете один из жанров:', reply_markup=keyboadr_genre())
    if message.text == 'Выборочно популярный фильм':
        pass
        #bot.send_message(message.chat.id, 'Выберете один из жанров:', reply_markup=keyboadr_genre())
    if message.text == 'ТОП 50':
        bot.send_message(message.chat.id, spisok_500())

                        # парсим сайт и получаем список
        # response_get = requests.get('link')
        # soup = bs(response_get.text, features='html.parser')
        # qutes_films = soup.find_all('b') # тег
        # for film in qutes_films:
        #     print(film.text)

                    # получили ответ
        # response_get = requests.get('link')
        # print(response_get.status_code)


@bot.callback_query_handler(func=lambda call: True) # для callback_data
def genre_reply_but(call):
    if call.data == 'comedy':
        bot.send_message(call.message.chat.id, 'Вы выбрали комеди') # обработчик комедии
        # bot.send_message(call.message.chat.id, spisok_comedy())

    if call.data == 'mult':
        bot.send_message(call.message.chat.id, 'вы выбрали мультфильмы')

    if call.data == 'fantasy':
        bot.send_message(call.message.chat.id, 'Вы выбрали фентези')

    if call.data == 'horror':
        bot.send_message(call.message.chat.id, spisok_horror())


bot.polling() # запустили бота

