import aiogram
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from database import database as db
from database.database import check_admin, insert_user, insert_food
from src.keyboards.reply_kb import main_kb, admin_kb


class States(StatesGroup):
    waiting_for_input = State()
    waiting_for_name = State()

router = Router()
@router.message(Command('start'))
async def start(message: Message):
    await message.answer('Добро пожаловать в бот для выбора еды на ужин!', reply_markup=main_kb())
    await insert_user(message.from_user.id, False)

@router.message(aiogram.F.text.lower() == '⚙️ админ')
async def admin_panel(message: Message, state: FSMContext):
    if await check_admin(message.from_user.id):
        await message.answer('Добро пожаловать в админ панель', reply_markup=admin_kb())
    else:
        await message.answer('Нужно ввести пароль')
        await state.set_state(States.waiting_for_input)

@router.message(States.waiting_for_input)
async def process_pass_input(message: Message, state: FSMContext):
    if message.text.strip() == '12345':
        await message.answer('✅ Пароль верный, доступ открыт')
        await db.change_admin(message.from_user.id)
    else:
        await message.answer('❌ Неверный пароль!')

@router.message(aiogram.F.text.lower() == '❌ выйти')
async def quit_panel(message: Message):
    await message.answer('Выходим из админ панели', reply_markup=main_kb())

@router.message(aiogram.F.text.lower() == '🛒 добавить блюдо')
async def add_food(message: Message, state: FSMContext):
    await message.answer('Введите название и загрузите картинку')
    await state.set_state(States.waiting_for_name)

@router.message(States.waiting_for_name)
async def get_food_name(message: Message):
    photo = message.photo[-1].file_id
    name = message.text
    await insert_food(name, photo)