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
        'operator': operator,
        'first_number': first_number,
        'second_number': second_number,
        'result': result,
        'date': datetime.datetime.utcnow()
    }
    inserted_id = history_collection.insert_one(operation).inserted_id

    operation_in_db = history_collection.find_one({'_id': inserted_id})
    operation_in_db['_id'] = str(operation_in_db['_id'])

    return operation_in_db


def find_one(q_filter=None, *args, **kwargs):
    result = history_collection.find_one(q_filter, *args, **kwargs)
    result['_id'] = str(result['_id'])
    return result
