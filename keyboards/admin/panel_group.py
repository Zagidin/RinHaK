from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_key_group = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="Удалить 👤")
btn2 = KeyboardButton(text="Новая команда ♻")
main_key_group.row(btn1, btn2)
