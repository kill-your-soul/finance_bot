from aiogram.fsm.state import State, StatesGroup

class Finance(StatesGroup):
    agreement = State()
    subscription = State()
    main = State()
    income = State()
    outcome = State()
    report = State()