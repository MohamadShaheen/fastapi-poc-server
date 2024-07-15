import random
from fastapi import APIRouter, Form
from DAL.telegram_bot import TelegramBot
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.post('/random-number/', response_class=PlainTextResponse)
async def random_number():
    number = random.randint(1, 100_000_000)

    telegram_bot = TelegramBot()
    telegram_bot.insert_number(number=number)

    return f'Number inserted: {number}'


@router.post('/string/', response_class=PlainTextResponse)
async def random_string(string: str = Form(...)):
    telegram_bot = TelegramBot()
    telegram_bot.insert_string(string=string)

    return f'String inserted: {string}'
