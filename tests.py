from starlette.testclient import TestClient

from main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Calculator"}


def test_add():
    response = client.get("/add?first=345&second=678")
    assert response.status_code == 200
    assert response.json() == 1023


def test_subtract():
    response = client.get("/sub?first=344&second=23")
    assert response.status_code == 200
    assert response.json() == 321


def test_multiply():
    response = client.get("/multi?first=600&second=65")
    assert response.status_code == 200
    assert response.json() == 39000


def test_division():
    response = client.get("/div?first=877&second=47")
    assert response.status_code == 200
    assert round(response.json(), 2) == 18.66


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_division()
