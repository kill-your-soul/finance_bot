from aiogram.fsm.state import State, StatesGroup


class Income(StatesGroup):
    base = State()
    amount = State()
    category = State()
    comment = State()
