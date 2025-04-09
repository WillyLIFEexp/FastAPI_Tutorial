from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.todo import ToDo
from app.schemas import todo as schemas_todo
from app.crud import todo as crud_todo
from app.database.database_postgres import SessionLocal

router = APIRouter(prefix='/todos', tags=['to_dos'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas_todo.TodoResponse])
def read_todos(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud_todo.get_todos(db, skip=skip, limit=limit)

@router.get("/{todo_id}", response_model=schemas_todo.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud_todo.get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.post("/", response_model=schemas_todo.TodoResponse)
def create_todo(todo: schemas_todo.TodoCreate, db: Session = Depends(get_db)):
    return crud_todo.create_todo(db, todo)

@router.put("/{todo_id}", response_model=schemas_todo.TodoResponse)
def update_todo(todo_id: int, todo: schemas_todo.TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = crud_todo.update_todo(db, todo_id, todo)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}", response_model=schemas_todo.TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted_todo = crud_todo.delete_todo(db, todo_id)
    if deleted_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return deleted_todo
