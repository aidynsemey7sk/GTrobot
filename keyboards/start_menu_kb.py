from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_START_MENU


def create_start_menu_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for button, text in LEXICON_START_MENU.items():
        buttons.append(InlineKeyboardButton(
            text=text,
            callback_data=button))
    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup()