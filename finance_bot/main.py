from aiogram import Bot, Dispatcher, executor
from aiohttp import web
import os
import logging


async def on_startup(dp: Dispatcher):
    logging.info("start")
    import handlers

    handlers.prices.setup(dp)


async def on_shutdown(dp: Dispatcher):
    logging.info("shutdowning...")
    await dp.bot.close()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot = Bot(os.environ.get("bot_token"))
    dp = Dispatcher(bot)
    # web.run_app(init(bot, dp), host="localhost", port=5005)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
