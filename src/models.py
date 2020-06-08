import datetime
from typing import Union

from pymongo import MongoClient

from src import config

client = MongoClient(config.MONGODB_URL)
db = client[config.MONGODB_NAME]
history_collection = db[config.MONGODB_COLLECTION]


def save_operation(operator: str,
                   first_number: Union[int, float],
                   second_number: Union[int, float],
                   result: Union[int, float]):
    operation = {
        "operator": operator,
        "first_number": first_number,
        "second_number": second_number,
        "result": result,
        "date": datetime.datetime.utcnow()
    }
    return history_collection.insert_one(operation).inserted_id
