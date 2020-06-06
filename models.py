import datetime
from typing import Union

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.pulsu_pro_test

history_collection = db.history


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
