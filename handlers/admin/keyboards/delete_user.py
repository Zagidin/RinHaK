from bot.bot import dp
from aiogram.types import Message


@dp.message_handler(text="Удалить 👤")
async def delete_user(message: Message):
    await message.answer(
        text="В разработке ❗\n\n📌 Для удаления, Введите команду /удалить @<ник-пользователя> 🔍"
    )
