from finance_bot import states

from aiogram import Router, Dispatcher
from aiogram.filters import CommandStart, StateFilter
# from aiogram.types import Message, CallbackQuery


from . import start


def setup_handlers() -> Router:
    router = Router()
    router.message.register(start.command_start_handler, CommandStart())
    router.callback_query.register(start.callback_agreement_handler, StateFilter(states.start.Finance.agreement))
    router.message.register(start.main_handler, StateFilter(states.start.Finance.main))
    return router