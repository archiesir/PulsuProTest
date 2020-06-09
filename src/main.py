from fastapi import FastAPI

from src.models import save_operation

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Calculator'}


@app.get('/add')
def add(first, second):
    try:
        result = int(first) + int(second)

    except ValueError:
        return {'error': 'Invalid argument'}

    operation = save_operation('+', first, second, result)
    return {'operation': operation}


@app.get('/sub')
def subtract(first, second):
    try:
        result = int(first) - int(second)

    except ValueError:
        return {'error': 'Invalid argument'}

    operation = save_operation('-', first, second, result)
    return {'operation': operation}


@app.get('/multi')
def multiply(first, second):
    try:
        result = int(first) * int(second)

    except ValueError:
        return {'error': 'Invalid argument'}

    operation = save_operation('*', first, second, result)
    return {'operation': operation}


@app.get('/div')
def division(first, second):
    try:
        result = int(first) / int(second)

    except ValueError:
        return {'error': 'Invalid argument'}

    except ZeroDivisionError:
        return {'error': 'Division by zero'}

    operation = save_operation('/', first, second, result)
    return {'operation': operation}
