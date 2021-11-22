import re
import telegram
from telegram.keyboardbutton import KeyboardButton
from key_bottons import main_menu

def main_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(main_menu[0])
    ],
    [
        telegram.KeyboardButton(main_menu[1])
    ],
    [
        telegram.KeyboardButton(main_menu[2])
    ],
    [
        telegram.KeyboardButton(main_menu[3])
    ],
    [
        telegram.KeyboardButton(main_menu[4])
    ],
    [
        telegram.KeyboardButton(main_menu[5])
    ]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )
