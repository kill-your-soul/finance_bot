from aiogram import types

PRICES = {
    "month": types.LabeledPrice(label="Подписка на месяц", amount=int(10_000)),
    "three_months": types.LabeledPrice(label="Подписка на 3 месяца", amount=int(10_000 * 2.7)),
}
