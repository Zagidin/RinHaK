from bot.bot import dp
from aiogram import types
from keyboards.admin.add_group import keyboard

count_admin = 1

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global count_admin
    if message.chat.type in [types.ChatType.GROUP, types.ChatType.SUPERGROUP]:
        await message.reply("Команда /start недоступна в этой группе.")
    else:
        await message.answer(
            text=f"👋 Здравствуйте, <i><b>{message.from_user.first_name} {message.from_user.last_name}</b></i>!\n"
                 f"\nДобавьте меня в чат-группу по кнопке ниже\n либо самостоятельно."
                 f"\n\n📌 <b><u>Не забудьте предоставить мне все права администрирования</u></b> 😉",
            parse_mode="HTML",
            reply_markup=keyboard
        )

        if not is_user_id_exists(message.from_user.id):
            with open('handlers/user_admin_start.txt', 'a', encoding='utf-8') as file:
                file.write(
                    f"ADMIN \n\t{count_admin}=> User_ID: {message.from_user.id}"
                )
            count_admin += 1


def is_user_id_exists(user_id):
    """Проверка, существует ли User ID в файле."""
    try:
        with open('handlers/user_admin_start.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if f"User_ID: {user_id}" in line:
                    return True
    except FileNotFoundError:
        return False
    return False
