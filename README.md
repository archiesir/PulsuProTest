# PulsuProTest
PulsuPro Test Calculator API

## Dependencies
- fastapi
- uvicorn
- requests
- pymongo
- envparse
- pathlib

## Install
```
git clone https://github.com/archieruin/PulsuProTest.git
cd PulsuProTest
pipenv install
```

##Setup environment
Copy .env.dist to .env file and change values in this file

## Run
```
pipenv shell
uvicorn src:app --reload
```

## Tests
```
pipenv shell
python -m tests
```
