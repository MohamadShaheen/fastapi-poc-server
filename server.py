from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from routes import telegram_bot

app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
async def root():
    return 'Hello! I am the FastAPI server, we successfully connected!'


app.include_router(telegram_bot.router, prefix='/telegram-bot')
