from os import getenv
from pyrogram import Client
from dotenv import load_dotenv
from configparser import ConfigParser


load_dotenv()

with open('config.ini', 'w') as file_config:
    file_config.write(
        f"[pyrogram]\n"
        f"api_id = {getenv('TG_API_ID')}\n"
        f"api_hash = {getenv('TG_API_HASH')}"
    )

config = ConfigParser()
config.read('config.ini')

api_id = config.get(section='pyrogram', option='api_id')
api_hash = config.get(section='pyrogram', option='api_hash')

pyrogram_client = Client(
    name="my_account",
    api_id=getenv('TG_API_ID'),
    api_hash=getenv('TG_API_HASH')
)

