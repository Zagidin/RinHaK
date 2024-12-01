from os import getenv
from dotenv import load_dotenv
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

load_dotenv()

invite_button = InlineKeyboardButton(
    text="🤖 Добавить бота в чат",
    url=f"https://t.me/{getenv('USERNAME_BOT')}?startgroup=true"
)

keyboard = InlineKeyboardMarkup().add(invite_button)
