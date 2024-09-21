import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


client = MongoClient(os.getenv("MONGO_URI"))

def get_db():
    return client[os.getenv("MONGO_DB_NAME")]


def get_collection(collection_name):
    return get_db()[collection_name]



