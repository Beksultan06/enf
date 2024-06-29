import os
import django
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Создаем бота и диспетчера
bot = Bot(token='6573964275:AAFQYZ_JqNA9ND4hGhYNX4fvutv1D-sE-RA')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
