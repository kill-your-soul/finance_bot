from aiogram.fsm.state import State, StatesGroup


class Subscription(StatesGroup):
    subscription = State()
    pre_checkout = State()
    payment = State()
