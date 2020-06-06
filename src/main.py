from typing import Union

from fastapi import FastAPI

from src.models import save_operation

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Calculator"}


@app.get("/add")
def add(first: Union[int, float], second: Union[int, float]):
    result = first + second
    save_operation("+", first, second, result)
    return result


@app.get("/sub")
def subtract(first: Union[int, float], second: Union[int, float]):
    result = first - second
    save_operation("-", first, second, result)
    return result


@app.get("/multi")
def multiply(first: Union[int, float], second: Union[int, float]):
    result = first * second
    save_operation("*", first, second, result)
    return result


@app.get("/div")
def division(first: Union[int, float], second: Union[int, float]):
    result = first / second
    save_operation("/", first, second, result)
    return result
