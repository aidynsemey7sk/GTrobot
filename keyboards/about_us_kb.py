from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_ABOUT_US


def create_about_us_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for button, text in LEXICON_ABOUT_US.items():
        if button != 'text':
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
    kb_builder.row(*buttons)
    return kb_builder.as_markup()
