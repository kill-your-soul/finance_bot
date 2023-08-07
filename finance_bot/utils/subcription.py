from aiogram.types import Message


async def subscription_handler(message: Message):
    await message.answer("Необходимо купить подписку, чтобы продолжить работу с ботом")
