import os
import asyncio

from aiogram import Dispatcher
from aiogram import Bot
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from keyboards.inline_keyboards import language_btn

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.answer("Assalomu alaykum oq yol taksi xizmati telegram botimizga xush kelibsiz")
    btn_lang = language_btn()
    await message.answer('Kerakli tilni tanlang.', reply_markup=btn_lang)


@dp.callback_query(lambda callback_data: callback_data.data == 'uz_lang')
async def uz_lang(callback_data: CallbackQuery):
    await callback_data.message.delete()
    await callback_data.message.answer('To be continued my brother')


async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())
