import os

from aiogram import Bot
from aiogram import Dispatcher
import handlers

def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(handlers.start.setup_handlers())


def main()-> None:
    bot = Bot(os.environ.get("TOKEN"))
    dp = Dispatcher(bot)
    setup_handlers(dp)
    dp.run_polling()


if __name__ == "__main__":
    main()