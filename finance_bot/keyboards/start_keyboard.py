from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


start_keyboard_builder = InlineKeyboardBuilder()
start_keyboard_builder.row(
    types.InlineKeyboardButton(text="Согласен", callback_data="agreement")
)

agreement_keyboard_builder = ReplyKeyboardBuilder()
agreement_keyboard_builder.row(types.KeyboardButton(text="Оформить подписку"), types.KeyboardButton(text="Пробная версия на 7 дней"))

main_keyboard = ReplyKeyboardBuilder()
main_keyboard.row(types.KeyboardButton(text="Доходы"), types.KeyboardButton(text="Расходы"))
main_keyboard.row(types.KeyboardButton(text="Отчеты"))