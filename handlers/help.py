from bot.bot import dp
from aiogram import types


@dp.message_handler(commands=["help"])
async def help_bot(msg: types.Message):
    if msg.chat.type in [types.ChatType.GROUP, types.ChatType.SUPERGROUP]:
        await msg.reply("Команда /help доступна для администратора.")
    else:
        await msg.answer(
            text="🤖 Режим просмотра способностей Чат-бота 🕶\n"
                 "\n\t📚 Доступные команды:\n\n"
                 "/удалить - Удаление Пользователя 👤\n"
                 "/start - Начальная настройка Чат-Бота 🏚\n"
                 "<b><i>В РАЗРАБОТКЕ ...</i></b>",
            parse_mode="HTML"
        )