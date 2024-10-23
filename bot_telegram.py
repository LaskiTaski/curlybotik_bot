from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
from aiogram import Bot
import os

load_dotenv()
storage = MemoryStorage()


TOKEN = os.getenv('TOKEN_API')
TARGET_CHAT_ID = os.getenv('TARGET_CHAT_ID')

bot = Bot(token=TOKEN, parse_mode='Markdown')
dp = Dispatcher(bot, storage=storage)
