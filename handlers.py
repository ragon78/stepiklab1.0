from aiogram.filters import CommandStart
from aiogram import types
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from loader import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    kb = [
        [types.KeyboardButton(text='Робот')]
        [types.KeyboardButton(text='Не робот')]
        [types.KeyboardButton(text='Робот, но мне сказали что я не робот')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer(text: 'Привет! Ты кто такой?', reply_markup=keyboard)


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
