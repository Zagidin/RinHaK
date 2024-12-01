import re
from bot.bot import dp
from aiogram import types
from bot.client.client import pyrogram_client
from handlers.open_files import list_group_id

@dp.message_handler(commands=['удалить', 'delete'])
async def delete_user_all_group(message: types.Message):
    if message.chat.type in [types.ChatType.GROUP, types.ChatType.SUPERGROUP]:
        await message.reply("Команда /удалить недоступна в этой группе.")
    else:
        admin_command = message.text.split()

        if len(admin_command) != 2:
            await message.reply(
                text="❌ Неверно прописана команда ❗\n"
                     "\nВведите команду:\n\n/удалить @<ник-пользователя>."
            )
            return

        username = admin_command[1].lstrip('@')

        # Ищем пользователя -> Pyrogram
        try:
            user = await pyrogram_client.get_users(username)
            user_id = user.id  # user_id пользователя
            await message.reply("🤖 Отлично, начинаю удаление...")

            # Блокировка пользователя во всех группах
            for chat_id in list_group_id:
                try:
                    await message.bot.ban_chat_member(chat_id, user_id)
                    await message.answer(f"Пользователь @{username} был удалён в группе с ID: {chat_id}.")
                except Exception as e:
                    # Проверка на ошибку миграции группы
                    match = re.search(r'New id: (-?\d+)', str(e))
                    if match:
                        new_chat_id = int(match.group(1))  # Новый ID супергруппы
                        await message.reply(
                            text=f"Группа с ID {chat_id} была мигрирована в супергруппу. Новый ID: {new_chat_id}. Попробую снова."
                        )
                        # Попробуем заблокировать пользователя в новой супергруппе
                        await message.bot.kick_chat_member(new_chat_id, user_id)
                        await message.reply(f"Пользователь @{username} был удалён в супергруппе с ID: {new_chat_id}.")
                    else:
                        # В случае другой ошибки
                        await message.reply(
                            text=f"Ошибка при удаления пользователя в группе с ID {chat_id}: {e}"
                        )

            await message.reply("✅ Пользователь был заблокирован и удалён во всех Чат-Группах.")

        except Exception as e:
            await message.reply(
                text=f"Ошибка при получении user_id для @{username}: {e}"
            )
