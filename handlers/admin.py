from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from data.config import ADMIN_ID
from states.strings import Strings
from keyboards.default import markup_keyboard as kb
from utils.database import add_new_string


@dp.message_handler(user_id=ADMIN_ID, commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет я РЖАКИЧ bot🤡')
    await message.answer('🏞Отправь мне картинку, чтобы сделать демотиватор с ним.\n\n'
                         '📝_Если хочешь свою надпись – отправь картинку с текстом в описании._',
                         parse_mode='Markdown',
                         reply_markup=kb.keyboard_admin)


@dp.message_handler(user_id=ADMIN_ID, text=['Добавить фразАчко🌚'])
async def add_string(message: types.Message):
    await message.answer('Пришли новую фразу:', reply_markup=kb.keyboard_back)
    await Strings.new_strings.set()


@dp.message_handler(user_id=ADMIN_ID, commands=['add'])
async def add_string(message: types.Message):
    await message.answer('Пришли новую фразу:', reply_markup=kb.keyboard_back)
    await Strings.new_strings.set()


@dp.message_handler(state=Strings.new_strings)
async def get_string(message: types.Message, state: FSMContext):
    if message.text == 'Назад↩️':
        await message.answer('Ты вернулся назад🐷', reply_markup=kb.keyboard_admin)
        await state.finish()
    else:
        add_new_string(message.text)
        await message.answer('Текст успешно добавлен', reply_markup=kb.keyboard_admin)
        await state.finish()
