import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

load_dotenv(find_dotenv())

DATABASE_URI = os.getenv('MONGO_DB')


def get_database():
    CONNECTION_STRING = DATABASE_URI

    client = MongoClient(CONNECTION_STRING)

    return client['user_shopping_list']


if __name__ == "__main__":

    dbname = get_database()
