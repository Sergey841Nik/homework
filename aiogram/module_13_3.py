import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message()
async def all_massages(message: types.Message) -> None:
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main() -> None:
    await dp.start_polling(bot)


asyncio.run(main())
