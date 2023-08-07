from states.income import Income

from aiogram import types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


async def add_income_handler(message: Message, state: FSMContext):
    await message.answer("Меню")
    await state.set_state(Income.amount)


async def add_amount_handler(message: Message, state: FSMContext):
    # await
    pass


async def add_category_handler(message: Message, state: FSMContext):
    pass


async def add_comment_handler(message: Message, state: FSMContext):
    pass
