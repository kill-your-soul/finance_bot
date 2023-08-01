from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter
from states.start import Finance

from . import start

# from aiogram.types import Message, CallbackQuery




def setup_handlers() -> Router:
    router = Router()
    router.message.register(start.command_start_handler, CommandStart())
    router.callback_query.register(start.callback_agreement_handler, StateFilter(Finance.agreement))
    router.message.register(start.message_subscription_handler, F.text == 'Оформить подписку', StateFilter(Finance.subscription))
    router.message.register(start.buy_subscription_handler, F.text == 'Пробная версия на 7 дней', StateFilter(Finance.subscription))
    router.message.register(start.main_handler, StateFilter(Finance.main))
    # router.message.register()
    return router