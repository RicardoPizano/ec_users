from typing import Union

import pymongo
from fastapi import FastAPI, Response, status

import logger
import utils

from constans import MONGO_URL
from models.requests import UserRequest
from models.responses import UserResponse, ErrorResponse
from repositories import db
from schemas_responses import user_response

app = FastAPI()

LOGGER_FILE_NAME = "main.py"

client = pymongo.MongoClient(MONGO_URL)
db_session = client.ecdb_comics


@app.post("/users", responses={**user_response})
async def create_user(r: Response, request: UserRequest = None):
    if not request:
        request = UserRequest()
    name = utils.get_random_name()
    age = 0
    password = utils.get_random_password()
    if request.name:
        name = request.name
    if request.age:
        age = request.age
    if request.password:
        password = request.password
    try:
        user = db.create_user(db_session=db_session, name=name, password=password, age=age)
        response = utils.transform_user(user=user, password=password)
        return response
    except Exception as e:
        logger.err(LOGGER_FILE_NAME, "create_user", f"error: {str(e)}")
        r.status_code = status.HTTP_409_CONFLICT
        return ErrorResponse(message="user name already exist")


@app.get("/users", responses={**user_response})
async def find_user(r: Response,
                    name: Union[str, None] = None,
                    password: Union[str, None] = None,
                    token: Union[str, None] = ""):
    try:
        if name and password:
            user = db.find_user_by_name_and_password(db_session=db_session, name=name, password=password)
        else:
            user = db.find_user_by_token(db_session=db_session, token=token)
        response = utils.transform_user(user, user['password'])
        return response
    except Exception as e:
        logger.err(LOGGER_FILE_NAME, "find_user", f"error: {str(e)}")
        r.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponse(message="user does not exist")
