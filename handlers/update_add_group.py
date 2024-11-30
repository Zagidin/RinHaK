# import re
#
# from bot.bot import dp
# from aiogram import types
# from keyboards.admin.panel_group import main_key_group
#
#
# count_group=1
#
#
# @dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
# async def new_chat_member_handler(message: types.Message):
#     """Тут проходим регуляркой по файлу админов, взяв только USER_ID, а потом ID заменять на USERNAME"""
#     global count_group
#     for new_member in message.new_chat_members:
#         if new_member.id == dp.bot.id:
#             chat_id = message.chat.id
#             chat = await dp.bot.get_chat(message.chat.id) # для названия чата-группы
#             if not is_group_id_exists(chat_id):
#                 with open('handlers/GROUP_ID.txt', 'a', encoding='utf-8') as file:
#                     file.write(f"GROUP\n\t{count_group}=> GROUP_ID: {chat_id}\n")
#                 count_group += 1
#                 with open('handlers/user_admin_start.txt', 'r', encoding='utf-8') as file:
#                     match = re.search(r"User_ID:\s*(\d+)", file.read()) # admin_id
#                     match = match.group(1) # ID в чистом виде
#                 admin_username = await dp.bot.get_chat(match)
#
#                 if message.from_user.id == admin_username.id:
#                     await message.answer("Панель Админа Открыт для Администратора 🔐", reply_markup=main_key_group)
#
#                 await message.reply(
#                     text=f"👋 Здравствуйте!\n\n🤖 Я Чат-бот помощник Администратора, группы: <i><b>{chat.title}</b></i>\n"
#                     f"\n😎 Администратор Группы: @{admin_username.username}",
#                     parse_mode='HTML'
#                 )
#             else:
#                 await message.reply(
#                     text=f"Всем Привет 👋 \n"
#                          f"🤖 Я Чат-бот помощник Администратора, группы: <i><b>{chat.title}</b></i>",
#                     parse_mode='HTML'
#                 )
#
#
# def is_group_id_exists(chat_id):
#     """Проверка, существует ли ID группы в файле."""
#     try:
#         with open('handlers/GROUP_ID.txt', 'r', encoding='utf-8') as file:
#             for line in file:
#                 if f"GROUP_ID: {chat_id}" in line:
#                     return True
#     except FileNotFoundError:
#         return False
#     return False
import re
import logging
from bot.bot import dp
from aiogram import types
from keyboards.admin.panel_group import main_key_group

count_group = 1


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_chat_member_handler(message: types.Message):
    """Тут проходим регуляркой по файлу админов, взяв только USER_ID, а потом ID заменять на USERNAME"""
    global count_group
    for new_member in message.new_chat_members:
        if new_member.id == dp.bot.id:  # Если бот добавлен в группу
            chat_id = message.chat.id
            chat = await dp.bot.get_chat(chat_id)  # Получаем название чата-группы

            if not is_group_id_exists(chat_id):
                with open('handlers/GROUP_ID.txt', 'a', encoding='utf-8') as file:
                    file.write(f"GROUP\n\t{count_group}=> GROUP_ID: {chat_id}\n")
                count_group += 1

                with open('handlers/user_admin_start.txt', 'r', encoding='utf-8') as file:
                    match = re.search(r"User_ID:\s*(\d+)", file.read())  # admin_id
                    if match:
                        admin_id = match.group(1)  # ID в чистом виде
                        admin_username = await dp.bot.get_chat(admin_id)

                        if message.from_user.id == admin_username.id:  # Проверяем ID администратора
                            try:
                                await message.answer("Панель Админа Открыт для Администратора 🔐",
                                                     reply_markup=main_key_group)
                            except Exception as e:
                                logging.error(f"Ошибка при отправке панели администратора: {e}")

                        await message.reply(
                            text=f"👋 Здравствуйте!\n\n🤖 Я Чат-бот помощник Администратора, группы: <i><b>{chat.title}</b></i>\n"
                                 f"\n😎 Администратор Группы: @{admin_username.username}",
                            parse_mode='HTML'
                        )
                    else:
                        await message.reply("Не удалось найти ID администратора.")
            else:
                await message.reply(
                    text=f"Всем Привет 👋 \n"
                         f"🤖 Я Чат-бот помощник Администратора, группы: <i><b>{chat.title}</b></i>",
                    parse_mode='HTML'
                )


def is_group_id_exists(chat_id):
    """Проверка, существует ли ID группы в файле."""
    try:
        with open('handlers/GROUP_ID.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if f"GROUP_ID: {chat_id}" in line:
                    return True
    except FileNotFoundError:
        return False
    return False