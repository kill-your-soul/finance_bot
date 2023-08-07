import os
import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
import handlers


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(handlers.income.setup_handlers())
    dp.include_router(handlers.start.setup_handlers())


async def main() -> None:
    bot = Bot(os.environ.get("TOKEN"))
    dp = Dispatcher()
    setup_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
