from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_P2P


def create_p2p_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for button, text in LEXICON_P2P.items():
        if button != 'text':
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
    kb_builder.row(*buttons, width=2)

    return kb_builder.as_markup()
