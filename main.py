import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("TOKEN")  # Бот-токен із змінних оточення

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привіт! Я працюю!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
