from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_back = KeyboardButton('Назад↩️')

keyboard_back = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)
# -----------------------------------------------------------------------------------------------------------------------
add_button = KeyboardButton('Добавить фразАчко🌚')

keyboard_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(add_button)
