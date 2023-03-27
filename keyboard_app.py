import telebot


def keyboard_pusk(): # buttons created
    keyboard_markup = telebot.types.ReplyKeyboardMarkup()

    button_genre = telebot.types.KeyboardButton('Жанры фильмов')
    button_random_popular = telebot.types.KeyboardButton('Выборочно популярный фильм')
    button_top_50_better = telebot.types.KeyboardButton('ТОП 50')

    keyboard_markup.row(button_genre) # set in keyboard
    keyboard_markup.row(button_random_popular)
    keyboard_markup.row(button_top_50_better)
    return keyboard_markup