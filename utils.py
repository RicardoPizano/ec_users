import random
import string
from typing import Dict

from bson import UuidRepresentation
from random_username.generate import generate_username

from models.responses import UserResponse


def get_random_name() -> str:
    return generate_username()[0]


def get_random_password(length: int = 8) -> str:
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    characters = random.sample(all_characters, length)
    return "".join(characters)


def transform_user(user: Dict[str, any], password: str) -> UserResponse:
    user_uuid = user["uuid"].as_uuid(UuidRepresentation.STANDARD)
    return UserResponse(
        id=str(user_uuid),
        name=user.get('name'),
        age=user.get('age') if user.get('age') != 0 else None,
        token=user.get('token'),
        password=password,
    )
