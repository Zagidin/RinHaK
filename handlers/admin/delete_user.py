from configparser import ConfigParser
from pyrogram import Client

config = ConfigParser()
config.read('config.ini')

api_id = config.get('pyrogram', 'api_ai')
api_hash = config.get('pyrogram', 'api_hash')

app = Client(name='my_account', api_id=api_id, api_hash=api_hash)

app.run()