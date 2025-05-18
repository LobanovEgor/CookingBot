from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_kb():
    kb_list = [
        [KeyboardButton(text='📋 Menu'), KeyboardButton(text='⚙️ Админ')]
    ]

    return ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)

def admin_kb():
    kb_list = [
        [KeyboardButton(text='🛒 Добавить блюдо'), KeyboardButton(text='✂️ Удалить блюдо')],
        [KeyboardButton(text='❌ Выйти')]
    ]

    return ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)

