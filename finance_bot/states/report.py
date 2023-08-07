from aiogram.fsm.state import State, StatesGroup


class Report(StatesGroup):
    period = State()
    report = State()
