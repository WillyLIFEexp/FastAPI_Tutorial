from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    email: Optional[str] = None
    age: Optional[int] = None

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)