import os
import asyncio

from aiogram import Bot, Dispatcher


from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Совесть не позволила писать всё в одном модуле
from handlers.users import user_router

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)

dp = Dispatcher()

dp.include_router(user_router)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True) #что бы удалялись сообщения отправленные когда бот был офлайн
    await dp.start_polling(bot)


asyncio.run(main())
