from finance_bot.states.start import Finance
from finance_bot.keyboards.start_keyboard import start_keyboard_builder, agreement_keyboard_builder, main_keyboard

from aiogram import types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

async def command_start_handler(message: Message, state: FSMContext):
    await message.answer("Где-то тут будет соглашение на обработку персональных данных", reply_markup=start_keyboard_builder.as_markup())
    await state.set_state(Finance.agreement)


async def callback_agreement_handler(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer("Вы согласились c обработкой персональных данных", reply_markup=agreement_keyboard_builder.as_markup(resize_keyboard=True, one_time=True))
    await state.set_state(Finance.subscription)
    await main_handler(query.message, state)

async def main_handler(message: Message, state: FSMContext):
    await message.answer("Главное меню", reply_markup=main_keyboard.as_markup())
    await state.set_state(Finance.main)