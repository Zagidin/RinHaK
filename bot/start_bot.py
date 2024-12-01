import logging
from bot.bot import dp
from aiogram.utils import executor
from bot.client.client import pyrogram_client

logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    logging.info('Бот в Логировании Запущен ✔')

def start_bot():
    """Первым Запускаем Клиента (Вход в аккаун в ТГ),
            а уже после бота, если будет наооброт не работает"""
    pyrogram_client.start()
    print('Бот запущен ✔\nВсе обновления пропущена: ', end=' ')
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    print("Бот остановлен ❌")
