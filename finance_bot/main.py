import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F

TOKEN = os.environ.get("TOKEN")
router = Router()

main_keyboard = ReplyKeyboardBuilder()
main_keyboard.row(types.KeyboardButton(text="Доходы"), types.KeyboardButton(text="Расходы"))
main_keyboard.row(types.KeyboardButton(text="Отчеты"))

class Finance(StatesGroup):
    agreement = State()
    subscription = State()
    main = State()
    income = State()
    outcome = State()
    report = State()

class Income(StatesGroup):
    amount = State()
    category = State()
    comment = State()

class Outcome(StatesGroup):
    amount = State()
    category = State()
    comment = State()

class Report(StatesGroup):
    period = State()
    report = State()

@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="Согласен", callback_data="agreement")
    )
    await state.set_state(Finance.agreement)
    await message.answer(f"Где-то тут будет соглашение на обработку персональных данных", reply_markup=builder.as_markup())


@router.callback_query(Finance.agreement, F.data == "agreement")
async def callback_agreement_handler(query: types.CallbackQuery, state: FSMContext) -> None:
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Оформить подписку"), types.KeyboardButton(text="Пробная версия на 7 дней"))
    await query.message.answer("Вы согласились c обработкой персональных данных", reply_markup=builder.as_markup(resize_keyboard=True, one_time=True))
    await state.set_state(Finance.subscription)

@router.message(Finance.subscription)
async def message_subscription_handler(message: Message, state: FSMContext) -> None:
    
    logging.info(f'{message.from_user.id} {message.chat.username} {message.text}')
    # TODO: Здесь будет логика оформления подписки
    await message.answer("Подписка оформлена", reply_markup=main_keyboard.as_markup(resize_keyboard=True, one_time=True))
    await state.set_state(Finance.main)


@router.message(Finance.main, F.text == "Доходы")
async def message_income_handler(message: Message, state: FSMContext) -> None:
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Добавить доход"), types.KeyboardButton(text="Назад"))
    await message.answer("Добавить доход или назад", reply_markup=builder.as_markup(resize_keyboard=True, one_time=True))
    await state.set_state(Finance.income)

@router.message(Finance.income, F.text == "Добавить доход")
async def message_add_income_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Введите количество дохода")
    await state.set_state(Income.amount)

@router.message(Income.amount)
async def message_amount_income_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Введите категорию дохода")
    await state.set_state(Income.category)

@router.message(Income.category)
async def message_category_income_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Введите комментарий")
    await state.set_state(Income.comment)

@router.message(Income.comment)
async def message_comment_income_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Доход добавлен")
    await state.set_state(Finance.main)
    await message_main_handler(message, state)

@router.message(Finance.main)
async def message_main_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Главное меню", reply_markup=main_keyboard.as_markup(resize_keyboard=True, one_time=True))


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())