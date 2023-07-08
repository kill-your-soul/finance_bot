from aiogram.fsm.state import State, StatesGroup

class Income(StatesGroup):
    amount = State()
    category = State()
    comment = State()