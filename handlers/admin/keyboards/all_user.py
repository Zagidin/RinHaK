from bot.bot import dp
from aiogram.types import Message


@dp.message_handler(text="Новая команда ♻")
async def delete_user(message: Message):
    await message.answer(
        text="Пока в разработке ❗\n\n📌 Попробуйте Ввести команду /help 🤔"
    )
