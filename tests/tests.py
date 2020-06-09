from bson import ObjectId
from starlette.testclient import TestClient

from src.main import app
from src.models import find_one

client = TestClient(app)


def check_db_operation(response):
    response_operation = response.json()['operation']

    object_id = ObjectId(response_operation['_id'])
    database_operation = find_one({'_id': object_id})

    assert database_operation['operator'] == response_operation['operator']
    assert database_operation['first_number'] == response_operation['first_number']
    assert database_operation['second_number'] == response_operation['second_number']
    assert database_operation['result'] == response_operation['result']


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Calculator'}
    print('\tTest: test_root, success!')


def test_add():
    response = client.get('/add?first=345&second=678')
    assert response.status_code == 200
    assert response.json()['operation']['result'] == 1023
    check_db_operation(response)
    print('\tTest: test_add, success!')


def test_subtract():
    response = client.get('/sub?first=344&second=23')
    assert response.status_code == 200
    assert response.json()['operation']['result'] == 321
    check_db_operation(response)
    print('\tTest: test_subtract, success!')


def test_multiply():
    response = client.get('/multi?first=600&second=65')
    assert response.status_code == 200
    assert response.json()['operation']['result'] == 39000
    check_db_operation(response)
    print('\tTest: test_multiply, success!')


def test_division():
    response = client.get('/div?first=877&second=47')
    assert response.status_code == 200
    assert round(response.json()['operation']['result'], 2) == 18.66
    check_db_operation(response)
    print('\tTest: test_division, success!')


def test_division_by_zero():
    response = client.get('/div?first=877&second=0')
    assert response.status_code == 200
    assert response.json() == {'error': 'Division by zero'}
    print('\tTest: test_division_by_zero, success!')
