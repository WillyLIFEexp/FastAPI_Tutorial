from fastapi import APIRouter, Depends, HTTPException, Path, Query, Body
from sqlalchemy.orm import Session
from app.models.todo_list import NewToDo
from app.schemas import ToDoCreate, ToDoResponse, ToDoUpdate
from app.crud import get_all_todos, get_todo, create_todo, delete_todo, update_todo
from app.database.db_postgres import SessionLocal
from typing import Optional, Annotated
from starlette import status

router = APIRouter(prefix='/todo_list', tags=['todos'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get('/', 
            status_code=status.HTTP_200_OK, 
            response_model=list[ToDoResponse],
            description="Retrieve a list of tasks from the database with optional pagination.")
async def read_all_task(
    db: db_dependency, 
    skip: int = Query(0, description="Number of tasks to skip"),
    limit: int = Query(100, description="Maximum number of tasks to return")
    ):
    return get_all_todos(db=db, skip=skip, limit=limit)

@router.get('/{task_id}', 
            status_code=status.HTTP_200_OK, 
            response_model=ToDoResponse,
            description="This is to get a certain task base on the given id")
async def read_task(
    db: db_dependency, 
    task_id: int = Path(gt=0, description="The query task id")
    ):
    task_data = get_todo(db=db, todo_id=task_id)
    if task_data is None:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task_data

@router.post('/', 
             status_code=status.HTTP_201_CREATED)
async def create_task(
    db: db_dependency, 
    task_data: ToDoCreate
    ):
    return create_todo(db=db, todo=task_data)

@router.put('/{task_id}', 
            status_code=status.HTTP_204_NO_CONTENT,
            description="This endpoint updates an existing task identified by `task_id`.")
async def update_task(
    db: db_dependency,
    update_data: ToDoUpdate = Body(..., description="The updated task data"),
    task_id: int = Path(..., gt=0, description="ID of the task to update (must be a positive integer)"),
    ):
    updated_todo = update_todo(db=db, todo_id=task_id, todo=update_data)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Task not found.")
    
@router.delete('/{task_id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description="This endpoirt delete an existing task identified by `task_id`.")
async def remove_task(
    db: db_dependency,
    task_id: int = Path(..., gt=0, description="ID of the task to update (must be a positive integer)")
    ):
    deleted_todo = delete_todo(db=db, todo_id=task_id)
    if deleted_todo is None:
        raise HTTPException(status_code=404, detail="Task not found.")
