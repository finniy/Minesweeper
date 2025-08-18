from aiogram import Bot, Dispatcher
from app.config import API_KEY

# Создаём объект бота
bot = Bot(token=API_KEY)

# Диспетчер для обработки апдейтов
dp = Dispatcher()