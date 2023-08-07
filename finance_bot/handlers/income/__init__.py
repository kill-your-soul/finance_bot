# from src.states.income import Income
from states.start import Finance
from states.income import Income

from aiogram import Router, F
from aiogram.filters import StateFilter

from . import add


def setup_handlers() -> Router:
    router = Router()
    router.message.register(
        add.add_income_handler,
        F.text == "Доходы",
        StateFilter(Finance.main),
    )
    router.message.register(
        add.add_amount_handler, StateFilter(Income.amount)
    )
    router.message.register(
        add.add_category_handler, StateFilter(Income.category)
    )
    router.message.register(
        add.add_comment_handler, StateFilter(Income.comment)
    )

    return router
