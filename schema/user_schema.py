from lib2to3.pytree import Base
from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str]
    firstname: str
    lastname: str
    user_password: str
