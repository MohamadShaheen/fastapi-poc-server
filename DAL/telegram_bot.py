import os
from dotenv import load_dotenv
from pymongo import MongoClient
from urllib.parse import quote_plus

load_dotenv()

# quote_plus is used in case the username/password has special characters
mongodb_username = quote_plus(os.getenv('MONGODB_USERNAME'))
mongodb_password = quote_plus(os.getenv('MONGODB_PASSWORD'))

mongodb_url = f'mongodb+srv://{mongodb_username}:{mongodb_password}@telegrambot.ztcvwep.mongodb.net/'


class TelegramBot:
    def __init__(self):
        client = MongoClient(mongodb_url)
        database = client['telegram_bot_data']
        self.collection = database['numbers']

    def insert_number(self, number: int) -> None:
        self.collection.insert_one({'random_number': number})

