from pydantic import BaseModel
from typing import Optional

class TaskCreateResponse(BaseModel):
    """Schema for task creation response"""
    task_id: str
    status: str

class TaskStatusResponse(BaseModel):
    """Schema for task status response"""
    task_id: str
    status: Optional[str]

class TaskListResponse(BaseModel):
    """Schema for getting all tasks (cached)"""
    task_id: str
    cached: bool