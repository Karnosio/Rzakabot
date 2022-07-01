import logging

from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from loader import dp, bot
from utils.utils import make_image, check_caption


logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет я РЖАКИЧ bot🤡')
    await message.answer('🏞Отправь мне картинку, чтобы сделать демотиватор с ним.\n\n'
                         '📝_Если хочешь свою надпись – отправь картинку с текстом в описании._', parse_mode='Markdown')


async def send_mem(message: types.Message, path: str):
    await bot.send_photo(chat_id=message.from_user.id, photo=open(path, 'rb'))
    await bot.send_document(chat_id=message.from_user.id, document=open(path, 'rb'))


@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    msg = await message.answer('⏳', parse_mode='Markdown')
    await message.photo[-1].download(f'image/{message.photo[-1].file_id}.jpg')

    caption = check_caption(message.caption)
    path = make_image(f'{message.photo[-1].file_id}.jpg', caption)

    await send_mem(message, path)
    await msg.delete()


@dp.message_handler(content_types=['document'])
async def get_photo(message: types.Message):
    msg = await message.answer('⏳', parse_mode='Markdown')
    await message.document.download(f'image/{message.document.file_id}.jpg')

    caption = check_caption(message.caption)
    path = make_image(f'{message.document.file_id}.jpg', caption)

    await send_mem(message, path)
    await msg.delete()
