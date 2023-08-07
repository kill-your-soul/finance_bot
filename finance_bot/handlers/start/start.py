from states.start import Finance
from states.subscription import Subscription
from keyboards.start_keyboard import (
    start_keyboard_builder,
    agreement_keyboard_builder,
    main_keyboard,
)
from keyboards.subcription_keyboard import subscription_keyboard_builder
import config
from utils.prices import PRICES

from aiogram import types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


async def command_start_handler(message: Message, state: FSMContext):
    await message.answer(
        "Где-то тут будет соглашение на обработку персональных данных",
        reply_markup=start_keyboard_builder.as_markup(),
    )
    await state.set_state(Finance.agreement)


async def callback_agreement_handler(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer(
        "Вы согласились c обработкой персональных данных",
        reply_markup=agreement_keyboard_builder.as_markup(
            resize_keyboard=True, one_time=True
        ),
    )
    await state.set_state(Finance.subscription)


async def buy_subscription_handler(message: Message, state: FSMContext):
    await message.answer(
        "На какой срок вы хотите оформить подписку",
        reply_markup=subscription_keyboard_builder.as_markup(
            resize_keyboard=True, one_time=True
        ),
    )
    await state.set_state(Subscription.subscription)


async def month_subscription_handler(message: Message, state: FSMContext):
    await message.answer_invoice(
        title="Подписка на бота",
        description="Активация подписки на бота на 1 месяц",
        provider_token=config.PAYMENTS_PROVIDER_TOKEN,
        currency="rub",
        # photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
        # photo_width=416,
        # photo_height=234,
        # photo_size=416,
        # is_flexible=False,
        prices=[PRICES["month"]],
        start_parameter="one-month-subscription",
        payload="one-invoice-payload",
    )
    await state.set_state(Subscription.pre_checkout)


async def three_month_subscription_handler(message: Message, state: FSMContext):
    await message.answer_invoice(
        title="Подписка на бота",
        description="Активация подписки на бота на 1 месяц",
        provider_token=config.PAYMENTS_PROVIDER_TOKEN,
        currency="rub",
        # photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
        # photo_width=416,
        # photo_height=234,
        # photo_size=416,
        # is_flexible=False,
        prices=[PRICES["three_months"]],
        start_parameter="three-month-subscription",
        payload="three-invoice-payload",
    )
    await state.set_state(Subscription.pre_checkout)

async def pre_checkout_handler(query: types.PreCheckoutQuery, state: FSMContext):
    await query.answer(ok=True)
    # print(query.invoice_payload)
    # TODO: add payment 
    await state.set_state(Subscription.payment)

async def successful_payment_handler(query: types.Message, state: FSMContext):
    await query.answer("Спасибо за покупку!")
    await state.set_state(Finance.main)
    await main_handler(query, state)


async def message_subscription_handler(message: Message, state: FSMContext):
    await message.answer(
        "Подписка оформлена",
        reply_markup=main_keyboard.as_markup(resize_keyboard=True, one_time=True),
    )
    await state.set_state(Finance.main)


async def main_handler(message: Message, state: FSMContext):
    await message.answer(
        "Главное меню",
        reply_markup=main_keyboard.as_markup(resize_keyboard=True, one_time=True),
    )
