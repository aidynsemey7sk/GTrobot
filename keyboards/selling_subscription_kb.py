from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_SELLING_SUBSCRIPTION


def create_selling_subscription_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    buttons_sec: list[InlineKeyboardButton] = []
    for button, text in LEXICON_SELLING_SUBSCRIPTION.items():
        if button[:3] == 'sec':
            buttons_sec.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
            continue
        if button != 'text':
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    kb_builder.row(*buttons, width=2)
    kb_builder.row(*buttons_sec, width=1)

    return kb_builder.as_markup()
