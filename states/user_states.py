from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup


# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    start_menu_state = State()
    contact_state = State
    trading_instruments_state = State()
    selling_subscription_state = State()
    copy_trading_state = State()
    gtr_trade_state = State()

