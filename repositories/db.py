import uuid
import time
from hashlib import sha256
from typing import Optional, Dict

from bson import Binary, UuidRepresentation
from pymongo.collection import Collection

from exceptions import UsersExist, UserDoesNotExist


def encrypt_password(raw_password: str) -> str:
    encrypted_password = sha256(raw_password.encode('utf-8'))
    return encrypted_password.hexdigest()


def create_token(name: str, raw_password: str) -> str:
    token = sha256(f"{name}{raw_password}{time.time()}".encode('utf-8'))
    return token.hexdigest()


def create_user(db_session: Collection, name: str, password: str, age: Optional[int] = None) -> Dict[str, any]:
    user_exist = db_session.users.find({"name": name})
    if len(list(user_exist)):
        raise UsersExist()
    encrypted_password = encrypt_password(password)
    token = create_token(name=name, raw_password=password)
    uuid_obj = Binary.from_uuid(uuid.uuid4(), UuidRepresentation.STANDARD)
    user = {
        "uuid": uuid_obj,
        "name": name,
        "password": encrypted_password,
        "age": age,
        "token": token
    }
    db_session.users.insert_one(user)
    return user


def find_user_by_name_and_password(db_session: Collection, name: str, password: str):
    try:
        encrypted_password = encrypt_password(password)
        user = db_session.users.find({"name": name, "password": encrypted_password})
        return list(user)[0]
    except IndexError:
        raise UserDoesNotExist()


def find_user_by_token(db_session: Collection, token: str):
    try:
        user = db_session.users.find({"token": token})
        return list(user)[0]
    except IndexError:
        raise UserDoesNotExist()
