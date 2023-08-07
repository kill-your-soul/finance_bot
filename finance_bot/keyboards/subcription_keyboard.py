from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

subscription_keyboard_builder = ReplyKeyboardBuilder()
subscription_keyboard_builder.row(
    types.KeyboardButton(text="Подписка на месяц"),
    types.KeyboardButton(text="Подписка на 3 месяца"),
)
