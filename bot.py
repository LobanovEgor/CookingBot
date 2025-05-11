import asyncio
from aiogram import Bot, Dispatcher, Router
import logging
from src.handlers.handlers import router


bot = Bot(token='7686255808:AAGvRVhjDAKMZNlNOa3l06BVga7zhbXuEW8')
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())