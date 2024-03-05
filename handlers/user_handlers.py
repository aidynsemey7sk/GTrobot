from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message
from keyboards.start_menu_kb import create_start_menu_keyboard
from keyboards.trading_instruments_kb import create_trading_instruments_keyboard
from keyboards.selling_subscription_kb import create_selling_subscription_keyboard
from keyboards.gtr_trade_kb import create_gtr_trade_keyboard
from keyboards.contact_kb import create_contact_keyboard
from keyboards.about_the_bot_kb import create_how_work_bot_keyboard
from keyboards.about_us_kb import create_about_us_keyboard
from keyboards.copy_trading_kb import create_copy_trading_menu_keyboard
from keyboards.crypto_kb import create_crypto_keyboard
from keyboards.p2p_kb import create_p2p_keyboard
from keyboards.package_kb import (create_pro_keyboard, create_vip_keyboard, create_gold_keyboard, create_mini_keyboard,
                                  create_standard_keyboard)
from lexicon.lexicon import (LEXICON, LEXICON_SELLING_SUBSCRIPTION, LEXICON_HOW_WORK_BOT,
                             LEXICON_TRADING_INSTRUMENTS, LEXICON_COPY_TRADING, LEXICON_GTR_TRADE, LEXICON_ABOUT_US,
                             LEXICON_CONTACT, LEXICON_REFERAL, LEXICON_CRYPTO, LEXICON_STANDART_PACKAGE,
                             LEXICON_GOLD_PACKAGE, LEXICON_PRO_PACKAGE, LEXICON_VIP_PACKAGE, LEXICON_MINI_PACKAGE,
                             LEXICON_P2P)
from states.user_states import FSMFillForm
from aiogram.fsm.context import FSMContext

router = Router()


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    text = LEXICON[message.text]
    text = str(text).replace('$$NAME$$', message.from_user.first_name)
    buttons = create_start_menu_keyboard()
    await message.answer(text, reply_markup=buttons)
    await state.set_state(FSMFillForm.start_menu_state)


# 1.0 Вход в 'ТОРГОВЫЕ ИНСТРУМЕНТЫ'
@router.callback_query(F.data == 'trading instruments', StateFilter(FSMFillForm.start_menu_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_trading_instruments_keyboard()
    text = LEXICON_TRADING_INSTRUMENTS['text']
    await state.set_state(FSMFillForm.trading_instruments_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 1.1.0 Вход из 'ТОРГОВЫЕ ИНСТРУМЕНТЫ' в Copy Trading
@router.callback_query(F.data == 'Copy Trading', StateFilter(FSMFillForm.trading_instruments_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_copy_trading_menu_keyboard()
    text = LEXICON_COPY_TRADING['text']
    await state.set_state(FSMFillForm.copy_trading_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 1.1.1 Вход из Copy Trading в SELLING_SUBSCRIPTION
@router.callback_query(F.data == 'selling_subscription')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_selling_subscription_keyboard()
    text = LEXICON_SELLING_SUBSCRIPTION['text']
    await state.set_state(FSMFillForm.selling_subscription_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 1.2 Вход из ТОРГОВЫЕ ИНСТРУМЕНТЫ в АНАЛИЗ и СИГНАЛ + ВЫХОД В ТОРГОВЫЕ ИНСТРУМЕНТЫ
@router.callback_query(F.data == 'analitika and signals', StateFilter(FSMFillForm.trading_instruments_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_selling_subscription_keyboard()
    text = LEXICON_SELLING_SUBSCRIPTION['text']
    await state.set_state(FSMFillForm.selling_subscription_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 1.3.0 Вход из ТОРГОВЫЕ ИНСТРУМЕНТЫ в GTR TRADE
@router.callback_query(F.data == 'gtr_trade', StateFilter(FSMFillForm.trading_instruments_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_gtr_trade_keyboard()
    text = LEXICON_GTR_TRADE['text']
    await state.set_state(FSMFillForm.gtr_trade_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 1.3.1 Вход из GTR TRADE в CRYPTO + ВЫХОД В ТОРГОВЫЕ ИНСТРУМЕНТЫ
@router.callback_query(F.data == 'crypto')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_crypto_keyboard()
    text = LEXICON_CRYPTO['text']
    await callback.message.edit_text(text, reply_markup=buttons)


# 1.3.2 Вход из GTR TRADE в CRYPTO
@router.callback_query(F.data == 'crypto')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_crypto_keyboard()
    text = LEXICON_CRYPTO['text']
    await callback.message.edit_text(text, reply_markup=buttons)


# 1.3.3 Вход из GTR TRADE в STOCK
@router.callback_query(F.data == 'stock')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    await callback.answer('⚠️В данный период времени ведутся \n технические работы', show_alert=True)


# 1.4 Вход из ТОРГОВЫЕ ИНСТРУМЕНТЫ в MONITORING + ВЫХОД В ТОРГОВЫЕ ИНСТРУМЕНТЫ
@router.callback_query(F.data == 'monitoring', StateFilter(FSMFillForm.trading_instruments_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_selling_subscription_keyboard()
    text = LEXICON_SELLING_SUBSCRIPTION['text']
    await callback.message.edit_text(text, reply_markup=buttons)


# 1.6 Вход из ТОРГОВЫЕ ИНСТРУМЕНТЫ в КУПИТЬ ПОДПИСКУ
@router.callback_query(F.data == 'sec_buy')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_selling_subscription_keyboard()
    text = LEXICON_SELLING_SUBSCRIPTION['text']
    await callback.message.edit_text(text, reply_markup=buttons)


# 1.7 Возврат в ГЛАВНОЕ МЕНЮ !!!
@router.callback_query(F.data == 'sec_home', StateFilter(FSMFillForm.trading_instruments_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    text = LEXICON['/start']
    text = str(text).replace('$$NAME$$', callback.message.from_user.first_name)
    buttons = create_start_menu_keyboard()
    print(state.__dict__)
    await callback.message.edit_text(text, reply_markup=buttons)
    await state.set_state(FSMFillForm.start_menu_state)


# 1.8 Вход из ТОРГОВЫЕ ИНСТРУМЕНТЫ в p2p арбитраж
@router.callback_query(F.data == '2p2_arbitration', StateFilter(FSMFillForm.trading_instruments_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_p2p_keyboard()
    text = LEXICON_P2P['text']
    await callback.message.edit_text(text, reply_markup=buttons)


# 2.0 Вход в ветку СВЯЗЬ !!!
@router.callback_query(F.data == 'contact', StateFilter(FSMFillForm.start_menu_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_contact_keyboard()
    text = LEXICON_CONTACT['text']
    await callback.message.edit_text(text, reply_markup=buttons)
    await state.set_state(FSMFillForm.contact_state)


# 2.1 Возврат в ГЛАВНОЕ МЕНЮ !!!
@router.callback_query(F.data == 'sec_back_menu')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    text = LEXICON['/start']
    text = str(text).replace('$$NAME$$', callback.message.from_user.first_name)
    buttons = create_start_menu_keyboard()
    await callback.message.edit_text(text, reply_markup=buttons)
    await state.set_state(FSMFillForm.start_menu_state)


# 3.0 Вход в ветку КАК РАБОТАЕТ БОТ !!!
@router.callback_query(F.data == 'about_the_bot', StateFilter(FSMFillForm.start_menu_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_how_work_bot_keyboard()
    text = LEXICON_HOW_WORK_BOT['text']
    await callback.message.edit_text(text, disable_web_page_preview=True, reply_markup=buttons)


# 3.1 Возврат в ГЛАВНОЕ МЕНЮ !!!
@router.callback_query(F.data == 'sec_back_menu')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    text = LEXICON['/start']
    text = str(text).replace('$$NAME$$', callback.message.from_user.first_name)
    buttons = create_start_menu_keyboard()
    await state.set_state(FSMFillForm.start_menu_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 4.0 Вход в ветку О НАС !!!
@router.callback_query(F.data == 'about us', StateFilter(FSMFillForm.start_menu_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_about_us_keyboard()
    text = LEXICON_ABOUT_US['text']
    await callback.message.edit_text(text, disable_web_page_preview=True, reply_markup=buttons)


# 4.1 Возврат в ГЛАВНОЕ МЕНЮ !!!
@router.callback_query(F.data == 'sec_back_menu')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    text = LEXICON['/start']
    text = str(text).replace('$$NAME$$', callback.message.from_user.first_name)
    buttons = create_start_menu_keyboard()
    await state.set_state(FSMFillForm.start_menu_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 5.0 Вход в ветку РЕФЕРАЛ !!!
@router.callback_query(F.data == 'referal', StateFilter(FSMFillForm.start_menu_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_selling_subscription_keyboard()
    text = LEXICON_REFERAL['text']
    await callback.message.edit_text(text, reply_markup=buttons)


# 5.1 Возврат в РАБОЧИЕ ИНСТРУМЕНТЫ
@router.callback_query(F.data == 'sec_back')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_trading_instruments_keyboard()
    text = LEXICON_TRADING_INSTRUMENTS['text']
    await state.set_state(FSMFillForm.trading_instruments_state)
    await callback.message.edit_text(text, reply_markup=buttons)


'''МЕНЮ ПОКУПКИ'''


# 6.0 ВХОД В МИНИ
@router.callback_query(F.data == 'mini')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_mini_keyboard()
    text = LEXICON_MINI_PACKAGE['text']
    await state.set_state(FSMFillForm.trading_instruments_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 6.1 Вход в GOLD
@router.callback_query(F.data == 'gold')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_gold_keyboard()
    text = LEXICON_GOLD_PACKAGE['text']
    await state.set_state(FSMFillForm.trading_instruments_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 6.2 Вход в standart
@router.callback_query(F.data == 'standart')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_standard_keyboard()
    text = LEXICON_STANDART_PACKAGE['text']
    await state.set_state(FSMFillForm.trading_instruments_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 6.3 Вход в gtr_pro
@router.callback_query(F.data == 'gtr_pro')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_pro_keyboard()
    text = LEXICON_PRO_PACKAGE['text']
    await state.set_state(FSMFillForm.trading_instruments_state)
    await callback.message.edit_text(text, reply_markup=buttons)


# 6.3 Вход в vip
@router.callback_query(F.data == 'vip')
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    buttons = create_vip_keyboard()
    text = LEXICON_VIP_PACKAGE['text']
    await state.set_state(FSMFillForm.trading_instruments_state)
    await callback.message.edit_text(text, reply_markup=buttons)
