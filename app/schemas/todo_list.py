from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


class ToDoListBase(BaseModel):
    task_name: str = Field(min_length=3, description="Task name")
    description: str
    task_status: str

class ToDoCreate(ToDoListBase):
    pass

class ToDoUpdate(BaseModel):
    task_name: Optional[str] = None
    description: Optional[str] = None
    task_status: Optional[str] = None

class ToDoResponse(ToDoListBase):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)