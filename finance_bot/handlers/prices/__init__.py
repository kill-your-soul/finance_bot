from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from .start import payment_start
from aiogram import Dispatcher
import states.user
import states.admin


def setup(dp: Dispatcher):
    # dp.register_message_handler(payment_start, CommandStart(), state=None)
    pass
    
