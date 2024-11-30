from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

invite_button = InlineKeyboardButton(
    text="🤖 Добавить бота в чат",
    url="https://t.me/RinHacksoftbot?startgroup=true"
)

keyboard = InlineKeyboardMarkup().add(invite_button)
