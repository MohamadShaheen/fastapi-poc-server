from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
async def root():
    return 'Hello! I am the FastAPI server, we successfully connected!'
