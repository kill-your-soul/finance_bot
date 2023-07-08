from aiogram.fsm.state import State, StatesGroup

class Outcome(StatesGroup):
    amount = State()
    category = State()
    comment = State()