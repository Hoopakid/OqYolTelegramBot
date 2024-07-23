from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def language_btn():
    uz_language = InlineKeyboardButton(text="O'zbekcha 🇺🇿", callback_data='uz_lang')
    ru_language = InlineKeyboardButton(text="Русский 🇷🇺", callback_data='ru_lang')
    btn = InlineKeyboardMarkup(inline_keyboard=[[uz_language], [ru_language]])
    return btn
