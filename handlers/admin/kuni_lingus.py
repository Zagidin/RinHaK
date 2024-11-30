from bot.bot import dp, bot
from aiogram import types


# @dp.message_handler(commands=['удалить'])
# async def kick_user(message: types.Message):
#     # Проверяем, что команда была вызвана в группе
#     if message.chat.type in ['group', 'supergroup']:
#         # Проверяем, что сообщение является ответом на другое сообщение
#         if message.reply_to_message:
#             user_id = message.reply_to_message.from_user.id  # Получаем ID пользователя из сообщения
#             try:
#                 # Кикаем пользователя из группы
#                 await message.bot.kick_chat_member(message.chat.id, user_id)
#                 await message.bot.unban_chat_member(message.chat.id, user_id)  # Разрешаем повторное добавление
#                 await message.answer(f"Пользователь {message.reply_to_message.from_user.full_name} был удален из группы.")
#             except Exception as e:
#                 await message.answer(f"Не удалось удалить пользователя: {e}")
#         else:
#             await message.answer("Пожалуйста, ответьте на сообщение пользователя, которого хотите удалить.")
#     else:
#         await message.answer("Эта команда доступна только в группах.")


# @dp.message_handler(commands=['kick'])
# async def kick_user(message: types.Message):
#     # Проверяем, что команда была вызвана в группе
#     global user_id, username
#     if message.chat.type in ['group', 'supergroup']:
#         # Проверяем наличие упоминания пользователя
#         if message.reply_to_message:
#             user_id = message.reply_to_message.from_user.id  # Получаем ID пользователя из сообщения
#         else:
#             # Проверяем, есть ли упоминание в тексте команды
#             if len(message.entities) > 0:
#                 for entity in message.entities:
#                     if entity.type == 'mention':
#                         username = message.text[entity.offset:entity.offset + entity.length]
#                         # Убираем "@" из имени пользователя
#                         username = username[1:]
#                         try:
#                             user = await bot.get_chat(username)
#                             user_id = user.id
#                         except Exception as e:
#                             await message.answer(f"Не удалось получить пользователя: {e}")
#                             return
#
#                 if not user_id:
#                     await message.answer("Пользователь не найден.")
#                     return
#             else:
#                 await message.answer("Пожалуйста, укажите пользователя для удаления через упоминание.")
#                 return
#
#         try:
#             # Кикаем пользователя из группы
#             await bot.kick_chat_member(message.chat.id, user_id)
#             await bot.unban_chat_member(message.chat.id, user_id)  # Разрешаем повторное добавление
#             await message.answer(f"Пользователь {username} был удален из группы.")
#         except Exception as e:
#             await message.answer(f"Не удалось удалить пользователя: {e}")
#     else:
#         await message.answer("Эта команда доступна только в группах.")

# @dp.message_handler(commands=['kick'])
# async def kick_user(message: types.Message):
#     # Проверяем, что команда была вызвана в группе
#     if message.chat.type not in ['group', 'supergroup']:
#         await message.answer("Эта команда доступна только в группах.")
#         return
#
#     user_id = None
#     username = None
#
#     # Проверяем, есть ли ответ на сообщение (reply)
#     if message.reply_to_message:
#         user_id = message.reply_to_message.from_user.id  # Получаем ID пользователя из ответа
#         username = message.reply_to_message.from_user.username
#     else:
#         # Проверяем, есть ли упоминание в тексте команды
#         if len(message.entities) > 0:
#             for entity in message.entities:
#                 if entity.type == 'mention':  # Если это упоминание
#                     username = message.text[entity.offset + 1: entity.offset + entity.length]
#                     try:
#                         # Получаем информацию о пользователе по username
#                         chat_member = await bot.get_chat_member(message.chat.id, username)
#                         user_id = chat_member.user.id
#                     except Exception as e:
#                         await message.answer(f"Не удалось получить пользователя: {e}")
#                         return
#
#         if not user_id:
#             await message.answer("Пожалуйста, укажите пользователя для удаления через упоминание или ответьте на сообщение пользователя.")
#             return
#
#     try:
#         # Кикаем пользователя из группы
#         await bot.kick_chat_member(message.chat.id, user_id)
#         await bot.unban_chat_member(message.chat.id, user_id)  # Разрешаем повторное добавление
#         await message.answer(f"Пользователь @{username} был удален из группы.")
#     except Exception as e:
#         await message.answer(f"Не удалось удалить пользователя: {e}")

# @dp.message_handler(commands=['kick'])
# async def kick_user(message: types.Message):
#     # Проверяем, что команда была вызвана в группе
#     if message.chat.type not in ['group', 'supergroup']:
#         await message.answer("Эта команда доступна только в группах.")
#         return
#
#     # Проверяем, есть ли упоминание пользователя в тексте команды
#     command_parts = message.text.split()
#     if len(command_parts) != 2:
#         await message.answer("Неверный формат команды. Используйте: /kick @username")
#         return
#
#     username = command_parts[1].lstrip('@')  # Убираем символ "@" из начала никнейма
#
#     try:
#         # Получаем информацию о пользователе по его username
#         chat_member = await bot.get_chat(message.chat.id, username)
#
#         # Получаем user_id пользователя
#         user_id = chat_member.user.id
#
#         # Проверяем, что пользователь существует в чате
#         if chat_member.status in ['member', 'administrator', 'creator']:
#             try:
#                 # Кикаем пользователя из группы
#                 await bot.kick_chat_member(message.chat.id, user_id)
#                 await bot.unban_chat_member(message.chat.id, user_id)  # Разрешаем повторное добавление
#                 await message.answer(f"Пользователь @{username} был удален из группы.")
#             except Exception as e:
#                 await message.answer(f"Не удалось удалить пользователя @{username}: {e}")
#         else:
#             await message.answer(f"Пользователь @{username} не найден в чате.")
#     except Exception as e:
#         await message.answer(f"Не удалось найти пользователя с ником @{username}: {e}")

# @dp.message_handler(commands=['kick'])
# async def kick_user(message: types.Message):
#     # Проверяем, что команда была вызвана в группе
#     if message.chat.type in ['group', 'supergroup']:
#         # Проверяем наличие упоминания в тексте команды
#         if len(message.entities) > 0:
#             for entity in message.entities:
#                 if entity.type == 'mention':
#                     username = message.text[entity.offset:entity.offset + entity.length][1:]  # Убираем "@" из имени пользователя
#                     try:
#                         # Получаем информацию о пользователе по username
#                         member = await bot.get_chat_member(message.chat.id, username)
#                         user_id = member.user.id
#
#                         # Кикаем пользователя из группы
#                         await bot.kick_chat_member(message.chat.id, user_id)
#                         await message.answer(f"Пользователь {username} был удален из группы.")
#                     except Exception as e:
#                         await message.answer(f"Не удалось удалить пользователя: {e}")
#                     return
#
#         await message.answer("Пожалуйста, укажите пользователя для удаления через упоминание.")
#     else:
#         await message.answer("Эта команда доступна только в группах.")

# @dp.message_handler(commands=['kick'])
# async def kick_user(message: types.Message):
#     # Проверяем, что команда была вызвана в группе
#     if message.chat.type in ['group', 'supergroup']:
#         # Проверяем наличие упоминания в тексте команды
#         if len(message.entities) > 0:
#             for entity in message.entities:
#                 if entity.type == 'mention':
#                     username = message.text[entity.offset:entity.offset + entity.length][1:]  # Убираем "@" из имени пользователя
#                     try:
#                         # Получаем информацию о пользователе по username
#                         member = await bot.get_chat_member(message.chat.id, username)
#                         user_id = member.user.id
#
#                         # Кикаем пользователя из группы
#                         await bot.kick_chat_member(message.chat.id, user_id)
#                         await message.answer(f"Пользователь {username} был удален из группы.")
#                     except Exception as e:
#                         await message.answer(f"Не удалось удалить пользователя: {e}")
#                     return
#
#         await message.answer("Пожалуйста, укажите пользователя для удаления через упоминание.")
#     else:
#         await message.answer("Эта команда доступна только в группах.")

# chats = [-1002316480049]
#
# # Функция для удаления пользователя
# @dp.message_handler(commands=['Удалить'])
# async def cmd_remove_user(message: types.Message):
#     if 930661860 == message.from_user.id:
#         args = message.get_args()
#
#         if not args:
#             await message.reply("Используйте команду в формате: /Удалить @ник")
#             return
#
#         username_to_remove = args.strip()
#
#         # Проходим по всем чатам, в которых добавлен бот
#         for chat_id in chats:
#             try:
#                 user = await bot.get_chat_member(chat_id, username_to_remove)
#                 if user.status in ['member', 'administrator', 'creator']:
#                     await bot.kick_chat_member(chat_id, user.user.id)
#                     await message.reply(f"Пользователь {username_to_remove} был удалён из чата {chat_id}.")
#             except Exception as e:
#                 await message.reply(f"Не удалось удалить пользователя {username_to_remove} из чата {chat_id}: {str(e)}")
#     else:
#         await message.reply("Только администратор может удалить пользователя.")

# @dp.message_handler(commands=['kick'])
# async def kick_user(message: types.Message):
#     # Проверяем, что команда была вызвана в группе
#     if message.chat.type in ['group', 'supergroup']:
#         # Проверяем наличие упоминания в тексте команды
#         if message.entities:
#             for entity in message.entities:
#                 if entity.type == 'mention':
#                     username = message.text[entity.offset:entity.offset + entity.length][1:]  # Убираем "@" из имени пользователя
#                     try:
#                         # Получаем информацию о пользователе по username
#                         member = await bot.get_chat_member(message.chat.id, username)
#                         user_id = member.user.id
#
#                         # Кикаем пользователя из группы
#                         await bot.kick_chat_member(message.chat.id, user_id)
#                         await bot.unban_chat_member(message.chat.id, user_id)  # Разрешаем повторное добавление
#                         await message.answer(f"Пользователь {username} был удален из группы.")
#                     except Exception as e:
#                         await message.answer(f"Не удалось удалить пользователя: {e}")
#                     return
#
#         await message.answer("Пожалуйста, укажите пользователя для удаления через упоминание.")
#     else:
#         await message.answer("Эта команда доступна только в группах.")

# @dp.message_handler(commands=['kick'])
# async def kick_user(message: types.Message):
#     # Проверяем, что команда была вызвана в группе
#     if message.chat.type in ['group', 'supergroup']:
#         # Проверяем наличие упоминания в тексте команды
#         if message.entities:
#             for entity in message.entities:
#                 if entity.type == 'mention':
#                     # Получаем username с символом "@" для вывода
#                     username_with_at = message.text[entity.offset:entity.offset + entity.length]
#                     username = username_with_at[1:]  # Убираем "@" для использования в get_chat_member
#
#                     try:
#                         # Получаем информацию о пользователе по username
#                         member = await bot.get_chat_member(message.chat.id, username)
#                         user_id = member.user.id
#
#                         # Кикаем пользователя из группы
#                         await bot.kick_chat_member(message.chat.id, user_id)
#                         await bot.unban_chat_member(message.chat.id, user_id)  # Разрешаем повторное добавление
#                         await message.answer(f"Пользователь {username_with_at} был удален из группы.")
#                     except Exception as e:
#                         await message.answer(f"Не удалось удалить пользователя: {e}")
#                     return
#
#         await message.answer("Пожалуйста, укажите пользователя для удаления через упоминание.")
#     else:
#         await message.answer("Эта команда доступна только в группах.")

@dp.message_handler(commands=['kick'])
async def kick_user(message: types.Message):
    # Проверяем, что команда была вызвана в группе
    if message.chat.type in ['group', 'supergroup']:
        # Проверяем наличие упоминания в тексте команды
        if message.entities:
            for entity in message.entities:
                if entity.type == 'mention':
                    # Получаем username с символом "@" для вывода
                    username_with_at = message.text[entity.offset:entity.offset + entity.length]
                    username = username_with_at[1:]  # Убираем "@" для использования в get_chat_member

                    try:
                        # Получаем список участников группы
                        members = await bot.get_chat_members(message.chat.id)

                        # Ищем пользователя по username
                        user_id = None
                        for member in members:
                            if member.user.username == username:
                                user_id = member.user.id
                                break

                        if user_id is not None:
                            # Кикаем пользователя из группы
                            await bot.kick_chat_member(message.chat.id, user_id)
                            await bot.unban_chat_member(message.chat.id, user_id)  # Разрешаем повторное добавление
                            await message.answer(f"Пользователь {username_with_at} был удален из группы.")
                        else:
                            await message.answer("Пользователь не найден.")
                    except Exception as e:
                        await message.answer(f"Не удалось удалить пользователя: {e}")
                    return

        await message.answer("Пожалуйста, укажите пользователя для удаления через упоминание.")
    else:
        await message.answer("Эта команда доступна только в группах.")
