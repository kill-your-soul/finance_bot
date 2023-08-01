# from src.states.income import Income
import states

from aiogram import Router, F
from aiogram.filters import StateFilter

from . import add

def setup_handlers() -> Router:
    router = Router()
    router.message.register(add.add_income_handler, F.text == "Доходы", StateFilter(states.start.Finance.main))
    router.message.register(add.add_amount_handler, StateFilter(states.income.Income.amount))
    router.message.register(add.add_category_handler, StateFilter(states.income.Income.category))
    router.message.register(add.add_comment_handler, StateFilter(states.income.Income.comment))

    return router