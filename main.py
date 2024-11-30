# from handlers import dp
# from bot.start_bot import start_bot
from configparser import ConfigParser
from pyrogram import Client

config = ConfigParser()
config.read('config.ini')

api_id = config.get('pyrogram', 'api_id')
api_hash = config.get('pyrogram', 'api_hash')

app = Client(name='my_account', api_id=api_id, api_hash=api_hash)

app.run()


# __all__ = ["dp"]
#
#
# if __name__ == '__main__':
#     start_bot()
