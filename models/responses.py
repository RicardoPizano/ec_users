from typing import Union

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: str
    name: str
    age: Union[int, None] = 0
    token: str
    password: str
