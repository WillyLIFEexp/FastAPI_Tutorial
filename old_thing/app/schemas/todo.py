from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


# These schemas ensure that incoming data is validated and that your responses are formatted correctly.
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(TodoBase):
    id: int
    completed: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
