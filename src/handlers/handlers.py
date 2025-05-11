import aiogram
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.keyboards.reply_kb import main_kb


router = Router()
@router.message(Command('start'))
async def start(message: Message):
    await message.answer('Добро пожаловать в бот для выбора еды на ужин!', reply_markup=main_kb())

