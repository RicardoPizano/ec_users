from typing import Union

from pydantic import BaseModel


class UserRequest(BaseModel):
    name: Union[str, None] = None
    age: Union[int, None] = None
    password: Union[str, None] = None
