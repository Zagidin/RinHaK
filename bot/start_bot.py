import logging
from bot.bot import dp
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    logging.info('Bot is online!')


def start_bot():
    print('Бот запущен ✔\nВсе обновления пропущена: ', end=' ')
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    print("Бот остановлен ❌")
