import os
from dotenv import load_dotenv
from pymongo import MongoClient
from urllib.parse import quote_plus

load_dotenv()

# quote_plus is used in case the username/password has special characters
mongodb_username = quote_plus(os.getenv('MONGODB_USERNAME'))
mongodb_password = quote_plus(os.getenv('MONGODB_PASSWORD'))

# mongodb_url = f'mongodb+srv://{mongodb_username}:{mongodb_password}@telegrambot.ztcvwep.mongodb.net/'
mongodb_url = f'mongodb+srv://{mongodb_username}:{mongodb_password}@telegrambot.ztcvwep.mongodb.net/?retryWrites=true&w=majority&appName=telegrambot'


class TelegramBot:
    def __init__(self):
        client = MongoClient(mongodb_url)
        self.database = client['telegram_bot_data']

    def insert_number(self, number: int) -> None:
        collection = self.database['numbers']
        collection.insert_one({'random_number': number})

    def insert_string(self, string: str) -> None:
        collection = self.database['strings']
        collection.insert_one({'string': string})



