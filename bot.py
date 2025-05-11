import asyncio
from aiogram import Bot, Dispatcher, Router


bot = Bot(token='7686255808:AAGvRVhjDAKMZNlNOa3l06BVga7zhbXuEW8')
dp = Dispatcher()
router = Router()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())