from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton
from aiogram.types import  Message

button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')

animal_keyboard = ReplyKeyboardMarkup(keyboard=[[button_1],[button_2]],
                                      resize_keyboard=True,
                                      one_time_keyboard=True)