import random
from fastapi import APIRouter
from DAL.telegram_bot import TelegramBot

router = APIRouter()


@router.get('/random-number/')
async def random_number():
    number = random.randint(1, 100_000_000)

    telegram_bot = TelegramBot()
    telegram_bot.insert_number(number=number)

    return f'Number inserted: {number}'
