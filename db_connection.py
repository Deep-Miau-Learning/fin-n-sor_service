import os

from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

client = MongoClient(config["MONGO_URI"])

def get_db():
    return client[config["MONGO_DB_NAME"]]



def get_collection(collection_name):
    return get_db()[collection_name]



