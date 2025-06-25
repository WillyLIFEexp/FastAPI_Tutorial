from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    user_name: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    password: str
    new_password: str = Field(min_length=6)

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str