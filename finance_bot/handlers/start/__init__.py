from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter
from states.start import Finance
from states.subscription import Subscription

from . import start

# from aiogram.types import Message, CallbackQuery


def setup_handlers() -> Router:
    router = Router()
    router.message.register(start.command_start_handler, CommandStart())
    router.callback_query.register(
        start.callback_agreement_handler, StateFilter(Finance.agreement)
    )
    router.message.register(
        start.buy_subscription_handler,
        F.text == "Оформить подписку",
        StateFilter(Finance.subscription),
    )
    router.message.register(
        start.month_subscription_handler,
        F.text == "Подписка на месяц",
        StateFilter(Subscription.subscription),
    )
    router.message.register(
        start.three_month_subscription_handler,
        F.text == "Подписка на 3 месяца",
        StateFilter(Subscription.subscription),
    )
    router.pre_checkout_query.register(start.pre_checkout_handler, StateFilter(Subscription.pre_checkout))
    router.message.register(start.successful_payment_handler, StateFilter(Subscription.payment))
    router.message.register(
        start.message_subscription_handler,
        F.text == "Пробная версия на 7 дней",
        StateFilter(Finance.subscription),
    )
    router.message.register(start.main_handler, StateFilter(Finance.main))
    # router.message.register()
    return router
