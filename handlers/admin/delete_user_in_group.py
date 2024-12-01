from bot.bot import dp
from aiogram import types
from bot.client.client import pyrogram_client


@dp.message_handler(commands=['ban'])
async def delete_user_in_group(message: types.Message):
    command_parts = message.text.split()

    if len(command_parts) != 2:
        await message.reply("❌ Неверно прописана команда ❗\n\nВведите команду:\n\n/удалить @<ник-пользователя>.")
        return

    username = command_parts[1]

    username = username.lstrip('@')

    # Ищем пользователя -> Pyrogram
    try:
        user = await pyrogram_client.get_users(username)
        user_id = user.id # user_id пользователя
        await dp.bot.send_message(
            message.from_user.id,
            text=f"Удален Пользователь:\n"
                 f"\n👤 <b>Username: <i>@{username}</i></b>"
                 f"\n\n🌐 https://t.me/{username}",
            parse_mode='HTML'
        )
        await message.bot.kick_chat_member(message.chat.id, user_id)
    except Exception as e:
        await dp.bot.send_message(
            message.from_user.id,
            text=f"Ошибка при получении user_id для @{username}: {e}"
        )