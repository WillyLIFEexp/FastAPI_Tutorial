from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Annotated
from datetime import datetime


class ToDoListBase(BaseModel):
    title: str = Field(min_length=3)
    description: str
    task_status: str

class ToDoCreate(ToDoListBase):
    pass

    