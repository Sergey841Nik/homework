import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())  # найти и загрузить переменные окружения из файла .env

TOKEN = os.getenv("TOKEN")  # получаем токен из переменного окружения

bot = Bot(token=TOKEN)

# экземпляр класса Bot сюда передаётся через start_polling
# по умолчанию storage=MemoryStorage()
# поэтому не передаём в Dispatcher() ни каких данных, как в видео уроке
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message) -> None:
    print("Привет! Я бот помогающий твоему здоровью.")
    # ответ от бота в ТГ на команду /start
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message()
async def all_massages(message: types.Message) -> None:
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")
    # дразнит (отвечает эхом)
    await message.answer(message.text)


async def main() -> None:
    await dp.start_polling(bot)


asyncio.run(main())
